# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FirstPipeline:
    def __init__(self):
        self.file = open("itcast.json",'w')
    def process_item(self, item, spider):
        json_data = json.dumps(item,ensure_ascii=False) + ",\n"
        self.file.write(json_data)
    def __del__(self):
        self.file.close()
