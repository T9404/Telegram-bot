import requests
from bs4 import BeautifulSoup


def get_html(url):  # получаем html разметку
    """ получаем html страницу с ссылки"""
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    html = response.text
    return html



def get_discussions(user_input): # сообщение и количество постов, если не хватает постов на странице, то
    user_object, amount = user_input.split('-')
    amount = int(amount)

    url = f'https://www.reddit.com/search/?q={user_object}' #message.text.lower()
    soup = BeautifulSoup(get_html(url), 'html.parser')
    mem_need = soup.findAll('div', class_='_2XDITKxlj4y3M99thqyCsO')
    #print(mem_need)
    result = []
    for mem in mem_need:
        try: description = mem.find('a', class_='SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE').get_text(strip=True)
        except: description = 'Описание не найдено'
        try: image = mem.find('img', class_='_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax').get('src')
        except: image = 'Картинка не найдена'
        try: link = 'https://www.reddit.com'+ mem.find('a', class_='SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE').get('href')  # .find('a')
        except: link = 'Ссылка не найдена'
        result.append({
            'description':description,
            'image': image,
            'link': link
        })
    return result[:amount]
#print(get_discussions('russia', 2))





def get_memes_reddit_old(amount):
    url = 'https://www.reddit.com/r/memes/'
    soup = BeautifulSoup(get_html(url), 'html.parser')
    mem_need = soup.findAll('div', class_='_1poyrkZ7g36PawDueRza-J _11R7M_VOgKO1RJyRSRErT3')
    #print(len(mem_need))
    result = []
    for mem in mem_need:
        try: description = mem.find('a', class_='SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE').get_text(strip=True)
        except: description = 'Описание не найдено'
        try: image = mem.find('img', class_='_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax').get('src')
        except: image = 'Картинка не найдена'
        try: link = mem.find('div', class_='_1NSbknF8ucHV2abfCZw2Z1').find('a').get('href')
        except: link = 'Ссылка не найдена'
        if image != 'Картинка не найдена' and link != 'Ссылка не найдена':
            result.append({
                'description': description,
                'image': image,
                'link': 'https://www.reddit.com'+link
            })
    #print(len(result))
    return result[:amount]
#print(get_memes_reddit_old(5))
# Проблемы с get_memes_reddit_old  - практически нет картинок, делать проверку на картинку? можно ли присылать гифку или видео? ПАГИНАААААААААЦИЯ!





def get_memes_reddit_now(amount):
    url = 'https://www.reddit.com/r/meme/'
    soup = BeautifulSoup(get_html(url), 'html.parser')
    mem_need = soup.findAll('div', class_='_1poyrkZ7g36PawDueRza-J _11R7M_VOgKO1RJyRSRErT3')
    result = []
    for mem in mem_need:
        try: description = mem.find('h3', class_='_eYtD2XCVieq6emjKBH3m').get_text(strip=True)
        except: description = 'Описание не найдено'
        try: image = mem.find('img', class_='_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax').get('src')
        except: image = 'Картинка не найдена'
        try: link = 'https://www.reddit.com' + mem.find('div', class_='_1NSbknF8ucHV2abfCZw2Z1').find('a').get('href')
        except: link = 'Ссылка не найдена'
        result.append({
            'description': description,
            'image': image,
            'link':  link
        })
    return result[3:amount+3]

#print(get_memes_reddit_now(3))

'''Мемы с 2008 года https://www.reddit.com/r/memes/ | Самые актуальные мемы https://www.reddit.com/r/meme/ | Введи текст и получи новость https://www.reddit.com/search/?q=здесьтекстпользователя '''





