# 需求：
# 1、打开qq首页
# 2、点击qq首页的邮箱按钮
# 3、在qq邮箱页面点击“基本版”
# 4、在点击账号密码登录ann
# 5、输入qq
# 6、输入密码
# 7、点击登录
# 希望处理嵌套的html页面的话，需要进行switch_to.frame()
# 1、切到内层：switch_to.frame()
# 2、从里层一层一层跳出frame,使用方法：driver.switch_to.parent_frame()
# 3、一次性跳出到主文档,使用方法：driver.switch_to.default_content()
# 导包
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from  selenium.webdriver.common.action_chains import ActionChains

# 创建浏览器对象
driver = webdriver.Firefox()

# 1、打开浏览器的指定地址,打开qq首页
driver.get("https://www.qq.com")

# 最大化显示页面
driver.maximize_window()

# 2、点击qq首页的邮箱按钮
driver.find_element(By.LINK_TEXT,"Qmail").click()
# 点完之后需要跳转到qq邮箱页面，加载比较慢，需要等待3s
time.sleep(3)

# 跳转到邮箱登录页面，driver对象也要切换过去
handles = driver.window_handles
driver.switch_to.window(handles[1])

# 3、在qq邮箱页面点击“基本版”，控制主文档
# driver.find_element(By.LINK_TEXT,"基本版").click()

# iframe标签嵌套的html文档,driver没法操作嵌套的文档。
# 需要切换driver对象到内层html页面中
# webdriver提供了三种切换方式
# 1、直接指定默认的iframe标签的name或者id属性
# driver.switch_to.frame("login_frame")
# 2、给出主文档的frame标签的索引，从1开始的（自己验证）
# driver.switch_to.frame(1)
# 3、指定frame标签对象
element = driver.find_element(By.NAME,"login_frame")
driver.switch_to.frame(element)
# driver.switch_to.parent_frame() # 切换到上一层
# driver.switch_to.default_content() #切换主文档

# 4、在点击账号密码登录
driver.find_element(By.LINK_TEXT,"帐号密码登录").click()
time.sleep(1)
# 5、输入qq
driver.find_element("id",'u').send_keys("287939828")
time.sleep(1)
# 6、输入密码
driver.find_element("id",'p').send_keys("123456789")
time.sleep(1)
# 7、点击登录
driver.find_element('id',"login_button").click()
# 等待3s

# 先将driver转到最内层
aa = driver.find_element(By.XPATH,'//*[@id="tcaptcha_iframe"]')
# print(aa)
driver.switch_to.frame(aa)
time.sleep(5)
on_element = driver.find_element(By.ID,'tcaptcha_drag_thumb')
# 按照一定的间隔进行拖动(不保证100%能通过)
ActionChains(driver).drag_and_drop_by_offset(on_element,170,0).perform()

time.sleep(3)

# 还是想点击“基本版”
# driver.switch_to.parent_frame()
# driver.switch_to.parent_frame()
# 直接切到主文档
driver.switch_to.default_content()
driver.find_element(By.LINK_TEXT,"基本版").click()

time.sleep(3)
# 退出浏览器
driver.quit()