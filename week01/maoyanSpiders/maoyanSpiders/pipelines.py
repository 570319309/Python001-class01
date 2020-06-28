# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class MaoyanspidersPipeline:
    # def process_item(self, item, spider):
    #     return item
    # 每一个item管道组件都会调用该方法，并且返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        name = item['name']
        mytype = item['mytype']
        date = item['date']
        mylist = [name, mytype, date]
        mydata = pd.DataFrame(mylist)
        mydata.to_csv("./maoyanScrapy.csv", encoding="utf_8_sig", mode='a')
        return item  # 默认写法，不能删 uyZ m
