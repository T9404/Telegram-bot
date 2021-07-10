import logging

from aiogram import Dispatcher

from applications.pgbd import message_to_subscribers
from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    # рассылка админам, что бот запущен
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")
        except Exception as err:
            logging.exception(err)
    # рассылка подписчикам, что бот запущен
    users = message_to_subscribers()
    for user in users:
        await dp.bot.send_message(user, "Бот активирован и готов к работе\n(вы это видите т.к. вы подписаны)")
