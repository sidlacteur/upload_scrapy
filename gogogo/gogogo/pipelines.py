# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log
import pymongo

class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Question added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item

class GoImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        if request.meta['source']=='decitre':
            image=request.meta['url_image_full'].split('/')[-1].replace('.html','').replace('gif','jpg').replace('FS','')
            return 'full/%s' % (image)
        elif request.meta['source']=='nwf':
            return 'thumb/%s' % (request.meta['url_image_thumb'].split('/')[-1].replace('.html','').replace('gif','jpg').replace('FS',''))

    def get_media_requests(self, item, info):
        if item['source']=='decitre' :
            yield scrapy.Request(item['url_image_full'].replace('200x303','475x500'),meta=item)
        elif item['source']=='nwf':
            yield scrapy.Request(item['url_image_thumb'],meta=item)




class GogogoPipeline(object):
    def process_item(self, item, spider):
        return item
