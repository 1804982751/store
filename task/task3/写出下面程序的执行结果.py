#输入54321时，写出下面程序的执行结果
num = int(input("请输入一个数："))
while num != 0:
    print(num % 10)
    num = num // 10
