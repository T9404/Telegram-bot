from applications.kinopoisk_api import KP


kinopoisk = KP(token='Your token')


def get_film(user_input):
    global kinopoisk
    name, count = user_input.split('-')
    count = int(count)
    search = kinopoisk.search(name)

    kino = [[None]*4 for _ in range(50)]
    i = 0

    for item in search:
        kino[i][0] = item.ru_name
        kino[i][1] = item.year
        kino[i][2] = item.kp_rate
        kino[i][3] = item.poster_preview
        i += 1

    kino = kino[::-1]

    j = 0
    while kino[j][0] == None:
        del(kino[j])

    # sorting by movie rating
    kino.sort(key=lambda x: x[2], reverse=True)

    if count > len(kino):
        kino.append(len(kino))
        kino.append(
            'https://i.mycdn.me/i?r=AzEPZsRbOZEKgBhR0XGMT1Rktb5tvjJBmafby7jp-PTXfKaKTM5SRkZCeTgDn6uOyic')

     # at the beginning the worst , then better
    kino = kino[::-1]

    return kino[:count]


def get_film_top20():
    global kinopoisk
    top500 = kinopoisk.top500()
    good_film = {item.ru_name: item.kp_rate for item in top500}

    return good_film
