# -*- coding: utf-8 -*-
import scrapy


class MytokenBaseInfoSpider(scrapy.Spider):
    name = 'MytokenBaseInfoSpider'

    start_urls = ['https://www.mytoken.io/currency/55523#info']
    global domain
    domain = start_urls[0]

    global Name
    global Type
    global Desc
    global Base
    global Issues
    global Contributors
    global Opens
    global Closes

    def parse(self, response):
        global domain
        global Name
        global Type
        global Desc
        global Base
        global Issues
        global Contributors
        Name = response.css('h2.name::text').extract()

        Type = response.css('div.tag::text')[0].extract()

        Desc = response.css('div.desc').css('p::text').extract()

        labels = response.css('div.label::text')
        values = response.css('div.value::text')

        Desc = labels[0].extract()
        for index, label in enumerate(labels):
            if cmp(label.extract(), "\u57fa\u7840\u94fe'"):
                Type = values[index].extract()

        scraped_info = {
            'Name': Name,
            'Type': Type,
            'Desc': Desc,
            'BaseOn': Type,

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
