# -*- coding: gbk -*-
from bs4 import BeautifulSoup
import urllib
import codecs
import re
def download(url,name):
    soup=BeautifulSoup(urllib.urlopen(url).read())
    cont=soup.find(id="contents").text
    title=soup.title.text
    f=codecs.open('%s.txt'%name,'a','utf-8')
    f.write('\r\n'+title+'\r\n')
    f.write(cont)
    f.close()
def search():
    name=raw_input('小说名：')
    soup=BeautifulSoup(urllib.urlopen('http://so.23wx.com/cse/search?q=%s&click=1&s=15772447660171623812&nsid='%name).read())
    N=soup.find('a', {'class': 'result-game-item-title-link'})
    print N['title'],N['href']
    return N

def getChapter(url):
    b=urllib.urlopen(url).read()
    a=re.compile(r'<a href="(.*?)">(.*?)</a>')
    aa=a.findall(b)
    for i in aa:
            if re.compile('^[0-9]*\.html').match(i[0]):
                yield url+i[0],i[1]
N=search()
num=0
for url in getChapter(N['href']):
    num+=1
    try:
        download(url[0],N['title'])
        t='-'*(50-len(url[1]))
        print '%s%s已下载'%(url[1],t)
    except:
        print 'error'

    

