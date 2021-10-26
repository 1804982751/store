

class InitPageDate:
    logon_success_data=[
        {"id":"a121212","username":"a","password":"1234567","password1":"1234567",
         "old":"20","sex":"女","type":"测试开发",
         "Email":"1804982667@qq.com","number":"15029561236",
         "expect":"成功"},
        {"id": "b121212", "username": "b", "password": "1234567", "password1": "1234567",
         "old":"20","sex":"女","type":"测试开发",
         "Email":"1804986891@qq.com","number":"15029562347",
         "expect":"成功"}
    ]

    logon_error_data=[
        {"id": "a", "username": "a", "password": "1234567", "password1": "123",
         "old":"15","sex":"男","type":"测试开发",
         "Email":"1804982711@qq.com","number":"15029563280",
         "expect":""},
        {"id": "b", "username": "b", "password": "1234567", "password1": "1234567",
         "old": "15", "sex": "女","type": "测试开发",
         "Email": "1804982711@qq.com", "number": "15029563280",
         "expect":""
         }
    ]


#从表格中读取写入数据————>>
# from xlutils.copy import copy
# workbook = xlwt.Workbook(encoding="utf-8")
# copywb =  copy(work)
# target = copywb.get_sheet(0)
# target.write(rows + 1,0,"总销售额：" +  str(round(sum,1)))
# target.write(rows + 1,count_index,"平均日销售量：" + str(avg))
# copywb.save("总数据.xls")













