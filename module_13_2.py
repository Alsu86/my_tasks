import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage


API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')
    print('Привет! Я бот, помогающий твоему здоровью.')

@dp.message()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    dp.run_polling(bot)
