# 导入模块
import os
import sys
import websockets
import asyncio
import datetime
import time
import json
import traceback
import re
import requests

# 导入程序模块
from modules.Application.Printc import Printc
from modules.Application.Config import Config
from modules.Application.Variable import Variable
from modules.BotModules.CQCode import CQCode

# 导入指令模块
from modules.BotModules.Template import Template

# 导入上报消息模块
from modules.MessageUpload.SendPrivateMessage import SendPrivateMessage
from modules.MessageUpload.SetGroupAddRequest import SetGroupAddRequest
from modules.MessageUpload.SendGroupMessage import SendGroupMessage
from modules.MessageUpload.SetGroupKick import SetGroupKick
from modules.MessageUpload.GetBotInfo import GetBotInfo
from modules.MessageUpload.DeleteMsg import DeleteMsg
from modules.MessageUpload.SetGroupCard import SetGroupCard

config = Config()  # 实例化Config类
variable = Variable()  # 实例化Variable类


# 启动自检
def checkBeforeStart():
    global sys

    # STEP 1: 检查Python版本
    if sys.version_info.major < 3:
        Printc("Python版本过低，请使用Python 3.x", "E")
        return 0
    else:
        Printc(
            "(STEP 1 / 3) Python版本检查通过 (Python "
            + str(sys.version_info.major)
            + "."
            + str(sys.version_info.minor)
            + ")",
            "I",
        )

    # STEP 2: 检查配置文件
    if config.readFromFile(variable.configFilePath) == 0:
        Printc("配置文件读取失败", "E")
        Printc("正在创建默认配置文件", "I")
        config.saveDefaultConfig(variable.configFilePath)
        Printc("配置文件创建成功", "I")

    # 检查黑名单文件是否存在
    if not os.path.exists(variable.blacklistFilePath):
        Printc("黑名单文件不存在，正在创建", "I")
        with open(variable.blacklistFilePath, "w", encoding="utf-8") as f:
            f.write("")
        Printc("黑名单文件创建成功", "I")
    else:
        Printc("(STEP 2 / 3) 配置文件检查通过", "I")
        config.readFromFile(variable.configFilePath)
        Printc("(STEP 2 / 3) 即将连接的服务器：" + config.ip + ":" + str(config.port), "I")
        Printc("(STEP 2 / 3) 主人QQ：" + str(config.master), "I")
        Printc("(STEP 2 / 3) 正在启动ZeroBot", "I")


# 保存最新收到的消息
def saveLastMessage(data):
    variable.lastMessage = data["message"]
    variable.lastMessageSender = data["sender"]["user_id"]
    variable.lastMessageSenderNickname = (
        data["sender"]["card"]
        if data["sender"]["card"] != ""
        else data["sender"]["nickname"]
    )
    variable.isGroupMessage = True
    variable.lastMessageGroup = data["group_id"]
    variable.lastMessageID = data["message_id"]


# 输出信息
def PrintMessage(data):
    Printc("收到群聊消息：", "I")
    Printc(" - 消息内容：" + data["message"], "I")
    Printc(
        " - 发送者："
        + (
            data["sender"]["card"]
            if data["sender"]["card"] != ""
            else data["sender"]["nickname"]
        ),
        "I",
    )
    Printc(" - 发送者QQ：" + str(data["sender"]["user_id"]), "I")
    Printc(" - 群号：" + str(data["group_id"]), "I")
    print()  # 空行


# 主程序
async def main():
    os.system("title " + config.title)  # 设置窗口标题
    try:
        async with websockets.connect(
            "ws://" + config.ip + ":" + str(config.port)
        ) as websocket:
            Printc("(STEP 3 / 3) WebSocket服务器 连接成功", "I")
            Printc("欢迎使用！", "I")
            print()  # 空行

            while True:
                # 等待服务器发送消息
                meessage = await websocket.recv()

                # 调试模式
                if config.debug == 1:
                    Printc(meessage, "D")

                # 读取Json
                data = json.loads(meessage)

                # 若为首次启动，则获取机器人信息
                if variable.isFirstStart == True:
                    variable.isFirstStart = False
                    await websocket.send(GetBotInfo.dump())

                # 若为机器人信息，则保存机器人信息
                if "data" in data:
                    if data["data"] != None:
                        if "nickname" in data["data"] and "user_id" in data["data"]:
                            config.bot_name = data["data"]["nickname"]
                            config.bot = data["data"]["user_id"]

                            Printc("机器人信息获取成功", "I")
                            Printc(" - 机器人QQ：" + str(data["data"]["user_id"]), "I")
                            Printc(" - 机器人昵称：" + data["data"]["nickname"], "I")
                            print()

                            config.saveToFile(variable.configFilePath)

                # 展示收到的消息以及记录最新收到的消息
                if "post_type" in data:
                    if data["post_type"] != "meta_event":
                        if data["post_type"] == "message":  # 消息事件
                            if data["message_type"] == "group":  # 群聊消息
                                if data["group_id"] == 897259899:
                                    # 展示收到的消息
                                    PrintMessage(data)

                                    # 保存最新收到的消息
                                    variable.isLastMessageProcessed = False
                                    saveLastMessage(data)

                                    # 在下方添加指令
                                    if (
                                        variable.lastMessageSenderNickname == "请修改群备注"
                                        or variable.lastMessageSenderNickname == "🌹"
                                    ):
                                        Printc(
                                            "检测到新人，正在撤回消息",
                                            "I",
                                        )
                                        await websocket.send(
                                            DeleteMsg(
                                                variable.lastMessageID,
                                            ).dump()
                                        )
                                        Printc(
                                            "已撤回消息",
                                            "I",
                                        )
                                        await websocket.send(
                                            SendGroupMessage(
                                                variable.lastMessageGroup,
                                                CQCode(
                                                    "at", variable.lastMessageSender
                                                ).dump()
                                                + "请修改群备注之后再发言",
                                            ).dump()
                                        )

                        if data["post_type"] == "notice":  # 通知事件（如群成员增加，群成员减少等）
                            # 光遇群号判断
                            # 群成员减少，则拉入黑名单
                            if data["group_id"] == 897259899:
                                if data["notice_type"] == "group_decrease":
                                    Printc(
                                        "检测到光遇群成员减少，正在拉入黑名单",
                                        "I",
                                    )
                                    # 添加黑名单
                                    with open(
                                        variable.blacklistFilePath,
                                        "a",
                                        encoding="utf-8",
                                    ) as f:
                                        f.write(str(data["user_id"]) + "\n")
                                    Printc(
                                        "已将 " + str(data["user_id"]) + " 拉入黑名单",
                                        "I",
                                    )
                                    await websocket.send(
                                        SendGroupMessage(
                                            data["group_id"],
                                            "\n群成员"
                                            + str(data["user_id"])
                                            + "已退群\n已将 "
                                            + str(data["user_id"])
                                            + " 拉入黑名单",
                                        ).dump()
                                    )
                                # 群成员增加，则发送欢迎消息
                                if data["notice_type"] == "group_increase":
                                    Printc(
                                        "检测到光遇群成员增加，正在发送欢迎消息",
                                        "I",
                                    )
                                    # 发送欢迎消息
                                    await websocket.send(
                                        SendGroupMessage(
                                            data["group_id"],
                                            CQCode("at", data["user_id"]).dump()
                                            + "欢迎新人！\n请先阅读群公告，了解群规则。\n然后请发送你的光遇名称并将群昵称修改成你的光遇名字，以便管理为您添加头衔\n若您在两天后仍然处于无头衔状态\n您将被踢出群聊并拉入黑名单！",
                                        ).dump()
                                    )
                                    # 修改群名片
                                    await websocket.send(
                                        SetGroupCard(
                                            data["group_id"],
                                            data["user_id"],
                                            "请修改群备注",
                                        ).dump()
                                    )

                                    Printc(
                                        "已发送欢迎消息至 " + str(data["group_id"]),
                                        "I",
                                    )

                        if data["post_type"] == "request":  # 请求事件（如申请加入群聊，申请添加好友）
                            if data["request_type"] == "group":
                                # 光遇群号判断
                                if data["group_id"] == 89725989:
                                    # 黑名单判断
                                    with open(
                                        variable.blacklistFilePath,
                                        "r",
                                        encoding="utf-8",
                                    ) as f:
                                        blacklist = f.readlines()
                                        for i in blacklist:
                                            if i.strip("\n") == str(data["user_id"]):
                                                await websocket.send(
                                                    SetGroupAddRequest(
                                                        data["flag"],
                                                        data["sub_type"],
                                                        False,
                                                        "您已被管理员加入黑名单",
                                                    ).dump()
                                                )

                    # 设置已经处理过最新收到的消息
                    variable.isLastMessageProcessed = True

    # 捕获错误
    except ConnectionRefusedError:
        Printc("WebSocket服务器 连接失败", "E")
        Printc("可能的原因：", "E")
        Printc("1. 服务器未启动", "E")
        Printc("2. 服务器IP或端口错误", "E")
    except Exception as e:
        # 输出错误信息
        Printc("\n" + traceback.format_exc(), "E")
        Printc("程序已退出", "E")
        os.system("pause")


checkBeforeStart()
asyncio.get_event_loop().run_until_complete(main())
