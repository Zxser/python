class person:
    def __init__(self,name):
            self.name=name
def whoami(self):
    print  ("You are" + self.name)


# empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。
# 第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
# self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
# 构建一个简单的类
# !/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print (
        "Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print (
        "Name : ", self.name, ", Salary: ", self.salary)

class a:
    empcount = 0
    def __init__(self,name,salary):
        self.name=name
        self.salary =salary
        Employee.empCount +=1
    def displaycount(self):
        print
        ("total employee %d" % Employee.empCount)
    def displayEmployee(self):
        print
        ("Name:",self.name,"salary:",self.salary)

class person:
        def __init__(self,name):
            self.name=name
        def whoami(self):
            return "you are " + self.name

# p1=person('tom')
p1=person('jerry')
print(p1.whoami())
print(p1.name)


