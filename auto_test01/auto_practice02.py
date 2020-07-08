

"""
from https://github.com/playone/forpython/blob/master/Automation/test2.py
ref https://blog.csdn.net/qq_36711420/article/details/79382327
https://kknews.cc/zh-tw/code/ql6qx6g.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html

Testing Pandas dataframe , iloc , requests.get with url&text , lxml.html.fromstring

"""
# encoding: utf-8

import lxml.html
import sys
import importlib
import pandas as pd
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


importlib.reload(sys)
#df = pd.read_excel('copy2.xls',sheet_name='1')
df = pd.read_excel('copy2.xls',sheet_name='st02')
url = 'https://udn.com/rank/pv/2'
html = requests.get(url,verify=False).text
doc = lxml.html.fromstring(html)

titles = doc.xpath('//div[@class="story-list__news"]/div[2]/h2/a/text()')
href = doc.xpath('////div[@class="story-list__news"]/div[2]/h2/a/@href')
i=0
j=0
print(len(df))
print(len(titles))

for i in range(len(titles)):
    df.iloc[i,0] = titles[i]

for j in range(len(href)):
    df.iloc[j,1] = href[j]

print(df)
df.to_excel('copyto.xls', index = False)

"""
import requests
import time
import json
import xlrd

#sys.setdefaultencoding()
#print(df)
#search_title = list(df.iloc[:, 0])
#print(search_title)
#search_link = list(df.iloc[:, 1])
#print(search_link)

#titles = doc.xpath('//h3[@class="rounded-thumb__title"]/a/text()')
#href = doc.xpath('//h3[@class="rounded-thumb__title"]/a/@href')

#/html/body/main/div/section[2]/section/div[1]/div[2]/div[2]/h2/a
#//*[@id="Col1-1-Hero-Proxy"]/div/ul/ul/li[7]/a
#//*[@id="Col1-1-Hero-Proxy"]/div/ul/ul/li[1]/a
#/html/body/main/div/aside/div/div[2]/div/div[1]/h3/a
#k=0
#for k in range(len(titles)-len(df)):
    #df.append(df.iloc[0:1,])
#print(df)
#print(len(href))
    #print(titles[i])
    #print(df.iloc[:, 0])
    #print(href[j])
    #print(df.iloc[:, 1])

i = 0
for content in titles:
    results = {'標題': titles[i], '鏈結': href[i]}
    i += 1
    print results
    jsonobj = json.dumps(results)
    fileobj = open('jsonfile.json', 'a')
    fileobj.write(jsonobj)
    fileobj.close()
"""