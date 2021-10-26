'''
    自动测试报告实现了!
    unittest:单元测试框架：
    参数化，测试。
    1.子类继承unittest的TestCase
    2.写用例： testXxxxxx
'''


from unittest import TestCase
from calc import calc
class Testcalc(TestCase):

    #写第一条用例
    def testAdd1(self):
        a = 6
        b = 5
        s = 11
        c= calc()
        sum=c.add(a,b)
        #断言
        self.assertEqual(s,sum)

    #写第二条用例
    def testAdd2(self):
        # 准备数据
        a = -6
        b = -5
        s = -11
        #
        c= calc()
        sum = c.add(a,b)

        #断言
        self.assertEqual(s,sum)

    #写第三条用例
    def testAdd3(self):
        # 准备数据
        a = -6
        b = 5
        s = -1
        #
        c = calc()
        sum = c.add(a,b)

        #断言
        self.assertEqual(s,sum)

    #写第四条用例
    def testAdd4(self):
        # 准备数据
        a = 6
        b = -5
        s = 1
        #
        c = calc()
        sum = c.add(a,b)

        #断言
        self.assertEqual(s,sum)








