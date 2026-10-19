# 案例4：将一个元素拖动到另外一个页面元素上去 （比如图形拖动验证码）
# 1、导包、创建对象、打开百度首页
from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("file:///E:/%E9%BC%A0%E6%A0%87%E6%8B%96%E6%8B%BD%E6%A1%88%E4%BE%8B/%E9%BC%A0%E6%A0%87%E6%93%8D%E4%BD%9C%E6%A1%88%E4%BE%8B.html")
driver.maximize_window()

# 拖拽一个元素到另一个元素上去
# 源元素：sourceElement
# 目标元素：targetElement
sourceElement = driver.find_element(By.ID,"draggable")
targetElement = driver.find_element(By.ID,"droppable")
# 封装鼠标对象并执行
ActionChains(driver).drag_and_drop(sourceElement,targetElement).perform()

time.sleep(3)
driver.quit()