#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:xiaoer
@file: file_manager.py 
@time: 2018/05/{DAY} 
"""
import os


def file_manager():
    for root, dirs, files in os.walk(r"E:\Python\pixiv\old_picture"):
        files
    for root1, dirs1, files1 in os.walk(r"E:\Python\pixiv\picture"):
        files1
    for i in files1:
        if i in files:
            os.remove(r"E:\Python\pixiv\picture\\" + i)
            print("已删除文件"+i)