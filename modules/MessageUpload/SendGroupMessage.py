import json

from modules.Application.Printc import Printc


class SendGroupMessage:
    def __init__(self, group_id, message):
        self.group_id = group_id
        self.message = message

    def dump(self):
        Printc("正在发送群聊消息", "I")
        Printc(" - 消息内容：" + str(self.message), "I")
        Printc(" - 发送到：" + str(self.group_id), "I")
        print()  # 空行

        self.message = "【小巫正】 \n" + str(self.message)

        return json.dumps(
            {
                "action": "send_group_msg",
                "params": {"group_id": self.group_id, "message": str(self.message)},
            }
        )
