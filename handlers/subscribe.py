from aiogram import types
from aiogram.dispatcher import FSMContext

from data import config
from loader import dp
from applications.pgbd import add_subscriber,  unsubscribers, get_subscribers


@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    print(message.from_user.id)
    name = message.from_user.full_name
    user_id = message.from_user.id
    text = add_subscriber(name=name, user_id=user_id)
    await message.answer(text)


@dp.message_handler(commands=['getsubscribe'])
async def get_subscribe(message: types.Message):
    users = get_subscribers()
    await message.answer(users)


@dp.message_handler(commands=['unsubscribe'])
async def get_unsubscribe(message: types.Message):
    text = unsubscribers(message.from_user.id)
    await message.answer(text)