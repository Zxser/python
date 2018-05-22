# -*- coding: UTF-8 -*-

class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
# set()的好处在于 不会储存相同的的URl 所以不重复爬取同一个URL

    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
# 如果没有抓取到URl 直接退出
# 如果URL 不存在于新的URL池或旧的URL池中 将把该URL添加到新的URL池中

    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
# 与上相同 但是是批量的添加URL

    def has_new_url(self):
        return len(self.new_urls)!=0
# 当有新的URL时返回一个非零的值 即 返回一个真的值 使调度器中的while循环持续进行

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
# 将一个URl从new_urls 的池中取出（.pop方法） 返回出url的值 然后将该url存入 old_urls 的池中