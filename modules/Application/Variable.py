import os


class Variable:  # Class:程序变量
    # 是否第一次启动
    isFirstStart = True
    # 最新版本号
    latestVersion = ""
    # 配置文件路径，读取程序目录下的config文件夹下的config.json
    configFilePath = str(os.getcwd() + "\\data\\config.json")
    # Logo文件路径，读取程序目录下的config文件夹下的logo.txt
    logoFilePath = str(os.getcwd() + "\\data\\logo.txt")
    # 黑名单文件路径，读取程序目录下的config文件夹下的blacklist.txt
    blacklistFilePath = str(os.getcwd() + "\\data\\blacklist.txt")
    # 是否已经处理过最新收到的消息
    isLastMessageProcessed = False
    # 最新收到的消息
    lastMessage = ""
    # 最新收到的消息的发送者
    lastMessageSender = 0
    # 最新收到的消息的发送者的昵称
    lastMessageSenderNickname = ""
    # 是否为群消息
    isGroupMessage = False
    # 最新收到消息的群号
    lastMessageGroup = 0
    # 最新收到的消息的群昵称
    lastMessageGroupName = ""
    # 最新收到的消息的ID
    lastMessageID = 0
