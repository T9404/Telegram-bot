from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}!\n"
                         "Glad you're using me! 🔥 To call for help, enter or press /help 🤖", reply_markup=menu)
