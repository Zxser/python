#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:xiaoer
@file: demo5.py 
@time: 2018/05/{DAY} 
"""

import re

list = ['https://i.pximg.net/c/150x150/img-master/img/2018/04/30/12/07/36/68484171_p0_master1200.jpg', 'https://i.pximg.net/c/600x600/img-master/img/2018/04/30/12/07/36/68484171_p0_master1200.jpg', 'https://i.pximg.net/img-original/img/2018/04/30/12/07/36/68484171_p0.jpg', 'https://i.pximg.net/c/150x150/img-master/img/2018/04/30/12/07/36/68484171_p0_master1200.jpg']

rap = "\d+"
num = []
list_ = []
for i in range(len(list)):
    r = re.compile(rap).findall(list[i])
    num.append(r)
for i in range(len(num)):
    for j in range(len(num[i])):
        num[i][0]
    list_.append(num[i][0])
list_ = [int(c) for c in list_]
indexes = list_.index(max(list_))

print(type(indexes))