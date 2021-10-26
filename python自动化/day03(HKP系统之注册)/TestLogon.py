
from selenium import webdriver
from unittest import TestCase
from ddt import ddt
from ddt import data

from LogonOperation import LogonOperation
from initPage import InitPageDate


@ddt
class TestLogon(TestCase):
    #在每个用例执行之前执行
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(r"http://localhost:8080/HKR/")
        self.driver.find_element_by_link_text("新来的童鞋来这里注册一下哦").click()
    #在每个用例执行之后执行
    def tearDown(self) -> None:
        self.driver.quit()

    @data(*InitPageDate.logon_success_data)
    def testLogonSuccess(self,testdata):
        id = testdata["id"]
        username = testdata["username"]
        password = testdata["password"]
        password1 = testdata["password1"]
        old = testdata["old"]
        sex = testdata["sex"]
        type = testdata["type"]
        Email = testdata["Email"]
        number = testdata["number"]
        expect=testdata["expect"]

        a=LogonOperation(self.driver)
        #登录操的系列操作
        a.logon(id,username,password,password1,old,sex,type,Email,number)

        result = a.getSuccess_result()

        self.assertEqual(result,expect)

    @data(InitPageDate.logon_error_data)
    def testLogonError(self,testdata):
        id = testdata["id"]
        username = testdata["username"]
        password = testdata["password"]
        password1 = testdata["password1"]
        old = testdata["old"]
        sex = testdata["sex"]
        type = testdata["type"]
        Email = testdata["Email"]
        number = testdata["number"]
        expect = testdata["expect"]

        a = LogonOperation(self.driver)

        a.logon(id,username,password,password1,old,sex,type,Email,number)

        result = a.getError_result()

        self.assertEqual(result,expect)






