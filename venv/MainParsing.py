import sqlalchemy as db
from sqlalchemy import Integer,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from app.local.models import data_model
from app.local.repository import main_repository
from sqlalchemy.ext.declarative import declarative_base
# Здесь определяем функцию для сбора ссылок с веб-страницы
# Здесь определяем функцию для сбора заголовка и ключевых слов с веб-страницы
def collect_title(base_url, page_url):
    # Загрузить веб-страницу
    response = requests.get(page_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Найдите и разберите тег <title>
        title_tag = soup.find('title')
        title = title_tag.text.strip() if title_tag else ""

        # Найдите и разберите тег <meta> с ключевыми словами
        keywords = ""
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
        if meta_keywords:
            keywords = meta_keywords.get('content', '')

        return title, keywords
    else:
        print(f"Ошибка при загрузке страницы {page_url}")
        return "", ""

# Пример использования функции
base_url = "https://gdz.ru"
page_url = "https://gdz.ru/"
title, keywords = collect_title(base_url, page_url)
print("Title:", title)
print("Keywords:", keywords)
# Здесь определяем функцию для сбора ссылок с веб-страницы
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
title, keywords = collect_title(base_url, page_url)
print("Title:", title)
print("Keywords:", keywords)

links = collect_links(base_url, page_url)
for link in links:
    main_repository.create_new_link(base_url, link, title, keywords)


# main_repository.create_new_link(base_url,links)

