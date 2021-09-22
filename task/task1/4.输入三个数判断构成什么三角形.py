print("===================================")
print("请输入以下边长，我们会告诉您是否可以构成三角形！")
b=int(input("请输入第一个任意整数边长："))
c=int(input("请输入第二个任意整数边长："))
d=int(input("请输入第三个任意整数边长："))
print(b,c,d,)
if b+c > d and b+d > c and c+d > b:
    if b == c and c != d:
        print("结果：等腰三角形")
    elif b == d and b != c:
        print("结果：等腰三角形")
    elif c == d and c != b:
        print("结果：等腰三角形")
    elif b == c == d:
        print("结果：等边三角形")
    elif b ^ 2 + c ^ 2 == d ^ 2 and b != c:
        print("结果：直角（非等腰）三角形")
    elif c ^ 2 + d ^ 2 == b ^ 2 and c != d:
        print("结果：直角（非等腰）三角形")
    elif b ^ 2 + c ^ 2 == d ^ 2 and b != c:
        print("结果：直角（非等腰）三角形")
    elif b ^ 2 + c ^ 2 == d ^ 2 and b == c:
        print("结果：等腰直角三角形")
    elif c ^ 2 + d ^ 2 == b ^ 2 and c == d:
        print("结果：等腰直角三角形")
    elif b ^ 2 + d ^ 2 == c ^ 2 and b == d:
        print("结果：等腰直角三角形")
    else:
        print("结果：普通三角形")
else:
    print("结果：不能构成三角形")