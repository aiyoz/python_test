
from selenium import webdriver
from datetime import datetime
import time
import pyautogui

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

#chrome_path = "C:\temp\chromedriver\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
driver = webdriver.Chrome(r"C:\Python38-32\chromedriver.exe", options=options)
time.sleep(3)

driver.get('https://www.facebook.com/')

time.sleep(3)

#login=driver.find_element_by_xpath('//*[@id="email"]')
#login.send_keys('aiyo0608@gmail.com')
driver.find_element_by_xpath('//*[@id="email"]').send_keys('@gmail.com')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('')
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
driver.save_screenshot('D:\\AUTO\\python_test\\auto_test01\\screenshots\\test_aiyo02.png')

driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[3]/div[2]/div').click()

#with open(r'C:\...properties','w') as f:
 #   s=s.replace('&lt;','<')
  #  f.write(s)
   # time.sleep(3)

aiyotime = datetime.now()
print('test FB type post completed' , aiyotime)

#driver.quit()
#driver.close()
