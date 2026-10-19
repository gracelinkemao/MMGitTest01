from selenium import webdriver
#ui--模块，WebDriverWait是个类
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver.implicitly_wait(10)
driver.get("http://www.baidu.com")



try:
    driver.find_element_by_id("kw").send_keys("selenium")
    element = WebDriverWait(driver,10,0.5,ignored_exceptions=None).until(EC.presence_of_element_located((By.ID,"su1")),"找不到")

    element.click()
    # 强制等待 定了10S，就一定要等10S
    time.sleep(3)
    # 隐式等待 定了10，但3S成功就只会等待3S。但超过10S异常
    # driver.implicitly_wait(10)
    # 显示等待 webDriverWait(driver,10,0.5) 定10S，每0.5S刷新 仅关心的元素进行等待
    # element = WebDriverWait(driver, 10, 0.5, ignored_exceptions=None).until(EC.presence_of_element_located((By.ID, "su")), "找不到")
    # element.click()

except Exception as e:
    print(e)

driver.quit()