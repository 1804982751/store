import time

from selenium.webdriver.support.select import Select

class LogonOperation:
    #在创建对象的时候必定调用
    def __init__(self,driver):
        self.driver=driver

    def logon(self,id,username,password,password1,old,sex,type,Email,number):
    #注册1.0
        self.driver.find_element_by_xpath('//*[@name="loginname"]').send_keys(id)
        self.driver.find_element_by_xpath('//*[@name="username"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@name="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@name="reloginpass"]').send_keys(password1)

        self.driver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[5]').click()
        time.sleep(3)
    #注册2.0
        self.driver.find_element_by_xpath('//*[@id="valid_age"]').send_keys(old)

        self.driver.find_element_by_xpath('//*[@id="msform"]/fieldset[2]/select[1]').send_keys("女")
        # sel=Select(sele)
        # sel.select_by_value(sex)

        self.driver.find_element_by_xpath('//*[@id="classname"]').send_keys("数学")
        # sel=Select(sele)
        # sel.select_by_value(type)

        self.driver.find_element_by_xpath('//*[@id="msform"]/fieldset[2]/input[3]').click()
        time.sleep(3)
    #注册3.0
        self.driver.find_element_by_xpath('//*[@id="reg_mail"]').send_keys(Email)
        self.driver.find_element_by_xpath('//*[@id="reg_phone"]').send_keys(number)

        self.driver.find_element_by_xpath('//*[@id="btn_reg"]').click()
        time.sleep(3)

    #获取成功实际数据
    def getSuccess_result(self):
        return self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]').text
    #获取失败实际数据
    def getError_result(self):
        return 0








