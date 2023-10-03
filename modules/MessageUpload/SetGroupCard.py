import json

from modules.Application.Printc import Printc


class SetGroupCard:
    def __init__(self, group_id, user_id, card):
        self.user_id = user_id
        self.group_id = group_id
        self.card = card

    def dump(self):
        Printc("正在设置群成员名片", "I")
        Printc(" - 被处理成员：" + str(self.user_id), "I")
        Printc(" - 群聊" + str(self.group_id), "I")
        Printc(" - 名片" + str(self.card), "I")
        print()  # 空行

        return json.dumps(
            {
                "action": "set_group_card",
                "params": {
                    "group_id": self.group_id,
                    "user_id": self.user_id,
                    "card": self.card,
                },
            }
        )
