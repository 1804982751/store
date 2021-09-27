from bank表导入 import update
from bank表导入 import select




print("============================================")
print("==========中国工商银行账户管理系统   ============")
print("==========1、开户                 ===========")
print("==========2、取钱                 ===========")
print("==========3、存钱                 ===========")
print("==========4、转账                 ===========")
print("==========5、查询                 ===========")
print("==========6、退出                 ===========")
print("============================================")


bank_name="汉科软地球中国老牛湾分行"#全局变量

def bank_adduser(username,password,country,province,street,door,money,registerDate,bankname):
    sql = 'select count(*) from t_person'
    param=[]
    data = select(sql,param)
    if data >=100 :
        return 3

    sql1='select * from t_person where username = %s'
    param1 = [username]
    data1 = select(sql1,param1,mode='one')[0]
    if len(data1) > 0:#如果一个变量在容器内就运行代码
        return 2

    sql2="insert into t_person values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [username,password,country,province,street,door,money,registerDate,bankname]
    update(sql2,param2)
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
    registerDate = input("请输入日期：")
    bankname = input("请输入开户银行名称：")
    bankadd = bank_adduser(username,password,country,province,street,door,money,registerDate,bankname)
    sql = "select * from t_person username=%s"
    param = [username]
    data = select(sql, param)
    if len(data) ==0:
        print("添加用户成功，以下是您的信息")
        sql1 = "INSERT INTO person VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param1 = [username,password,country,province,street,door,money,registerDate,bankname]
        data1 = select(sql1, param1)
        print(data1)

    elif len(data) > 0 :
        print("用户已存在")
    else:
        print("数据库已满")


#存钱（报错）
def deposit111():
    deposit_user = input("请确认你存钱的账户(Frank):")
    sql = 'select * from t_person where username = %s'
    param = [deposit_user]
    data = select(sql, param)
    if deposit_user in data:
        deposit_money = int(input("请输入存钱金额:"))
        print(deposit_money)
        sql1 = 'update t_person set money=money+%s where username=%s'
        param1 = [deposit_money,deposit_user]
        update(sql1, param1)
        sql1 ='select * from t_person where username = deposit_user'
        param1 = []
        data1 = select(sql1,param1)
        for i in data1:
            print(i)
    else:
        print("用户不存在")
#存钱
def deposit():
    username = input('请输入您的用户名')
    sql = "select * from t_person where username = %s"
    param = [username]
    name = select(sql, param)
    if len(name) == 0:
        print('用户名输入错误')
    else:
        deposit_money = int(input('请输入您要存入的金额'))
        sql = "UPDATE t_person SET money = money + %s  WHERE username = %s"
        param = [deposit_money, username]
        update(sql, param)

#取钱
def git():
    git_username = input("用户账号(Frank)：")
    sql = 'select * from t_person where username = %s'
    param = [git_username]
    data = select(sql, param)
    if len(data)>0:
        git_password = input("用户密码(123456)：")
        sql1 = 'select password from t_person where username = %s'
        param1 = [ git_username]
        data1 = select(sql1, param1)
        if len(data1) > 0:
            git_money = int(input("取钱金额："))
            sql2 = 'select money from t_person where username = %s '
            param2 = [ git_username]
            data2 = select(sql2, param2)
            if len(data2) > 0:
                sql3 = 'update t_person set money = money - %s where usename = %s '
                param3 = [git_money, git_username]
                data3 = select(sql3, param3)
                print(data3)
            else:
                print("账户余额不足")
        else:
            print("密码错误")
    else:
        print("用户不存在")



#转账
def transfer():
    n = 4
    m = 0
    transfer_username = int(input("请输入您的账号"))
    sql = "select * from t_person where username = %s"
    param = [transfer_username]
    data = select(sql, param)
    if len(data) > 0:
        transfer_username2 = int(input("请输入您要转账的账号："))
        sql1 = "select * from t_person where username = %s"
        param1 = [transfer_username2]
        data1 = select(sql1, param1)
        if len(data1) > 0:
            password = int(input("请输入您的密码"))
            sql2 = 'select password from t_person  where username = %s'
            param2 = [transfer_username]
            data2 = select(sql2, param2, mode='one')[0]
            while True:
                if password == data2:
                    money = int(input("请输入您要转账的金额："))
                    sql3 = 'select money from t_person where username = %s'
                    param3 = [transfer_username]
                    data3 = select(sql3, param3, mode='one')[0]
                    if money > data3:
                        print('您的余额不足，转账失败！')
                        break
                    else:
                        sql4 = 'update t_person set money = money - %s  where username  = %s'
                        param4 = [money,transfer_username]
                        update(sql4, param4)
                        sql5 = 'select money from t_person  where username = %s'
                        param5 = [transfer_username]
                        data4 = select(sql5, param5,mode='one')[0]
                        print("转账成功！您的余额为：", data4)
                        sql6 = "update t_person  set  money = money + %s  where username = %s"
                        param6 = [money,transfer_username2]
                        update(sql6,param6)
                        break
                else:
                    print("密码错误！您还有", n - 1, "次机会")
                    n -= 1
                    m += 1
                    if m == 4:
                        print("您的账号今天不能继续登录！")
                        break
        else:
            print("您输入的账号不存在")
    else:
        print("您输入的账号不正确！")



#查询功能
def search():
    username = input("请输入要查询的账号/姓名：")
    sql= 'select * from t_person where username=%s'
    param = [username]
    data = select(sql,param)
    if len(data)>0:
        password = input("请输入要查询的密码：")
        sql1 = 'select * from t_person where username=%s'
        param1 = [username]
        data1 = select(sql1, param1)
        if len(data1)<0:
            print("密码错误！")
        else:
            print("查询成功！")
            print(data1)
    else:
        print("用户名不存在！")





while True:
    begin=input("请输入你的业务命令（1、2、3）：")
    if begin == "1":
        adduser()  #添加用户
    elif begin == "2":
        git()   #取钱
    elif begin == "3":
        deposit()   #存钱
    elif begin == "4":
        transfer()    #转账
    elif begin == "5":
        search()  #查询
    elif begin == "6":
        print("退出系统")
    else:
        print("输入错误")
        break







