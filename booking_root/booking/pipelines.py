# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import requests
import logging
import json
import time
import re


class ObjectStoragePipeline:
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def __init__(self, settings):
        self.settings = settings

    def process_item(self, item, spider):
        ts = int(time.time())
        file_name = re.sub("[^\w ]", "", item["hotel_name"].lower()).replace(" ", "-")
        file_name += ".json"  # + str(ts) '-' +
        url = self.settings.get("OBJECT_STORAGE_BUCKET")
        r = requests.put(url + file_name, data=json.dumps(dict(item)))
        if r.status_code == 200:
            logging.info(f"Successfully stored {file_name}")
        else:
            logging.error(f"Error to store {file_name}")
