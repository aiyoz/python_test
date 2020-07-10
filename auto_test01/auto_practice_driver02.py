"""
test different kind of requests
urllib.request
requests.packages.urllib3
requests
"""

import urllib.request
from bs4 import BeautifulSoup as bs
with urllib.request.urlopen('http://python.org/') as response:
   #html0 = response.read()
   html0=response
   print(type(html0))
   print('==========')
   print(html0)
   print('==========')
html1=urllib.request.urlopen('http://python.org/')
print(type(html1))
print('==========')
soup = bs(html1, 'html.parser')
print(type(soup))
print('==========')
print(soup)
print('==========')
file01=open('request_soup_test.txt' , 'w', encoding='UTF-8')
file01.write(str(soup) )

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
html2 = requests.get('http://python.org/',verify=False)
print(type(html2))
print('==========')
print(html2)
print('==========')

import requests
html3 = requests.get('http://python.org/').text
print(type(html3))
print('==========')
print(html3)
print('==========')
file02=open('request_test.txt' , 'w')
file02.write(html3)



