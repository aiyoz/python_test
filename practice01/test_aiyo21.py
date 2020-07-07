
# from https://github.com/playone/forpython/blob/master/Newbie/test18.py

"""
re 正規表示式的練習
"""


import re

regexp = re.compile(r'(?P<last>[a-zA-Z]+),' #?P<name> 群組化
                    r' (?P<first>[a-zA-Z]+)'
                    r'( (?P<middle>([a-zA-Z]+)))?'
                    r': (?P<phone>\d\d\d\d-?\d\d\d\d\d\d)'
                    )
file = open('dirbook.txt', 'r')
filew = open('dirbookre.txt', 'w')
filew.writelines('first_name middle_name last_name +phone_no\n')
for line in file.readlines():
    print(line)
    result = regexp.search(line)
    print(result)
    if result==None:
        print ('Not found')
    else:
        last_name = result.group('last')
        first_name = result.group('first')
        middle_name = result.group('middle')
        if middle_name==None:
            middle_name = ''
        phone_no = result.group('phone')
        print ('Name: '+'fn:'+first_name+' ' \
        + 'mn:'+middle_name + ' ' \
        + 'ln:'+last_name +'\n' \
        + 'Phone: ' + phone_no)
        filew.writelines(first_name+' '+middle_name+' '+last_name+':'+phone_no+'\n')

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