# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # user_intro = scrapy.Field()
    establish_collection = scrapy.Field()
    admin_collection = scrapy.Field()
    user_subscriptions = scrapy.Field()