from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Launch the bot"),
            types.BotCommand("help", "Output help"),
            types.BotCommand("menu", "Open the menu"),
            types.BotCommand("subscribe", "Subscribe"),
            types.BotCommand("unsubscribe", "Unsubscribe"),
            types.BotCommand("get_weather", "Find out the weather"),
            types.BotCommand("get_weather_6_days",
                             "Find out the weather for 6 days"),
            types.BotCommand("get_news", "We get hi-tech news"),
            types.BotCommand("get_fresh_news",
                             "We get the latest hi-tech news"),
            types.BotCommand(
                "get_films", "Find out the rating of films by keyword"),
            types.BotCommand("get_film_top20",
                             "Bring out the top 20 films of humanity"),
            types.BotCommand("get_translation", "Text translation")

        ]
    )
