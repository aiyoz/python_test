"""
test different kind of requests
urllib.request
requests.packages.urllib3
requests
"""

import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html0 = response.read()
   print(type(html0))
   print('==========')
   print(html0)
   print('==========')
html1=urllib.request.urlopen('http://python.org/')
print(type(html1))
print('==========')
print(html1)
print('==========')

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
html2 = requests.get('http://python.org/',verify=False).text
print(type(html2))
print('==========')
print(html2)
print('==========')

import requests
html3 = requests.get('http://python.org/')
print(type(html3))
print('==========')
print(html3)
print('==========')



