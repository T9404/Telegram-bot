from aiogram import Dispatcher
from applications.pgbd import message_to_subscribers
from data.config import ADMINS
import logging


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "The Bot Is Running")
        except Exception as err:
            logging.exception(err)

    users = message_to_subscribers()
    for user in users:
        await dp.bot.send_message(user, "The bot is activated and ready to work")
