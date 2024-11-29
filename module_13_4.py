import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

API_TOKEN = '7969859121:AAELYRjAnRVABf1nA9k89Lp69X0MjA9Fg1w'

bot = Bot(token = API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(storage = storage)

class UserState (StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message(lambda msg: msg.text == 'Calories', StateFilter(default_state))
async def set_age(message : Message, state : FSMContext):
    await message.answer(text = 'Введите свой возраст')
    await state.set_state(UserState.age)

@dp.message(UserState.age)
async def set_growth(message : Message, state : FSMContext):
    await state.update_data(age = int(message.text))
    await message.answer(text = 'Введите свой рост')
    await state.set_state(UserState.growth)

@dp.message(UserState.growth)
async def set_weight(message : Message, state : FSMContext):
    await state.update_data(growth = int(message.text))
    await message.answer(text = 'Введите свой вес')
    await  state.set_state(UserState.weight)

@dp.message(UserState.weight)
async def send_calories(message : Message, state : FSMContext):
    await state.update_data(weight = int(message.text))
    data = dict(await state.get_data())
    calories = 10 * data['weight'] - 6.25 * data['growth'] - 5 * data['age'] + 5
    await message.answer(text=f'Ваша норма калорий {calories}')
    await state.clear()

if __name__ == '__main__':
    dp.run_polling(bot)