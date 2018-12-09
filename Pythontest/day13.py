# from Pythontest.day5 import d

print ('I','love','you')
print ('100+200 =',100+200)
print ('1024x768 =',1024*768)
a=100
if a==0:
	print (a)
else:
	print (-a)
print ('I\'m \"ok\"')
print ('I\'m ok')
print ('I\'m \nlearning python')
print ('\\\\\n\\\\')#\n 表示换行，\t 表示制表符(一个tab)，字符\本身也要转义，所以\\表示的字符就是\。
print ('\\\\\t\\\\')
print ('	\\')
print (r'hello')
print (r'\\\\t\\')
print ('''
	line1
	line2
	line3
	''')


print ('\\\\')


print ('I\'am ok')
print ('I\'am \n learning python')
print ('''line1
...line2
...line3''')
print ('''...''')



# if age >=18:
# 	print('jerry')
# else:
# 	print ('Tom')

a=123
print (a)
a='ABC'
print (a)
# 一种错误的用法
# int a=123
# a='ABC'
# print (a)

a=123
b=a
a='ABC'
print (b)

print (10/3)
print (10//3)
print (10%3)

print (9/3)

n=123
f=456.789
s1='hello world'
s2='hello \'adam\''
s5='hello \n \'adam\''
s3=(r'hello,"bart"')
s4=(r'''hello,
	lisa!''')
print (n,f,s1,s2,s3,s4,s5)





#字符编码问题
print (ord('A'))
print (ord('中'))
print (chr(20013))
print (ord('国'))
print ('\u4e2d\u6587')
print ('ABC'.encode('ascii'))
print ('中文'.encode('utf-8'))
print ('abc'.encode('ascii'))
print (b'abc'.decode('ascii'))
print (b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print (len('abc'))
print (len('中文'))
#为了让它按 UTF-8 编码读取，我们通常在文件开头写上这两行
#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-




# 在字符串内部，%s表示用字符串替换，
# %d 表示用整数替换，
# 有几个%?占位符，后面就跟几个变量或者值，
# 顺序要对应好。如果只有一个%?，括号可以省略。
# %d 整数
# %f 浮点数
# %s 字符串
# %x 十六进制整数


print ("hello,my name's %s i'am %d years,old" %('mengqingyu',19))
print ("hello,my name's %(name)s. i am %(age)d year old" % {'name':'mengqingyu','age':19})
print ("I'm %(name)s. I'm %(age)d year old" % {'name':'Vamei', 'age':99})
# print("I'm %s. I'm %d year old" % ('Vamei', 99))
print ('%03d-%03d' %(3,1))
print ('%.3f' %3.1415926)
print ("i  am my name is %s, i'm %s years old "  % ("mengqingyu","19"))
print ("age:%s,name:%s" %(25,"mengqingyu"))
print ("groth rate:%d%%" %(7))
print ("my name is %s,i am %s years old" %("mengqingyu",19))

s1=72
s2=85
print ("xiaoming is %.1f%%" %(s2-s1))

test=['test1','test2','test3']
test.append('test4')

print (test)
print (test[0])
print (test[1])
print (test[2])
print (test[-1])
test.pop(-1)
print (test[-1])
# IndexError: list index out of range

list=('apple中',123,True)
print (list)

p=['asp','php']
s=['python','java',p,'scheme']
print (p,s)
L=[""]
print (len(L))

classments=('tom','jerry','Michael')
print (classments)


# tuple
t=(1,2)
print (t)
t=()
print (t)
t=(1,)
print (t)


# t=('a','b',['A','B'])
# print (t[2])
# print (t[2][0]='X')
# -*- coding: utf-8 -*- 
 
L = [['Apple', 'Google', 'Microsoft'],     
	['Java', 'Python', 'Ruby', 'PHP'],
	['Adam', 'Bart', 'Lisa'] ] 
print (L[0][0])
print (L[1][1])
print (L[2][2])




# age=20
# if age >=18:
# 	print ('your age is',age)
# 	print ('adult')
# age=20
# if age >=18:
# 	print ('your age is ',age)
# 	print ('adult')
# else:
# 	print ('your age is ',age)
# 	print ('teenager')

