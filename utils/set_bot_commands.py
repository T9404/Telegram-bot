from aiogram import types


async def set_default_commands(dp):
    # список команд бота
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("menu", "Открыть менюшку"),
            types.BotCommand("subscribe", "Подписка!"),
            types.BotCommand("unsubscribe", "Отписка!"),
            #types.BotCommand("getsubscribe", "Все подписки"),
            types.BotCommand("get_weather", "Узнаем погоду"),
            types.BotCommand("get_weather_6_days", "Узнаем погоду на 6 дней вперед"),
            types.BotCommand("get_news", "Получаем новости hi-tech"),
            types.BotCommand("get_fresh_news", "Получаем свежие новости hi-tech"),
            types.BotCommand("get_films", "Узнать рейтинг фильмов по ключевому слову"),
            types.BotCommand("get_film_top20", "Вывести топ 20 фильмов человечества"),
            types.BotCommand("get_translation", "Перевод текста")

        ]
    )
