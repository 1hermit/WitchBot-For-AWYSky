import json

from modules.Application.Printc import Printc


class SendPrivateMessage:
    def __init__(self, user_id, message):
        self.user_id = user_id
        self.message = message

    def dump(self):
        Printc("正在发送私聊消息", "I")
        Printc(" - 消息内容：" + self.message, "I")
        Printc(" - 发送到：" + str(self.user_id), "I")
        print()  # 空行

        self.message = "【小巫正】 \n" + self.message

        return json.dumps(
            {
                "action": "send_private_msg",
                "params": {"user_id": self.user_id, "message": self.message},
            }
        )
