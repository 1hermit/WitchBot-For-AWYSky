# 导入模块
import json
import time
import datetime

from modules.Application.Printc import Printc

from modules.MessageUpload.SendGroupMessage import SendGroupMessage


class Template:
    def __init__(self, group_id, message):
        self.group_id = group_id
        self.message = message

    def SendGroupMessage(self):
        return SendGroupMessage(self.group_id, self.message).dump()
