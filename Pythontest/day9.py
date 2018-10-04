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

