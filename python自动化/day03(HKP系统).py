from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r"http://localhost:8080/HKR")
#1.正常登录
username="jason"
password=1234567
driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
driver.find_element_by_xpath("//*[@id='submit']").click()

#2.换头像
time.sleep(2)
driver.find_element_by_xpath("//*[@id='img']").click()
#系统头像
picture = driver.find_elements_by_class_name('default_picture')
for i in picture:
    i.click()

#自定义头像
# driver.find_element_by_xpath("//*[@id='lablefile']").send_keys(r"D:\壁纸\壁纸\5a630f21a5045.jpg")
# driver.find_element_by_xpath("//*[@id='pic_btn']").click()

# driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[3]/a[2]").click()



#3.修改个人信息
time.sleep(2)
driver.find_element_by_xpath("//*[@id='_easyui_tree_8']").click()
driver.find_element_by_xpath('//*[@id="_easyui_textbox_input1"]').send_keys(76)
time.sleep(2)
sele = driver.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[5]/td[2]/select')
sel = Select(sele)
sel.select_by_value("女")
#点提交
driver.find_element_by_xpath('//*[@id="btn_modify"]').click()


#4.评价表//*[@id="form_table"]/tbody/tr[2]/td[2]/select
time.sleep(2)
driver.find_element_by_xpath('//*[@id="tt"]/div[1]/div[3]/ul/li/a/span[2]').click()
time.sleep(2)
sele = driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[2]/td[2]/select')
sel =Select(sele)
sel.select_by_value('9')
time.sleep(2)
sele = driver.find_element_by_xpath('//*[@id="tea_td"]/select')
sel = Select(sele)
sel.select_by_value("贾生")
#写建议
driver.find_element_by_xpath('//*[@id="textarea"]').send_keys('无')
#点提交
driver.find_element_by_xpath('//*[@id="subtn"]').click()
#点弹框确定
#driver.switch_to.alert.accept()-->不行
driver.find_element_by_xpath('/html/body/div[7]/div[3]/a/span/span').click()


time.sleep(5)
driver.quit()




