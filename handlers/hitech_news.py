import asyncio

from aiogram import types

from applications.hi_tech_news import get_news_and_save_bd
from applications.work_with_bd import get_data_from_db
from loader import dp


@dp.message_handler(commands=['get_news'], state=None)
async def get_news(message: types.Message):
    get_news_and_save_bd()
    data = get_data_from_db()
    for d in data:
        await message.answer(f'Новость 📧:\n{d[0]}\nСсылка:\n{d[1]}')



@dp.message_handler(commands=['get_fresh_news'], state=None)
async def get_fresh_news(message: types.Message):
    fresh_news = get_news_and_save_bd()
    #await message.answer(f'Новость:\n{len(fresh_news)}')
    if len(fresh_news) == 0:
        await message.reply("Нету свежих новостей ⏰")
    else:
        for f in fresh_news:
            await message.answer(f'Новость 🗞:\n{f["title"]}\n{f["link"]}')


# функция для автоматического мониторинга свежих новостей
# from loader import bot
# async def news_every_time():
#     # для автоматической отправки пользователю
#     while True:
#         fresh_news = get_news_and_save_bd()
#         if len(fresh_news) >= 1:
#             for f in fresh_news:
#                 await bot.send_message('456110449', f'Новость:\n{f["link"]}', )
#         else:
#             text = 'новостей нет'
#             await bot.send_message('456110449', text)
#         await asyncio.sleep(20)