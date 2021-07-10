from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Приветствие",
            "/help - Получить справку",
            "/menu - Открыть основное меню",
            "/get_weather - Узнать погоду",
            "/get_films - Ввести ключевое слово и получить фильмы с рейтингом",
            "/get_film_top20 - Вывести топ 20 фильмов человечества",
            "/get_news - выводит 5 новостей про hi-tech",
            "/get_fresh_news - выводит свежие новости про hi-tech",
            "/get_translation - открывает меню переводов с русс на англ и наоборот",
            "/get_memes - Отдых с Reddit",
            "/subcriber - Подписаться на бота(пока ничего не дает,в разработке)",
            "/unsubcriber - Отписаться от бота",
            "'@ gamee ' - Введите команду, обязательно без пробела и вас ждет сюрприз")

    await message.answer("\n".join(text))
