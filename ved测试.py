
money = 5000000
name = None
name = input("您好，请输入您的姓名")
def query(show_header):
    if show_header:
        print("------查询余额------")
    print(f"{name}您好，您的余额剩余为{money}")

def saving(num):
    global money
    money += num
    print("------存款------")
    print(f"{name},您好，您存款{num}元成功。")

    query(False)

def get_money(num):
    global money
    money -= num
    print("------取款------")
    print(f"{name}，您好，您取款{money}成功")

    query(False)

def main():
    print("------主菜单------")
    print(f"{name}，您好，欢迎来到西安工程大银行，请选择操作：")
    print("查询余额\t{输入1}")
    print("存款\t\t{输入2}")
    print("取款\t\t{输入3}")
    print("退出\t\t{输入4}")
    return input("请输入您的选择")

while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = int(input("您想要存入多少钱？，请输入："))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取出多少钱？，请输入："))
        get_money(num)
        continue
    else:
        print("程序退出啦")
        break







    


             

