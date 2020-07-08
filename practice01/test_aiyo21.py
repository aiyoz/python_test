
"""
from https://github.com/playone/forpython/blob/master/Newbie/test18.py
http://www.chinesepython.org/pythonfoundry/marrpydoc/python5.htm
re 正規表示式的練習
其內容格式大致為：

Last_Name, First_Name Middle_Name: Phone_Number

觀察 Last_Name 的組成，只有英文字母而無數字，可用 [a-zA-Z] 來表示，而完整的 Last_Name 包括一個以上的英文字母，所以用 [a-zA-Z]+ 來表示。Last_Name 後緊跟著一個逗號 (,)。

First_Name 部份原則上如法泡製，但 Middle_Name 算是可有可無，因此可用 [a-zA-Z]+( [a-zA-Z]+)? 來表示。之後再緊跟著一個冒號 (:)。

Phone_Number 部份，本範例所呈現者並不算複雜，可分成 4 個數字 (數字可用 \d 表示)，緊跟一個可有可無的 - 符號，再接 6 個數字，可以用 \d\d\d\d-?\d\d\d\d\d\d 來表示。

檔案中，除了兩行 "Beatles, Liverpool" 與 "Smiths, Manchester" 之外，都符合上述的表示式分析。
"""


import re

regexp = re.compile(r'(?P<last>[a-zA-Z]+),' #?P<name> 群組化
                    r' (?P<first>[a-zA-Z]+)'
                    r'( (?P<middle>([a-zA-Z]+)))?'
                    r': (?P<phone>\d\d\d\d-?\d\d\d\d\d\d)'
                    r'( (?P<email>[a-zA-Z0-9.]*["@"]*[a-zA-Z0-9.]*))?'
                    )
file = open('dirbook.txt', 'r')
filew = open('dirbookre.txt', 'w')
filew.writelines('first_name middle_name last_name + phone_no + email\n')
for line in file.readlines():
    #print(line)
    result = regexp.search(line)
    #print(result)
    if result==None:
        print ('Not found')
    else:
        last_name = result.group('last')
        first_name = result.group('first')
        middle_name = result.group('middle')
        if middle_name==None:
            middle_name = ''
        email2 = result.group('email')
        if email2==None:
            email2 = ''
        phone_no = result.group('phone')
        print ('Name: '+'fn:'+first_name+' ' \
        + 'mn:'+middle_name + ' ' \
        + 'ln:'+last_name +'\n' \
        + 'Phone: ' + phone_no
        + ' Email= ' + email2)
        filew.writelines(first_name+' '+middle_name+' '+last_name+':'+phone_no+email2+'\n')

file.close()


"""
基本用法
import re
regexp = re.compile(r"[a-zA-Z]+,"
r" [a-zA-Z]+"
r"( [a-zA-Z]+)?"
r": \d\d\d\d-?\d\d\d\d\d\d")
file = open("dirbook.txt", 'r')
for line in file.readlines():
    if regexp.search(line):
        print "found"
file.close()
"""