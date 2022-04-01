from aiogram import types
from loader import dp


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"'{message.text}' - I can't understand what you meant by that\n"
                         f"You didn't choose a team. I do not know what you want 🤖 ")
