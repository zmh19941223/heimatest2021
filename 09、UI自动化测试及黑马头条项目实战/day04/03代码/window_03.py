import time

import autoit
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
# 点击百度上面的照相机按钮
driver.find_element(By.CSS_SELECTOR, ".soutu-btn").click()
# 点击选择文件
ele = driver.find_element(By.CSS_SELECTOR, ".upload-pic")
# 定义鼠标对象
action = ActionChains(driver)
# 调用鼠标事件
action.click(ele)
# 执行鼠标事件方法
action.perform()
time.sleep(2)
#  针对windows操作
# 通过autoit来获取弹出的窗口
autoit.win_wait_active("打开", 3)
# 在文件选择输入框中输入文件的地址及文件名称
autoit.control_send("打开", "Edit1", r"C:\Users\LiaoFei\Pictures\Saved Pictures\333.jpg")

# 在弹出窗口中点击打开按钮
autoit.control_click("打开", "Button1")

time.sleep(10)
driver.quit()