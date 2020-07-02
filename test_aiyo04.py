
from selenium import webdriver
from datetime import datetime
import time
import pyautogui
import facebook

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

#login=driver.find_element_by_xpath('//*[@id="email"]')
#login.send_keys('aiyo0608@gmail.com')
driver.find_element_by_xpath('//*[@id="email"]').send_keys('aiyo0608@gmail.com')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('Ixhxpns1')
#//*[@id="pass"]
time.sleep(1)
driver.find_element_by_xpath('//*[@id="u_0_b"]').click()
time.sleep(3)

driver.maximize_window()

driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[1]').click()

#driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div').click()
#driver.find_element_by_css_selector('css=/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys('test')

#useing pyautogui https://stackoverflow.com/questions/136734/key-presses-in-python
pyautogui.press('space')
time.sleep(1)
pyautogui.typewrite('test\n')
time.sleep(1)
pyautogui.typewrite('post')
driver.save_screenshot('D:\\AUTO\\screenshots\\test_aiyo02.png')

driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[3]/div[2]/div').click()


#with open(r'C:\Silverpop\PII\2019dec\1223\bg-crmi\src\resources\bundles\java\bgCrmi.properties','w') as f:
 #   s=driver.page_source.encode('utf-8')
  #  s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
   # s=s.replace('</pre></body></html>','')
    #s=s.replace('amp;','')
#    s=s.replace('&gt;','>')
 #   s=s.replace('&lt;','<')
  #  f.write(s)
   # time.sleep(3)   

##########2222


aiyotime = datetime.now()
print('test FB login completed' , aiyotime)

#driver.quit()
#driver.close()
