from aiogram import types

from loader import dp


# сюда попадает все то, что не было учтено ботом
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"'{message.text}' - не могу понять, что вы хотели этим сказать\n"
                         f"Вы не выбрали команду. Я не знаю, что вы хотите 🤖")

