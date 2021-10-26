import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r"http://8.129.91.152:8765/")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/span[1]/a").click()

driver.find_element_by_xpath("//*[@id='phone']").send_keys("15029560009")

#图片验证码元素
# a=driver.find_element_by_link_text("//8.129.91.152:8765/Service/Sms/member_vcode")
# driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[3]/input").send_keys(a)

driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[4]/input").send_keys("123aaa!!!")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[5]/label/input").click()


time.sleep(20)

#短信验证码元素
# driver.find_element('link text','获取短信验证码').click()
# text = driver.find_element('xpath', '//*[@id="layui-layer1"]/div').text
# driver.find_element('xpath', '//input[@name="code"]').send_keys(text[-4:])


#点击下一步
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[6]/button").click()

# 系统自动分配
time.sleep(3)
driver.find_element_by_xpath("//*[@class='layui-layer-btn1']").click()




