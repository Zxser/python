import urllib2


class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return
        else:
         urllib2.urlopen(url)
        if urllib2.urlopen(url).getcode()!=200:
            return None
        else:
            return urllib2.urlopen(url).read()


