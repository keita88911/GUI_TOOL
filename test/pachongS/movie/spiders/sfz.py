# -*- coding: utf-8 -*-

import scrapy
import re
from .. import  items

class SfzSpider(scrapy.Spider):
    name = 'sfz'
    allowed_domains = ['sfz.ckd.cc']
    start_urls = ['http://sfz.ckd.cc/']

    def parse(self, response):
        movies = response.xpath('//div[@class="result"]')
        ab=movies.extract()[0]
        # print(movies.extract())
        # print(len(movies.extract()))
        # print(type(movies.extract()))
        for each_movie in movies:
            print(len(movies))
            item = items.MovieItem()
            for i in range(1,20):
                item['name'] = each_movie.xpath('./table/tr/td[1]').extract()[i]
                # print(type(item['name']))
                item['name']=item['name'].replace("<td>","")
                item['name'] = item['name'].replace("</td>", "")
                print(item['name'])
                # pattern = re.compile(r'<td>(.*?)</td>')
                # item['name']=re.findall(pattern,item['name'])
                # item['name']=re.match(pattern,item['name']).group()
                # print(type(item['name']))
                # print( item['name'])
                yield item