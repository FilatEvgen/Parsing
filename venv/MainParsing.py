import sqlalchemy as db
from sqlalchemy import Integer,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy.orm import sessionmaker
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from app.local.models import data_model
from app.local.repository import main_repository
from sqlalchemy.ext.declarative import declarative_base

# Здесь определяем функцию для сбора ссылок с веб-страницы!
def collect_links(base_url, page_url):
    # Загрузить веб-страницу
    response = requests.get(page_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        # Здесь определяем логику для сбора ссылок с веб-страницы
        # Например, найдите все теги <a> и извлеките атрибут href

        for a_tag in soup.find_all('a'):
            link = a_tag.get('href')
            if link:
                full_link = urljoin(base_url, link)  # Преобразовать относительный URL в абсолютный
                links.append(full_link)

        return links
    else:
        print(f"Ошибка при загрузке страницы {page_url}")
        return []

# Пример использования функции
base_url = "https://gdz.ru"
page_url = "https://gdz.ru/"
links = collect_links(base_url, page_url)

