
"""
from https://github.com/playone/forpython/blob/master/Automation/test7.py

practice with urllib.request , soup.find , strip() , csv
"""

import csv
from datetime import datetime
import urllib.request
from bs4 import BeautifulSoup as bs

quote_page ='http://www.bloomberg.com/quote/SPX:IND'
page = urllib.request.urlopen(quote_page)
soup = bs(page, 'html.parser')
print (soup)
name_box = soup.find('h1', attrs={'class' : 'logo'})
#print(name_box)
name = name_box.text.strip()# strip() 函數用於去除前後空格
print(name)

price_box = soup.find('div', attrs={'id' : 'block_uuid'})
price = price_box.text.strip()
print (price)

with open('index.csv', 'a') as csv_file: #利用csv套件將資料存進csv 檔
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])