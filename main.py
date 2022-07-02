import requests
from bs4 import BeautifulSoup

from bsparser import BaseParser
from configs import *

import time


class SalesProducts(BaseParser):
    def __init__(self):
        super(SalesProducts, self).__init__() # Второй вариант запуска конструктора от наследования
        self.data = []

    def get_data(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        block = soup.find('div', class_='product-list')
        products = block.find_all('div', class_='product-list__item')
        for product in products:
            title = product.find('a', class_='product-name').get_text(strip=True)
            print(title)
            price = product.find('div', class_='product-price')
            old_price = int(price.find_all('div')[0].get_text(strip=True).replace(' cум', '').replace(' ', ''))
            print(old_price)
            new_price = int(price.find_all('div')[1].get_text(strip=True).replace(' cум', '').replace(' ', ''))
            print(new_price)
            percent = round((100 - new_price * 100 / old_price), 2)
            print(percent)
            self.data.append({
                'Товар': title,
                'Обычная цена':old_price,
                'Цена со скидкой':new_price,
                'Процент скидки':f'{percent} %'
            })


def start_parsing():
    parser = SalesProducts()
    print('Парсер начал работу')
    start = time.time()
    html = parser.get_html('https://texnomart.uz/ru/katalog/tovary-so-skidkoi')
    parser.get_data(html)

    BaseParser.save_data_to_json('sales', parser.data)
    end = time.time()
    print(f'Парсер отработал за {end - start} секунд')

start_parsing()

