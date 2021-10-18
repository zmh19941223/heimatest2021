# 导入selenium
import time

from selenium import webdriver
# 实例化浏览器驱动对象（创建浏览器驱动对象）
driver = webdriver.Chrome()  # 创建的是谷歌浏览器驱动对象   chrome后面有括号，而且第一个字母要大写
# driver = webdriver.Firefox() # 创建火狐浏览器驱动对象
# 打开百度网站
driver.get("file:///D:/software/UI%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/web%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E9%9B%86%E5%90%88/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 通过partial_link_text定位到新浪网站并点击
driver.find_element_by_partial_link_text("访问 新浪 网站").click()
# 等待3s（代表业务操作）
time.sleep(3)     # 通过快捷导包的方式导入time模块，  光标要在time后面再按alt+enter
# 退出浏览器驱动(释放系统资源)
driver.quit()
