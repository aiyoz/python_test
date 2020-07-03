# encoding: utf-8
# from https://github.com/playone/forpython/blob/master/Newbie/test3.py
"""
Dictionary像是Hash table一樣 一個key對應一個變數
"""

passwd = {'mars':00000, 'mark':56789}
passwd['happy']=9999
passwd['smile']=123456
print (passwd)

del passwd['mars']
passwd['mark']=passwd['mark']+1

print (passwd)
print (passwd.keys())
print (passwd.get('tony'))
print (passwd.get('smile'))