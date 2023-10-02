import datetime


def Printc(string, printType="error"):  # 函数:打印带提示信息和颜色的文字
    nowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 获取当前时间
    printType = printType.lower()
    if printType == "e":
        print("[" + nowTime + "][WitchBot 错误] " + string)
    elif printType == "w":
        print("[" + nowTime + "][WitchBot 警告] " + string)
    elif printType == "i":
        print("[" + nowTime + "][WitchBot 信息] " + string)
    elif printType == "d":
        print("[" + nowTime + "][WitchBot 调试] " + string)
    else:
        print("[" + nowTime + "][WitchBot 信息] " + string)
