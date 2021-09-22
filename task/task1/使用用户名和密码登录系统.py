print("注：用户名root，密码admin，允许输入错误次数3次。")
_username = 'root'
_password = 'admin'
for i in range(1, 4):#利用range()函数可以打印任意区间的数值
    username = input("请输入你的用户名：")
    password = input('请输入你的密码：')
    if username == _username and password == _password:
        print("登录成功！")
        break
    else:
        print("您的用户名或密码输入错误！")
else:
    print("您输入次数过多，账户锁定！")