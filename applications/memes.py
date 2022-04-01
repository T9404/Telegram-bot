import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    html = response.text

    return html


# the message and the number of posts, if there are not enough posts on the page, then
def get_discussions(user_input):
    user_object, amount = user_input.split('-')
    amount = int(amount)

    url = f'https://www.reddit.com/search/?q={user_object}'
    soup = BeautifulSoup(get_html(url), 'html.parser')
    mem_need = soup.findAll('div', class_='_2XDITKxlj4y3M99thqyCsO')

    result = []

    for mem in mem_need:

        try:
            description = mem.find(
                'a', class_='SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE').get_text(strip=True)
        except:
            description = 'Description not found'

        try:
            image = mem.find(
                'img', class_='_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax').get('src')
        except:
            image = 'Picture not found'

        try:
            link = 'https://www.reddit.com' + \
                mem.find('a', class_='SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE').get(
                    'href')
        except:
            link = 'Link not found'

        result.append({
            'description': description,
            'image': image,
            'link': link
        })

    return result[:amount]


def get_memes_reddit_old(amount):
    url = 'https://www.reddit.com/r/memes/'
    soup = BeautifulSoup(get_html(url), 'html.parser')
    mem_need = soup.findAll(
        'div', class_='_1poyrkZ7g36PawDueRza-J _11R7M_VOgKO1RJyRSRErT3')

    result = []

    for mem in mem_need:

        try:
            description = mem.find(
                'a', class_='SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE').get_text(strip=True)
        except:
            description = 'Description not found'

        try:
            image = mem.find(
                'img', class_='_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax').get('src')
        except:
            image = 'Picture not found'

        try:
            link = mem.find('div', class_='_1NSbknF8ucHV2abfCZw2Z1').find(
                'a').get('href')
        except:
            link = 'Link not found'

        if image != 'Picture not found' and link != 'Link not found':
            result.append({
                'description': description,
                'image': image,
                'link': 'https://www.reddit.com'+link
            })

    return result[:amount]


def get_memes_reddit_now(amount):
    url = 'https://www.reddit.com/r/meme/'
    soup = BeautifulSoup(get_html(url), 'html.parser')
    mem_need = soup.findAll(
        'div', class_='_1poyrkZ7g36PawDueRza-J _11R7M_VOgKO1RJyRSRErT3')

    result = []

    for mem in mem_need:

        try:
            description = mem.find(
                'h3', class_='_eYtD2XCVieq6emjKBH3m').get_text(strip=True)
        except:
            description = 'Description not found'

        try:
            image = mem.find(
                'img', class_='_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax').get('src')
        except:
            image = 'Picture not found'

        try:
            link = 'https://www.reddit.com' + \
                mem.find('div', class_='_1NSbknF8ucHV2abfCZw2Z1').find(
                    'a').get('href')
        except:
            link = 'Link not found'

        result.append({
            'description': description,
            'image': image,
            'link':  link
        })

    return result[3:amount+3]
