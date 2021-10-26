#生成测试报告
from HTMLTestRunner import HTMLTestRunner  #界面报告运行，给用例，返回报告
import unittest
#1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"D:\gitbash\demo\day13(计算器测试发送报告)",pattern="Test*.py")
#2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title= '邮件发送练习',
    description= '计算器报告',
    verbosity= 1,
    stream= open(file='邮件练习.html',mode='w+',encoding='utf-8')
)
#3.运行用例
runner.run(tests)





