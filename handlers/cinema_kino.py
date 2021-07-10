from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from applications.cinema_kino import get_film, get_film_top20
from loader import dp


class Films(StatesGroup):
    command1 = State()


# активация первого состояния
@dp.message_handler(commands=['get_films'], state=None)
async def state_activate_films_command1(message: types.Message):
    await message.answer('🎥 Введите ключевое слово и количество фильмов на выходе программы . \n Пример: \n Шрэк-10  ')
    await Films.command1.set()


# выполняем команду первого состояния, выводим названия фильмов и их рейтинг
@dp.message_handler(state=Films.command1)
async def get_rate_films_by_keyword(message: types.Message, state: FSMContext):
    """Выводит рейтинг фильмов по ключевому слову"""
    try:
        films = get_film(message.text)
        for film, year, rate, link in films:
            await message.answer(f'Фильм: "{film}"\nГод: {year}\nРейтинг: "{rate}\nСсылка: {link}')
    except:
        await message.answer('В написании допущена ошибка!\nСледуйте правилам написание "названия"-"количество выдачи 🤖"')
    await state.finish()


@dp.message_handler(commands=['get_film_top20'])
async def get_top20_films_by_rate_kinopoisk(message: types.Message):
    """Выводит топ20 фильмов по версии кинопоиска"""
    films = get_film_top20()
    text_films = 'Фильм: "{film}"\nРейтинг: "{rate}"'
    text = '\n\n'.join(
        [
            text_films.format(film=film, rate=rate)
            for film, rate in films.items()
        ]
    )
    await message.answer(text)


