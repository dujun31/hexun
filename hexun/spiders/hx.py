# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from hexun.items import HexunItem
import re,requests

class HxSpider(CrawlSpider):
    name = 'hx'
    allowed_domains = ['hexun.com']
    start_urls = ['http://blog.hexun.com/']

    rules = (
        Rule(LinkExtractor(allow=('http://.*?.blog.hexun.com/.*?_d.html'), allow_domains=('hexun.com')),callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=('http://.*?.blog.hexun.com/.*?_d.html'), allow_domains=('hexun.com')),
        #      callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = HexunItem()
        item['title'] = response.xpath("//span[@class='ArticleTitleText']/a/text()").extract()[0]
        item['link'] = response.url
        item['blog_id'] = response.xpath("//script").re('ARecommend.aspx\?blogid=(.*?)&',re.S)[0]
        item['article_id'] = response.xpath("//span[@class='ArticleTitleText']/a/@href").re('blog.hexun.com/(.*?)_d.html')[0]

        cc_url = "http://click.tool.hexun.com/click.aspx?articleid=%s&blogid=%s" %(item['article_id'],item['blog_id'])
        print('url', cc_url)
        headers = {
            'Referer': response.url,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        res = requests.get(cc_url, headers=headers)
        data=res.text
        print(data)
        item['comment']=re.compile('articleCommentCount.*?= (.*?);', re.S).findall(data)[0]
        item['click'] = re.compile('articleClickCount.*?= (.*?);', re.S).findall(data)[0]
        return item
