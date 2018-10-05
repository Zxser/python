# 函数文档字符串
# Python有⼀个甚是优美的功能称作⽂档字符串（DocumentationStrings），
# 在称呼它时通常会使⽤另⼀个短⼀些的名字docstrings。
# DocStrings是⼀款你应当使⽤的重要⼯具，
# 它能够帮助你更好地记录程序并让其更加易于理解。
# 令⼈惊叹的是，当程序实际运⾏时，我们甚⾄可以通过⼀个函数来获取⽂档
# 在函数的第一个逻辑行的字符串是这个函数的 文档字符串 。注意，DocStrings也适用于模块和类，我们会在后面相应的章节学习它们。
# 文档字符串的惯例是一个多行字符串，它的首行以大写字母开始，句号结尾。第二行是空行，从第三行开始是详细的描述。 强烈建议 你在你的函数中使用文档字符串时遵循这个惯例。
# 你可以使用__doc__（注意双下划线）调用printMax函数的文档字符串属性（属于函数的名称）。请记住Python把 每一样东西 都作为对象，包括这个函数。我们会在后面的类一章学习更多关于对象的知识。
# 如果你已经在Python中使用过help()，那么你已经看到过DocStings的使用了！它所做的只是抓取函数的__doc__属性，然后整洁地展示给你。你可以对上面这个函数尝试一下——只是在你的程序中包括help(printMax)。记住按q退出help。
# 自动化工具也可以以同样的方式从你的程序中提取文档。因此，我 强烈建议 你对你所写的任何正式函数编写文档字符串。随你的Python发行版附带的pydoc命令，与help()类似地使用DocStrings。

def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x=int(x)
    y=int(y)

    if x > y:
        print (x, 'is maximum')
    else:
        print (y, 'is maximum')
print_max(1, 2)
print (print_max.__doc__)


def printMax(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x = int(x) # convert to integers, if possible
    y = int(y)

    if x > y:
        print (x, 'is maximum')
    else:
        print (y, 'is maximum')

printMax(3, 5)
print (printMax.__doc__)
