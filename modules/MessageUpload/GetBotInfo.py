import json

from modules.Application.Printc import Printc


class GetBotInfo:
    Printc("正在获取机器人信息", "I")
    print()  # 空行

    def dump():
        return json.dumps(
            {
                "action": "get_login_info",
            }
        )
