
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

#chrome_path = "C:\temp\chromedriver\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
driver = webdriver.Chrome(r"C:\Python38-32\chromedriver.exe", options=options)
time.sleep(3)

executor_url = driver.command_executor._url
session_id = driver.session_id
print(session_id)
print(executor_url)

##########1111 
driver.get('https://www.facebook.com/')

time.sleep(3)

driver.find_element_by_xpath('//*[@id="email"]').send_keys('aiyo0608@gmail.com')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('Ixhxpns1')
#//*[@id="pass"]
time.sleep(1)
driver.find_element_by_xpath('//*[@id="u_0_b"]').click()
time.sleep(3)

print('test FB login completed')

#driver.quit()
#driver.close()
