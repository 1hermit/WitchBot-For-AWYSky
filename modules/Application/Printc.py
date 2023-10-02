import datetime


def Printc(string, printType="error"):  # 函数:打印带提示信息和颜色的文字
    nowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 获取当前时间
    printType = printType.lower()
    if printType == "e":
        print("[" + nowTime + "]\033[1;31m[WitchBot 错误]\033[0m " + string)
    elif printType == "w":
        print("[" + nowTime + "]\033[1;33m[WitchBot 警告]\033[0m " + string)
    elif printType == "i":
        print("[" + nowTime + "]\033[1;32m[WitchBot 信息]\033[0m " + string)
    elif printType == "d":
        print("[" + nowTime + "]\033[1;36m[WitchBot 调试]\033[0m " + string)
    else:
        print("[" + nowTime + "]\033[1;32m[WitchBot 信息]\033[0m " + string)
