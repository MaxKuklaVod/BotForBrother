import asyncio
import json
from pathlib import Path
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


with open(Path(__file__).parent / "Json" / "tokens.json") as complex_data:
    data = complex_data.read()
    tokens = json.loads(data)

API_TOKEN = tokens["main_token"]

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer(
        "Привет! Я бот для обучения. Используйте /help, чтобы узнать список команд."
    )

# Обработчик команды /help
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Список команд:\n"
        "/start - Начать общение\n"
        "/help - Показать список команд\n"
        "/teory - Теоретическая часть\n"
        "/practis - Практическая часть"
    )

# Обработчик команды /teory
@dp.message(Command("teory"))
async def teory(message: Message):
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):  # Создаем 7 кнопок
        builder.add(InlineKeyboardButton(text=f"Тема {i}", callback_data=f"teory_{i}"))
    builder.adjust(1)  # Располагаем кнопки в один столбец
    await message.answer("Выберите тему для изучения теории:", reply_markup=builder.as_markup())

# Обработчик команды /practis
@dp.message(Command("practis"))
async def practis(message: Message):
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):  # Создаем 7 кнопок
        builder.add(InlineKeyboardButton(text=f"Практика {i}", callback_data=f"practis_{i}"))
    builder.adjust(1)  # Располагаем кнопки в один столбец
    await message.answer("Выберите тему для практики:", reply_markup=builder.as_markup())

# Обработчик нажатий на inline кнопки
@dp.callback_query(F.data.startswith("practis_"))
async def process_practis_callback(callback: CallbackQuery):
    topic_number = callback.data.split("_")[1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 4):  # Создаем 3 дополнительные кнопки
        builder.add(InlineKeyboardButton(text=f"Задание {i}", callback_data=f"{callback.data}_task{i}"))
    builder.adjust(1)  # Располагаем кнопки в один столбец
    await callback.message.edit_text(
        f"Вы выбрали Практику {topic_number}. Выберите задание:",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("teory_"))
async def process_teory_callback(callback: CallbackQuery):
    topic_number = callback.data.split("_")[1]
    await callback.message.edit_text(f"Вы выбрали теорию {topic_number}. Здесь будет объяснение.")
    await callback.answer()

@dp.callback_query(F.data.endswith("_task1"))
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.edit_text("Вы выбрали Задание 1.")
    await callback.answer()

@dp.callback_query(F.data.endswith("_task2"))
async def process_task2_callback(callback: CallbackQuery):
    await callback.message.edit_text("Вы выбрали Задание 2.")
    await callback.answer()

@dp.callback_query(F.data.endswith("_task3"))
async def process_task3_callback(callback: CallbackQuery):
    await callback.message.edit_text("Вы выбрали Задание 3.")
    await callback.answer()

# Запуск бота
if __name__ == '__main__':
    asyncio.run(dp.run_polling(bot))