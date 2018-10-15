# -*- coding: utf-8 -*-
# coding=utf-8
import scrapy
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class MytokenBaseInfoSpider(scrapy.Spider):
    name = 'MytokenBaseInfoSpider'

    start_urls = ['https://www.mytoken.io/currency/1400541#info']
    global domain
    domain = start_urls[0]

    def parse(self, response):
        Name = ""
        ICOTIME = ""
        RATE = ""
        ACCEPT = ""
        DISTRIBUTION = ""
        TOTALCAPITAL = ""

        Name = response.css('h2.name::text').extract()

        Type = response.css('div.tag::text')[0].extract()

        Desc = response.css('div.desc').css('p::text').extract()
        print Desc

        response.css('div.base-container').css('div.value::text')

        items = response.css('td.item')
        labels = response.css('td.item div.label::text')
        values = response.css('td.item div.value')

        print labels[0]
        for index, label in enumerate(labels):
            labelStr = label.extract()
            valueStr = values[index].css('::text').extract()[0]
            print labelStr + "------" + valueStr
            if labelStr == "时间":
                print "match 时间"
                ICOTIME = valueStr

            if labelStr == "兑换比例":
                print "match 兑换比例"
                RATE = valueStr

            if labelStr == "接受币种":
                print "match 接受币种"
                ACCEPT = valueStr

            if labelStr == "代币分配":
                print "match 代币分配"
                DISTRIBUTION = valueStr

            if labelStr == "筹集资金量":
                print "match 筹集资金量"
                TOTALCAPITAL = valueStr

        scraped_info = {
            'Name': Name,
            'ICOTIME': ICOTIME,
            'RATE': RATE,
            'ACCEPT': ACCEPT,
            'DISTRIBUTION': DISTRIBUTION,
            'TOTALCAPITAL': TOTALCAPITAL,

        }

        yield scraped_info
