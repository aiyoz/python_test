
# from https://github.com/playone/forpython/blob/master/Newbie/test11.py

"""
I/O
檔案讀取 print 還有函式write
"""

with open('db2.txt') as f:
    readfile=f.read()
    print(readfile)
    print(f)
    with open('copy.txt','w') as ff:
        readfile = readfile + '\n\ntest2020/7/6'
        ff.write(readfile)
    print(readfile)