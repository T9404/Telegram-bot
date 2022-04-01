from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink

from applications.pgbd import add_subscriber, unsubscribers
from keyboards.menu import subscriber_menu
from loader import dp

from applications.cinema_kino import get_film, get_film_top20
from applications.hi_tech_news import get_news_and_save_bd
from applications.weather import get_weather, get_weather_week
from applications.work_with_bd import get_data_from_db, create_table
from applications.translator import translator_en, translator_ru
from applications.memes import get_memes_reddit_now, get_discussions

from keyboards import menu, translate_menu, weather_back, news_back, top20_films, film_search, reddit_main


class Weather(StatesGroup):
    command1 = State()
    command2 = State()


class Films(StatesGroup):
    command1 = State()


class Translation(StatesGroup):
    command1 = State()
    command2 = State()


class Memes(StatesGroup):
    command2 = State()
    command3 = State()


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Select an action from the menu below 🤖", reply_markup=menu)


@dp.message_handler(text="Close the keyboard 🔒")
async def exit_from_menu(message: types.Message):
    await message.answer("You have disabled the keyboard ❎", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Text translation 👅")
async def translate_text(message: types.Message):
    await message.answer("Select translation options 🤖", reply_markup=translate_menu)


@dp.message_handler(text="Weather 🌏")
async def show_translate_menu(message: types.Message):
    await message.answer("Click on the button you need 🔀", reply_markup=weather_back)


@dp.message_handler(text="Weather ⛅", state=None)
async def state_activate_weather_command1(message: types.Message):
    await message.answer('Just enter a city or town 🏙:', reply_markup=weather_back)
    await Weather.command1.set()


@dp.message_handler(state=Weather.command1)
async def get_answer_one_day(message: types.Message, state: FSMContext):
    weather = get_weather(message)
    await message.answer(weather)
    await state.finish()


@dp.message_handler(text="Weather for 6 days 📆")
async def state_activate_weather_command2(message: types.Message):
    await message.answer('Just enter a city or town 🏙:', reply_markup=weather_back)
    await Weather.command2.set()


@dp.message_handler(state=Weather.command2)
async def get_answer_six_days(message: types.Message, state: FSMContext):
    days = get_weather_week(message)

    if len(days) > 2:
        text_test = "{day}"
        text = '\n\n'.join(
            [
                text_test.format(day=day)
                for day in days
            ]
        )
        await message.answer(text)

    else:
        await message.answer(' '.join(days))

    await state.finish()


@dp.message_handler(text="Rating of films 🎦", state=None)
async def state_activate_films_command1(message: types.Message):
    await message.answer(
        '📺 Enter the keyword and the number of movies on the program output . \n Example: \n Shrek-10 ', reply_markup=film_search)
    await Films.command1.set()


@dp.message_handler(state=Films.command1)
async def get_rate_films_by_keyword(message: types.Message, state: FSMContext):
    try:
        films = get_film(message.text)
        for film, year, rate, link in films:
            await message.answer(f'Movie: "{film}"\nYear: {year}\nPricing: "{rate}\nLink: {link}')

    except:
        await message.answer("There was a mistake in writing! Follow the rules for writing 'name'-'number of issues'")

    await state.finish()


@dp.message_handler(text="TOP 20 films🔺")
async def get_top20_films_by_rate_kinopoisk(message: types.Message):
    films = get_film_top20()
    text_films = 'Film: "{film}"\n Raiting: "{rate}"'
    text = '\n\n'.join(
        [
            text_films.format(film=film, rate=rate)
            for film, rate in films.items()
        ]
    )
    await message.answer(text, reply_markup=top20_films)


@dp.message_handler(text="News ⚡")
async def show_news_menu(message: types.Message):
    await message.answer("Click on the button you need 🔀", reply_markup=news_back)


@dp.message_handler(text="Hi-tech news 👤")
async def get_news(message: types.Message):
    create_table()
    data = get_data_from_db()

    for d in data:
        await message.answer(f'News 🗞:\n{d[0]}\nLink:\n{d[1]}', reply_markup=news_back)


@dp.message_handler(text="Latest hi-tech news 🗣")
async def get_fresh_news(message: types.Message):
    await message.answer("Processing is underway... ⏰")
    fresh_news = get_news_and_save_bd()

    if len(fresh_news) == 0:
        await message.reply("There is no fresh news ⏰")
    else:
        for f in fresh_news:
            await message.answer(f'News 🗞:\n{f["title"]}\n{f["link"]}')


@dp.message_handler(Command("get_translation"))
async def show_translate_menu(message: types.Message):
    await message.answer("Select translation options 👅", reply_markup=translate_menu)


@dp.message_handler(text="Translation into Russian (⌒_⌒;)", state=None)
async def state_activate_translation_command1(message: types.Message):
    await message.answer('🇬🇧 Enter the text to translate into Russian⬇')
    await Translation.command1.set()


@dp.message_handler(state=Translation.command1)
async def get_russian_text_from_english(message: types.Message, state: FSMContext):
    try:
        await message.answer(translator_ru(message.text))
        await state.finish()
    except:
        await message.answer('Enter the text in English 🇬🇧')


@dp.message_handler(text="Translation into English (づ￣ ³￣)づ")
async def state_activate_translation_command2(message: types.Message):
    await message.answer('🇷🇺 Enter the text to translate into English ⬇')
    await Translation.command2.set()


@dp.message_handler(state=Translation.command2)
async def get_english_text_from_russian(message: types.Message, state: FSMContext):
    try:
        await message.answer(translator_en(message.text))
        await state.finish()
    except:
        await message.answer('Enter the text in Russian 🇷🇺')


@dp.message_handler(text='Vacation with Reddit 🤡')
async def show_reddit_menu(message: types.Message):
    await message.answer("Click on the button", reply_markup=reddit_main)


@dp.message_handler(text="Fresh memes 😸")
async def state_activate_new_memes_command1(message: types.Message):
    await message.answer('How many memes do you want to get? \n Example: 4 ')
    await Memes.command2.set()


@dp.message_handler(state=Memes.command2)
async def state_activate_new_memes_command2(message: types.Message, state: FSMContext):
    try:
        memes = get_memes_reddit_now(int(message.text))
        for mem in memes:
            await message.answer(f'{mem["description"]}\n{hlink("Link to the picture", mem["image"])}')
    except:
        await message.answer('Repeat the request 👾')

    await state.finish()


@dp.message_handler(text="Interesting posts 👨‍💻", state=None)
async def state_activate_discussion_command1(message: types.Message):
    await message.answer('Enter the name of the object \n Example: Tiger-2')
    await Memes.command3.set()


@dp.message_handler(state=Memes.command3)
async def state_activate_discussion_command2(message: types.Message, state: FSMContext):
    try:
        informations = get_discussions(message.text)
        await message.answer(len(informations))
        for inf in informations:
            await message.answer(f'{inf["description"]}\n{hlink("Link to the post", inf["link"])} \n Number of comments: "there should have been a number of comments"')

    except Exception as ex:
        await message.answer(ex, '\n Repeat the request  👾')

    await state.finish()


@dp.message_handler(text="Go back to the main menu 🔙")
async def show_menu(message: types.Message):
    await message.answer("You are back in the main menu 🔙", reply_markup=menu)


@dp.message_handler(text="Subscription 🤖")
async def subscribers(message: types.Message):
    await message.answer(
        "The bot is located on a free heroku server, there may be interruptions in operation, subscribe and you will be notified when the bot is activated 🔀",
        reply_markup=subscriber_menu)


@dp.message_handler(text="Subscribe 🔗")
async def subscribe(message: types.Message):
    name = message.from_user.full_name
    user_id = message.from_user.id
    text = add_subscriber(name=name, user_id=user_id)
    await message.answer(text)


@dp.message_handler(text="Unsubscribe 🖇")
async def get_unsubscribe(message: types.Message):
    text = unsubscribers(message.from_user.id)
    await message.answer(text)
