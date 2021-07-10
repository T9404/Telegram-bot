import requests
from bs4 import BeautifulSoup


def get_html(url):
    """ получаем html страницу с ссылки"""
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    html = response.text
    return html


def get_weather(message):
    url = f'https://sinoptik.com.ru/погода-{message.text.lower()}'
    soup = BeautifulSoup(get_html(url), 'html.parser')
    try:
        temp = soup.find('div', class_='weather__article_main_temp').get_text(strip=True)
        description = soup.find('div', class_='weather__article_description-text').get_text(strip=True)
        result = f'Температура воздуха сейчас {temp}\n{description}'
    except:
        result = f'Город "{message.text}" не найден. Скорее всего вы сделали опечатку ❎'
    return result


def get_weather_week(message):
    url = f'https://sinoptik.com.ru/погода-{message.text.lower()}'
    soup = BeautifulSoup(get_html(url), 'html.parser')
    try:
        temps = soup.find('div', class_='weather__content_tabs clearfix').find_all('div', class_='weather__content_tab')
        days = []
        for temp in temps:
            try:
                day_week = temp.find('p', class_='weather__content_tab-day').get_text(strip=True)
                day_month = temp.find('p', class_='weather__content_tab-month').get_text(strip=True)
                date = temp.find('p', class_='weather__content_tab-date day_red').get_text(strip=True)
                t_min = temp.find('div', class_='min').get_text(strip=True)
                t_max = temp.find('div', class_='max').get_text(strip=True)
                result = f'{day_week} {date} {day_month}. {t_min}, {t_max}'
                days.append(result)
            except:
                pass
        return days
    except:
        result = ["Не удалось получить данные по запросу ❎:", f'"{message.text}"']
        return result