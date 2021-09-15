i=0
import random
list = ["张三", "李四", "王五", "赵六", "小七", "小八", "小九"]
while True :
    i=i+1
    num = random.randint(0, len(list))
    print(list[num])
    int(input("惩罚次数："))
else:
    print("Goodbye!")



