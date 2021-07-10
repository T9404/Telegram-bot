from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink

from loader import dp
from keyboards import reddit_main, menu

from applications.memes import get_memes_reddit_old, get_memes_reddit_now, get_discussions
from applications.active_reddit import get_reddit




@dp.message_handler(commands=['get_memes'])
async def show_reddit_menu(message: types.Message):
    """По команде get_memes открывает клавиатуру для выбора переводов"""
    await message.answer("Нажмите на кнопку", reply_markup=reddit_main)


class Memes(StatesGroup):
    #command1 = State()
    command2 = State()
    command3 = State()


# # активация первого состояния Translation
# @dp.message_handler(text="Old мемы 🧓", state=None)
# async def state_activate_old_memes_command1(message: types.Message):
#     await message.answer('Сколько мемов вы хотите получить? \n Пример: 5 \nP.S. Шрэк-10000000000 ))) ')
#     await Memes.command1.set()
#
#
# # выполняем команду первого состояния, переводим текст на русский язык
# @dp.message_handler(state=Memes.command1)
# async def state_activate_old_memes_command2(message: types.Message, state: FSMContext):
#     # await message.answer(get_memes_reddit_old(int(message.text)))
#     # await state.finish()
#     try:
#         memes = get_reddit(int(message.text))
#         for mem in memes:
#             await message.answer(f'{mem["description"]}\n{ mem["image"]}\n{hlink("Ссылка на пост", mem["link"]) }\n{hlink("Количество комментариев", mem["statistics"]) }')
#     except:
#         await message.answer('Повторите запрос 👾')
#
#     await state.finish()


# активация второго состояния Translation
@dp.message_handler(text="Свежие мемы 😸")
async def state_activate_new_memes_command1(message: types.Message):
    await message.answer('Сколько мемов вы хотите получить? \n Пример: 4')
    await Memes.command2.set()


# выполняем команду второго состояния, переводим текст на английский язык
@dp.message_handler(state=Memes.command2)
async def state_activate_new_memes_command2(message: types.Message, state: FSMContext):
    try:
        memes = get_memes_reddit_now(int(message.text))
        for mem in memes:
            await message.answer(f'{mem["description"]}\n{hlink("Ссылка на картинку", mem["image"])}')
    except:
        await message.answer('Повторите запрос 👾')


    await state.finish()


# активация первого состояния Translation
@dp.message_handler(text="Интересные посты 👨‍💻", state=None)
async def state_activate_discussion_command1(message: types.Message):
    await message.answer('Введите название объекта \n Пример: Russia')
    await Memes.command3.set()

# выполняем команду второго состояния, переводим текст на английский язык
@dp.message_handler(state=Memes.command3)
async def state_activate_discussion_command2(message: types.Message, state: FSMContext):
    try:
        informations = get_discussions(message.text)
        for inf in informations:
            await message.answer(f'{inf["description"]}\n{hlink("Ссылка на картинку", inf["image"]) }\n{hlink("Ссылка на пост", inf["link"]) }\n{hlink("Количество комментариев", inf["statistics"]) }')
    except:
        await message.answer('Повторите запрос 👾')

    await state.finish()


@dp.message_handler(text="Вернуться в основное меню 🔙")
async def show_menu(message: types.Message):
    """Выбор из меню переводов для возврата в основное меню"""
    await message.answer("Вы вернулись в основное меню ⏪", reply_markup=menu)