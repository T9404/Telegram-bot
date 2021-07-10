from aiogram import executor

# для автоматического запуска функции поиска свежих новостей
#from handlers.hitech_news import news_every_time

from loader import dp
import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
    # это для автозапуска поиска новых новостей
    # loop = asyncio.get_event_loop()
    # loop.create_task(news_every_time())

#goo
#pip freeze > requirements.txt