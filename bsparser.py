import requests
from configs import *
import json

class BaseParser:
    def __init__(self):
        self.URL = URL
        self.HOST = HOST

# Научим - Делать запрос
# Научим - Сохранять JSON данные

    def get_html(self, url):
        """Получение страницы сайта"""
        response = requests.get(url)
        return response.text

    @staticmethod
    def save_data_to_json(file_name, data):
        with open(f'{file_name}.json', mode='w', encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)