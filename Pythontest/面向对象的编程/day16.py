# # -*- coding:utf=8 -*-
# # a=['a','b','c']
# # a.sort()
# # print (a)
#
#
#
# # s1=12.34
# # r1=s1*3.14*2
# # print (r1)
# #
# # s1=1
# # s2=2
# # print (max(s1,s2))
# # print (max(2,3,1,-5))
# #
# # print (str(1.23))
#
#
# # birth=input('birth: ')
# # s=int(birth)
# # if s < 2000:
# #     print('00qian')
# # else:
# #     print('00hou')
#
#
# # age=3
# # if age >=18:
# #     print ('you age is',age)
# #     print ('adult')
# # else:
# #     print ('you age is',age)
# #     print ('teenager')
#
# # name=['a','b','c']
# # for name in name:
# #     print (name)
# #
#
#
#
# # 果要计算 1-100 的整数之和，从 1 写到 100 有点困难，幸好 Python
# # 提供一个 range() 函数，可以生成一个整数序列，再通过 list() 函数可
# # 以转换为 list。比如 range(5) 生成的序列是从 0 开始小于 5 的整数
# # sum=0
# # list=(range(101))
# # list1=list(range(101))
# # print (list1)
# # for x in list(range(101)):
# #     sum=sum+x
# # print (x)
# # print (sum)
# #
# # # step(2)
# # for x in range(101):
# #     sum=sum+x
# # print (sum)
#
# # #step3
# # sum=0
# # n=99
# # while n>0:
# #     sum=sum+n
# #     n=n-2
# # print(sum)
# #
# # L=['a','b','c']
# # for x in L:
# #     print ('hello',x,'!')
#
# # name=['a','b','c']
# # age=[1,2,3]
#
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print (d['Michael'])
# # 把数据放入 dict 的方法，除了初始化时指定外，还可以通过 key 放入：
# d['Bob']=67
# print (d['Bob'])
#
# # 由于一个 key 只能对应一个 value，所以，多次对一个 key 放入 value，
# # 后面的值会把前面的值冲掉：
# d['Tracy']=95
# d['Tracy']=94
# print (d['Tracy'])
# # 你可以猜到，这种 key-value 存储方式，在放进去的时候，必须根据 key
# # 算出 value 的存放位置，这样，取的时候才能根据 key 直接拿到 value。
#
# # 要删除一个 key，用 pop(key) 方法，对应的 value 也会从 dict 中删除：
# d.pop('Bob')
# print (d)
#
# # 和 list 比较，dict 有以下几个特点：
# # 1. 查找和插入的速度极快，不会随着 key 的增加而增加；
# # 2. 需要占用大量的内存，内存浪费多。
#
# # 而 list 相反：
# # 1. 查找和插入的时间随着元素的增加而增加；
# # 2. 占用空间小，浪费内存很少。
# # dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，
# # 正确使用 dict 非常重要，需要牢记的第一条就是 dict 的 key 必须是 不可
# # 变对象。
# # 这是因为 dict 根据 key 来计算 value 的存储位置，如果每次计算相同的
# # key 得出的结果不同，那 dict 内部就完全混乱了。这个通过 key 计算位置的算法称为哈希算法（Hash）。
#
# # 注意，传入的参数 [1, 2, 3] 是一个 list，而显示的 {1, 2, 3} 只是告诉你
# # 这个 set 内部有 1，2，3 这 3 个元素，显示的顺序也不表示 set 是有序的。。
# # 重复元素在 set 中自动被过滤：
# # >>> s = set([1, 1, 2, 2, 3, 3])
# # >>> s
# # # {1, 2, 3}
# #
# # s= set([3,2,1,1,1,2,3,4,])
# # s.add(5)
# # s.remove(1)
# # print (s)
# # set 可以看成数学意义上的无序和无重复元素的集合，因此，两个 set 可
# # 以做数学意义上的交集、并集等操作：
# s1=set([1,2,3,4])
# s2=set([4,5,6,7])
# print (s1&s2)
# print (s1|s2)
# # set 和 dict 的唯一区别仅在于没有存储对应的 value，但是，set 的原理和
# # dict 一样，所以，同样不可以放入可变对象，因为无法判断两个可变对
# # 象是否相等，也就无法保证 set 内部“不会有重复元素”。试试把 list 放入
# # set，看看是否会报错。
# # 对于可变对象，比如 list，对 list 进行操作，list 内部的内容是会变化的，
# # 比如：
# # >>> a = ['c', 'b', 'a']
# # >>> a.sort()
# # >>> a
# # ['a', 'b', 'c']
# # 而对于不可变对象，比如 str，对 str 进行操作呢：
# # >>> a = 'abc'
# # >>> a.replace('a', 'A')
# # 'Abc'
# # >>> a
# # 'abc'
# # 虽然字符串有个 replace() 方法，也确实变出了 'Abc' ，但变量 a 最后仍
# # 是 'abc' ，应该怎么理解呢？
# # 我们先把代码改成下面这样：
# # >>> a = 'abc'
# # >>> b = a.replace('a', 'A')
# # >>> b
# # print (help(abs))
# # list=['a','b','c']
# # print (max(list))
# # print (min(list))
# # list1=[1,2,3,4.5,5.1]
# # print (int(5.1))
#
# # a=[1,2,3,4,5]
# #
# # print (max(a))
# # print (min(a))
# #
# # sum=0
# # for x in range(1001):
# #     sum=sum+x
# # print (sum)
#
#
# # n1=255
# # n2=1000
# # print (hex(n1))
#
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x

