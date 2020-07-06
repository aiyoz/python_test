
# from https://github.com/playone/forpython/blob/master/Newbie/test13.py
"""
例外處理
"""

def my_divide():
    try:
        10 / 0
    except ZeroDivisionError:
        print('不能除以0')
    else:
        print('沒有任何錯誤')
    finally:
        print('無論有沒有錯誤都會執行這一行')

my_divide()

def my_divide2():
    try:
        0 / 1
    except ZeroDivisionError:
        print('不能除以0')
    else:
        print('沒有任何錯誤')
    finally:
        print('無論有沒有錯誤都會執行這一行')

my_divide2()