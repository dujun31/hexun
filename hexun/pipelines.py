# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HexunPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123", db="hexun")

    def process_item(self, item, spider):
        title = item["title"]
        link = item["link"]
        click = item["click"]
        comment = item["comment"]
        article_id = item["article_id"]
        blog_id = item["blog_id"]
        sql = "insert into hexun(title,link,click,comment,article_id,blog_id) values('" + str(title) + "','" + str(link) + "','" + str(click) + "','" + str(comment) + "','" + str(article_id) + "','" + str(blog_id) + "')"
        self.conn.query(sql)
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()
