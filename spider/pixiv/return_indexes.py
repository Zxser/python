#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:xiaoer
@file: return_indexes.py 
@time: 2018/05/{DAY} 
"""

import re
def return_indexes(list):
    rap = "[0-9]{3}"
    num = []
    list_ = []
    for i in range(len(list)):
        r = re.compile(rap).findall(list[i])
        num.append(r)
    for i in range(len(num)):
        for j in range(len(num[i])):
            num[i][0]
        list_.append(num[i][0])
    list_=[int(c) for c in list_]
    indexes = list_.index(max(list_))

    return indexes

