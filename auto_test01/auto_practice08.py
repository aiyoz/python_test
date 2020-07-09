
"""
from https://github.com/playone/forpython/blob/master/Automation/test8.py

輸入數字當作爬取的頁數的練習
現在這檔案有轉碼的問題
"""

import urllib.request
from bs4 import BeautifulSoup

temp=''
page = int(input("請輸入要擷取的頁數:"))

for i in range(1,page+1):
    url1 = "https://www.mobile01.com/forumtopic.php?c=17&p="+ str(i)
    res=urllib.request.urlopen(url1)
    soup = BeautifulSoup(res,'html.parser')

    for title in soup.select('a',attrs={'class','c-link u-ellipsis'}):
        print ("==============")
        url = str(title.get('href'))
        result = ("[標題]:"+title.text.encode('UTF-8').decode('UTF-8')+ '\n' +'https://www.mobile01.com/'+url)
        temp=temp+result+'\n'

print(temp)
with open('copy1.txt', 'w' , encoding='UTF-8') as f:
    f.write(temp)

    # import sys
    # reload(sys)
    # sys.setdefaultencoding('utf8')
    #print(url1)
    #res = requests.get(url1)
    #print('https://www.mobile01.com/forumtopic.php?c=17&p='+str(i))
    #res = requests.get('https://www.mobile01.com/forumtopic.php?c=17&p='+str(i),verify=False)
    #res= requests.get('http://rate.bot.com.tw/xrt?Lang=zh-TW')
    # print(res.text)
    # print(soup)
    # print(soup.select('a',attrs={'class','c-link u-ellipsis'}))
    # f.write(temp)

    # for title in soup.find('a' , attrs={'href' :'topicdetail.php'}):
    # print (result)
    # with open('copy1.txt', 'a') as f:
    #import requests