# encoding: utf-8
# from https://github.com/playone/forpython/blob/master/Newbie/test6.py
"""
中文的處理 我們可以透過unicode 的編解碼來處理
"""

s = "台灣"

u = s.encode('utf8')

print ('台', s[0], u[0])
#S 沒有被解碼 所以執行完之後會無法被顯示)
print (u[0] == '台')