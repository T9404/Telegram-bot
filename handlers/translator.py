from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from keyboards import translate_menu, menu

from loader import dp

from applications.translator import translator_en, translator_ru


@dp.message_handler(commands=['get_translation'])
async def show_translate_menu(message: types.Message):
    """По команде get_translation открывает клавиатуру для выбора переводов"""
    await message.answer("Выберите варианты переводов 🔀", reply_markup=translate_menu)


class Translation(StatesGroup):
    command1 = State()
    command2 = State()


# активация первого состояния Translation
@dp.message_handler(text="Перевод на русский (⌒_⌒;)", state=None)
async def state_activate_translation_command1(message: types.Message):
    await message.answer('🇬🇧 Введите текст для перевода на русский язык ⬇')
    await Translation.command1.set()


# выполняем команду первого состояния, переводим текст на русский язык
@dp.message_handler(state=Translation.command1)
async def get_russian_text_from_english(message: types.Message, state: FSMContext):
    try:
        await message.answer(translator_ru(message.text))
    except:
        await message.answer('Введите текст на английском языке 🇬🇧')
    await state.finish()


# активация второго состояния Translation
@dp.message_handler(text="Перевод на английский (づ￣ ³￣)づ")
async def state_activate_translation_command2(message: types.Message):
    await message.answer('🇷🇺 Введите текст для перевода на ангийский язык ⬇')
    await Translation.command2.set()


# выполняем команду второго состояния, переводим текст на английский язык
@dp.message_handler(state=Translation.command2)
async def get_english_text_from_russian(message: types.Message, state: FSMContext):
    try:
        await message.answer(translator_en(message.text))
    except:
        await message.answer('Введите текст на русском языке 🇷🇺')
    await state.finish()


@dp.message_handler(text="Вернуться в основное меню 🔙")
async def show_menu(message: types.Message):
    """Выбор из меню переводов для возврата в основное меню"""
    await message.answer("Вы вернулись в основное меню ⏪", reply_markup=menu)
