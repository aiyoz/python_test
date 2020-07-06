
# from https://github.com/playone/forpython/blob/master/Newbie/test15.py

"""
這程式是練習excel的讀取寫入
會用到函式 xlwt
"""

import xlwt
from datetime import datetime
from time import time

wb = xlwt.Workbook() #宣告一個excel

sh = wb.add_sheet('A new sheet') #新增一個sheet

#以下是寫入資料
sh.write(0, 0, 'hello100')
sh.write(1, 0, 'world')
sh.write(2, 0, 1234567)
sh.write(2, 1, '2020_07_06')
sh.write(2, 2, str(datetime.now().year) +'/'+ str(datetime.now().month)+'/'+str(datetime.now().day))
aiyotime=str(datetime.now())
print(aiyotime)
sh.write(2, 3, aiyotime)

wb.save('xlwt_test.xls') #存檔