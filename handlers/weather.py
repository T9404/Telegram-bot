from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from applications.weather import get_weather, get_weather_week
from keyboards import weather_back
from loader import dp


class Weather(StatesGroup):
    command1 = State()
    command2 = State()


@dp.message_handler(commands=['get_weather'])
async def show_translate_menu(message: types.Message):
    await message.answer("Click on the button you need 🔀", reply_markup=weather_back)


@dp.message_handler(text="Weather ⛅", state=None)
async def state_activate_weather_command1(message: types.Message):
    await message.answer('Just enter a city or town 🌆:')
    await Weather.command1.set()


@dp.message_handler(state=Weather.command1)
async def get_answer_one_day(message: types.Message, state: FSMContext):
    await message.answer(get_weather(message))
    await state.finish()


@dp.message_handler(text="Weather for 6 days 📆", state=None)
async def state_activate_weather_command2(message: types.Message):
    await message.answer('Just enter a city or town🌆:')
    await Weather.command2.set()


@dp.message_handler(state=Weather.command2)
async def get_answer_six_days(message: types.Message, state: FSMContext):
    days = get_weather_week(message)

    if len(days) > 2:
        text_test = "{day}"
        text = '\n\n'.join(
            [
                text_test.format(day=day)
                for day in days
            ]
        )
        await message.answer(text)
    else:
        await message.answer(' '.join(days))

    await state.finish()
