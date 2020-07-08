# encoding: utf-8
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

#chrome_path = "C:\temp\chromedriver\chromedriver.exe" #chromedriver.exe�����ɩҦs�b�����|
driver = webdriver.Chrome(r"C:\temp\chromedriver\chromedriver.exe", chrome_options=options)
time.sleep(3)

executor_url = driver.command_executor._url
session_id = driver.session_id
print(session_id)
print(executor_url)

##########1111 
driver.get('https://github.com/aipoweredmarketer/ca-bg-crmi/blob/master/src/resources/bundles/java/bgCrmi.properties')

time.sleep(3)

driver.find_element_by_link_text('Sign in').click()

driver.find_element_by_id('login_field').send_keys('')
time.sleep(1)
driver.find_element_by_id('password').send_keys('')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[8]').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div/div[2]/form/button').click()
time.sleep(3)

##login part2
driver.find_element_by_id('okta-signin-username').send_keys('')
time.sleep(1)
driver.find_element_by_id('okta-signin-password').send_keys('')
time.sleep(1)

driver.find_element_by_id('okta-signin-submit').click()
time.sleep(90)

driver.get('https://github.com/aipoweredmarketer/ca-bg-crmi/blob/master/src/resources/bundles/java/bgCrmi.properties')
time.sleep(3)

driver.find_element_by_link_text('Raw').click()
#"Raw" button
time.sleep(3)

with open(r'C:\Silverpop\PII\2019dec\1223\bg-crmi\src\resources\bundles\java\bgCrmi.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
    time.sleep(3)   

##########2222
driver.get('https://github.com/aipoweredmarketer/ca-bg-send-engine/blob/pre-master/src/resources/bundles/java/bgSendEngine.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\bg-send-engine\src\resources\bundles\java\bgSendEngine.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########3333
driver.get('https://github.com/aipoweredmarketer/ca-common-gwt-ui/blob/pre-master/src/resources/com/silverpop/common/gwt/ui/client/importfile/resource/ImportFileMessages.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\common-gwt-ui\src\resources\com\silverpop\common\gwt\ui\client\importfile\resource\ImportFileMessages.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)
          
##########4444
driver.get('https://github.com/aipoweredmarketer/ca-common-gwt-ui/blob/pre-master/src/resources/com/silverpop/common/gwt/ui/client/resource/resource/MenuMessages.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\common-gwt-ui\src\resources\com\silverpop\common\gwt\ui\client\resource\resource\MenuMessages.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)
          
##########5555
driver.get('https://github.com/aipoweredmarketer/ca-common-gwt-ui/blob/pre-master/src/resources/com/silverpop/common/gwt/ui/client/resource/CommonUIMessages.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\common-gwt-ui\src\resources\com\silverpop\common\gwt\ui\client\resource\CommonUIMessages.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########6
driver.get('https://github.com/aipoweredmarketer/ca-common-gwt-ui/blob/pre-master/src/resources/com/silverpop/common/gwt/ui/client/resource/HelptextMessages.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\common-gwt-ui\src\resources\com\silverpop\common\gwt\ui\client\resource\HelptextMessages.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########7
driver.get('https://github.com/aipoweredmarketer/ca-common-msg-mgmt/blob/pre-master/src/main/resources/commonMsgMgmt.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\common-msg-mgmt\src\main\resources\commonMsgMgmt.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########8
driver.get('https://github.com/aipoweredmarketer/ca-common-services/blob/pre-master/src/resources/bundles/java/commonServices.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\common-services\src\resources\bundles\java\commonServices.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########9
driver.get('https://github.com/aipoweredmarketer/ca-common-ui/blob/pre-master/src/resources/bundles/java/commonUi.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\common-ui\src\resources\bundles\java\commonUi.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########10
driver.get('https://github.com/aipoweredmarketer/ca-common-ui/blob/pre-master/src/static/js/common/nls/CkEditor.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\common-ui\target\TDCFiles\CkEditor.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########11

driver.get('https://github.com/aipoweredmarketer/ca-common-ui/blob/pre-master/src/static/js/common/nls/CommonResources.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\common-ui\target\TDCFiles\CommonResources.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)
          
##########12
driver.get('https://github.com/aipoweredmarketer/ca-common-ui/blob/pre-master/src/static/js/common/nls/commonUiProperties.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\common-ui\target\TDCFiles\commonUiProperties.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########13
driver.get('https://github.com/aipoweredmarketer/ca-common-ui/blob/pre-master/src/static/js/common/nls/LoadingDialogResourceBundle.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\common-ui\target\TDCFiles\LoadingDialogResourceBundle.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########14
driver.get('https://github.com/aipoweredmarketer/ca-common-ui/blob/pre-master/src/static/js/common/nls/Query.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\common-ui\target\TDCFiles\Query.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########15
driver.get('https://github.com/aipoweredmarketer/ca-core/blob/pre-master/src/resources/bundles/java/core.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\core\src\resources\bundles\java\core.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)


##########16
driver.get('https://github.com/aipoweredmarketer/ca-recip-webhost/blob/pre-master/src/resources/bundles/java/recipWebhost.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\recip-webhost\src\resources\bundles\java\recipWebhost.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########17
driver.get('https://github.com/aipoweredmarketer/ca-selfservice/blob/pre-master/src/resources/bundles/java/crmiApp.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\selfservice\src\resources\bundles\java\crmiApp.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########18
driver.get('https://github.com/aipoweredmarketer/ca-shell-auth-api/blob/pre-master/src/resources/bundles/java/shellAuthApi.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\shell-auth-api\src\resources\bundles\java\shellAuthApi.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########19
driver.get('https://github.com/aipoweredmarketer/ca-user-msg-mgmt-ux/blob/pre-master/src/web/frontend/src/assets/i18n/en.json')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-msg-mgmt-ux\src\web\frontend\src\assets\i18n\en.json','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########20
driver.get('https://github.com/aipoweredmarketer/ca-user-programs/blob/pre-master/src/resources/bundles/java/userPrograms.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-programs\src\resources\bundles\java\userPrograms.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########21
driver.get('https://github.com/aipoweredmarketer/ca-user-programs/blob/pre-master/src/resources/com/silverpop/campaign/framework/gwt/client/resource/CampaignFrameworkMessages.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-programs\src\resources\com\silverpop\campaign\framework\gwt\client\resource\CampaignFrameworkMessages.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########22
driver.get('https://github.com/aipoweredmarketer/ca-user-programs/blob/pre-master/src/resources/com/silverpop/campaign/gwt/client/resource/CampaignMessages.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-programs\src\resources\com\silverpop\campaign\gwt\client\resource\CampaignMessages.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########23
driver.get('https://github.com/aipoweredmarketer/ca-user-programs/blob/master/src/web/js/ca/nls/userProgramsProperties.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-programs\target\TDCFiles\userProgramsProperties.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########24 - user-programs-ux\target\user-programs-ux.war\resources\en.json needs developer help building
##########25 - user-push-ux\target\user-push-ux.war\resources\en.json needs developer help building

##########26
driver.get('https://github.com/aipoweredmarketer/ca-user-reports/blob/pre-master/src/resources/com/silverpop/reporting/gwt/client/resource/EngageConstants.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-reports\src\resources\com\silverpop\reporting\gwt\client\resource\EngageConstants.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########27
driver.get('https://github.com/aipoweredmarketer/ca-user-reports/blob/pre-master/src/resources/com/silverpop/reporting/gwt/client/resource/LandingPagesConstants.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-reports\src\resources\com\silverpop\reporting\gwt\client\resource\LandingPagesConstants.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########28
driver.get('https://github.com/aipoweredmarketer/ca-user-reports/blob/pre-master/src/resources/com/silverpop/reporting/gwt/client/resource/LPReportingMessages.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-reports\src\resources\com\silverpop\reporting\gwt\client\resource\LPReportingMessages.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########29
driver.get('https://github.com/aipoweredmarketer/ca-user-reports/blob/pre-master/src/resources/com/silverpop/reporting/gwt/client/resource/MarketerParameterPageMessages.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-reports\src\resources\com\silverpop\reporting\gwt\client\resource\MarketerParameterPageMessages.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########30
driver.get('https://github.com/aipoweredmarketer/ca-user-reports/blob/pre-master/src/resources/com/silverpop/reporting/gwt/client/resource/PagehosterParameterPageMessages.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-reports\src\resources\com\silverpop\reporting\gwt\client\resource\PagehosterParameterPageMessages.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########31
driver.get('https://github.com/aipoweredmarketer/ca-user-reports/blob/pre-master/src/resources/com/silverpop/reporting/gwt/client/resource/ReportingConstants.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-reports\src\resources\com\silverpop\reporting\gwt\client\resource\ReportingConstants.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########32
driver.get('https://github.com/aipoweredmarketer/ca-user-reports/blob/pre-master/src/resources/com/silverpop/reporting/gwt/client/resource/ReportingMessages.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-reports\src\resources\com\silverpop\reporting\gwt\client\resource\ReportingMessages.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########33
driver.get('https://github.com/aipoweredmarketer/ca-user-reports/blob/pre-master/src/web/WEB-INF/classes/MenuResources.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-reports\src\web\WEB-INF\classes\MenuResources.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)


##########34
driver.get('https://github.com/aipoweredmarketer/ca-user-sdm/blob/pre-master/src/resources/bundles/java/userSdm.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-sdm\src\resources\bundles\java\userSdm.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########35
driver.get('https://github.com/aipoweredmarketer/ca-user-sdm/blob/pre-master/src/web/js/sp/nls/AuthenticationWidget.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-sdm\target\TDCFiles\AuthenticationWidget.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########36
driver.get('https://github.com/aipoweredmarketer/ca-user-sdm/blob/pre-master/src/web/js/sp/nls/Compose.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-sdm\target\TDCFiles\Compose.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)
          
##########37
driver.get('https://github.com/aipoweredmarketer/ca-user-sdm/blob/pre-master/src/web/js/sp/nls/DeliveryHub.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-sdm\target\TDCFiles\DeliveryHub.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########38
driver.get('https://github.com/aipoweredmarketer/ca-user-sdm/blob/pre-master/src/web/js/sp/nls/Homepage.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-sdm\target\TDCFiles\Homepage.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########39
driver.get('https://github.com/aipoweredmarketer/ca-user-sdm/blob/pre-master/src/web/js/ls/nls/Leadscoring.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-sdm\target\TDCFiles\Leadscoring.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########40
driver.get('https://github.com/aipoweredmarketer/ca-user-sdm/blob/pre-master/src/web/js/sp/nls/OrgSettings.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-sdm\target\TDCFiles\OrgSettings.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########41
driver.get('https://github.com/aipoweredmarketer/ca-user-sdm/blob/pre-master/src/web/js/sp/nls/ResourceHub.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-sdm\target\TDCFiles\ResourceHub.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########42
driver.get('https://github.com/aipoweredmarketer/ca-user-sdm/blob/pre-master/src/web/js/spX/nls/spX.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-sdm\target\TDCFiles\spX.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########43
driver.get('https://github.com/aipoweredmarketer/ca-user-sdm/blob/pre-master/src/web/js/sp/nls/Tagging.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-sdm\target\TDCFiles\Tagging.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)


##########44
driver.get('https://github.com/aipoweredmarketer/ca-user-sdm/blob/pre-master/src/web/js/sp/nls/UniversalBehaviorActivityWidget.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-sdm\target\TDCFiles\UniversalBehaviorActivityWidget.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########45
driver.get('https://github.com/aipoweredmarketer/ca-user-sdm/blob/pre-master/src/web/js/nls/userSdmProperties.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-sdm\target\TDCFiles\userSdmProperties.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########46 - user-ux\target\user-ux.war\resources\en.json needs developer help building

##########47
driver.get('https://github.com/aipoweredmarketer/ca-user-webhost/blob/pre-master/src/resources/com/silverpop/pagehoster/gwt/client/resource/ApplicationMessages.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-webhost\src\resources\com\silverpop\pagehoster\gwt\client\resource\ApplicationMessages.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########48
driver.get('https://github.com/aipoweredmarketer/ca-user-webhost/blob/pre-master/src/resources/ApplicationMessages.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-webhost\src\resources\ApplicationMessages.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########49
driver.get('https://github.com/aipoweredmarketer/ca-user-webhost/blob/pre-master/src/resources/MenuResources.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-webhost\src\resources\MenuResources.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########50
driver.get('https://github.com/aipoweredmarketer/ca-user-webhost/blob/pre-master/src/web/js/nls/userWebhostProperties.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-webhost\target\TDCFiles\userWebhostProperties.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########51
driver.get('https://github.com/aipoweredmarketer/ca-selfservice/blob/pre-master/src/web/js/nls/selfserviceProperties.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\selfservice\src\web\js\nls\selfserviceProperties.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########52
driver.get('https://github.com/aipoweredmarketer/ca-user-sms-preview/blob/pre-master/src/assets/i18n/en.json')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\user-sms-preview\src\assets\i18n\en.json','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########53
driver.get('https://github.com/aipoweredmarketer/ca-common-ui/blob/pre-master/src/static/editor/fckeditor/editor/lang/en.js')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\common-ui\src\static\editor\fckeditor\editor\lang\en.js','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########54
driver.get('https://github.com/aipoweredmarketer/ca-wca-message/blob/master/src/main/resources/i18n/wcaMessageManagement.properties')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\wca-message\src\main\resources\i18n\wcaMessageManagement.properties','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

##########55 
driver.get('https://github.com/aipoweredmarketer/ca-wca-message-ui/blob/master/src/assets/wca-message-ui/i18n/en.json')
time.sleep(3)
driver.find_element_by_link_text('Raw').click() 
time.sleep(3)
with open(r'C:\Silverpop\PII\2019dec\1223\wca-message-ui\src\assets\wca-message-ui\i18n\en.json','w') as f:
    s=driver.page_source.encode('utf-8')
    s=s.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
    s=s.replace('</pre></body></html>','')
    s=s.replace('amp;','')
    s=s.replace('&gt;','>')
    s=s.replace('&lt;','<')
    f.write(s)
time.sleep(3)

print('download part 1 of PII completed')

#for 24,25,46 ux files download from GP
driver.get('https://gp-dashboard-private.mybluemix.net/login.wss')
#time.sleep(3)

driver.find_element_by_link_text('Switch login method').click()
#time.sleep(1)

driver.find_element_by_id('bm-login-metadata').send_keys('{"userId": "60fdc8a5038fc251226e357eb287c475",' )
#time.sleep(1)

driver.find_element_by_id('bm-login-metadata').send_keys('"password": "fmzGbnt4Fnzj0jnpwjrl2raqhw9Xnwqc",' )
#time.sleep(1)

driver.find_element_by_id('bm-login-metadata').send_keys('"instanceId": "12c3412d827c4af94b3c77598b7473d4"}' )
#time.sleep(10)

#driver.find_element_by_link_text('Sign in').click()
#driver.find_element_by_class_name("bx--btn bx--btn--primary").click()
driver.find_element_by_xpath('//html/body/nav/div/form/div[2]/div[2]/button').click()

time.sleep(10)

driver.find_element_by_link_text('Switch login method').click()
#time.sleep(1)

driver.find_element_by_id('bm-login-metadata').send_keys('{"userId": "60fdc8a5038fc251226e357eb287c475",' )
#time.sleep(1)

driver.find_element_by_id('bm-login-metadata').send_keys('"password": "fmzGbnt4Fnzj0jnpwjrl2raqhw9Xnwqc",' )
#time.sleep(1)

driver.find_element_by_id('bm-login-metadata').send_keys('"instanceId": "12c3412d827c4af94b3c77598b7473d4"}' )
#time.sleep(10)

#driver.find_element_by_link_text('Sign in').click()
#driver.find_element_by_class_name("bx--btn bx--btn--primary").click()
driver.find_element_by_xpath('//html/body/nav/div/form/div[2]/div[2]/button').click()

time.sleep(10)

#click Bundles /html/body/nav/nav/div/button[2]
driver.find_element_by_xpath('//html/body/nav/nav/div/button[2]').click()
time.sleep(5)

#==========24=========user-programs-ux.war-resources-en.json

driver.find_element_by_link_text('user-programs-ux.war-resources-en.json').click()
time.sleep(5)


#click EN and download
driver.find_element_by_link_text('English').click()
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

#==========25=========user-push-ux.war-resources-en.json
#BACK TO Bundle
driver.find_element_by_link_text('Bundles').click()
time.sleep(5)

driver.find_element_by_link_text('user-push-ux.war-resources-en.json').click()
time.sleep(5)
#click EN and download
driver.find_element_by_link_text('English').click()
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

#==========46=========user-ux.war-resources-en.json
#BACK TO Bundle
driver.find_element_by_link_text('Bundles').click()
time.sleep(5)
#BACK TO LANG LIST
driver.find_element_by_link_text('user-ux.war-resources-en.json').click()
time.sleep(5)
#click FR and download
#driver.find_element_by_xpath('//*[@id="pdTable"]/table/tbody/tr[2]/td[1]/a').click()
driver.find_element_by_link_text('English').click()
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


print('download all PII completed')

driver.quit()
#driver.close()
