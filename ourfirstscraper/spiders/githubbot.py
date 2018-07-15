# -*- coding: utf-8 -*-
import scrapy


class GithubbotSpider(scrapy.Spider):
    name = 'githubbot'

    start_urls = ['https://github.com/0xProject/0x-monorepo']
    global domain
    domain = start_urls[0]

    global Name
    global Watchs
    global Stars
    global Forks
    global Issues
    global Contributors
    global Opens
    global Closes

    def parse(self, response):
        global domain
        global Name
        global Watchs
        global Stars
        global Forks
        global Issues
        global Contributors
        Name = response.css('span.col-11.text-gray-dark.mr-2::text').extract()

        # Watch / Star / Fork
        items = response.css('a.social-count::text').extract()
        Watchs = items[0]
        Stars = items[1]
        Forks = items[2]

        # issue / pull request / project
        counts = response.css('span.Counter::text').extract()
        Issues = counts[0]

        # commit / branch / release / contributor
        nums = response.css('span.num.text-emphasized::text').extract()
        Contributors = nums[3]

        issue_page = domain + "/issues"
        yield scrapy.Request(url=issue_page, callback=self.parse_issues)

    def parse_issues(self, response):
        global Opens
        global Closes
        global domain

        # Open / Close
        items = response.css('a.btn-link::text').extract()
        Opens = items[1]
        Closes = items[3]

        issue_page = domain + "/pulse/monthly"
        yield scrapy.Request(url=issue_page, callback=self.parse_insight)

    def parse_insight(self, response):
        global Name
        global Watchs
        global Stars
        global Forks
        global Issues
        global Contributors
        global Opens
        global Closes

        adds = response.css('strong.insertions::text').extract()
        dels = response.css('strong.deletions::text').extract()

        # create a dictionary to store the scraped info
        scraped_info = {
            'Name': Name,
            'Watchs': Watchs,
            'Stars': Stars,
            'Forks': Forks,
            'Issues': Issues,
            'Contributors': Contributors,
            'Opens': Opens,
            'Adds': adds,
            'Dels': dels,

        }

        yield scraped_info
