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
        Type = ""
        Desc = ""
        DependOn = ""
        OnboardTime = ""
        consesus = ""

        Name = response.css('h2.name::text').extract()

        Type = response.css('div.tag::text')[0].extract()

        Desc = response.css('div.desc').css('p::text').extract()

        labels = response.css('div.label::text')
        values = response.css('div.value::text')

        print "------------------------------------------------------------------你好，世界" + values[0].extract()
        # Desc = labels[0].extract()
        for index, label in enumerate(labels):
            labelStr = label.extract()
            valueStr = values[index].extract()
            print labelStr + "------" + valueStr
            if labelStr == "基础链":
                DependOn = valueStr

            if labelStr == "共识机制":
                consesus = valueStr

            if labelStr == "项目启动日期":
                OnboardTime = valueStr

        scraped_info = {
            'Name': Name,
            'Type': Type,
            'Desc': Desc,
            'BaseOn': DependOn,
            'Consesus': consesus,
            'OnboardTime': OnboardTime,

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
