from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import  get_project_settings
import csv

from presentsparser.spiders.wb import WbSpider
if __name__ == '__main__':
    configure_logging()
    install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
    process = CrawlerProcess(get_project_settings())
    process.crawl(WbSpider)
    process.start()

"""
    def save_to_csv(data, filename):
        # Записываем данные в CSV-файл
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'link']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for item in data:
                writer.writerow(item)


    if __name__ == "__main__":
        # Получаем данные
        news_data = name_parse()

        if news_data:
            # Сохраняем данные в CSV-файл
            save_to_csv(news_data, 'news_data.csv')
            print("Данные успешно сохранены в файл 'news_data.csv'")
        else:
            print("Не удалось получить данные.")

"""