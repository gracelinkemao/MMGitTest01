# 对于alert框，只需要获取提示信息（一般可以用于断言）
# 百度首页的保存设置功能获取弹框的提示信息--text
# 点击确定按钮--accept()
# 点击取消按钮--dismiss()
# 输入提示信息--send_keys()
# 切换driver处理对象给弹窗- switch_to.alert
# 处理完弹出之后，driver对象会自动回到当前浏览器窗口中


from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# driver.get(r"e:\prompt.html")
driver.maximize_window()
# 封装鼠标对象，执行悬停动作
element = driver.find_element("id","s-usersetting-top")
ActionChains(driver).move_to_element(element).perform()

time.sleep(2)
# 5s之后点击搜索设置按钮
driver.find_element(By.LINK_TEXT,"搜索设置").click()
time.sleep(2)
# 设置搜索框提示参数：不显示
driver.find_element(By.XPATH,'//*[@id="s1_2"]').click()
# 点击保存按钮
driver.find_element(By.LINK_TEXT,"保存设置").click()

time.sleep(3)
# 就会弹出警告框（没法定位到它）
# 获取警告框的文本信息(先把driver控制权交给alert，才能对其进行处理)
# 已经记录下您的使用偏好
# 第一种写法（繁琐、重复切换driver）
# texts  = driver.switch_to.alert.text
# print(texts)
# # 点击警告框的确定按钮
# driver.switch_to.alert.accept()
# 第二种（建议用这种）
alertDriver = driver.switch_to.alert
# 获取文本
texts = alertDriver.text
# print(texts)
alertDriver.accept()  # 点击确定
# alertDriver.dismiss() # 点击取消


time.sleep(3)
driver.quit()