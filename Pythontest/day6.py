s1='welcome'
print ('come' in s1)
print ('a'in s1)
print ('tim'=='tie')
print ('tim'=='tim')
print ('free' !='free')
print ('free' !='freedom')
print ('feee' > 'freedom')
print ('freedom' > 'free' )
print ('freedom' < 'free')
print ('freedom' >= 'free')
print ('free' <= 'freedom')
print ('ab' <= 'abc')

# s='mengqingyu'
# for i in s:
# 	print (i,end='')

a='welcome to xinchao'
print (a.isalnum())
print ('Welcome'.isalpha())
print ('2018'.isdigit())
print('2018w'.isalnum())
print('first'.isidentifier())

print (' '.isidentifier())
print (' '.isspace())
print ('first'.islower())
print ('First'.isupper())
print ('firest'.isidentifier())





s='welcome to python'
print (s.find('y'))
print (s.find('p'))
print (s.replace('y','a'))
print (s.endswith('thon'))
