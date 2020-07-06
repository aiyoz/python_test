
# from https://github.com/playone/forpython/blob/master/Newbie/test11.py

"""
I/O
檔案讀取 print 還有函式write
"""

#import sys

#file_in = file('db2.txt', 'r')
#f=open('db2.txt','r')
with open('db2.txt') as f:

    readfile=f.read()

    print(readfile)
    #print(f)
    with open('copy.txt','w') as ff:



        #ff.write(readfile)
        readfile = readfile + '\n\ntest2020/7/6'
        ff.write(readfile)
    print(readfile)
    #ff.write(readfile)
    #print(ff)


#file_out = file('copy.txt', 'w')



#for line in file_in:
#    for i in range(0, len(line)):
#        if line[i] != '\n':
#            sys.stdout.write(line[i]+',')
#        else:
#            sys.stdout.write(line[i])
#        file_out.write(line[i])

#sys.stdout.write('\n')
#file_in.close()
#file_out.close()