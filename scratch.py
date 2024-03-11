import random
num = random.randint(1,100)
#print(num)
count = 0
flag = True
while flag:
    guess_num = int(input("请输入您猜测的数字:"))
    count += 1
    if guess_num == num:
        print("恭喜您 猜中了")
        flag = False
    else :
        if guess_num < num:
            print("对不起，您猜小了")
        else:
            print("对不起,您猜大了")
print(f"您一共猜了{count}机会")





