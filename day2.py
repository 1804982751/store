# noinspection PyUnresolvedReferences
print("开始游戏请按1")
print("结束游戏请按Q")
import random
ran=random.randint(0,90)
print(ran)
a=1
账户资金=10000
print("账户资金=",账户资金)
num = int(input("请输入一个数字"))
while True:
    if ran<num:
        账户资金=账户资金-500
        print("你猜小了，账户资金=", 账户资金)
    elif ran>num:
        账户资金=账户资金-500
        print("你猜大了，账户资金=", 账户资金)
    else :
        账户资金=账户资金*1.1
        print("ok，账户资金=", 账户资金)
        break