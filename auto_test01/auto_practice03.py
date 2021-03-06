
"""
from https://github.com/playone/forpython/blob/master/Automation/test3.py
使用 Python 的 Beautiful Soup 模組自動下載並解析網頁資料，開發典型的網路爬蟲(parser)程式。
"""
# encoding: utf-8

#import sys,importlib #for編碼轉換
import urllib3
import time
from bs4 import BeautifulSoup
from selenium import webdriver

#importlib.reload(sys) #for編碼轉換
#sys.setdefaultencoding('utf8') # 設定編碼in python2
url = 'http://baike.baidu.com/starrank?fr=lemmaxianhua'
driver = webdriver.Chrome() # 創建一個driver用於打開網頁
driver.get(url) # 打開網頁
name_counter = 0
page = 0;
soup = BeautifulSoup(driver.page_source, "html.parser")
try:
    #while len(soup.select("body > div.content-wrapper > div.layout > div > div.ranking-table.cur > div > a.pTag.next")) > 0: #判斷下一頁這元素是否存在 存在則繼續執行迴圈
    while (len(soup.select("div.list-overlay > div.rank-content__list > div > a.pTag.next")) > 0) :  # 判斷下一頁這元素是否存在 存在則繼續執行迴圈
     #while page < 10: # 共50頁，這裡用手動指定 , ANOTHER RULE FOR QUICK TEST & (page < 3)
        soupa = BeautifulSoup(driver.page_source, "html.parser")
        #current_names = soupa.select('div.ranking-table') # 選擇器用ranking-table css class, 可以取出本周, 上週的兩個table 的 div標籤
        current_names = soupa.select('div.rank-content__title > ul > li')  # 選擇器用, 可以取出本周, 上週的兩個table 的 div標籤
        for current_name_list in current_names: # 現在變數current_names 是 ranking-table裡面的 thisWeek 和 lastWeek 兩個標籤
            # print current_name_list['data-cat']更新soup
            #print(current_name_list)
            #if current_name_list['data-cat'] == 'thisWeek': # 這裡標籤是用本周. 如果想換成上周, 這裡的標籤改為lastWeek就可以
            if current_name_list['data-week'] == 'thisWeek':  # 這裡標籤是用本周. 如果想換成上周, 這裡的標籤改為lastWeek就可以
                #names = current_name_list.select('td.star-name > a') # beautifulsoup選擇器的語法
                names = soupa.select('p.star-name')  # beautifulsoup選擇器的語法
                #print(names)
                counter = 0;
                for star_name in names:
                    counter = counter + 1;
                    print(star_name.text) #明星的名字是a標籤裡面的文本, 雖然a標籤底下除了文本還有一個與文本同層級的img標籤, 但是.text輸出的只是文本
                    name_counter = name_counter + 1;
        driver.find_element_by_xpath("//a[contains(text(),'下一页')]").click() #  selenium的xpath 定位用法，找到包含“下一頁”的a標籤去點擊
        #print('page:'+str(page+1))
        page = page + 1
        time.sleep(2) # 睡2秒讓網頁加載完再去分析下一個頁面的html代碼
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print(soup.select("div.list-overlay > div.rank-content__list > div > a.pTag.next"))
except:
    print('共爬取得明星的名字數量:'+str(name_counter)) # 共爬取得明星的名字數量
finally:
    #IF USING ANOTHER RULE print('共爬取得明星的名字數量:' + str(name_counter))  # 共爬取得明星的名字數量
    driver.quit()

"""
會使用例外是因為最後一頁的下一步會不見導致第30行錯誤
因此用例外排除此錯誤
"""