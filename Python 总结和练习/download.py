# -*- coding: gbk -*-
from bs4 import BeautifulSoup
import urllib
import codecs
import re
def download(url,name):
    '''
        根据查找到的章节url下载章节页面的内容。name为获取到的小说的名称
    '''
    soup=BeautifulSoup(urllib.urlopen(url).read())#解析章节的页面
    cont=soup.find(id="contents").text#获取id为contents标签里的内容
    title=soup.title.text#解析出章节名也就是页面的title
    f=codecs.open('%s.txt'%name,'a','utf-8')#以小说名称命名文件名称，并以追加的方式打开
    f.write('\r\n'+title+'\r\n')#先写入章节名称
    f.write(cont)#再写入章节内容
    f.close()#关闭文件，其实打开文件用with更好~
def search():
    name=raw_input('小说名：')#获取输入
    soup=BeautifulSoup(urllib.urlopen('http://so.23wx.com/cse/search?q=%s&click=1&s=15772447660171623812&nsid='%name).read())
    #根据输入的内容，合成搜索url，并获取搜索内容，以beautifulsoup解析heml
    N=soup.find('a', {'class': 'result-game-item-title-link'})#根据特定标记找到小说的链接
    print N['title'],N['href']
    return N

def getChapter(url):
    '''
        根据小说链接获取所有章节，因为章节可能达到几千~所以此处用到生成器
    '''
    b=urllib.urlopen(url).read()#获取页面的内容
    a=re.compile(r'<a href="(.*?)">(.*?)</a>')#html解析的工具好像对于很多的标签，解析不了，所以不得不自己写正则来获取每个章节的url
    aa=a.findall(b)#从页面内容里找到所有章节的链接，因为链接是相对路径，所以要自己合成绝对路径。
    for i in aa:
            if re.compile('^[0-9]*\.html').match(i[0]):
                yield url+i[0],i[1]#每次循环得到一个章节名称，此处用到生成器。
N=search()
num=0
for url in getChapter(N['href']):
    num+=1
    try:                            #通过异常来跳过各种出问题的情况~
        download(url[0],N['title'])
        t='-'*(50-len(url[1]))
        print '%s%s已下载'%(url[1],t)
    except:
        print 'error'
'''
   此代码是在我很早期写出来的，现在看来实在丑陋不堪~注释尽量清晰，不明白的地方@我就行，不懂的名词或者模块就自己学习哈~
'''
    

