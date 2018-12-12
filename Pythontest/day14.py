age=20
if age>=18:
	print ('your age is',age)
	print ('hello')



age=3
if age >=18:
	print ('your age is',age)
	print ('adult')
else:
	print ('your age is',age)
	print ('teenager')



age=3
if age >=18:
	print ('adult')
elif age <=6:
	print ('world')
else:
	print ('kid')


# 是从上往下判断，如果在某个判断上是 True，
# 把该判断对应的语句执行后，就忽略掉剩下的 elif 和 else
age=20
if age >=6:
	print ('teenager')
elif age >=18:
	print ('adult')
else:
	print ('kid')



birth =1996
if birth < 2000:
	print ('00qian')
else:
	print ('00hou')


print ('%s-%s' %(3,1))
print ('%.2f' %3.14159276723)
s1=72
s2=85
r=s2-s1
print ('%.2f%%'%r)


a=['a','b','c']
print (a[0])


t=(1,)
print (t)

t=('a','b',['c','d'])
t[2][0]='x'
t[2][1]='y'
print (t)
# print (t[2][0]='x')
# print (t[2][1]='y')



L = [     
['Apple', 'Google', 'Microsoft'],    
['Java', 'Python', 'Ruby', 'PHP'],     
['Adam', 'Bart', 'Lisa'] 
]
print (L[0][0],L[1][2],L[2][2])

age=20
if age >= 18:
	print ('your age is',age)   #逗号
	print ('adult')

age=19
if age	>=19:
	print ('hello')
else:
	print ('world')

age=6
if age >=18:
	print ('adult')
elif age>=6:
	print ('message')
else:
	print ('kid')
age=20
if age >=6:
	print ('teenager')
elif age>=18:
	print ('adult')
else:
	print ('kid')

age=20
if age >=10:
	print ('hello')
else:
	print ('world')

#
# s=input('birth: ')
# birth=int(s)
# if birth >=2000:
# 	print ('00qian')
# else:
# 	print ('00hou')
#
# s=input ('birth: ')
# birth = int(s)
# if birth >=2000:
# 	print ('00qian')
# else:
# 	print ('00hou')


a=input ('height: ')#先接受输入，其次进行格式化
height =int (a)
b=input ('weight: ')
weight =int (b)
bmi=height/(weight*weight)
print ('you bmi is ',bmi)
if bmi <=18.5:
	print ('guoqing')
elif bmi <25:
	print ('normal')
elif bmi <28:
	print ('guozhong')
elif bmi <32:
	print ('feipang')
else:
	print ('yanzhongfeipang')

a=input ('height: ')
height = int (a)
b=input ('weight: ')
weight = int (b)
bmi=height * 2
print (bmi)
