# -*- coding: utf-8 -*-
import json
import scrapy
from jianshu.items import  ArticleItem

class JsmemberspiderSpider(scrapy.Spider):
    name = "jsMemberSpider"
    # allowed_domains = ["jianshu"]
    jianshu = 'http://www.jianshu.com'
    start_urls = ['http://www.jianshu.com/users/54b5900965ea/collections_and_notebooks.json?slug=54b5900965ea', ]
    # subscriptions_all = []
    # start_url = 'http://www.jianshu.com/users/54b5900965ea/subscriptions?page={}'
    # start_page = 1
    # userID = '54b5900965ea'
    # pageNumber = 1
    # stop_url = 'http://www.jianshu.com/users/54b5900965ea/collections_and_notebooks.json?slug={USERID}'.format(USERID = userID)

    def parse(self, response):
        collections = []
        admin_collections = []
        user_subscription = []
        jsonresponse = json.loads(response.body_as_unicode())
        item = ArticleItem()
        own_collections = jsonresponse["own_collections"]
        for collection in own_collections:
            collections.append(collection["title"])
        item["establish_collection"] = collections
        admin_collection = jsonresponse["manageable_collections"]
        for collection in admin_collection:
            admin_collections.append(collection["title"])
        item["admin_collection"] = admin_collections
        user_subscriptions = jsonresponse["notebooks"]
        for collection in user_subscriptions:
            user_subscription.append(collection["name"])
        item["user_subscriptions"] = user_subscription
        return item