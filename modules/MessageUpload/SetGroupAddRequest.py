import json

from modules.Application.Printc import Printc


class SetGroupAddRequest:
    def __init__(self, flag, sub_type, approve, reason):
        self.flag = flag
        self.sub_type = sub_type
        self.approve = approve
        self.reason = reason

    def dump(self):
        Printc("正在处理加群请求", "I")
        Printc(" - 是否通过：" + str(self.approve), "I")
        Printc(" - 请求理由：" + str(self.reason), "I")
        print()  # 空行

        return json.dumps(
            {
                "action": "_send_group_notice",
                "params": {
                    "flag": self.flag,
                    "sub_type": self.sub_type,
                    "approve": self.approve,
                    "reason": self.reason,
                },
            }
        )
