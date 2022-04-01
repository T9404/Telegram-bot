from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from keyboards import translate_menu, menu
from loader import dp
from applications.translator import translator_en, translator_ru


class Translation(StatesGroup):
    command1 = State()
    command2 = State()


@dp.message_handler(commands=['get_translation'])
async def show_translate_menu(message: types.Message):
    await message.answer("Select translation options 🔀", reply_markup=translate_menu)


@dp.message_handler(text="Translation into Russian (⌒_⌒;)", state=None)
async def state_activate_translation_command1(message: types.Message):
    await message.answer('🇬🇧 Enter the text to translate into Russian ⬇')
    await Translation.command1.set()


@dp.message_handler(state=Translation.command1)
async def get_russian_text_from_english(message: types.Message, state: FSMContext):
    try:
        await message.answer(translator_ru(message.text))
    except:
        await message.answer('Enter the text in English 🇬🇧')

    await state.finish()


@dp.message_handler(text="Translation into English (づ￣ ³￣)づ")
async def state_activate_translation_command2(message: types.Message):
    await message.answer('🇷🇺 Enter the text to translate into English ⬇')
    await Translation.command2.set()


@dp.message_handler(state=Translation.command2)
async def get_english_text_from_russian(message: types.Message, state: FSMContext):
    try:
        await message.answer(translator_en(message.text))
    except:
        await message.answer('Enter the text in Russian 🇷🇺')

    await state.finish()


@dp.message_handler(text="Go back to the main menu 🔙")
async def show_menu(message: types.Message):
    await message.answer("You are back in the main menu ⏪", reply_markup=menu)
