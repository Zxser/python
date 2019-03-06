# def person(name,age,*,city,job):
#     print (name,age,city,job)

# print (person('jack','24',city='beijing',job='work'))

# print ('hello world')

# def abc(name,age,*,city='beijing','job'):
#     print (name,age,city,job)
# print (abc('mengqingyu',24,'engineer'))

# def person(name, age, *, city='Beijing', job):
# 	print (name,age,city,job)
# print (person('mengqingyu',24,job='engineer'))


# def person(name,age,*,city='beijing',job):
# 	print (name,age,city,job)
# print (person('mengqingyu',24,job='engineer'))

def person(name,age,*,city='beijing',*,job='engineer',):
	print (name,age,city,job)
print (person('mengqingyu',24))




