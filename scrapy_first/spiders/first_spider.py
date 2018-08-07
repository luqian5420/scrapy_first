import scrapy
class scrapy_first(scrapy.Spider):  #继承scrapy.Spider类
    name = 'scrapy_first_spider'  #定义蜘蛛名，启动程序用到的名字

    def start_requests(self):     #由此方法爬取目标URL

        #定义爬取的URL
        urls = [
            'http://lab.scrapyd.cn/page/1',
            'http://lab.scrapyd.cn/page/2',
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)#爬取到的页面如何处理？提交给parse方法处理

    def parse(self,response):
        page = response.url.split('/')[-2]   #根据上面的链接提取分页,如：/page/1/，提取到的就是：1

        filename = 'first_spider-%s.html' % page   #拼接文件名，如果是第一页，最终文件名便是：first_spider-1.html

        with open(filename,'wb')as f:
            f.write(response.body)      #保存刚刚下载的页面
            self.log('保存文件:%s'%filename)  #记录日志



