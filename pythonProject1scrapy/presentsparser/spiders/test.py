import scrapy
from scrapy.http import HtmlResponse
import json


class WbSpider(scrapy.Spider):
    name = "wb"
    allowed_domains = ["chepetsk.ru"]
    start_urls = ["https://chepetsk.ru/do/real_estate/kvartiry/"]
    custom_settings = {'FEED_URI': "flats_%(time)s.json",
                       'FEED_FORMAT': 'json'}

    def parse(self, response: HtmlResponse):
        links = response.xpath('//div[@class="title"]/a/attribute::href').getall()
        for link in links:
            yield response.follow(link, callback=self.name_parse)

    def name_parse(self, response: HtmlResponse):
        response.xpath('//div[@class="title"]').getall()
        print()

        row_data = zip(links, )

        # извлечение данных строки
        for item in row_data:
            # создать словарь для хранения извлеченной информации
            scraped_info = {
                'page': response.url,
                'product_name': item[0],
                # item[0] означает продукт в списке и т. д., индекс указывает, какое значение назначить
                'price_range': item[1],
                'orders': item[2],
                'company_name': item[3],
            }

            # генерируем очищенную информацию для скрапа
            yield scraped_info


