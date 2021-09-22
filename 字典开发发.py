print("============================================")
print("==========中国工商银行账户管理系统   ============")
print("==========1、开户                 ===========")
print("==========2、取钱                 ===========")
print("==========3、存钱                 ===========")
print("==========4、转账                 ===========")
print("==========5、查询                 ===========")
print("==========6、退出                 ===========")
print("============================================")

bank={
    'Frank': {
        'password': '123456',
        'country': '中国',
        'province': '山东',
        'street': '001',
        'door': '002',
        'ran': 38340677,
        'money': 100
    },
    'Jason':{
        'password':'123456',
        'money':100
    }
}

bank_name="汉科软地球中国老牛湾分行"#全局变量

def bank_adduser(username,password,country,province,street,door,account,money):
    if username in bank :#如果一个变量在容器内就运行代码
        return 2
    if len(bank)>=100:
        return 3
    bank[username]={
        "account":account,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":money,
        "bank_name":bank_name
    }
    return 1

import random
def adduser():
    username=input("请输入您的用户名：")#局部变量
    password = input("请输入密码：")#print(bank['Frank']['password'])
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    account = random.randint(10000000,99999999)
    money = 0
    bankadd = bank_adduser(username,password,country,province,street,door,account,money)
    if bankadd == 1:
        print("添加用户成功，以下是您的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
    elif bankadd == 2:
        print("用户已存在")
    elif bankadd == 3:
        print("数据库已满")


#存钱
def deposit():
    deposit_user = input("请确认你存钱的账户(Frank):")
    if deposit_user in bank:
        deposit_money = int(input("请输入存钱金额:"))
        print(deposit_money)
        bank["Frank"]["money"] = bank["Frank"]["money"] + deposit_money
        print(bank)
    else:
        print("用户不存在")

#取钱
def git():
    git_username = input("用户账号(Frank)：")
    if git_username in bank:
        pass
    else:
        print("用户不存在")
        return begin
    git_password = input("用户密码(123456)：")
    if git_password == bank["Frank"]["password"]:
        pass
    else:
        print("密码错误")
        return begin
    git_money = int(input("取钱金额："))
    if git_money <= bank["Frank"]["money"]:
        bank["Frank"]["money"] = bank["Frank"]["money"] - git_money
        print(bank["Frank"])
    else:
        print("账户余额不足")

#转账
def transfer():
    transfer_user = input("输入登录账号Jason/Frank：")
    transfer_username = input("转账账号Jason/Frank：")
    if transfer_username in bank:
        pass
    else:
        print("用户不存在")
        return begin
    transfer_password = input("用户密码(123456)：")
    if transfer_password == bank[transfer_user]["password"]:
        pass
    else:
        print("密码错误")
        return begin
    transfer_money = int(input("转账金额："))
    if transfer_money <= bank[transfer_user]["money"]:
        bank[transfer_username]["money"] = bank[transfer_username]["money"] + transfer_money
        bank[transfer_user]["money"] = bank[transfer_user]["money"] - transfer_money
        print("转账成功")
        print(bank)
    else:
        print("账户余额不足")

#查询功能
def search():
    account = input("请输入要查询的账号：")
    password = input("请输入要查询的密码：")
    if account in bank:
        if password != bank[account]["password"]:
            print("密码错误！")
        else:
            print("查询成功！")
            info = '''
              ------------个人信息------------
                    用户名:%s
                    账号:%s
                    密码:%s
                    国籍:%s
                    省份:%s
                    街道:%s
                    门牌号:%s
                    余额:%s
                    开户行名称:%s
            '''
            print(info % (bank[account]["username"], bank[account]["account"],bank[account]["country"],
                          bank[account]["password"], bank[account]["province"], bank[account]["street"],
                          bank[account]["door"],bank[account]["money"],bank[account]["bank_name"]))
    else:
        print("用户名不存在！")





while True:
    begin=input("请输入你的业务命令（1、2、3）：")
    if begin == "1":
        adduser()
    elif begin == "2":
        git()
    elif begin == "3":
        deposit()
    elif begin == "4":
        transfer()
    elif begin == "5":
        search()
    elif begin == "6":
        print("退出系统")
    else:
        print("输入错误")
        break







