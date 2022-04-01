from aiogram import types
from applications.hi_tech_news import get_news_and_save_bd
from applications.work_with_bd import get_data_from_db
from loader import dp


@dp.message_handler(commands=['get_news'], state=None)
async def get_news(message: types.Message):
    get_news_and_save_bd()
    data = get_data_from_db()
    for d in data:
        await message.answer(f'News 📧 :\n{d[0]}\link:\n{d[1]}')


@dp.message_handler(commands=['get_fresh_news'], state=None)
async def get_fresh_news(message: types.Message):
    fresh_news = get_news_and_save_bd()
    
    if len(fresh_news) == 0:
        await message.reply("There is no fresh news ⏰")
    else:
        for f in fresh_news:
            await message.answer(f'News 🗞:\n{f["title"]}\n{f["link"]}')
