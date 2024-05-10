import scrapy
from scrapy.http import HtmlResponse
import json

class WbSpider(scrapy.Spider):
    name = "wb"
    allowed_domains = ["chepetsk.ru"]
    start_urls = ["https://chepetsk.ru/do/real_estate/kvartiry/"]
    custom_settings = {'FEED_URI': "flats_%(time)s.json",
                       'FEED_FORMAT': 'json'}

    def parse(self, response:HtmlResponse):
        links = response.xpath('//div[@class="title"]/a/attribute::href').getall()
        titles = response.xpath('//div[@class="title"]').getall()
        row_data = zip(links, titles)


        # извлечение данных строки
        for item in row_data:
            # создать словарь для хранения извлеченной информации
            scraped_info = {
                'links': item[0],  # item[0] означает продукт в списке и т. д., индекс указывает, какое значение назначить
                'titles': item[1]
            }

            # генерируем очищенную информацию для скрапа
            yield scraped_info


