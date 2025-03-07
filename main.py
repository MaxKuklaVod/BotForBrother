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
    Path(__file__).parent / "Json" / "Teory" / "firstblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    first_block_teory = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Teory" / "secondblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    second_block_teory = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Teory" / "thirdblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    third_block_teory = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Teory" / "fourthblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    fourth_block_teory = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Teory" / "fifthblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    fifth_block_teory = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "Teory" / "sixthblock.json", encoding="utf-8"
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
    Path(__file__).parent / "Json" / "themes_names.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    themes_names = json.loads(data)

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
    second_block_practice["first"],
    second_block_practice["second"],
    second_block_practice["third"],
    second_block_practice["fourth"],
    second_block_practice["fifth"],
    second_block_practice["sixth"],
    second_block_practice["seventh"],
    second_block_practice["eighth"],
]

THIRD_BLOCK_PRACTICE = [
    third_block_practice["first"],
    third_block_practice["second"],
    third_block_practice["third"],
]

FOURTH_BLOCK_PRACTICE = [
    fourth_block_practice["first"],
    fourth_block_practice["second"],
    fourth_block_practice["third"],
    fourth_block_practice["fourth"],
    fourth_block_practice["fifth"],
    fourth_block_practice["sixth"],
    fourth_block_practice["seventh"],
]

FIFTH_BLOCK_PRACTICE = [
    fifth_block_practice["first"],
    fifth_block_practice["second"],
    fifth_block_practice["third"],
    fifth_block_practice["fourth"],
    fifth_block_practice["fifth"],
]

SIXTH_BLOCK_PRACTICE = [
    sixth_block_practice["first"],
    sixth_block_practice["second"],
    sixth_block_practice["third"],
    sixth_block_practice["fourth"],
    sixth_block_practice["fifth"],
    sixth_block_practice["sixth"],
]

THEMES_NAMES = [
    themes_names["first_theme"],
    themes_names["second_theme"],
    themes_names["third_theme"],
    themes_names["fourth_theme"],
    themes_names["fifth_theme"],
    themes_names["sixth_theme"],
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
        builder.add(InlineKeyboardButton(text=f"{THEMES_NAMES[i]}", callback_data=f"teory_{i}"))
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
        f"Вы выбрали теорию по теме: \n{THEMES_NAMES[0]}"
    )

    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(FIRST_BLOCK_TEORY[0])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(FIRST_BLOCK_TEORY[1])
    await callback.message.answer(FIRST_BLOCK_TEORY[2])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(FIRST_BLOCK_TEORY[3])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(FIRST_BLOCK_TEORY[4])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await callback.message.answer(FIRST_BLOCK_TEORY[5])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await callback.message.answer(FIRST_BLOCK_TEORY[6])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))
    await callback.message.answer(FIRST_BLOCK_TEORY[7])
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
        f"Вы выбрали теорию по теме: \n{THEMES_NAMES[1]}"
    )

    # Отправляем изображение
    await callback.message.answer(SECOND_BLOCK_TEORY[0])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(SECOND_BLOCK_TEORY[1])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(SECOND_BLOCK_TEORY[2])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await callback.message.answer(SECOND_BLOCK_TEORY[3])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(SECOND_BLOCK_TEORY[4])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(SECOND_BLOCK_TEORY[5])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await callback.message.answer(SECOND_BLOCK_TEORY[6])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))
    await callback.message.answer(SECOND_BLOCK_TEORY[7])
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
        f"Вы выбрали теорию по теме: \n{THEMES_NAMES[2]}"
    )

    # Отправляем изображение
    await callback.message.answer(THIRD_BLOCK_TEORY[0])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(THIRD_BLOCK_TEORY[1])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(THIRD_BLOCK_TEORY[2])
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
        f"Вы выбрали теорию по теме: \n{THEMES_NAMES[3]}"
    )

    await callback.message.answer(FOURTH_BLOCK_TEORY[0])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(FOURTH_BLOCK_TEORY[1])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(FOURTH_BLOCK_TEORY[2])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(FOURTH_BLOCK_TEORY[3])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(FOURTH_BLOCK_TEORY[4])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await callback.message.answer(FOURTH_BLOCK_TEORY[5])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))
    await callback.message.answer(FOURTH_BLOCK_TEORY[6])
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
        f"Вы выбрали теорию по теме: \n{THEMES_NAMES[4]}"
    )

    await callback.message.answer(FIFTH_BLOCK_TEORY[0])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(FIFTH_BLOCK_TEORY[1])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(FIFTH_BLOCK_TEORY[2])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(FIFTH_BLOCK_TEORY[3])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(nineth_image_path))
    await callback.message.answer(FIFTH_BLOCK_TEORY[4])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tenth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eleventh_image_path))

@dp.callback_query(F.data.startswith("teory_5"))
async def process_sixth_block_teory_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "Teory" / "SixthTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "Teory" / "SixthTheme" / "2.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEMES_NAMES[5]}"
    )

    await callback.message.answer(SIXTH_BLOCK_TEORY[0])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(SIXTH_BLOCK_TEORY[1])
    await callback.message.answer(SIXTH_BLOCK_TEORY[2])
    await callback.message.answer(SIXTH_BLOCK_TEORY[3])
    await callback.message.answer(SIXTH_BLOCK_TEORY[4])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(SIXTH_BLOCK_TEORY[5])


# Обработчик команды /practis
@dp.message(Command("practis"))
async def teory(message: Message):
    builder = InlineKeyboardBuilder()
    for i in range(0, 6):
        builder.add(InlineKeyboardButton(text=f"{THEMES_NAMES[i]}", callback_data=f"practis_{i}"))
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
        f"Вы выбрали практику по теме: \n{THEMES_NAMES[0]}", 
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


# Запуск бота
if __name__ == "__main__":
    asyncio.run(dp.run_polling(bot))
