#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:xiaoer
@file: get_data.py 
@time: 2018/05/{DAY} 
"""
import time

def get_data():
    i = 1
    while i == 1:
        x = input("请输入开始日期：\n")
        try:
            time.strptime(x, "%Y%m%d")
            i += 1
        except:
            print("日期格式错误,请重新输入!\n")

    while i == 2 :
        y = input("请输入结束日期：\n")
        try:
            time.strptime(y, "%Y%m%d")
            i += 1
        except:
            print("日期格式错误,请重新输入!\n")

    return [i for i in range(int (x),int (y)+1)]

