# 打开百度，输入文字进行查询 页面元素的定位
'''
页面元素的定位方法：
webdriver中提供了八种定位方法：
id属性定位：身份证号码
name属性定位：姓名
class属性定位：类名
link text：超链接上显示的文本信息
partial link text：超链接上文本信息的一部份文字
tag标签：标签名
xpath：路径定位
css：层叠样式选择器定位
driver.find_element(By.ID,"kw").send_keys("测试allen说")
driver.find_element(By.ID,"su").click()
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(3)

# 1、通过ID定位
# driver.find_element(By.ID, "kw").send_keys("测试allen说")
# 2、通过name定位
# driver.find_element(By.NAME,"wd").send_keys("测试allen说")
# 3、通过标签名定位，如<div>标签
# 能定位到一个元素，是html页面中最先出现的一个a标签
# element = driver.find_element(By.TAG_NAME,"a")
# print(element)
element = driver.find_elements(By.TAG_NAME,"a")
print(element)
# 能不能点一下列表中的第五个元素
# element[3].click()
# 4、classname定位，多个同类型的标签，我们统一给相同的类名
# 默认选择的是classname为c‐color‐t第一次出现的那个元素
# element = driver.find_element(By.CLASS_NAME,"c‐color‐t")
# 返回的是所有的classname为c‐color‐t的元素列表,如果类名存在多个层级的话，选择最底层的即可
# element = driver.find_elements(By.CLASS_NAME,"title-content-title")
# element[1].click()
# 循环
# for n in element:
#     n.click()
# 5、link text定位 ：通过标签的文本信息进行定位
# driver.find_element(By.LINK_TEXT,"新闻").click()
# 6、partial link text定位，通过标签的文本信息的部分内容进行定位
# driver.find_element(By.PARTIAL_LINK_TEXT,"坚持“动态清零”不动摇，做好全链条精准防控").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "生动").click()
# 7、xpath定位，路径定位的方式：
# 浏览器中CTRL+F xpath的绝对路径：/html/body/div/div/div[5]/div/div/form/span/input
# 通过xpath定位百度文本框并输入”测试allen说“
# driver.find_element(By.XPATH,"/html/body/div/div/div[5]/div/div/form/span/input").send_keys("测试allen说")
# 相对路径用 : //标签名[@属性名=属性值]
# driver.find_element(By.XPATH,"//input[@id='kw']").send_keys("测试allen说")
# 8、CSS：
# id选择器语法：#id属性值。--> #kw
# driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("测试allen说")
# 类选择器语法：.class类属性值 --> .s_ipt
# driver.find_element(By.CSS_SELECTOR,".s_btn").click()
# 3)元素选择器：
# 标签名#id属性值 -->form#form
# 标签名.class属性值 -->input.s_ipt
# driver.find_element(By.CSS_SELECTOR,"input.s_ipt").send_keys("测试allen说")
#父子关系格式：父标签名>子标签名
#兄弟节点格式：父标签名>子标签+子标签
#driver.find_element(By.CSS_SELECTOR,"form#form>span>input").send_keys("测试allen说")
#driver.find_element(By.CSS_SELECTOR,"form#form>span+span>input").click()
#5）去浏览器复制css选择器
#su


time.sleep(3)
driver.find_element(By.ID, "su").click()
# driver.find_element(By.XPATH,"/html/body/div/div/div[5]/div/div/form/span[2]/input").click() #绝对路径查找 /
# driver.find_element(By.XPATH,"//input[@id='su']").click() # 相对路径 //
# driver.find_element(By.CSS_SELECTOR,"input#su").click() #CSS元素选择器

time.sleep(3)
# driver.quit()