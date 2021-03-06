from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get('http://www.python.org')
assert 'Python' in driver.title
testS=driver.find_element_by_xpath('//*[@id="id-search-field"]')
testS.clear()
testS.send_keys('Google')
testS.send_keys(Keys.ENTER)
time.sleep(3)
driver.save_screenshot('D:\\AUTO\\python_test\\auto_test01\\screenshots\\searchGoogleinPython.png')
assert 'Google' in driver.page_source
print('Google was found in Python')
time.sleep(3)
driver.quit()
