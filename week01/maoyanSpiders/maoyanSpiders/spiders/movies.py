import scrapy
from maoyanSpiders.items import MaoyanspidersItem
from scrapy.selector import Selector  # 自带的选择器

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass
    # 解析函数
    def parse(self, response):

        selector=Selector(response)
        name = selector.xpath("//div[@class='movie-hover-info']/div/span[@class='name ']/text()").extract()
        mytype = selector.xpath("//div[@class='movie-hover-info']/div[2]/text()").extract()
        date = selector.xpath("//div[@class='movie-hover-info']/div[4]/text()").extract()

        print(name, mytype, date)
        item = MaoyanspidersItem()
        item['name']=name
        item['mytype']=mytype
        item['date']=date
        yield item
