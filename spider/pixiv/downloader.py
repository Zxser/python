#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:xiaoer
@file: demo1.py
@time: 2018/05/{DAY} 
"""
import re
import requests
import get_All_img_list

def downloader():

    All_img_list,id_list= get_All_img_list.get_All_img_list()

    for i in range(len(All_img_list)):
        url = str(All_img_list[i])
        rap = "(6[0-9]{7})"
        num = re.compile(rap).findall(url)
        num = num[0]
        headers = {"referer": "https://www.pixiv.net/member_illust.php?mode=medium&illust_id=" + str(num),
                   "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"}
        r = requests.get(url,headers=headers,stream=True)
        with open ("E:\Python\pixiv\picture\\"+str(num)+".jpg","wb") as f:
            f.write(r.content)
        print ("已下载图片"+str(num)+"剩余"+str(len(All_img_list)-i)+"张图片未下载")







