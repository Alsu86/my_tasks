from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters.command import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.filters.callback_data import CallbackData
from aiogram.types.input_file import FSInputFile

API_TOKEN = ''

bot = Bot(token = API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(storage = storage)

class UserState (StatesGroup):
    age = State()
    growth = State()
    weight = State()

class BuyState(StatesGroup):
    price = State()
class ChooseBtn(CallbackData, prefix = 'any'):
    id_btn : int

class ChooseProduct(CallbackData, prefix = 'any'):
    id_product : int
@dp.message(CommandStart(), StateFilter(default_state))
async def start(message : Message):
    buttons = [
        [KeyboardButton(text = 'Рассчитать'), KeyboardButton(text = 'Информация')],
        [KeyboardButton(text = 'Купить')]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard = buttons)
    await  message.answer(text = 'Привет!', reply_markup = keyboard)


@dp.message(lambda msg: msg.text == 'Рассчитать', StateFilter(default_state))
async def main_menu(message : Message):
    buttons = [
        [InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data=ChooseBtn(id_btn = 0).pack())],
        [InlineKeyboardButton(text = 'Формулы расчета', callback_data = ChooseBtn(id_btn = 1).pack())]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard = buttons)
    await message.answer(text = 'Выбери опцию', reply_markup = keyboard)

@dp.callback_query(ChooseBtn.filter(), StateFilter(default_state))
async def set_age(callback : CallbackQuery, callback_data : ChooseBtn, state : FSMContext):
    if callback_data.id_btn == 0:
        await callback.message.answer(text = 'Введите свой возраст')
        await state.set_state(UserState.age)
    else:
        await callback.message.answer(text = '10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')


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

@dp.message(lambda msg: msg.text == 'Купить')
async def get_buying_list(message : Message, state : FSMContext):
    file = FSInputFile(path = r'photo.jpg')
    for i in range(4):
        await message.answer_photo(photo=file,caption=f'Название: Product{i + 1} | Описание: описание {i + 1} | Цена: {(i + 1) * 100}')
    buttons = [
        [InlineKeyboardButton(text = f'Продукт {i + 1}', callback_data = ChooseProduct(id_product = i).pack())] for i in range(4)
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard = buttons)
    await message.answer(text = 'Выберите продукт для покупки:', reply_markup = keyboard)
    await state.set_state(BuyState.price)
@dp.callback_query(ChooseProduct.filter(), StateFilter(BuyState.price))
async def send_confirm_message(callback : CallbackQuery, callback_data : ChooseProduct, state : FSMContext):
    await callback.message.delete()
    await callback.message.answer(text = f'Вы преобрели продукт {callback_data.id_product + 1}')
    await state.clear()

if __name__ == '__main__':
    dp.run_polling(bot)
