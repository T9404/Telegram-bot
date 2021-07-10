import requests
from bs4 import BeautifulSoup
import time

import random

from applications.work_with_bd import create_table, check_news, insert_news


def get_news_and_save_bd():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

    url = 'https://hi-tech.news/'
    domen = 'https://hi-tech.news'


    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')


    #  блок с новостями
    news = soup.find_all('a', class_='post-title-a')

    # создаем список ссылок на новости
    link_news = []
    for new in news[:5]:
        try:
            link = new.get('href')
        except Exception as ex:
            print(ex)
            link = 'не найдена'
        link_news.append(link)
        #print(link)
    print(f'Найдено {len(link_news)} новостей 🤖')

    # создаем бд
    create_table()

    # забераем контент новостей переберая ссылки
    fresh_news = []
    count = 1
    for link in link_news:
        r = requests.get(url=link, headers=headers, timeout=5)
        soup = BeautifulSoup(r.content, 'html.parser')
        # ищем название статьи, текст статьи, дату публикации
        title = soup.h1.get_text(strip=True)
        content = soup.find('div', class_='the-excerpt').get_text(strip=True)
        publish_date = soup.find('div', class_='tile-views').get_text(strip=True)

        print(f'Парсим страницу с новостью:\nЗаголовок: "{title[:30]}..." ({count} из {len(link_news)})')
        count += 1

        # вставляем запись в бд
        try:
            if check_news(title) == 0:
                insert_news(link, title, content, publish_date)
                fresh_news.append({
                    "title": title,
                    "content": content,
                    "link": link,
                    "publish_date": publish_date
                })
                print('[INFO] Новость добавлена в БД')
        except Exception as ex:
            print('[X] Ошибка вставки данных в бд: ', ex)
            continue
        time.sleep(random.randrange(1, 3))
    return fresh_news
#print(get_news_and_save_bd())

# # вывод данных с бд
# data_set = bd.get_data_from_db()
# print(pandas.DataFrame(data_set))


