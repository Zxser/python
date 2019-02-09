# -*- coding:utf=8 -*-
# a=['a','b','c']
# a.sort()
# print (a)



# s1=12.34
# r1=s1*3.14*2
# print (r1)
#
# s1=1
# s2=2
# print (max(s1,s2))
# print (max(2,3,1,-5))
#
# print (str(1.23))


# birth=input('birth: ')
# s=int(birth)
# if s < 2000:
#     print('00qian')
# else:
#     print('00hou')


# age=3
# if age >=18:
#     print ('you age is',age)
#     print ('adult')
# else:
#     print ('you age is',age)
#     print ('teenager')

# name=['a','b','c']
# for name in name:
#     print (name)
#



# 果要计算 1-100 的整数之和，从 1 写到 100 有点困难，幸好 Python
# 提供一个 range() 函数，可以生成一个整数序列，再通过 list() 函数可
# 以转换为 list。比如 range(5) 生成的序列是从 0 开始小于 5 的整数
# sum=0
# list=(range(101))
# list1=list(range(101))
# print (list1)
# for x in list(range(101)):
#     sum=sum+x
# print (x)
# print (sum)

# step(2)
for x in range(101):
    sum=sum+x
print (sum)
