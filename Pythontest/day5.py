s='abc'
print (s[0])
print (s[-1])
a='tom and' + ' jerry ' 
print (a)
a='love ' *3
print (a)

b='mengqingyu'
b1=b[1:3]
print (b1)
print (b[1:4])
b2="eng" in b1
print (b2)
#等同于
print ("eng" in b)


print (len('hello'))
print (max('123400'))
print (min('1230'))



user_name='mengqingyu'
print ('i am %s'%user_name)

c='mengqingyu'
print (c[1:3])
print (c[-4:])
print (c[1::2])
d=[1,2,3,4,5,6,7,8,9,10]
print (max(d))
print (min(d))
print (d[1::2])
print (d[1::1])
print (d[0:10:2])
print (d[0:10:3])


hello1='hello '
name='mengqingyu'
print (hello1+name)
print (hello1 * 6)


name1='tom'
mychar='a'
name1=str()
name2=str("newstring")
print (name2)
print (name1)
print (id(name1))
print (id(name2))

str1='welcome'
str2='welcome'
print (id(str1),id(str2))
print (str1+str2)
str2 += ' mengqingyu'
print (str2)
print (id (str2))