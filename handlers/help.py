from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("List of commands: ",
            "/start - Greeting",
            "/help - Get help",
            "/menu - Open the main menu",
            "/get_weather - Find out the weather",
            "/get_films - Enter a keyword and get rated movies",
            "/get_film_top20 - Display the top 20 movies humanity",
            "/get_news - displays 5 news about hi-tech",
            "/get_fresh_news - displays the latest news about hi-tech",
            "/get_translation - opens the menu of translations from Russian to English and vice versa",
            "/get_memes - Vacation with Reddit",
            "/subscribe - Subscribe to the bot (does not give anything yet, in development)",
            "/unsubscribe - Unsubscribe from the bot")

    await message.answer("\n".join(text))
