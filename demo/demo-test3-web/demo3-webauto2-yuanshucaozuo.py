#  导包 元素操作
'''在元素定位完成之后，才可以对元素进行操作，比如点击一下，输入文字、双击、拖动、悬
浮、获取元素的属性值、能不能判断元素是否可用、是否可选择等等。
click() : 点击
clear()：清除，清除文本框的内容send_keys() ： 通过键盘输入数据（数字、字母、汉字、特殊字符、快捷键、组合键、上
传图片等）
title：获取当前浏览器页面的标题
current_url ：当前浏览器页面的url地址
text：获取某些元素上文本信息，比如提示框的提示信息
get_attribute("属性名")：通过属性名获取属性值（属性名是value，取到的值
就是文本框中的数据）
is_enabled() :  元素是否可用（有些按钮是灰色的，不可用）
is_selected()：是否被选中了
is_displayed()：是否显示出来了
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

#  获取当前页面的title,并打印出来（driver.title）
title = driver.title
print("当前页面的title为：%s" % title)

#  获取页面底部的信息：把百度设为主页关于百度About  Baidu百度推广
#  先定位到这些信息所在的标签，然后调用text获取其值
#  通过class属性定位
element = driver.find_element(By.CLASS_NAME,"s-bottom-layer-content")
textInfo = element.text
print("获取的文本信息为：%s" % textInfo)

#  百度“测试allen说”，点击百度一下
driver.find_element("id","kw").send_keys("测试allen说")
#  判断页面中的“百度一下”按钮是否正常显示，是则打印“正常显示按钮”
elementBaidu = driver.find_element("id","su")
if elementBaidu.is_displayed():
    print("百度一下按钮正常显示了")
    elementBaidu.click()
    time.sleep(4)

#  再次查看当前页面的url地址
url2 = driver.current_url
#  当前页面的url地址为：https://www.baidu.com/
print("再点击完成百度一下后的当前页面的url地址为：%s" % url2)

#  获取文本框中的文本，并打印出来
value = driver.find_element("id", "kw").get_attribute("value")
classValue = driver.find_element("id", "kw").get_attribute("class")
print("百度文本框中的值为：%s" % value)
print("百度文本框的class属性值为：" + classValue)
#  清除百度文本框中内容
driver.find_element("id", "kw").clear()
time.sleep(5)
#  关闭浏览器
driver.quit()