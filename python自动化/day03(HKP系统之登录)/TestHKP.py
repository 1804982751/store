from selenium import webdriver
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from InitPage import InitPageData
from LoginOperation import LoginOpera
import time

'''
    成功的用例
    失败的用例
'''
@ddt
class TestLogin(TestCase):
    #在每个测试用例执行前执行
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/HKR")
        self.driver.maximize_window()

    # 在每个用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()


    @data(*InitPageData.login_success_data)
    def testLoginSuccess(self,testdata):
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        time.sleep(2)
        loginopr = LoginOpera(self.driver)
        #  登陆的三项操作
        loginopr.login(username,password)

        result = loginopr.getSuccess_result()
        time.sleep(2)

        self.assertEqual(result,expect)

    @data(*InitPageData.login_error_data)
    def testLoginError(self, testdata):
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]
        time.sleep(2)
        loginopr = LoginOpera(self.driver)
        #  登陆的三项操作
        loginopr.login(username, password)

        result = loginopr.getError_result()
        time.sleep(2)

        # 将测试结果回写到excel表里，xlwt
        self.assertEqual(result, expect)












