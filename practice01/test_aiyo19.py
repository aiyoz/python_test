
# from https://github.com/playone/forpython/blob/master/Newbie/test16.py

"""
99乘法表練習
print + %value
"""
import xlwt
nn=xlwt.Workbook()
pg1=nn.add_sheet('page_one')

for i in range(0, 10):
    for j in range(0, 10):
        print ('%i * %i = %i' %(i, j, i*j))
        pg1.write(i,j,i*j)

nn.save('9x9.xls')