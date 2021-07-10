from applications.kinopoisk_api import KP

kinopoisk = KP(token='d35406a7-1475-4210-bcf6-d0bc22125d96')

# Ссылка на API https://github.com/Ulbwaa/KinoPoiskAPI

def get_film(user_input):
    global kinopoisk
    name, count = user_input.split('-') #разделяем название и количество
    count = int(count)

    search = kinopoisk.search(name)

    kino = [[None]*4 for _ in range(50)]  # массив с подмассивом, обязателен лодашик - '_'
    i = 0
    for item in search:
        kino[i][0] = item.ru_name
        kino[i][1] = item.year
        kino[i][2] = item.kp_rate
        kino[i][3] = item.poster_preview
        i+=1
    kino = kino[::-1] #переворачиваем массив

    i = 0
    while kino[i][0] == None: #удаление пустых подмассивов
        del(kino[i])

    kino.sort(key=lambda x: x[2], reverse=True)#сортировка по рейтингу фильмов

    if count > len(kino):
        kino.append(f'я вас обманул, их всего {len(kino)}, расходимся') #немного юмора
        kino.append('https://i.mycdn.me/i?r=AzEPZsRbOZEKgBhR0XGMT1Rktb5tvjJBmafby7jp-PTXfKaKTM5SRkZCeTgDn6uOyic')

    kino = kino[::-1] # в начале худшие , потом лучше
    return kino[:count]


'''
Введите название, пробел, количество фильмов на выходе(ограничено)
Пример: 
print(get_film('Тачки-1000'))
'''

def get_film_top20():
    global kinopoisk
    top500 = kinopoisk.top500()
    good_film = {item.ru_name: item.kp_rate for item in top500} # выведем пользователю словарь для лучшей читабельности, информации по минимуму
    return good_film  # API сломалось, спасибо КиноПоиску, выводим по максимуму






#print(get_film('ну погоди'))


