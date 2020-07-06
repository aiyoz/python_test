
# from https://github.com/playone/forpython/blob/master/Newbie/test11.py

"""
I/O
檔案讀取 print 還有函式write
"""

import sys

file_in = open('db2.txt', 'r')
file_out = open('copy.txt', 'w')

for line in file_in:
    #print(line)
    for i in range(0, len(line)):
        if line[i] != '\n':
            sys.stdout.write(line[i]+',')
        else:
            sys.stdout.write(line[i])
        file_out.write(line[i])

sys.stdout.write('\n')
file_in.close()
file_out.close()


