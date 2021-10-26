'''
任务1：
    完成除了滑动验证之外的其他的操作。
任务2：
    京东搜索一个商品，点击查看详情。
    苏宁：搜索一个商品，点击商品详情 --> 添加购物车 --> 结算。
'''
#注意：各模块尽量不同时运行


#1.弹框的验证
from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r"D:/gitbash/course/python自动化/day01/练习的html/弹框的验证/dialogs.html")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='confirm']").click()

#进入弹窗，点击确定
driver.switch_to.alert.accept()

#注：进入弹窗，点击取消
# driver.switch_to.alert.dismiss()

#退出窗口
driver.quit()




#2.上传文件和下拉列表的验证
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(r"D:/gitbash/course/python自动化/day01/练习的html/上传文件和下拉列表/autotest.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='accountID']").send_keys("chen")
driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("123456")
driver.find_element_by_xpath("//*[@value='shanxi']").click()
driver.find_element_by_xpath("//*[@id='sexID2']").click()
driver.find_element_by_xpath("//*[@value='Auterm']").click()
driver.find_element_by_xpath("//input[@name='file' and @type='file']").send_keys(r"D:/壁纸/壁纸/5a630f21a5045.jpg")
driver.find_element_by_xpath("//*[@id='buttonID']").click()


#3.跳转页面
from selenium import webdriver
driver=webdriver.Chrome()
driver.get(r"D:/gitbash/course/python自动化/day01/练习的html/跳转页面/pop.html")
driver.find_element_by_xpath("//*[@id='goo']").click()


# 4.frame验证
from  selenium import webdriver
driver=webdriver.Chrome()
driver.get(r"D:/gitbash/course/python自动化/day01/练习的html/frame.html")
driver.find_element_by_xpath("//*[@id='input1']").send_keys("chen")


# 5.main验证
from selenium import webdriver
driver=webdriver.Chrome()
driver.get(r"D:/gitbash/course/python自动化/day01/练习的html/main.html")
#最大化窗口
driver.maximize_window()
#跳转到frame框架
driver.switch_to.frame("frame")
driver.find_element_by_xpath("//*[@id='input1']").send_keys("chen")



#6.京东商城搜索商品
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get(r"https://www.jd.com")

driver.maximize_window()

driver.find_element_by_xpath("//*[@type='text']").send_keys("电子琴")
driver.find_element_by_xpath("//*[@class='button']").click()

time.sleep(5)
driver.find_element_by_xpath("//*[@SRC='//img11.360buyimg.com/n7/jfs/t1/121986/32/7280/151628/5f113278E492d0334/c50b8189e901adbb.jpg']").click()

time.sleep(5)
driver.quit()


#7.苏宁搜索商品-->添加购物车-->结算
from selenium import webdriver

import time

driver=webdriver.Chrome()
driver.get(r"https://www.suning.com")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("华为手机")

driver.find_element_by_xpath("//*[@id='searchSubmit']").click()

time.sleep(5)

driver.find_element_by_xpath("//*[@src='//imgservice.suning.cn/uimg1/b2c/image/2bFTR4KGXj-CbiDrDHcZ0Q.png_400w_400h_4e']").click()

time.sleep(5)

data=driver.window_handles
driver.switch_to.window(data[1])

driver.find_element_by_xpath("//*[@id='addCart']").click()

time.sleep(5)
driver.quit()







