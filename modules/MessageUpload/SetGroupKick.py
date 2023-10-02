import json

from modules.Application.Printc import Printc


class SetGroupKick:
    def __init__(self, user_id, group_id, reject_add_request):
        self.user_id = user_id
        self.group_id = group_id
        self.reject_add_request = reject_add_request

    def dump(self):
        Printc("正在将成员踢出群聊", "I")
        Printc(" - 被处理成员：" + str(self.user_id), "I")
        Printc(" - 群聊" + str(self.group_id), "I")
        Printc(" - 是否允许再次申请加群：" + str(self.reject_add_request), "I")
        print()  # 空行

        return json.dumps(
            {
                "action": "set_group_kick",
                "params": {
                    "group_id": self.group_id,
                    "user_id": self.user_id,
                    "reject_add_request": self.reject_add_request,
                },
            }
        )
