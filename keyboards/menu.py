import keyboards
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Weather 🌏"),
            KeyboardButton(text="News"),
        ],
        [
            KeyboardButton(text="Vacation with Reddit 🤡"),
            KeyboardButton(text="Text translation 👅"),
        ],
        [
            KeyboardButton(text="TOP 20 films 🔺"),
            KeyboardButton(text="Rating of films 🎦")
        ],
        [
            KeyboardButton(text="Subscription🤖"),
            KeyboardButton(text="Close the keyboard 🔒"),
        ]
    ],
    resize_keyboard=True
)


translate_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Translation into Russian (⌒_⌒;)"),
            KeyboardButton(text="Translation into English (づ￣ ³￣)づ")
        ],
        [
            KeyboardButton(text="Go back to the main menu 🔙")
        ]
    ],
    resize_keyboard=True
)


weather_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Weather ⛅"),
            KeyboardButton(text="Weather for 6 days 📆"),
        ],

        [
            KeyboardButton(text="Go back to the main menu 🔙")
        ]

    ],
    resize_keyboard=True
)


news_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Hi-tech news 👤"),
            KeyboardButton(text="Latest hi-tech news 🗣"),
        ],
        [
            KeyboardButton(text="Go back to the main menu🔙")
        ]
    ],
    resize_keyboard=True
)


top20_films = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Go back to the main menu 🔙")
        ]
    ],
    resize_keyboard=True
)


film_search = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Rating of films 🎦")
        ],
        [
            KeyboardButton(text="Go back to the main menu 🔙")
        ]
    ],
    resize_keyboard=True
)


reddit_main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Fresh memes 😸")
        ],
        [
            KeyboardButton(text="Interesting posts 👨‍💻")
        ],
        [
            KeyboardButton(text="Go back to the main menu 🔙")
        ]
    ],
    resize_keyboard=True
)


subscriber_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Subscribe 🔗"),
            KeyboardButton(text="Unsubscribe 🖇"),
        ],
        [
            KeyboardButton(text="Go back to the main menu 🔙")
        ]
    ],
    resize_keyboard=True
)
