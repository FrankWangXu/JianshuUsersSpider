# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# class UserItem(scrapy.Item):
#     user_intro = scrapy.Field()
#     establish_collection = scrapy.Field()
#     admin_collection = scrapy.Field()
#     user_collection = scrapy.Field()

class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author_name = scrapy.Field()
    author_image = scrapy.Field()
    article_release_time = scrapy.Field()
    article_title = scrapy.Field()
    article_desc = scrapy.Field()
    article_link = scrapy.Field()
    read_count = scrapy.Field()
    reply_count = scrapy.Field()
    # likeit_count = scrapy.Field()
    # payit_count = scrapy.Field()