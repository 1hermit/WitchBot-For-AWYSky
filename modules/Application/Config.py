import os
import json


class Config:  # Class:程序设置
    # 程序版本号
    version = "1.0.0"
    # 程序标题
    title = "小巫正"
    # 服务器端口
    port = 8080
    # 服务器IP
    ip = "127.0.0.1"
    # 主人QQ
    master = 0
    # 管理员QQ
    admin = []
    # 机器人QQ
    bot = 0
    # 机器人昵称
    bot_name = ""
    # 调试模式
    debug = 0
    # 转发群聊消息给主人
    isForwardGroupMessageToMaster = 0

    # 读取配置文件
    def readFromFile(self, filePath):
        if not os.path.exists(filePath):
            return 0

        with open(filePath, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.version = data["version"]
            self.title = data["title"]
            self.port = data["port"]
            self.ip = data["ip"]
            self.master = data["master"]
            self.admin = data["admin"]
            self.bot = data["bot"]
            self.bot_name = data["bot_name"]
            self.debug = data["debug"]

    # 保存配置文件
    def saveToFile(self, filePath):
        with open(filePath, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "version": self.version,
                    "title": self.title,
                    "port": self.port,
                    "ip": self.ip,
                    "master": self.master,
                    "admin": self.admin,
                    "bot": self.bot,
                    "bot_name": self.bot_name,
                    "debug": self.debug,
                },
                f,
                ensure_ascii=False,
                indent=4,
            )

    # 保存默认配置文件
    def saveDefaultConfig(self, filePath):
        with open(filePath, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "version": self.version,
                    "title": "小巫正",
                    "port": 8080,
                    "ip": "127.0.0.1",
                    "master": 0,
                    "admin": [],
                    "bot": 0,
                    "bot_name": "",
                    "debug": 0,
                },
                f,
                ensure_ascii=False,
                indent=4,
            )
