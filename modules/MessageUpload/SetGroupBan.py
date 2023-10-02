import json

from modules.Application.Printc import Printc


class SetGroupBan:
    def __init__(self, group_id, user_id, duration):
        self.group_id = group_id
        self.user_id = user_id
        self.duration = duration

    def dump(self):
        Printc("正在禁言用户", "I")
        Printc(" - 用户：" + str(self.user_id), "I")
        Printc(" - 群组：" + str(self.group_id), "I")
        Printc(" - 时长：" + str(self.duration), "I")
        print()  # 空行

        return json.dumps(
            {
                "action": "set_group_ban",
                "params": {
                    "group_id": self.group_id,
                    "user_id": self.user_id,
                    "duration": self.duration,
                },
            }
        )
