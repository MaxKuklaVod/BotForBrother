import asyncio
import json
from pathlib import Path
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os

API_TOKEN = os.getenv("BOT_TOKEN")

with open(
    Path(__file__).parent / "Json" / "Theory" / "firstblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    first_block_teory = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Theory" / "secondblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    second_block_teory = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Theory" / "thirdblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    third_block_teory = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Theory" / "fourthblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    fourth_block_teory = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Theory" / "fifthblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    fifth_block_teory = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Theory" / "sixthblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    sixth_block_teory = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Practices" / "firstblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    first_block_practice = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Practices" / "secondblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    second_block_practice = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Practices" / "thirdblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    third_block_practice = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Practices" / "fourthblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    fourth_block_practice = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Practices" / "fifthblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    fifth_block_practice = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Practices" / "sixthblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    sixth_block_practice = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Practices" / "seventhblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    seventh_block_practice = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Practices" / "eighthblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    eighth_block_practice = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Themes" / "theor_names.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    theor_names = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Themes" / "pract_names.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    pract_names = json.loads(data)

FIRST_BLOCK_TEORY = [
    first_block_teory["first"],
    first_block_teory["second"],
    first_block_teory["third"],
    first_block_teory["fourth"],
    first_block_teory["fifth"],
    first_block_teory["sixth"],
    first_block_teory["seventh"],
    first_block_teory["eighth"],
]

SECOND_BLOCK_TEORY = [
    second_block_teory["first"],
    second_block_teory["second"],
    second_block_teory["third"],
    second_block_teory["fourth"],
    second_block_teory["fifth"],
    second_block_teory["sixth"],
    second_block_teory["seventh"],
    second_block_teory["eighth"],
]

THIRD_BLOCK_TEORY = [
    third_block_teory["first"],
    third_block_teory["second"],
    third_block_teory["third"],
]

FOURTH_BLOCK_TEORY = [
    fourth_block_teory["first"],
    fourth_block_teory["second"],
    fourth_block_teory["third"],
    fourth_block_teory["fourth"],
    fourth_block_teory["fifth"],
    fourth_block_teory["sixth"],
    fourth_block_teory["seventh"],
]

FIFTH_BLOCK_TEORY = [
    fifth_block_teory["first"],
    fifth_block_teory["second"],
    fifth_block_teory["third"],
    fifth_block_teory["fourth"],
    fifth_block_teory["fifth"],
]

SIXTH_BLOCK_TEORY = [
    sixth_block_teory["first"],
    sixth_block_teory["second"],
    sixth_block_teory["third"],
    sixth_block_teory["fourth"],
    sixth_block_teory["fifth"],
    sixth_block_teory["sixth"],
]

FIRST_BLOCK_PRACTICE = [
    first_block_practice["first_hint"],
    first_block_practice["first_answer"],
    first_block_practice["second_hint"],
    first_block_practice["second_answer"],
    first_block_practice["third_hint"],
    first_block_practice["third_answer"],
    first_block_practice["fourth_hint"],
    first_block_practice["fourth_answer"],
    first_block_practice["fifth_hint"],
    first_block_practice["fifth_answer"],
]

SECOND_BLOCK_PRACTICE = [
    second_block_practice["first_hint"],
    second_block_practice["first_answer"],
    second_block_practice["second_hint"],
    second_block_practice["second_answer"],
    second_block_practice["third_hint"],
    second_block_practice["third_answer"],
    second_block_practice["fourth_hint"],
    second_block_practice["fourth_answer"],
    second_block_practice["fifth_hint"],
    second_block_practice["fifth_answer"],
]

THIRD_BLOCK_PRACTICE = [
    third_block_practice["first_hint"],
    third_block_practice["first_answer"],
    third_block_practice["second_hint"],
    third_block_practice["second_answer"],
    third_block_practice["third_hint"],
    third_block_practice["third_answer"],
    third_block_practice["fourth_hint"],
    third_block_practice["fourth_answer"],
    third_block_practice["fifth_hint"],
    third_block_practice["fifth_answer"],
]

FOURTH_BLOCK_PRACTICE = [
    fourth_block_practice["first_hint"],
    fourth_block_practice["first_answer"],
    fourth_block_practice["second_hint"],
    fourth_block_practice["second_answer"],
    fourth_block_practice["third_hint"],
    fourth_block_practice["third_answer"],
    fourth_block_practice["fourth_hint"],
    fourth_block_practice["fourth_answer"],
    fourth_block_practice["fifth_hint"],
    fourth_block_practice["fifth_answer"],
]

FIFTH_BLOCK_PRACTICE = [
    fifth_block_practice["first_hint"],
    fifth_block_practice["first_answer"],
    fifth_block_practice["second_hint"],
    fifth_block_practice["second_answer"],
    fifth_block_practice["third_hint"],
    fifth_block_practice["third_answer"],
    fifth_block_practice["fourth_hint"],
    fifth_block_practice["fourth_answer"],
    fifth_block_practice["fifth_hint"],
    fifth_block_practice["fifth_answer"],
]

SIXTH_BLOCK_PRACTICE = [
    sixth_block_practice["first_hint"],
    sixth_block_practice["first_answer"],
    sixth_block_practice["second_hint"],
    sixth_block_practice["second_answer"],
    sixth_block_practice["third_hint"],
    sixth_block_practice["third_answer"],
    sixth_block_practice["fourth_hint"],
    sixth_block_practice["fourth_answer"],
    sixth_block_practice["fifth_hint"],
    sixth_block_practice["fifth_answer"],
]

SEVENTH_BLOCK_PRACTICE = [
    seventh_block_practice["first_hint"],
    seventh_block_practice["first_answer"],
    seventh_block_practice["second_hint"],
    seventh_block_practice["second_answer"],
    seventh_block_practice["third_hint"],
    seventh_block_practice["third_answer"],
    seventh_block_practice["fourth_hint"],
    seventh_block_practice["fourth_answer"],
    seventh_block_practice["fifth_hint"],
    seventh_block_practice["fifth_answer"],
]

EIGHTH_BLOCK_PRACTICE = [
    eighth_block_practice["first_hint"],
    eighth_block_practice["first_answer"],
    eighth_block_practice["second_hint"],
    eighth_block_practice["second_answer"],
    eighth_block_practice["third_hint"],
    eighth_block_practice["third_answer"],
    eighth_block_practice["fourth_hint"],
    eighth_block_practice["fourth_answer"],
    eighth_block_practice["fifth_hint"],
    eighth_block_practice["fifth_answer"],
]

THEOR_NAMES = [
    theor_names["first_theme"],
    theor_names["second_theme"],
    theor_names["third_theme"],
    theor_names["fourth_theme"],
    theor_names["fifth_theme"],
    theor_names["sixth_theme"],
]

PRACT_NAMES = [
    pract_names["first_theme"],
    pract_names["second_theme"],
    pract_names["third_theme"],
    pract_names["fourth_theme"],
    pract_names["fifth_theme"],
    pract_names["sixth_theme"],
    pract_names["seventh_theme"],
    pract_names["eighth_theme"],
]


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
    for i in range(0, 6):
        builder.add(InlineKeyboardButton(text=f"{THEOR_NAMES[i]}", callback_data=f"teory_{i}"))
    builder.adjust(1)  # Располагаем кнопки в один столбец
    await message.answer(
        "Выберите тему для изучения теории:", reply_markup=builder.as_markup()
    )


@dp.callback_query(F.data.startswith("teory_0"))
async def process_first_block_teory_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "Teory" / "FirstTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "Teory" / "FirstTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "Teory" / "FirstTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "Teory" / "FirstTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "Teory" / "FirstTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "Teory" / "FirstTheme" / "6.jpg"
    seventh_image_path = Path(__file__).parent / "Image" / "Teory" / "FirstTheme" / "7.jpg"
    eighth_image_path = Path(__file__).parent / "Image" / "Teory" / "FirstTheme" / "8.jpg"
    nineth_image_path = Path(__file__).parent / "Image" / "Teory" / "FirstTheme" / "9.jpg"
    tenth_image_path = Path(__file__).parent / "Image" / "Teory" / "FirstTheme" / "10.jpg"
    eleventh_image_path = Path(__file__).parent / "Image" / "Teory" / "FirstTheme" / "11.jpg"
    tvelveth_image_path = Path(__file__).parent / "Image" / "Teory" / "FirstTheme" / "12.jpg"
    thirteenth_image_path = Path(__file__).parent / "Image" / "Teory" / "FirstTheme" / "13.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEOR_NAMES[0]}"
    )

    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(FIRST_BLOCK_TEORY[0], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(FIRST_BLOCK_TEORY[1], parse_mode="Markdown")
    await callback.message.answer(FIRST_BLOCK_TEORY[2], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(FIRST_BLOCK_TEORY[3], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(FIRST_BLOCK_TEORY[4], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await callback.message.answer(FIRST_BLOCK_TEORY[5], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await callback.message.answer(FIRST_BLOCK_TEORY[6], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))
    await callback.message.answer(FIRST_BLOCK_TEORY[7], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(nineth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tenth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eleventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tvelveth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(thirteenth_image_path))


@dp.callback_query(F.data.startswith("teory_1"))
async def process_second_block_teory_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "Teory" / "SecondTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "Teory" / "SecondTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "Teory" / "SecondTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "Teory" / "SecondTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "Teory" / "SecondTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "Teory" / "SecondTheme" / "6.jpg"
    seventh_image_path = Path(__file__).parent / "Image" / "Teory" / "SecondTheme" / "7.jpg"
    eighth_image_path = Path(__file__).parent / "Image" / "Teory" / "SecondTheme" / "8.jpg"
    nineth_image_path = Path(__file__).parent / "Image" / "Teory" / "SecondTheme" / "9.jpg"
    tenth_image_path = Path(__file__).parent / "Image" / "Teory" / "SecondTheme" / "10.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEOR_NAMES[1]}"
    )

    # Отправляем изображение
    await callback.message.answer(SECOND_BLOCK_TEORY[0], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(SECOND_BLOCK_TEORY[1], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(SECOND_BLOCK_TEORY[2], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await callback.message.answer(SECOND_BLOCK_TEORY[3], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(SECOND_BLOCK_TEORY[4], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(SECOND_BLOCK_TEORY[5], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await callback.message.answer(SECOND_BLOCK_TEORY[6], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))
    await callback.message.answer(SECOND_BLOCK_TEORY[7], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(nineth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tenth_image_path))


@dp.callback_query(F.data.startswith("teory_2"))
async def process_third_block_teory_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "Teory" / "ThirdTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "Teory" / "ThirdTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "Teory" / "ThirdTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "Teory" / "ThirdTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "Teory" / "ThirdTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "Teory" / "ThirdTheme" / "6.jpg"
    seventh_image_path = Path(__file__).parent / "Image" / "Teory" / "ThirdTheme" / "7.jpg"
    eighth_image_path = Path(__file__).parent / "Image" / "Teory" / "ThirdTheme" / "8.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEOR_NAMES[2]}"
    )

    # Отправляем изображение
    await callback.message.answer(THIRD_BLOCK_TEORY[0], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(THIRD_BLOCK_TEORY[1], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(THIRD_BLOCK_TEORY[2], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))


@dp.callback_query(F.data.startswith("teory_3"))
async def process_fourth_block_teory_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "Teory" / "FourthTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "Teory" / "FourthTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "Teory" / "FourthTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "Teory" / "FourthTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "Teory" / "FourthTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "Teory" / "FourthTheme" / "6.jpg"
    seventh_image_path = Path(__file__).parent / "Image" / "Teory" / "FourthTheme" / "7.jpg"
    eighth_image_path = Path(__file__).parent / "Image" / "Teory" / "FourthTheme" / "8.jpg"
    nineth_image_path = Path(__file__).parent / "Image" / "Teory" / "FourthTheme" / "9.jpg"
    tenth_image_path = Path(__file__).parent / "Image" / "Teory" / "FourthTheme" / "10.jpg"
    eleventh_image_path = Path(__file__).parent / "Image" / "Teory" / "FourthTheme" / "11.jpg"
    tvelveth_image_path = Path(__file__).parent / "Image" / "Teory" / "FourthTheme" / "12.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEOR_NAMES[3]}"
    )

    await callback.message.answer(FOURTH_BLOCK_TEORY[0], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(FOURTH_BLOCK_TEORY[1], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(FOURTH_BLOCK_TEORY[2], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(FOURTH_BLOCK_TEORY[3], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(FOURTH_BLOCK_TEORY[4], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await callback.message.answer(FOURTH_BLOCK_TEORY[5], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))
    await callback.message.answer(FOURTH_BLOCK_TEORY[6], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(nineth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tenth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eleventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tvelveth_image_path))

@dp.callback_query(F.data.startswith("teory_4"))
async def process_fifth_block_teory_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "Teory" / "FifthTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "Teory" / "FifthTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "Teory" / "FifthTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "Teory" / "FifthTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "Teory" / "FifthTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "Teory" / "FifthTheme" / "6.jpg"
    seventh_image_path = Path(__file__).parent / "Image" / "Teory" / "FifthTheme" / "7.jpg"
    eighth_image_path = Path(__file__).parent / "Image" / "Teory" / "FifthTheme" / "8.jpg"
    nineth_image_path = Path(__file__).parent / "Image" / "Teory" / "FifthTheme" / "9.jpg"
    tenth_image_path = Path(__file__).parent / "Image" / "Teory" / "FifthTheme" / "10.jpg"
    eleventh_image_path = Path(__file__).parent / "Image" / "Teory" / "FifthTheme" / "11.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEOR_NAMES[4]}"
    )

    await callback.message.answer(FIFTH_BLOCK_TEORY[0], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(FIFTH_BLOCK_TEORY[1], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(FIFTH_BLOCK_TEORY[2], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(FIFTH_BLOCK_TEORY[3], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(nineth_image_path))
    await callback.message.answer(FIFTH_BLOCK_TEORY[4], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tenth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eleventh_image_path))

@dp.callback_query(F.data.startswith("teory_5"))
async def process_sixth_block_teory_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "Teory" / "SixthTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "Teory" / "SixthTheme" / "2.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEOR_NAMES[5]}"
    )

    await callback.message.answer(SIXTH_BLOCK_TEORY[0], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(SIXTH_BLOCK_TEORY[1], parse_mode="Markdown")
    await callback.message.answer(SIXTH_BLOCK_TEORY[2], parse_mode="Markdown")
    await callback.message.answer(SIXTH_BLOCK_TEORY[3], parse_mode="Markdown")
    await callback.message.answer(SIXTH_BLOCK_TEORY[4], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(SIXTH_BLOCK_TEORY[5], parse_mode="Markdown")


# Обработчик команды /practis
@dp.message(Command("practis"))
async def teory(message: Message):
    builder = InlineKeyboardBuilder()
    for i in range(0, 8):
        builder.add(InlineKeyboardButton(text=f"{PRACT_NAMES[i]}", callback_data=f"practis_{i}"))
    builder.adjust(1)  # Располагаем кнопки в один столбец
    await message.answer(
        "Выберите тему для практики:", reply_markup=builder.as_markup()
    )


# Обработчик выбора темы
@dp.callback_query(F.data == "practis_0")
async def process_practis_callback(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(1, 6):
        builder.add(
            InlineKeyboardButton(
                text=f"Задание {i}", 
                callback_data=f"_task0{i}"
            )
        )
    builder.adjust(1)
    await callback.message.answer(
        f"Вы выбрали практику по теме: \n{PRACT_NAMES[0]}", 
        reply_markup=builder.as_markup()
    )
    await callback.answer()  # Важно!

# Обработчик выбора задания
@dp.callback_query(F.data == "_task01")  # Точное совпадение
async def process_task1_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "FirstTheme" / "1.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_01"),
        InlineKeyboardButton(text="Решение", callback_data="answer_01"),
    )
    await callback.message.answer(
        "Вы выбрали задание 1", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_01")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(FIRST_BLOCK_PRACTICE[0])

@dp.callback_query(F.data == "answer_01")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(FIRST_BLOCK_PRACTICE[1])
    


# Обработчик выбора задания
@dp.callback_query(F.data == "_task02")  # Точное совпадение
async def process_task2_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "FirstTheme" / "2.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_02"),
        InlineKeyboardButton(text="Решение", callback_data="answer_02"),
    )
    await callback.message.answer(
        "Вы выбрали задание 2", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_02")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(FIRST_BLOCK_PRACTICE[2])

@dp.callback_query(F.data == "answer_02")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(FIRST_BLOCK_PRACTICE[3])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task03")  # Точное совпадение
async def process_task1_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "FirstTheme" / "3.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_03"),
        InlineKeyboardButton(text="Решение", callback_data="answer_03"),
    )
    await callback.message.answer(
        "Вы выбрали задание 3", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_03")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(FIRST_BLOCK_PRACTICE[4])

@dp.callback_query(F.data == "answer_03")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(FIRST_BLOCK_PRACTICE[5])

# Обработчик выбора задания
@dp.callback_query(F.data == "_task04")  # Точное совпадение
async def process_task1_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "FirstTheme" / "4.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_04"),
        InlineKeyboardButton(text="Решение", callback_data="answer_04"),
    )
    await callback.message.answer(
        "Вы выбрали задание 4", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_04")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(FIRST_BLOCK_PRACTICE[6])

@dp.callback_query(F.data == "answer_04")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(FIRST_BLOCK_PRACTICE[7])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task05")  # Точное совпадение
async def process_task1_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "FirstTheme" / "5.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_05"),
        InlineKeyboardButton(text="Решение", callback_data="answer_05"),
    )
    await callback.message.answer(
        "Вы выбрали задание 5", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_05")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(FIRST_BLOCK_PRACTICE[8])

@dp.callback_query(F.data == "answer_05")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(FIRST_BLOCK_PRACTICE[9])


# Обработчик выбора темы
@dp.callback_query(F.data == "practis_1")
async def process_practis_callback(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(1, 6):
        builder.add(
            InlineKeyboardButton(
                text=f"Задание {i}", 
                callback_data=f"_task1{i}"
            )
        )
    builder.adjust(1)
    await callback.message.answer(
        f"Вы выбрали практику по теме: \n{PRACT_NAMES[1]}", 
        reply_markup=builder.as_markup()
    )
    await callback.answer()  # Важно!

# Обработчик выбора задания
@dp.callback_query(F.data == "_task11")  # Точное совпадение
async def process_task1_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "SecondTheme" / "1.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_11"),
        InlineKeyboardButton(text="Решение", callback_data="answer_11"),
    )
    await callback.message.answer(
        "Вы выбрали задание 1", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_11")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(SECOND_BLOCK_PRACTICE[0])

@dp.callback_query(F.data == "answer_11")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(SECOND_BLOCK_PRACTICE[1])
    


# Обработчик выбора задания
@dp.callback_query(F.data == "_task12")  # Точное совпадение
async def process_task2_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "SecondTheme" / "2.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_12"),
        InlineKeyboardButton(text="Решение", callback_data="answer_12"),
    )
    await callback.message.answer(
        "Вы выбрали задание 2", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_12")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(SECOND_BLOCK_PRACTICE[2])

@dp.callback_query(F.data == "answer_12")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(SECOND_BLOCK_PRACTICE[3])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task13")  # Точное совпадение
async def process_task1_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "SecondTheme" / "3.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_13"),
        InlineKeyboardButton(text="Решение", callback_data="answer_13"),
    )
    await callback.message.answer(
        "Вы выбрали задание 3", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_13")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(SECOND_BLOCK_PRACTICE[4])

@dp.callback_query(F.data == "answer_13")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(SECOND_BLOCK_PRACTICE[5])

# Обработчик выбора задания
@dp.callback_query(F.data == "_task14")  # Точное совпадение
async def process_task1_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "SecondTheme" / "4.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_14"),
        InlineKeyboardButton(text="Решение", callback_data="answer_14"),
    )
    await callback.message.answer(
        "Вы выбрали задание 4", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_14")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(SECOND_BLOCK_PRACTICE[6])

@dp.callback_query(F.data == "answer_14")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(SECOND_BLOCK_PRACTICE[7])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task15")  # Точное совпадение
async def process_task1_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "SecondTheme" / "5.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_15"),
        InlineKeyboardButton(text="Решение", callback_data="answer_15"),
    )
    await callback.message.answer(
        "Вы выбрали задание 5", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_15")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(SECOND_BLOCK_PRACTICE[8])

@dp.callback_query(F.data == "answer_15")
async def process_task1_callback(callback: CallbackQuery):
    await callback.message.answer(SECOND_BLOCK_PRACTICE[9])


# Обработчик выбора темы
@dp.callback_query(F.data == "practis_2")
async def process_practis_callback(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(1, 6):
        builder.add(
            InlineKeyboardButton(
                text=f"Задание {i}", 
                callback_data=f"_task2{i}"
            )
        )
    builder.adjust(1)
    await callback.message.answer(
        f"Вы выбрали практику по теме: \n{PRACT_NAMES[2]}", 
        reply_markup=builder.as_markup()
    )
    await callback.answer()  # Важно!

# Обработчик выбора задания
@dp.callback_query(F.data == "_task21")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "ThirdTheme" / "1.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_21"),
        InlineKeyboardButton(text="Решение", callback_data="answer_21"),
    )
    await callback.message.answer(
        "Вы выбрали задание 1", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_21")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(THIRD_BLOCK_PRACTICE[0])

@dp.callback_query(F.data == "answer_21")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(THIRD_BLOCK_PRACTICE[1])
    


# Обработчик выбора задания
@dp.callback_query(F.data == "_task22")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "ThirdTheme" / "2.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_22"),
        InlineKeyboardButton(text="Решение", callback_data="answer_22"),
    )
    await callback.message.answer(
        "Вы выбрали задание 2", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_22")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(THIRD_BLOCK_PRACTICE[2])

@dp.callback_query(F.data == "answer_22")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(THIRD_BLOCK_PRACTICE[3])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task23")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "ThirdTheme" / "3.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_23"),
        InlineKeyboardButton(text="Решение", callback_data="answer_23"),
    )
    await callback.message.answer(
        "Вы выбрали задание 3", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_23")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(THIRD_BLOCK_PRACTICE[4])

@dp.callback_query(F.data == "answer_23")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(THIRD_BLOCK_PRACTICE[5])

# Обработчик выбора задания
@dp.callback_query(F.data == "_task24")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "ThirdTheme" / "4.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_24"),
        InlineKeyboardButton(text="Решение", callback_data="answer_24"),
    )
    await callback.message.answer(
        "Вы выбрали задание 4", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_24")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(THIRD_BLOCK_PRACTICE[6])

@dp.callback_query(F.data == "answer_24")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(THIRD_BLOCK_PRACTICE[7])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task25")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "ThirdTheme" / "5.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_25"),
        InlineKeyboardButton(text="Решение", callback_data="answer_25"),
    )
    await callback.message.answer(
        "Вы выбрали задание 5", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_25")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(THIRD_BLOCK_PRACTICE[8])

@dp.callback_query(F.data == "answer_25")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(THIRD_BLOCK_PRACTICE[9])

# Обработчик выбора темы
@dp.callback_query(F.data == "practis_3")
async def process_practis_callback(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(1, 6):
        builder.add(
            InlineKeyboardButton(
                text=f"Задание {i}", 
                callback_data=f"_task3{i}"
            )
        )
    builder.adjust(1)
    await callback.message.answer(
        f"Вы выбрали практику по теме: \n{PRACT_NAMES[3]}", 
        reply_markup=builder.as_markup()
    )
    await callback.answer()  # Важно!

# Обработчик выбора задания
@dp.callback_query(F.data == "_task31")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "FourthTheme" / "1.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_31"),
        InlineKeyboardButton(text="Решение", callback_data="answer_31"),
    )
    await callback.message.answer(
        "Вы выбрали задание 1", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_31")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(FOURTH_BLOCK_PRACTICE[0])

@dp.callback_query(F.data == "answer_31")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(FOURTH_BLOCK_PRACTICE[1])
    


# Обработчик выбора задания
@dp.callback_query(F.data == "_task32")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "FourthTheme" / "2.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_32"),
        InlineKeyboardButton(text="Решение", callback_data="answer_32"),
    )
    await callback.message.answer(
        "Вы выбрали задание 2", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_32")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(FOURTH_BLOCK_PRACTICE[2])

@dp.callback_query(F.data == "answer_32")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(FOURTH_BLOCK_PRACTICE[3])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task33")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "FourthTheme" / "3.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_33"),
        InlineKeyboardButton(text="Решение", callback_data="answer_33"),
    )
    await callback.message.answer(
        "Вы выбрали задание 3", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_33")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(FOURTH_BLOCK_PRACTICE[4])

@dp.callback_query(F.data == "answer_33")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(FOURTH_BLOCK_PRACTICE[5])

# Обработчик выбора задания
@dp.callback_query(F.data == "_task34")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "FourthTheme" / "4.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_34"),
        InlineKeyboardButton(text="Решение", callback_data="answer_34"),
    )
    await callback.message.answer(
        "Вы выбрали задание 4", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_34")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(FOURTH_BLOCK_PRACTICE[6])

@dp.callback_query(F.data == "answer_34")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(FOURTH_BLOCK_PRACTICE[7])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task35")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "FourthTheme" / "5.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_35"),
        InlineKeyboardButton(text="Решение", callback_data="answer_35"),
    )
    await callback.message.answer(
        "Вы выбрали задание 5", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_35")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(FOURTH_BLOCK_PRACTICE[8])

@dp.callback_query(F.data == "answer_35")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(FOURTH_BLOCK_PRACTICE[9])

# Обработчик выбора темы
@dp.callback_query(F.data == "practis_4")
async def process_practis_callback(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(1, 6):
        builder.add(
            InlineKeyboardButton(
                text=f"Задание {i}", 
                callback_data=f"_task4{i}"
            )
        )
    builder.adjust(1)
    await callback.message.answer(
        f"Вы выбрали практику по теме: \n{PRACT_NAMES[4]}", 
        reply_markup=builder.as_markup()
    )
    await callback.answer()  # Важно!

# Обработчик выбора задания
@dp.callback_query(F.data == "_task41")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "FifthTheme" / "1.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_41"),
        InlineKeyboardButton(text="Решение", callback_data="answer_41"),
    )
    await callback.message.answer(
        "Вы выбрали задание 1", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_41")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(FIFTH_BLOCK_PRACTICE[0])

@dp.callback_query(F.data == "answer_41")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(FIFTH_BLOCK_PRACTICE[1])
    


# Обработчик выбора задания
@dp.callback_query(F.data == "_task42")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "FifthTheme" / "2.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_42"),
        InlineKeyboardButton(text="Решение", callback_data="answer_42"),
    )
    await callback.message.answer(
        "Вы выбрали задание 2", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_42")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(FIFTH_BLOCK_PRACTICE[2])

@dp.callback_query(F.data == "answer_42")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(FIFTH_BLOCK_PRACTICE[3])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task43")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "FifthTheme" / "3.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_43"),
        InlineKeyboardButton(text="Решение", callback_data="answer_43"),
    )
    await callback.message.answer(
        "Вы выбрали задание 3", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_43")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(FIFTH_BLOCK_PRACTICE[4])

@dp.callback_query(F.data == "answer_43")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(FIFTH_BLOCK_PRACTICE[5])

# Обработчик выбора задания
@dp.callback_query(F.data == "_task44")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "FifthTheme" / "4.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_44"),
        InlineKeyboardButton(text="Решение", callback_data="answer_44"),
    )
    await callback.message.answer(
        "Вы выбрали задание 4", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_44")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(FIFTH_BLOCK_PRACTICE[6])

@dp.callback_query(F.data == "answer_44")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(FIFTH_BLOCK_PRACTICE[7])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task45")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "FifthTheme" / "5.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_45"),
        InlineKeyboardButton(text="Решение", callback_data="answer_45"),
    )
    await callback.message.answer(
        "Вы выбрали задание 5", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_45")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(FIFTH_BLOCK_PRACTICE[8])

@dp.callback_query(F.data == "answer_45")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(FIFTH_BLOCK_PRACTICE[9])


# Обработчик выбора темы
@dp.callback_query(F.data == "practis_5")
async def process_practis_callback(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(1, 6):
        builder.add(
            InlineKeyboardButton(
                text=f"Задание {i}", 
                callback_data=f"_task5{i}"
            )
        )
    builder.adjust(1)
    await callback.message.answer(
        f"Вы выбрали практику по теме: \n{PRACT_NAMES[5]}", 
        reply_markup=builder.as_markup()
    )
    await callback.answer()  # Важно!

# Обработчик выбора задания
@dp.callback_query(F.data == "_task51")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "SixthTheme" / "1.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_51"),
        InlineKeyboardButton(text="Решение", callback_data="answer_51"),
    )
    await callback.message.answer(
        "Вы выбрали задание 1", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_51")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(SIXTH_BLOCK_PRACTICE[0])

@dp.callback_query(F.data == "answer_51")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(SIXTH_BLOCK_PRACTICE[1])
    


# Обработчик выбора задания
@dp.callback_query(F.data == "_task52")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "SixthTheme" / "2.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_52"),
        InlineKeyboardButton(text="Решение", callback_data="answer_52"),
    )
    await callback.message.answer(
        "Вы выбрали задание 2", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_52")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(SIXTH_BLOCK_PRACTICE[2])

@dp.callback_query(F.data == "answer_52")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(SIXTH_BLOCK_PRACTICE[3])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task53")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "SixthTheme" / "3.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_53"),
        InlineKeyboardButton(text="Решение", callback_data="answer_53"),
    )
    await callback.message.answer(
        "Вы выбрали задание 3", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_53")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(SIXTH_BLOCK_PRACTICE[4])

@dp.callback_query(F.data == "answer_53")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(SIXTH_BLOCK_PRACTICE[5])

# Обработчик выбора задания
@dp.callback_query(F.data == "_task54")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "SixthTheme" / "4.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_54"),
        InlineKeyboardButton(text="Решение", callback_data="answer_54"),
    )
    await callback.message.answer(
        "Вы выбрали задание 4", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_54")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(SIXTH_BLOCK_PRACTICE[6])

@dp.callback_query(F.data == "answer_54")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(SIXTH_BLOCK_PRACTICE[7])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task55")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "SixthTheme" / "5.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_55"),
        InlineKeyboardButton(text="Решение", callback_data="answer_55"),
    )
    await callback.message.answer(
        "Вы выбрали задание 5", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_55")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(SIXTH_BLOCK_PRACTICE[8])

@dp.callback_query(F.data == "answer_55")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(SIXTH_BLOCK_PRACTICE[9])


# Обработчик выбора темы
@dp.callback_query(F.data == "practis_6")
async def process_practis_callback(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(1, 6):
        builder.add(
            InlineKeyboardButton(
                text=f"Задание {i}", 
                callback_data=f"_task6{i}"
            )
        )
    builder.adjust(1)
    await callback.message.answer(
        f"Вы выбрали практику по теме: \n{PRACT_NAMES[6]}", 
        reply_markup=builder.as_markup()
    )
    await callback.answer()  # Важно!

# Обработчик выбора задания
@dp.callback_query(F.data == "_task61")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "SeventhTheme" / "1.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_61"),
        InlineKeyboardButton(text="Решение", callback_data="answer_61"),
    )
    await callback.message.answer(
        "Вы выбрали задание 1", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_61")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(SEVENTH_BLOCK_PRACTICE[0])

@dp.callback_query(F.data == "answer_61")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(SEVENTH_BLOCK_PRACTICE[1])
    


# Обработчик выбора задания
@dp.callback_query(F.data == "_task62")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "SeventhTheme" / "2.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_62"),
        InlineKeyboardButton(text="Решение", callback_data="answer_62"),
    )
    await callback.message.answer(
        "Вы выбрали задание 2", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_62")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(SEVENTH_BLOCK_PRACTICE[2])

@dp.callback_query(F.data == "answer_62")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(SEVENTH_BLOCK_PRACTICE[3])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task63")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "SeventhTheme" / "3.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_63"),
        InlineKeyboardButton(text="Решение", callback_data="answer_63"),
    )
    await callback.message.answer(
        "Вы выбрали задание 3", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_63")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(SEVENTH_BLOCK_PRACTICE[4])

@dp.callback_query(F.data == "answer_63")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(SEVENTH_BLOCK_PRACTICE[5])

# Обработчик выбора задания
@dp.callback_query(F.data == "_task64")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "SeventhTheme" / "4.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_64"),
        InlineKeyboardButton(text="Решение", callback_data="answer_64"),
    )
    await callback.message.answer(
        "Вы выбрали задание 4", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_64")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(SEVENTH_BLOCK_PRACTICE[6])

@dp.callback_query(F.data == "answer_64")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(SEVENTH_BLOCK_PRACTICE[7])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task65")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "SeventhTheme" / "5.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_65"),
        InlineKeyboardButton(text="Решение", callback_data="answer_65"),
    )
    await callback.message.answer(
        "Вы выбрали задание 5", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_65")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(SEVENTH_BLOCK_PRACTICE[8])

@dp.callback_query(F.data == "answer_65")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(SEVENTH_BLOCK_PRACTICE[9])

# Обработчик выбора темы
@dp.callback_query(F.data == "practis_7")
async def process_practis_callback(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(1, 6):
        builder.add(
            InlineKeyboardButton(
                text=f"Задание {i}", 
                callback_data=f"_task7{i}"
            )
        )
    builder.adjust(1)
    await callback.message.answer(
        f"Вы выбрали практику по теме: \n{PRACT_NAMES[7]}", 
        reply_markup=builder.as_markup()
    )
    await callback.answer()  # Важно!

# Обработчик выбора задания
@dp.callback_query(F.data == "_task71")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "EighthTheme" / "1.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_71"),
        InlineKeyboardButton(text="Решение", callback_data="answer_71"),
    )
    await callback.message.answer(
        "Вы выбрали задание 1", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_71")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(EIGHTH_BLOCK_PRACTICE[0])

@dp.callback_query(F.data == "answer_71")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(EIGHTH_BLOCK_PRACTICE[1])
    


# Обработчик выбора задания
@dp.callback_query(F.data == "_task72")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "EighthTheme" / "2.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_72"),
        InlineKeyboardButton(text="Решение", callback_data="answer_72"),
    )
    await callback.message.answer(
        "Вы выбрали задание 2", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_72")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(EIGHTH_BLOCK_PRACTICE[2])

@dp.callback_query(F.data == "answer_72")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(EIGHTH_BLOCK_PRACTICE[3])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task73")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "EighthTheme" / "3.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_73"),
        InlineKeyboardButton(text="Решение", callback_data="answer_73"),
    )
    await callback.message.answer(
        "Вы выбрали задание 3", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_73")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(EIGHTH_BLOCK_PRACTICE[4])

@dp.callback_query(F.data == "answer_73")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(EIGHTH_BLOCK_PRACTICE[5])

# Обработчик выбора задания
@dp.callback_query(F.data == "_task74")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "EighthTheme" / "4.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_74"),
        InlineKeyboardButton(text="Решение", callback_data="answer_74"),
    )
    await callback.message.answer(
        "Вы выбрали задание 4", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_74")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(EIGHTH_BLOCK_PRACTICE[6])

@dp.callback_query(F.data == "answer_74")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(EIGHTH_BLOCK_PRACTICE[7])


# Обработчик выбора задания
@dp.callback_query(F.data == "_task75")  # Точное совпадение
async def process_task_callback(callback: CallbackQuery):
    task = Path(__file__).parent / "Image" / "Practices" / "EighthTheme" / "5.jpg"
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Подсказка", callback_data="hint_75"),
        InlineKeyboardButton(text="Решение", callback_data="answer_75"),
    )
    await callback.message.answer(
        "Вы выбрали задание 5", 
    )
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task), reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "hint_75")
async def process_hint_callback(callback: CallbackQuery):
    await callback.message.answer(EIGHTH_BLOCK_PRACTICE[8])

@dp.callback_query(F.data == "answer_75")
async def process_answer_callback(callback: CallbackQuery):
    await callback.message.answer(EIGHTH_BLOCK_PRACTICE[9])

# Запуск бота
if __name__ == "__main__":
    asyncio.run(dp.run_polling(bot))
