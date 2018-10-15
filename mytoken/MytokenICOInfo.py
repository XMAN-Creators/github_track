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

    global AAA

    def parse(self, response):
        global AAA
        Name = ""
        ICOTIME = ""
        RATE = ""
        ACCEPT = ""
        DISTRIBUTION = ""
        TOTALCAPITAL = ""

        Name = response.css('h2.name::text').extract()

        Type = response.css('div.tag::text')[0].extract()

        Desc = response.css('div.desc').css('p::text').extract()

        labels = response.css('div.label::text')
        values = response.css('div.value::text')

        # print "------------------------------------------------------------------你好，世界" + labels.extract()
        # Desc = labels[0].extract()
        for index, label in enumerate(labels):
            labelStr = label.extract()
            valueStr = values.extract()[index]
            print labelStr + "------" + valueStr
            if labelStr == "时间":
                ICOTIME = valueStr

            if labelStr == "兑换比例":
                RATE = valueStr

            if labelStr == "接受币种":
                ACCEPT = valueStr

            if labelStr == "代币分配":
                DISTRIBUTION = valueStr

            if labelStr == "筹集资金量":
                TOTALCAPITAL = valueStr

        AAA = values.extract()

        scraped_info = {
            'Name': Name,
            'ICOTIME': AAA,
            'RATE': RATE,
            'ACCEPT': ACCEPT,
            'DISTRIBUTION': DISTRIBUTION,
            'TOTALCAPITAL': TOTALCAPITAL,

        }

        yield scraped_info

    # def parse_issues(self, response):
    #     global Opens
    #     global Closes
    #     global domain
    #
    #     # Open / Close
    #     items = response.css('a.btn-link::text').extract()
    #     Opens = items[1]
    #     Closes = items[3]
    #
    #     issue_page = domain + "/pulse/monthly"
    #     yield scrapy.Request(url=issue_page, callback=self.parse_insight)
    #
    # def parse_insight(self, response):
    #     global Name
    #     global Watchs
    #     global Stars
    #     global Forks
    #     global Issues
    #     global Contributors
    #     global Opens
    #     global Closes
    #
    #     adds = response.css('strong.insertions::text').extract()
    #     dels = response.css('strong.deletions::text').extract()
    #
    #     # create a dictionary to store the scraped info
    #     scraped_info = {
    #         'Name': Name,
    #         'Watchs': Watchs,
    #         'Stars': Stars,
    #         'Forks': Forks,
    #         'Issues': Issues,
    #         'Contributors': Contributors,
    #         'Opens': Opens,
    #         'Adds': adds,
    #         'Dels': dels,
    #
    #     }
    #
    #     yield scraped_info
