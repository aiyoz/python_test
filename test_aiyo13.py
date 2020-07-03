
# from https://github.com/playone/forpython/blob/master/Newbie/test10.py

"""
class 開頭 : 結尾
Class 的初始化函式是由兩條底線包含著init做宣告
"""

class student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def set_name(self, name):
        self.name = name

Student_object = []
Student_object.append(student('john', 'A', 10))
Student_object.append(student('becky', 'B', 11))
Student_object.append(student('Lin', 'S', 12))

print (Student_object)

Student_object[0].set_name('John')

for i in Student_object:
    print (i.name, i.grade, i.age)