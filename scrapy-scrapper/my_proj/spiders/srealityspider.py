import scrapy
from scrapy_playwright.page import PageMethod
import logging
from time import sleep
#from items import RealityItem

class SrealityspiderSpider(scrapy.Spider):
    name: str = "srealityspider"
    base_url: str = "https://www.sreality.cz/hledani/prodej/byty"
    current_page = 1
    item_counter: int = 0
    max_items_amount = 500

    # div.dir-property-list

    def start_requests(self):
        yield scrapy.Request(
            url=self.base_url,
            meta = {
                'playwright': True,
                'playwright_include_page': True,
                'playwright_page_methods': [
                    # PageMethod(
                    #     'wait_for_selector',
                    #     'div.dir-property-list'
                    # ),
                    PageMethod(
                        'wait_for_selector',
                        'a.btn-paging-pn.icof.icon-arr-right.paging-next'
                    )
                ]
            }
        )

    def parse(self, response):
        for item in response.css('div.property.ng-scope'):
            if self.item_counter >= self.max_items_amount:
                break
            
            self.item_counter += 1
            # item = RealityItem()
            # item['title'] = item.css("span.name.ng-binding::text").get()
            # item['img_url'] = item.css('img::attr(src)').get()

            # yield item

            yield {
                'id': self.item_counter,
                'title': item.css("span.name.ng-binding::text").get(),
                'img_url': item.css('img::attr(src)').get()
            }
        
        if self.item_counter < self.max_items_amount:
            self.current_page += 1
            next_page_url = f'{self.base_url}?strana={self.current_page}'
            yield scrapy.Request(next_page_url, callback=self.parse,
                                 meta = {
                                    'playwright': True,
                                    'playwright_include_page': True,
                                    'playwright_page_methods': [
                                        # PageMethod(
                                        #     'wait_for_selector',
                                        #     'div.dir-property-list'
                                        # ),
                                        PageMethod(
                                            'wait_for_selector',
                                            'a.btn-paging-pn.icof.icon-arr-right.paging-next'
                                        )
                                    ]
                                }
                                )

            ## Doesn't find element even after waiting for page to load...
            # a.btn-paging-pn.icof.icon-arr-right.paging-next
            # next_page = response.css("a.btn-paging-pn.icof.icon-arr-right.paging-next::attr(href)").get()
            # yield {
            #     'next_page': next_page
            # }
            # if next_page is not None:
            #     next_page = response.urljoin(next_page)
            #     yield response.follow(next_page, callback=self.parse)
                #yield scrapy.Request(next_page, callback=self.parse)

