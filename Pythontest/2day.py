s="welcome"
print (s.isalnum())
# or
print ("welcome".isalnum())
# isalnum() 如果 string 包含字符都是字母或数字则返回 True
# isalpha() 如果 string 包含字符都是字母则返回 True
# isdigit() 如果 string 包含字符都是数字则返回 True
# isidentifier() 判断字符串是否是合格的标识名
# islower() 判断字符串中是否都是⼩写字母
# isupper() 判断字符串中是否都是⼤写字母
# isspace() 判断字符串是否由空格组成
print ("welcome".isalpha())
print ("WELCOME".isupper())
print ("Welcome".isupper())
print (" \t\t ".isspace())
print ("welcome to xinchao".find('to'))
print ("welcome to xinchao".replace('to','and'))



# 查找字符串
# endswith(s1: str): bool 如果字符串以指定的字符串结尾，则返回真
# startswith(s1: str): bool 如果字符串以指定的字符串开始，则返回真
# count(substring): int 返回⼦字符串在字符串中出现的次数
# find(s1): int 返回⼦字符串在字符串中第⼀次出现的索引，如果没有，则返回-1
# rfind(s1): int 返回⼦字符串在字符串中最后⼀次出现的索引，如果没有，则返回-1

print ("welcome to xinchao".endswith("xinchao"))
print ("welcome to xinchao".startswith("welcome"))
print ("welcome to xinchao".find("xinchao"))
print ("welcome to xinchao".find("aaa"))
print ("welcome to xinchao".rfind("aaa"))
print ("welcome to xinchaoaaa".count("a"))



# Python 的列表（list）对象是最常⽤的序列 (Sequence)。与字符串是不可变序列不同，列表是可变的。可通过对偏移量进⾏修改和读取
# 列表可通过索引对其对应的元素进⾏赋值，从⽽改变列表的内容，如：
a=[2,2,2]
a[1]=1
print (a)

a=[2,2,2]
del a[1]
print (a)

# 分⽚赋值可以⼀次为多个元素赋值，并且不⽤考虑原列表的长度是否和新的列表长度⼀直，如：
name = list('Python')
print (name)
name [2:] = list ('data')
print (name)
name [3:] = list ('data')
print (name)
name [4:5] = list ('data')
print (name)


# 分⽚赋值还可以⽤来插⼊元素，如：
name = list ('Python')
name [1:] = list ('--')
print (name)
name = list ('Python')
name [1:1] = list ('--')
print (name)


# 追加列表元素
code = [1,2,3]
code.append(4)
print (code)

# count ⽅法统计指定元素在列表中出现的次数，如：

code = ['1','2','3','1','3','2','3','3']
print (code.count('3'))


code = [1,2,3,3,3,3,3,3,3,2,2,2,2]
print (code.count(3))


# extend ⽅法在列表的末尾⼀次性追加另⼀个序列中的多个值，如：
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print (a)


# 以上代码将把 b 列表追加到 a 列表中，打印出的 a 列表的值为 [1, 2, 3, 4, 5, 6]。和序列加运算不同， extend ⽅法将改变原有列表的内容，⽽加运算却不会。
a=[1,2,3]
a + [4,5,6]
print (a)


 BH9T4-4N7CW-67J3M-64J36-WW98Y



 # 链接：https://pan.baidu.com/s/1bmXgmqDavDlwxeYJT7fF8g 密码：70e9



TMCM
Officescan
Office scan client
TMMS

#07487




*#123# 
*#789# ping



日常使用方法
基本配置策略
后期维护方法
