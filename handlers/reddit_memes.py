from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink
from loader import dp
from keyboards import reddit_main, menu
from applications.memes import get_memes_reddit_now, get_discussions


class Memes(StatesGroup):
    command2 = State()
    command3 = State()


@dp.message_handler(commands=['get_memes'])
async def show_reddit_menu(message: types.Message):
    await message.answer("Click on the button", reply_markup=reddit_main)


@dp.message_handler(text="Fresh memes 😸")
async def state_activate_new_memes_command1(message: types.Message):
    await message.answer('How many memes do you want to get? \n Example: 4')
    await Memes.command2.set()


@dp.message_handler(state=Memes.command2)
async def state_activate_new_memes_command2(message: types.Message, state: FSMContext):
    try:
        memes = get_memes_reddit_now(int(message.text))
        for mem in memes:
            await message.answer(f'{mem["description"]}\n{hlink("Link to the picture", mem["image"])}')
    except:
        await message.answer('Repeat the request 👾')

    await state.finish()


@dp.message_handler(text="Interesting posts 👨‍💻", state=None)
async def state_activate_discussion_command1(message: types.Message):
    await message.answer('Enter the name of the object \n Example: Russia')
    await Memes.command3.set()


@dp.message_handler(state=Memes.command3)
async def state_activate_discussion_command2(message: types.Message, state: FSMContext):
    try:
        informations = get_discussions(message.text)
        for inf in informations:
            await message.answer(f'{inf["description"]}\n{hlink("Link to the picture", inf["image"]) }\n{hlink("Link to the post", inf["link"]) } \
            \n{hlink("Number of comments", inf["statistics"]) }')
    except:
        await message.answer('Repeat the request 👾')

    await state.finish()


@dp.message_handler(text="Go back to the main menu 🔙")
async def show_menu(message: types.Message):
    await message.answer("You are back in the main menu ⏪", reply_markup=menu)
