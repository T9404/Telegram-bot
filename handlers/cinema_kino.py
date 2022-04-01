from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from applications.cinema_kino import get_film, get_film_top20
from loader import dp


class Films(StatesGroup):
    command1 = State()


@dp.message_handler(commands=['get_films'], state=None)
async def state_activate_films_command1(message: types.Message):
    await message.answer('🎥 Enter the keyword and the number of movies on the program output . \n Example: \n Shrek-10')
    await Films.command1.set()


@dp.message_handler(state=Films.command1)
async def get_rate_films_by_keyword(message: types.Message, state: FSMContext):
    try:
        films = get_film(message.text)
        for film, year, rate, link in films:
            await message.answer(f'Film: "{film}"\Year: {year}\Pricing: "{rate}\Link: {link}')
    except:
        await message.answer('There was a mistake in writing!\n follow the rules for writing "names"-"number of issues 🤖"')

    await state.finish()


@dp.message_handler(commands=['get_film_top20'])
async def get_top20_films_by_rate_kinopoisk(message: types.Message):
    films = get_film_top20()
    text_films = 'Movie: "{film}"\Rating: "{rate}"'

    text = '\n\n'.join(
        [
            text_films.format(film=film, rate=rate)
            for film, rate in films.items()
        ]
    )
    await message.answer(text)
