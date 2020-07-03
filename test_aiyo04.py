#! Python3.8
#encoding: utf-8
# practice from https://github.com/playone/forpython/blob/master/Newbie/test1.py
"""
這是一個簡單的程式範例
主要是要表現第一行的解碼
這樣才能在檔案裏面使用中文
在標頭限定python的版本，這樣可以限定要用python2 或者 python3
"""
y=input('input for y:')
print('type of y' , type(y) ,',y=', y)
#x = 3
x=int(y)
x += 2
x -= 2
print('type of x' , type(x) ,',x=', x)

x,y = 99.99, 5
print(x,'+' ,y,'=',x+y)