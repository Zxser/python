# -*- coding: UTF-8 -*-
from urllib import unquote


class HtmlOutput(object):
    def __init__(self):
        self.datas = []
# 创建一个空的列表作为数据库来存放数据

    def append_data(self,data):
        if data is None:
            return
        self.datas.append(data)
# 将数据添加到数据库中


    def output_html(self):
        open('output1.html', 'w').write("<html>")
        open('output1.html', 'w').write("<body>")
        open('output1.html', 'w').write("<table>")

        for data in self.datas:
            open('output1.html', 'w').write("<tr>")
            open('output1.html', 'w').write("<td style=\"width:20%%;border:1px solid\">%s</td>" % unquote(data['url'].encode('utf-8')))
            open('output1.html', 'w').write("<td style=\"width:20%%;border:1px solid\">%s</td>" % data['title'].encode('utf-8'))
            open('output1.html', 'w').write("<td style=\"width:60%%;border:1px solid\">%s</td>" % data['summary'].encode('utf-8'))
            open('output1.html', 'w').write("</tr>")

        open('output1.html', 'w').write("</table>")
        open('output1.html', 'w').write("</body>")
        open('output1.html', 'w').write("</html>")
        open('output1.html', 'w').close()
# 将爬到的结果 循环输出 生成一个网页
