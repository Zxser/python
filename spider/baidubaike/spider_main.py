# -*- coding: UTF-8 -*-

import html_downloader
import html_output
import html_parser
import url_manager
# 导入各个模板


class SpiderMain(object):
    def __init__(self):
        self.url = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.outputer = html_output.HtmlOutput()
        self.parser = html_parser.HtmlParser()
# 设置各个属性

    def craw(self,rootUrl):
# 获取各一个最开始的URL
        count = 1
# 为了防止死循环 设置一个数值 与 后面if语句进行配合 限定爬取循环次数
        self.url.add_new_url(rootUrl)
        while self.url.has_new_url():
# 当新URl存在时 进行循环
            try:
                new_url = self.url.get_new_url()
                html_cont = self.downloader.download(new_url)
                print 'craw %d:%s' %(count,new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.url.add_new_urls(new_urls)
                self.outputer.append_data(new_data)
            except:
                print "craw failed!"

            if count == 2:
                break
            count += 1
        self.outputer.output_html()

if __name__ == "__main__":
    rootUrl = "https://baike.baidu.com/item/Python"
    SpiderMain().craw(rootUrl)




