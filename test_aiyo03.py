# practice spydr

from spydr.webdriver import Spydr
#import Spydr from spydr.webdriver
s=Spydr()
s.maximize_window()
s.get('https://www.google.com/')
s.send_keys('name=q', 'webdriver', s.keys.ENTER)
s.save_screenshot('spyde001')
s.quit()