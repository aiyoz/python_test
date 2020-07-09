
"""
from https://github.com/playone/forpython/blob/master/Automation/test4.py
practice parser with some table and requests without webdriver
"""
# encoding: utf-8
#from selenium import webdriver
import requests
from bs4 import BeautifulSoup

def main():
    resp = requests.get('http://rate.bot.com.tw/xrt?Lang=zh-TW')
    soup=BeautifulSoup(resp.text,'html.parser')
    #driver=webdriver.Firefox()
    #driver.get('http://rate.bot.com.tw/xrt?Lang=zh-TW')
    #resp=driver.page_source
    #soup = BeautifulSoup(resp, 'html.parser')

    rows = soup.find('table','table').tbody.find_all('tr')
    #print(rows)
    for row in rows:
        #print(row.stripped_strings)
        print(s for s in row.stripped_strings)


if __name__ == '__main__':
    main()