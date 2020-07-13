
"""
from https://github.com/playone/forpython/blob/master/Automation/test9.py
ref https://blog.gtwang.org/programming/python-beautiful-soup-module-scrape-web-pages-tutorial/
抓取瀑布式網頁的範例
"""

import xlwt #use excel
from bs4 import BeautifulSoup as bs #use beautifulsoup
from selenium import webdriver #use webdriver UI
import time #use time.sleep and others control

url_a = 'https://tw.eztable.com/channel/314'
driver = webdriver.Chrome()
driver.get(url_a)
time.sleep(2)


wb = xlwt.Workbook() #宣告excel檔案
sh= wb.add_sheet('A new sheet') #宣告新增一個新sheet
sh.write(0, 0, u'餐廳名稱') #新增某欄位內容 write(列, 欄, '欄位內容')
sh.write(0, 1, u'平均價位')
sh.write(0, 2, u'可預約時間')
sh.write(0, 3, u'餐廳網址')


def execute_times(times):
    for i in range(1, times+1):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') #捲動頁面的語法 利用execute script 來執行 "window.scrollTo(0, document.body.scrollHeight);"這指令
        time.sleep(5)

execute_times(10) #呼叫函式 執行10次滾動頁面的動作

soup = bs(driver.page_source, 'html.parser')

# 選取我們要爬的資料定位元素 利用for loop 將在此bs dataframe裡面屬於這元素的文字爬出來, 並將爬取出來的文字寫入excel
h=0
for block in soup.select('h4'):
    h += 1
    sh.write( h, 0, block.text)
    #print (block.text)

i=0
for block in soup.select('span.sc-bRBYWo.frTErj'):
    i += 1
    sh.write(i, 1, block.text)
    #print (block.text)

j=0
for block in soup.select('div.col-sm-5.col-xs-12.sc-cMljjf.idfRdX > div'):
    j += 1

    if (block.text =='您所選擇日期沒有可供預訂座位'):
        sh.write(j, 2, block.text)
        print(block.text)
    else:
        temp=list(block.text)
        temp2=''
        jj=0
        for jj in range(15):
            temp2 = temp2 + temp[jj]
            if (jj+1)%5==0:
                temp2=temp2+','
            jj += 1
        sh.write(j, 2, temp2)
        print(temp2)


k=0
for block in soup.select('a'):
    url = str(block.get('href'))
    if '/restaurant/' in url:
        k += 1
        rest = 'https://tw.eztable.com'+url
        sh.write(k, 3, rest)
        #print (url)


restlist = 'rest_list_'+time.strftime('%Y%m%d')+'.xls' #檔名會依日期生成
wb.save(restlist) #excel存檔
driver.quit()

#原本想抓取YAHOO新聞，但YAHOO block了 "window.scrollTo(0, document.body.scrollHeight);"這指令, 所以假如想爬取YAHOO的資料得要使用另外的方法