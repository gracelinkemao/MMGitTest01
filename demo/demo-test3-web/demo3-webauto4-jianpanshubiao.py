#  键盘鼠标操作
'''
'''
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


#  创建浏览器的对象
driver = webdriver.Chrome()
#  打开百度页面
driver.get("https://www.baidu.com")

driver.find_element(By.ID, "kw").send_keys("测试allen说")
element = driver.find_element(By.ID, "su") # 先获取鼠标点击的对象
# 2) 封装ActionChains类
# ActionChains(driver).click(on_element)
# ActionChains(driver).context_click(on_element)
# 下面这俩需要掌握：
# ActionChains(driver).move_to_element(on_element)
# ActionChains(driver).drag_and_drop(source,target)
ActionChains(driver).click(element)  # 鼠标绑定浏览器并执行点击操作
# 3)执行封装的鼠标对象 perform()
ActionChains(driver).click(element).perform()
# ActionChains(driver).move_to_element(element).perform() # 悬停

# 2、键盘操作
# keys模块的Keys类中定义了键盘的主要功能键常量。
# 格式：Keys.XXX
# 通过send_keys()来发送这些功能按键、组合键等。
# driver.find_element(By.ID,"xx").send_keys(Keys.SPACE)

#   driver.quit()
#   它是关闭百度页面还是百度新闻??
driver.close()