#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:xiaoer
@file: douban TOP250.py
@time: 2018/04/{DAY} 
"""
import requests
from bs4 import BeautifulSoup

headers = {
"Host":'movie.douban.com',
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"
}
movies = []
urls = []
for i in range(0,10):
    url = "https://movie.douban.com/top250?start="+str(i*25)+"&filter="
    urls.append(url)
for url in urls:
    r = requests.get(url, headers=headers,timeout=10)
    soup = BeautifulSoup(r.text,"lxml")
    div_list = soup.find_all('div',class_='hd')
    for div in div_list:
        movie = div.a.span.text.strip()
        movies.append(movie)
print (movies)








