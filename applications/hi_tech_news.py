from applications.work_with_bd import create_table, check_news, insert_news
from bs4 import BeautifulSoup
import requests
import time
import random


def get_news_and_save_bd():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

    url = 'https://hi-tech.news/'
    domen = 'https://hi-tech.news'

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    # block with news
    news = soup.find_all('a', class_='post-title-a')

    link_news = []

    for new in news[:5]:
        try:
            link = new.get('href')

        except Exception as ex:
            print(ex)
            link = 'not found'

        link_news.append(link)

    # we take the news content
    create_table()
    fresh_news = []
    count = 1

    for link in link_news:
        r = requests.get(url=link, headers=headers, timeout=5)
        soup = BeautifulSoup(r.content, 'html.parser')

        # we are looking for the title of the article, the text of the article, the date of publication
        title = soup.h1.get_text(strip=True)
        content = soup.find('div', class_='the-excerpt').get_text(strip=True)
        publish_date = soup.find(
            'div', class_='tile-views').get_text(strip=True)
        count += 1

        # inserting an entry into the database
        try:
            if check_news(title) == 0:
                insert_news(link, title, content, publish_date)
                fresh_news.append({
                    "title": title,
                    "content": content,
                    "link": link,
                    "publish_date": publish_date
                })
                print('[INFO] News added to the database')

        except Exception as ex:
            print('[X] Error inserting data into the database: ', ex)
            continue

        time.sleep(random.randrange(1, 3))

    return fresh_news
