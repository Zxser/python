#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:xiaoer
@file: demo.py 
@time: 2018/05/{DAY} 
"""

import os
for root, dirs, files in os.walk(r"E:\Python\pixiv\1"):
    files
for root1, dirs1, files1 in os.walk(r"E:\Python\pixiv\12"):
    files1
for i in files:
    if i in files1:
        os.remove(r"E:\Python\pixiv\1\\" + i)
# os.remove(r"E:\Python\pixiv\picture\123.txt")