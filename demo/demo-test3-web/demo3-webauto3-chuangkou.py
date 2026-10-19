#  浏览器窗口操作
'''
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#  创建浏览器的对象
driver = webdriver.Chrome()

#  打开百度页面
driver.get("https://www.baidu.com")

#  获取当前页面的url,并打印出来（driver.current_url）
url = driver.current_url
#  当前页面的url地址为：https://www.baidu.com/
print("当前页面的url地址为：%s" % url)
# 1‐调整窗口的大小
# driver.set_window_size(500,500)
# 最大化\最小化
# driver.maximize_window()
# driver.minimize_window()
# driver.set_window_position(500,500)


# 2‐窗口的前进和后退和刷新:  forward()和back()
#   driver.find_element("id","kw").send_keys("测试allen说")
#   driver.find_element("id","su").click()17 #  time.sleep(2)
#   driver.back()
#   time.sleep(2)
#   driver.forward()
#   time.sleep(2)
#   #  刷新功能
#   driver.refresh()
#   time.sleep(2)
#   #  3‐通过截图保存附件,默认文件格式是png格式
#   driver.save_screenshot(r"e:\aaa.png")

#   #  关闭和延时
#   time.sleep(5)

#   4‐不就是关闭浏览器吗?close()\quit()
#   quit():直接关闭浏览器,不管你开启了几个窗口
#   close():  如果有多个窗口开启的话,关闭当前的窗口;如果只有一个窗口就是关闭浏览


#   点击新闻按钮
driver.find_element(By.LINK_TEXT, "新闻").click()
time.sleep(2)


 # 代码执行到这一行，已经有两个窗口啦，现在可以获取两个窗口的名字
 # 获取当前窗口的名字（CDwindow‐1CB3D1E68C6A3A121A15D95D77E24F70）
 #handle1 = driver.current_window_handle
 # print(handle1)

 # 还可以获取当前浏览器所有窗口的名字
 # ['CDwindow‐1CB3D1E68C6A3A121A15D95D77E24F70', 'CDwindow‐36D84F294937A5D7B54609D2929F64']
handles = driver.window_handles
 # print(handles)
 # 将driver和第二个窗口绑定一下
driver.switch_to.window(handles[1])

 # 点击新闻页面的新闻：跨区公共交通恢复
 # 定位不到该超链接，代码终止，连浏览器都关不了。
driver.find_element(By.LINK_TEXT,"跨区公共交通恢复").click()
time.sleep(2)

#   driver.quit()
#   它是关闭百度页面还是百度新闻??
driver.close()