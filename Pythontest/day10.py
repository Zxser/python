# 函数文档字符串
# Python有⼀个甚是优美的功能称作⽂档字符串（DocumentationStrings），
# 在称 呼它时通常会使⽤另⼀个短⼀些的名字docstrings。
# DocStrings是⼀款你应当使⽤的重要⼯具，
# 它能够帮助你更好地记录程序并让其更加易于理解。
# 令⼈惊叹的是，当程序实际运⾏时，我们甚⾄可以通过⼀个函数来获取⽂档

def a  (x,y):
    if x > y:
        print (x,'is a maximum')
        print (y,'is a minimum')
    else:
        print (x,'is a maxumin')
        print (y,'is a minimum')
a(1,2)
print (a.__doc__)
