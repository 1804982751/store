'''
    类：只能做页面的逻辑操作，其他的数据不应该出现
'''
class LoginOpera:

    # 在创建对象的时候必定调用
    def __init__(self,driver):
        self.driver = driver

    # 登陆的三项操作
    def login(self,username,password):
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

    # 获取成功实际数据
    def getSuccess_result(self):
        return self.driver.title

    # 获取失败的实际数据
    def getError_result(self):
        return  self.driver.find_element_by_xpath("//*[@id='msg_uname']").text


