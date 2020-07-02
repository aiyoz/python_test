# encoding: utf-8

"""
python的list 是可變動大小的陣列
可透過append增加
也有許多好用的函式
"""

aiyolist = []
aiyolist.append(1)
aiyolist.append(2)
aiyolist2 = [5.5, "hi", 3, 99, 222, 222]
print(aiyolist2[0])
aiyolist2[0]= 333.333

print(len(aiyolist), sum(aiyolist), aiyolist2.count(222))
print(aiyolist2[0], aiyolist2[-1], aiyolist2[1:3], aiyolist2[2:])