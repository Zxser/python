#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:xiaoer
@file: 2.py 
@time: 2018/05/{DAY} 
"""
import requests
import re
import json

url='http://music.163.com/discover/toplist?id=3778678'
headers = {
"Host":"music.163.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36",
}
data = {
    "params": "Ht6h3WdCblPVgB5R85G60R0OpfiUkNF8oiS8rm7TBllxXh4UscmYWLecmDyc1Qipj7MhOSxhawhCO0SqRiStPDKs1uB9C1GIGNH2AIXFfqRnj1mzSjXym3DAUw2ZNUCt010klfZde + MmCeoEnWPg8UG4AtwL83QRZ6o2QnzovUNnDxcVjZSHZAb2TBzQSSbt",
    "encSecKey": "7b452bd5846e1420fd4a4810ea09e015459d827ffef6ddf8ab53cb229f26cddbc4cfeb8d9fecdfb8d24b6a017779a2579cb9ad5c5b8b34989136ceabecb64fe4a33fe7c8a40e4d291a8ae1b129ad75c1ea4b9752e55832042e57e38172942d37b096fc2cdfb70aff43812ece50280b26c8a372e906ea659f00804a09682f7129"
}
r = requests.get(url,headers=headers)
r = r.text

pat1=r'<ul class="f-hide"><li><a href="/song\?id=\d*?">.*</a></li></ul>'
result=re.compile(pat1).findall(r)
result = result[0]

pat2=r'<li><a href="/song\?id=\d*?">(.*?)</a></li>'
pat3=r'<li><a href="/song\?id=(\d*?)">.*?</a></li>'
hot_song_name=re.compile(pat2).findall(result)
hot_song_id=re.compile(pat3).findall(result)

x = 0

for i in range(len(hot_song_id)):
    url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + hot_song_id[i] + '?csrf_token='

    r = requests.post(url, headers=headers, data=data)
    html = r.text
    pat = r'"content":"(\S+?)"'
    content = re.compile(pat).findall(html)

    num = 0

    f = open('./text1.txt', 'ab')
    f.write((hot_song_name[i] + ";" + "\n").encode('utf-8'))

    for i in range(len(content)):
        num+=1
        f.write((str(num)+'.'+ content[i] +'\n').encode("utf-8"))
    f.write(('\n==============================================\n\n').encode('utf-8'))
    f.close()
    x += 1
    print ("录入"+str(x)+"首成功\n")










