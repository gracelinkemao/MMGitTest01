# 对键盘的操作，通过键盘输入字符、快捷键、组合键等
# 所有的键盘输入都是通过send_keys()来实现的
# 键盘事件案例：
# 1、百度“seleniumm”
# 2、删除多输入的m   -->Keys.BACk_SPACE
# 3、再输入“空格 教程”
# 4、ctrl+a，全选文本框内容
# 5、ctrl+x，剪切选择的内容
# 6、ctrl+v，粘贴复制的内容
# 7、回车代替单击，完成搜索
# 8、退出浏览器

# 导包
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 1、百度“seleniumm”
driver.find_element(By.ID,"kw").send_keys("seleniumm")
# 2、删除多输入的m   -->Keys.BACk_SPACE
driver.find_element(By.ID,"kw").send_keys(Keys.BACKSPACE)
time.sleep(2)
# 3、再输入“空格 教程”
driver.find_element(By.ID,"kw").send_keys(Keys.SPACE)
time.sleep(2)
driver.find_element(By.ID,"kw").send_keys("教程")
time.sleep(2)
# 4、ctrl+a，全选文本框内容
driver.find_element(By.ID,"kw").send_keys(Keys.CONTROL,"a")
time.sleep(2)
# 5、ctrl+x，剪切选择的内容
driver.find_element(By.ID,"kw").send_keys(Keys.CONTROL,"x")
time.sleep(2)
# 6、ctrl+v，粘贴复制的内容
driver.find_element(By.ID,"kw").send_keys(Keys.CONTROL,"v")
time.sleep(2)
# 7、回车代替单击，完成搜索
driver.find_element(By.ID,"kw").send_keys(Keys.ENTER)
time.sleep(2)
# 8、退出浏览器
driver.quit()