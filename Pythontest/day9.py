globals_var=12
def func ():
    local_var=11
    print (globals_var)
    print (local_var)

func()
print (globals_var)


xy=100
def aaa():
    xy=200
    print (xy)
aaa()

# def 后面的函数名，头尾要一致

# 使⽤global关键字，可以将局部变量同全局变量绑定在⼀起
# 使⽤global关键字声明全局变量时，⽆法直接赋值，⽐ 如“global t=1”的写法存在语法错误。
a=1
def math():
    global a
    b=1+a
    print (b)
math()
print (a)
# or  也可以直接在函数定义的时候直接给a赋值，这样就不用用global声明变量了
def math(a=1):
    b=1+a
    print (b)



def func1(i,j=100,):
    print (i+j)
    func1()


def name_args(name,greeting):
    print (greeting+" "+name)
name_args(name='jim',greeting='hello')
name_args(greeting='hello',name='jim')
name_args('jim',greeting='hello')
# 关键字参数使⽤“name=value”的名称、值对传递数据，正如上⾯代码演⽰的那样，使⽤关键字参数的时候，参数的顺序是可以调换的，⽽且位置参数和关键字参数 可以混合使⽤（只能先使⽤位置参数，后使⽤关键字参数）


def a(a=1,b=2):
    if a>b:
        return a,b
    else:
        return b,a
s=a(12,100)
print (s)
print (type(s))














