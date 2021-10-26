'''
    专门存储数据源
    任务1：
        使用自动化对HKR系统进行测试。
    任务2：
        将参数化数据集中写到excel表里，并使用excel表参数化。
        将测试结果进行回写到excel表里。
'''

import xlrd
import xlwt


class InitPageData:
    login_success_data = xlrd.read(r'D:\gitbash\demo\python自动化\day03(HKP系统之登录)')

    # login_success_data = [
    #     {"username": "jason", "password": "1234567", "expect": "Student Login"},
    #     {"username": "不再爱了", "password": "1234567", "expect": "Student Login"}
    # ]
    # login_error_data = [
    #     # id :'msg_uname'
    #     {"username": "jason", "password": "12345678", "expect": "账户名错误或密码错误!别瞎弄!"},
    #     {"username": "jason112234", "password": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"}
    # ]
    from xlutils.copy import copy
    data = xlrd.open_workbook('excel_test.xls', formatting_info=True)
    excel = copy(wb=data)  # 完成xlrd对象向xlwt对象转换
    excel_table = excel.get_sheet(0)  # 获得要操作的页
    table = data.sheets()[0]
    nrows = table.nrows  # 获得行数
    ncols = table.ncols  # 获得列数
    values = ["E", "X", "C", "E", "L"]  # 需要写入的值
    for value in values:
        excel_table.write(nrows, 1, value)  # 因为单元格从0开始算，所以row不需要加一
        nrows = nrows + 1
    excel.save('excel_test.xls')








# from xlutils.copy import copy
# workbook = xlwt.Workbook(encoding="utf-8")
# copywb =  copy(work)
# target = copywb.get_sheet(0)
# target.write(rows + 1,0,"总销售额：" +  str(round(sum,1)))
# target.write(rows + 1,count_index,"平均日销售量：" + str(avg))
# copywb.save("总数据.xls")






