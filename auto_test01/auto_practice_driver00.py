"""
from https://github.com/playone/forpython/blob/master/Automation/test1.py
簡單的python呼叫selenium程式
"""

from selenium import webdriver #呼叫webdriver
from selenium.webdriver.common.keys import Keys #模擬輸入的函式
import time

driver = webdriver.Firefox() #定義以FIREFOX為主的webdriver
driver.get('http://www.python.org') #開啟網頁
assert 'Python' in driver.title #判定網頁title裡面有含某個關鍵字,有=pass=繼續下面動作，無=fail & assertion error=跳出
elem = driver.find_element_by_name('q') #將被定位的元素所關聯的內容定義出來
elem.clear() # elem此元素是一個輸入欄位, 此class是將欄位內容清空
driver.save_screenshot('D:\\AUTO\\python_test\\auto_test01\\screenshots\\ap01.png')
elem.send_keys('pycon') #輸入文字

elem.send_keys(Keys.RETURN) #模擬按鍵
driver.save_screenshot('D:\\AUTO\\python_test\\auto_test01\\screenshots\\ap02.png')
assert 'No results found' not in driver.page_source
#driver.get_screenshot_as_file('screenshot/test.png') #截圖
time.sleep(2)
driver.save_screenshot('D:\\AUTO\\python_test\\auto_test01\\screenshots\\ap03.png')
print('test completed')
driver.quit() #關閉webdriver釋放空間