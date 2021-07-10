from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import keyboards

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Погода 🌏"),
            KeyboardButton(text="Новости⚡"),
        ],
        [
            KeyboardButton(text="Отдых с Reddit 🤡"),
            KeyboardButton(text="Перевод текста 👅"),
        ],
        [
            KeyboardButton(text="ТОП 20 фильмов 🔺"),
            KeyboardButton(text="Рейтинг фильмов 🎦")
        ],
        [
            KeyboardButton(text="Подписка 🤖"),
            KeyboardButton(text="Закрыть клавиатуру 🔒"),
        ]
    ],
    resize_keyboard=True
)

translate_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Перевод на русский (⌒_⌒;)"),
            KeyboardButton(text="Перевод на английский (づ￣ ³￣)づ")
        ],
        [
            KeyboardButton(text="Вернуться в основное меню 🔙")
        ]
    ],
    resize_keyboard=True
)

weather_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Погода ⛅"),
            KeyboardButton(text="Погода на 6 дней 📆"),
        ],

        [
            KeyboardButton(text="Вернуться в основное меню 🔙")
        ]

    ],
    resize_keyboard=True
)

news_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Новости hi-tech 👤"),
            KeyboardButton(text="Свежие новости hi-tech 🗣"),
        ],
        [
            KeyboardButton(text="Вернуться в основное меню 🔙")
        ]
    ],
    resize_keyboard=True
)

top20_films = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Вернуться в основное меню 🔙")
        ]
    ],
    resize_keyboard=True
)



film_search = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Рейтинг фильмов 🎦")
        ],
        [
            KeyboardButton(text="Вернуться в основное меню 🔙")
        ]
    ],
    resize_keyboard=True
)


reddit_main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Свежие мемы 😸")
        ],
        [
            KeyboardButton(text="Интересные посты 👨‍💻")
        ],
        [
            KeyboardButton(text="Вернуться в основное меню 🔙")
        ]
    ],
    resize_keyboard=True
)

subscriber_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Подписаться 🔗"),
            KeyboardButton(text="Отписаться 🖇"),
        ],
        [
            KeyboardButton(text="Вернуться в основное меню 🔙")
        ]
    ],
    resize_keyboard=True
)