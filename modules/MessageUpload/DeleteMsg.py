import json

from modules.Application.Printc import Printc


class DeleteMsg:
    def __init__(self, message_id):
        self.message_id = message_id

    def dump(self):
        Printc("正在撤回消息", "I")
        Printc(" - 消息ID：" + str(self.message_id), "I")
        print()  # 空行

        return json.dumps(
            {
                "action": "delete_msg",
                "params": {"message_id": self.message_id},
            }
        )
