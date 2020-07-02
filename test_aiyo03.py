
from selenium import webdriver
from datetime import datetime
import time
import pyautogui
import facebook

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

#chrome_path = "C:\temp\chromedriver\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
driver = webdriver.Chrome(r"C:\Python38-32\chromedriver.exe", options=options)

aiyotime = datetime.now()
executor_url = driver.command_executor._url
session_id = driver.session_id
print(session_id)
print(executor_url)

##########1111
driver.get('https://www.facebook.com/')
driver.maximize_window()

graph = facebook.GraphAPI(access_token="EAAIFBqucXHIBAPLO89miZAA1OfPK1PudbcGhF3LXKY35CNx6SjIYJjyvsSyM8ZCxunVeZAlD0PfrplTQh3eOsoXhecBBelb9jWDwET2ZBmiYqbkbc2K8UlirRLGRANcuJlzacClTjZB9k06H5bAllesJnIMPnegzPYZBmYwNOMkptDT2yESuVBDNIPhGZBUP6FBV1f1ffGwpNKoolu7Igy6U1snpuQkaXTZCPklqE6Y15k5G8qCaqKuMxEaFvzBgmP8ZD")
print('GraphAPI is' , graph)

# Get the message from a post.
#post = graph.get_object(id='post_id', fields='message')
#print(post['message'])

#to post to your wall
#graph.put_object(parent_object='me', connection_name='feed', message='Hello, world')
graph.put_object('me','feed',message='hello world')
driver.save_screenshot('D:\\AUTO\\screenshots\\test_aiyo03.png')
print('test FB PKG POST completed' , aiyotime , 'to' , datetime.now())

#driver.quit()
driver.close()
