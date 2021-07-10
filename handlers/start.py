from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         "Рад, что ты мной пользуешься! 🔥  Для вызова помощи введи или нажми /help 🤖", reply_markup=menu)
