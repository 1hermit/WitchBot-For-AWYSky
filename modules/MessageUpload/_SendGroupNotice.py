import json

from modules.Application.printc import printc


class _SendGroupNotice:
    def __init__(self, group_id, content, imageURL):
        self.group_id = group_id
        self.content = message
        self.imageURL = imageURL

    def dump(self):
        printc("正在发送群聊公告", "I")
        printc(" - 消息内容：" + self.message, "I")
        printc(" - 发送到：" + str(self.group_id), "I")
        print()  # 空行

        self.message = "【小巫正】 \n" + self.message

        return (
            json.dumps(
                {
                    "action": "_send_group_notice",
                    "params": {
                        "group_id": self.group_id,
                        "message": self.message,
                        "image": self.imageURL,
                    },
                }
            )
            if self.imageURL != ""
            else json.dumps(
                {
                    "action": "_send_group_notice",
                    "params": {"group_id": self.group_id, "message": self.message},
                }
            )
        )
