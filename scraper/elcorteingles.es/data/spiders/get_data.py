# -*- coding: utf-8 -*-
import scrapy
from data.items import DataItem
from data.spreadsheet import save

class GetDataSpider(scrapy.Spider):
    name = 'get_data'
    allowed_domains = ['elcorteingles.es']
    start_urls = ['https://www.elcorteingles.es/club-del-gourmet/vinos/espana/']

    def parse(self, response):
        items = DataItem()
        items['title'] = response.xpath('//h3[@class="info-name"]/a[1]/@title').extract()
        items['precio'] = response.xpath('//div[@class="product-price "]/span[1]/text()').extract()
        save(items)

        yield items        
