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


