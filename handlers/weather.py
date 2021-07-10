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
    """По команде get_translation открывает клавиатуру для выбора переводов"""
    await message.answer("Нажмите на нужную вам кнопку 🔀", reply_markup=weather_back)



# активация первого состояния
@dp.message_handler(text="Погода ⛅", state=None)
async def state_activate_weather_command1(message: types.Message):
    await message.answer('Просто вводи город или населенный пункт 🌆:')
    await Weather.command1.set()


# выполняем команду первого состояния, выводим температуру и описание погоды
@dp.message_handler(state=Weather.command1)
async def get_answer_one_day(message: types.Message, state: FSMContext):
    await message.answer(get_weather(message))
    await state.finish()


# активация второго состояния
@dp.message_handler(text="Погода на 6 дней 📆", state=None)
async def state_activate_weather_command2(message: types.Message):
    await message.answer('Просто вводи город или населенный пункт 🌆:')
    # активируем состояние 2
    await Weather.command2.set()


# выполняем команду второго состояния, выводим прогноз погоды на следующие 6 дней
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
