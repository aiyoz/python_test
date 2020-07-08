

"""
from https://github.com/playone/forpython/blob/master/Automation/test2.py
ref https://blog.csdn.net/qq_36711420/article/details/79382327
https://kknews.cc/zh-tw/code/ql6qx6g.html

Testing Panda dataframe ,

"""
# encoding: utf-8

import requests
import lxml.html
import sys
import importlib
import pandas as pd
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import time
import json
import xlrd

importlib.reload(sys)
#sys.setdefaultencoding()
df = pd.read_excel('copy2.xls')
print(df)
url = 'https://udn.com/rank/pv/2'
html = requests.get(url,verify=False).text
doc = lxml.html.fromstring(html)

search_title = list(df.iloc[:, 0])
print(search_title)
search_link = list(df.iloc[:, 1])
print(search_link)

#titles = doc.xpath('//h3[@class="rounded-thumb__title"]/a/text()')
#href = doc.xpath('//h3[@class="rounded-thumb__title"]/a/@href')

titles = doc.xpath('//div[@class="story-list__news"]/div[2]/h2/a/text()')
href = doc.xpath('////div[@class="story-list__news"]/div[2]/h2/a/@href')
#/html/body/main/div/section[2]/section/div[1]/div[2]/div[2]/h2/a
#//*[@id="Col1-1-Hero-Proxy"]/div/ul/ul/li[7]/a
#//*[@id="Col1-1-Hero-Proxy"]/div/ul/ul/li[1]/a
#/html/body/main/div/aside/div/div[2]/div/div[1]/h3/a
i=0
j=0
print(len(titles))
print(len(href))

for i in range(len(titles)):
    df.iloc[:, 0] = titles[i]
    print(titles[i])
    print(df.iloc[:, 0])

for j in range(len(href)):
    df.iloc[:, 1] = href[j]
    print(href[j])

print(df)
df.to_excel('copyto.xls', index = False)

"""
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