from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

#chrome_path = "C:\temp\chromedriver\chromedriver.exe" #chromedriver.exe�����ɩҦs�b�����|
driver = webdriver.Chrome(r"C:\temp\chromedriver\chromedriver.exe", chrome_options=options)

#time.sleep(3)


driver.get('https://gp-dashboard-private.mybluemix.net/login.wss')
#time.sleep(3)

driver.find_element_by_link_text('Switch login method').click()
#time.sleep(1)

driver.find_element_by_id('bm-login-metadata').send_keys('{"userId": "",' )
#time.sleep(1)

driver.find_element_by_id('bm-login-metadata').send_keys('"password": "",' )
#time.sleep(1)

driver.find_element_by_id('bm-login-metadata').send_keys('"instanceId": ""}' )
#time.sleep(10)


#driver.find_element_by_link_text('Sign in').click()
#driver.find_element_by_class_name("bx--btn bx--btn--primary").click()
driver.find_element_by_xpath('//html/body/nav/div/form/div[2]/div[2]/button').click()

time.sleep(10)

#web.close()
#driver.quit()
#login issue , have to login second time

driver.find_element_by_link_text('Switch login method').click()
#time.sleep(1)

driver.find_element_by_id('bm-login-metadata').send_keys('{"userId": "",' )
#time.sleep(1)

driver.find_element_by_id('bm-login-metadata').send_keys('"password": "",' )
#time.sleep(1)

driver.find_element_by_id('bm-login-metadata').send_keys('"instanceId": ""}' )
#time.sleep(10)


#driver.find_element_by_link_text('Sign in').click()
#driver.find_element_by_class_name("bx--btn bx--btn--primary").click()
driver.find_element_by_xpath('//html/body/nav/div/form/div[2]/div[2]/button').click()

time.sleep(10)


#click Bundles /html/body/nav/nav/div/button[2]
driver.find_element_by_xpath('//html/body/nav/nav/div/button[2]').click()
time.sleep(5)


#==========1=========bgCrmi

driver.find_element_by_link_text('bgCrmi').click()
time.sleep(5)


#click PTBR and download
driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('bgCrmi').click()
time.sleep(5)
#click CAFR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Canadian French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('bgCrmi').click()
time.sleep(5)
#click FR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('bgCrmi').click()
time.sleep(5)
#click DE and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('German').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('bgCrmi').click()
time.sleep(5)
#click JA and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Japanese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('bgCrmi').click()
time.sleep(5)
#click ZH and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Simplified Chinese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('bgCrmi').click()
time.sleep(5)
#click ES and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Spanish').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#===================

#==========2=========bgSendEngine
#BACK TO Bundle
driver.find_element_by_link_text('Bundles').click()
time.sleep(5)
driver.find_element_by_link_text('bgSendEngine').click()
time.sleep(5)


#click PTBR and download
driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('bgSendEngine').click()
time.sleep(5)
#click CAFR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Canadian French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('bgSendEngine').click()
time.sleep(5)
#click FR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('bgSendEngine').click()
time.sleep(5)
#click DE and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('German').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('bgSendEngine').click()
time.sleep(5)
#click JA and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Japanese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('bgSendEngine').click()
time.sleep(5)
#click ZH and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Simplified Chinese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('bgSendEngine').click()
time.sleep(5)
#click ES and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Spanish').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#===================
#==========3=========importfile.resource.ImportFileMessages
#BACK TO Bundle
driver.find_element_by_link_text('Bundles').click()
time.sleep(5)
driver.find_element_by_link_text('importfile.resource.ImportFileMessages').click()
time.sleep(5)


#click PTBR and download
driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('importfile.resource.ImportFileMessages').click()
time.sleep(5)
#click CAFR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Canadian French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('importfile.resource.ImportFileMessages').click()
time.sleep(5)
#click FR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('importfile.resource.ImportFileMessages').click()
time.sleep(5)
#click DE and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('German').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('importfile.resource.ImportFileMessages').click()
time.sleep(5)
#click JA and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Japanese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('importfile.resource.ImportFileMessages').click()
time.sleep(5)
#click ZH and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Simplified Chinese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('importfile.resource.ImportFileMessages').click()
time.sleep(5)
#click ES and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Spanish').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#===================

#==========4=========resource.resource.MenuMessages
#BACK TO Bundle
driver.find_element_by_link_text('Bundles').click()
time.sleep(5)
driver.find_element_by_link_text('resource.resource.MenuMessages').click()
time.sleep(5)


#click PTBR and download
driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('resource.resource.MenuMessages').click()
time.sleep(5)
#click CAFR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Canadian French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('resource.resource.MenuMessages').click()
time.sleep(5)
#click FR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('resource.resource.MenuMessages').click()
time.sleep(5)
#click DE and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('German').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('resource.resource.MenuMessages').click()
time.sleep(5)
#click JA and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Japanese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('resource.resource.MenuMessages').click()
time.sleep(5)
#click ZH and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Simplified Chinese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('resource.resource.MenuMessages').click()
time.sleep(5)
#click ES and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Spanish').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#===================
#==========5=========CommonUIMessages
#BACK TO Bundle
driver.find_element_by_link_text('Bundles').click()
time.sleep(5)
driver.find_element_by_link_text('CommonUIMessages').click()
time.sleep(5)


#click PTBR and download
driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('CommonUIMessages').click()
time.sleep(5)
#click CAFR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Canadian French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('CommonUIMessages').click()
time.sleep(5)
#click FR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('CommonUIMessages').click()
time.sleep(5)
#click DE and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('German').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('CommonUIMessages').click()
time.sleep(5)
#click JA and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Japanese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('CommonUIMessages').click()
time.sleep(5)
#click ZH and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Simplified Chinese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('CommonUIMessages').click()
time.sleep(5)
#click ES and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Spanish').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#===================
#==========6=========HelptextMessages
#BACK TO Bundle
driver.find_element_by_link_text('Bundles').click()
time.sleep(5)
driver.find_element_by_link_text('HelptextMessages').click()
time.sleep(5)


#click PTBR and download
driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('HelptextMessages').click()
time.sleep(5)
#click CAFR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Canadian French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('HelptextMessages').click()
time.sleep(5)
#click FR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('HelptextMessages').click()
time.sleep(5)
#click DE and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('German').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('HelptextMessages').click()
time.sleep(5)
#click JA and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Japanese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('HelptextMessages').click()
time.sleep(5)
#click ZH and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Simplified Chinese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('HelptextMessages').click()
time.sleep(5)
#click ES and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Spanish').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#===================
#==========7=========commonMsgMgmt
#BACK TO Bundle
driver.find_element_by_link_text('Bundles').click()
time.sleep(5)
driver.find_element_by_link_text('commonMsgMgmt').click()
time.sleep(5)


#click PTBR and download
driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonMsgMgmt').click()
time.sleep(5)
#click CAFR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Canadian French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonMsgMgmt').click()
time.sleep(5)
#click FR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonMsgMgmt').click()
time.sleep(5)
#click DE and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('German').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonMsgMgmt').click()
time.sleep(5)
#click JA and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Japanese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonMsgMgmt').click()
time.sleep(5)
#click ZH and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Simplified Chinese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonMsgMgmt').click()
time.sleep(5)
#click ES and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Spanish').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#===================
#==========8=========commonServices
#BACK TO Bundle
driver.find_element_by_link_text('Bundles').click()
time.sleep(5)
driver.find_element_by_link_text('commonServices').click()
time.sleep(5)


#click PTBR and download
driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
time.sleep(10)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#GP download issue 01
#BACK TO LANG LIST
driver.find_element_by_link_text('commonServices').click()
time.sleep(5)
#click CAFR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Canadian French').click()
time.sleep(10)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonServices').click()
time.sleep(5)
#click FR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('French').click()
time.sleep(10)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonServices').click()
time.sleep(5)
#click DE and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('German').click()
time.sleep(10)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonServices').click()
time.sleep(5)
#click JA and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Japanese').click()
time.sleep(10)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonServices').click()
time.sleep(5)
#click ZH and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Simplified Chinese').click()
time.sleep(10)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonServices').click()
time.sleep(5)
#click ES and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Spanish').click()
time.sleep(10)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#===================
#==========9=========commonUi
#BACK TO Bundle
driver.find_element_by_link_text('Bundles').click()
time.sleep(5)
driver.find_element_by_link_text('commonUi').click()
time.sleep(5)


#click PTBR and download
driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonUi').click()
time.sleep(5)
#click CAFR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Canadian French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonUi').click()
time.sleep(5)
#click FR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonUi').click()
time.sleep(5)
#click DE and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('German').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonUi').click()
time.sleep(5)
#click JA and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Japanese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonUi').click()
time.sleep(5)
#click ZH and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Simplified Chinese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('commonUi').click()
time.sleep(5)
#click ES and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Spanish').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#===================
#==========10=========common-ui-src-static-js-common-nls-CkEditor.js

#BACK TO Bundle
driver.find_element_by_link_text('Bundles').click()
time.sleep(5)

driver.find_element_by_link_text('common-ui-src-static-js-common-nls-CkEditor.js').click()
time.sleep(5)

#click PTBR and download
driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('common-ui-src-static-js-common-nls-CkEditor.js').click()
time.sleep(5)
#click CAFR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Canadian French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('common-ui-src-static-js-common-nls-CkEditor.js').click()
time.sleep(5)
#click FR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('French').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('common-ui-src-static-js-common-nls-CkEditor.js').click()
time.sleep(5)
#click DE and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('German').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('common-ui-src-static-js-common-nls-CkEditor.js').click()
time.sleep(5)
#click JA and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Japanese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('common-ui-src-static-js-common-nls-CkEditor.js').click()
time.sleep(5)
#click ZH and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Simplified Chinese').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#BACK TO LANG LIST
driver.find_element_by_link_text('common-ui-src-static-js-common-nls-CkEditor.js').click()
time.sleep(5)
#click ES and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('Spanish').click()
time.sleep(5)
#click download
driver.find_element_by_xpath('//html/body/nav/div[3]/div[1]/div[2]/button').click()                             
time.sleep(5)
#check JSON
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[2]/div/div/span[3]/label/span[1]').click()      
time.sleep(5)
#click Download
driver.find_element_by_xpath('//*[@id="downloadResModal"]/div/div[3]/button[2]').click()      
time.sleep(5)

#==========


print('download LANG PII completed')
driver.quit()
