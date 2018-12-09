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