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
    Path(__file__).parent / "Json" / "firstblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    first_block = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "secondblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    second_block = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "thirdblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    third_block = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "fourthblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    fourth_block = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "fifthblock.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    fifth_block = json.loads(data)

with open(
    Path(__file__).parent / "Json" / "themes_names.json", encoding="utf-8"
) as complex_data:
    data = complex_data.read()
    themes_names = json.loads(data)

FIRST_BLOCK = [
    first_block["first"],
    first_block["second"],
    first_block["third"],
    first_block["fourth"],
    first_block["fifth"],
    first_block["sixth"],
    first_block["seventh"],
    first_block["eighth"],
]

SECOND_BLOCK = [
    second_block["first"],
    second_block["second"],
    second_block["third"],
    second_block["fourth"],
    second_block["fifth"],
    second_block["sixth"],
    second_block["seventh"],
    second_block["eighth"],
]

THIRD_BLOCK = [
    third_block["first"],
    third_block["second"],
    third_block["third"],
]

FOURTH_BLOCK = [
    fourth_block["first"],
    fourth_block["second"],
    fourth_block["third"],
    fourth_block["fourth"],
    fourth_block["fifth"],
    fourth_block["sixth"],
    fourth_block["seventh"],
]

FIFTH_BLOCK = [
    fifth_block["first"],
    fifth_block["second"],
    fifth_block["third"],
    fifth_block["fourth"],
    fifth_block["fifth"],
]

THEMES_NAMES = [
    themes_names["first_theme"],
    themes_names["second_theme"],
    themes_names["third_theme"],
    themes_names["fourth_theme"],
    themes_names["fifth_theme"],
    themes_names["sixth_theme"],
    themes_names["seventh_theme"],
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
    for i in range(0, 7):
        builder.add(InlineKeyboardButton(text=f"{THEMES_NAMES[i]}", callback_data=f"teory_{i}"))
    builder.adjust(1)  # Располагаем кнопки в один столбец
    await message.answer(
        "Выберите тему для изучения теории:", reply_markup=builder.as_markup()
    )


@dp.callback_query(F.data.startswith("teory_0"))
async def process_first_block_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "FirstTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "FirstTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "FirstTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "FirstTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "FirstTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "FirstTheme" / "6.jpg"
    seventh_image_path = Path(__file__).parent / "Image" / "FirstTheme" / "7.jpg"
    eighth_image_path = Path(__file__).parent / "Image" / "FirstTheme" / "8.jpg"
    nineth_image_path = Path(__file__).parent / "Image" / "FirstTheme" / "9.jpg"
    tenth_image_path = Path(__file__).parent / "Image" / "FirstTheme" / "10.jpg"
    eleventh_image_path = Path(__file__).parent / "Image" / "FirstTheme" / "11.jpg"
    tvelveth_image_path = Path(__file__).parent / "Image" / "FirstTheme" / "12.jpg"
    thirteenth_image_path = Path(__file__).parent / "Image" / "FirstTheme" / "13.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEMES_NAMES[0]}"
    )

    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(FIRST_BLOCK[0])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(FIRST_BLOCK[1])
    await callback.message.answer(FIRST_BLOCK[2])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(FIRST_BLOCK[3])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(FIRST_BLOCK[4])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await callback.message.answer(FIRST_BLOCK[5])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await callback.message.answer(FIRST_BLOCK[6])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))
    await callback.message.answer(FIRST_BLOCK[7])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(nineth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tenth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eleventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tvelveth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(thirteenth_image_path))


@dp.callback_query(F.data.startswith("teory_1"))
async def process_first_block_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "SecondTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "SecondTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "SecondTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "SecondTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "SecondTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "SecondTheme" / "6.jpg"
    seventh_image_path = Path(__file__).parent / "Image" / "SecondTheme" / "7.jpg"
    eighth_image_path = Path(__file__).parent / "Image" / "SecondTheme" / "8.jpg"
    nineth_image_path = Path(__file__).parent / "Image" / "SecondTheme" / "9.jpg"
    tenth_image_path = Path(__file__).parent / "Image" / "SecondTheme" / "10.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEMES_NAMES[1]}"
    )

    # Отправляем изображение
    await callback.message.answer(SECOND_BLOCK[0])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(SECOND_BLOCK[1])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(SECOND_BLOCK[2])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await callback.message.answer(SECOND_BLOCK[3])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(SECOND_BLOCK[4])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(SECOND_BLOCK[5])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await callback.message.answer(SECOND_BLOCK[6])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))
    await callback.message.answer(SECOND_BLOCK[7])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(nineth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tenth_image_path))


@dp.callback_query(F.data.startswith("teory_2"))
async def process_first_block_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "ThirdTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "ThirdTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "ThirdTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "ThirdTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "ThirdTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "ThirdTheme" / "6.jpg"
    seventh_image_path = Path(__file__).parent / "Image" / "ThirdTheme" / "7.jpg"
    eighth_image_path = Path(__file__).parent / "Image" / "ThirdTheme" / "8.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEMES_NAMES[2]}"
    )

    # Отправляем изображение
    await callback.message.answer(THIRD_BLOCK[0])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(THIRD_BLOCK[1])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(THIRD_BLOCK[2])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))


@dp.callback_query(F.data.startswith("teory_3"))
async def process_first_block_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "FourthTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "FourthTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "FourthTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "FourthTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "FourthTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "FourthTheme" / "6.jpg"
    seventh_image_path = Path(__file__).parent / "Image" / "FourthTheme" / "7.jpg"
    eighth_image_path = Path(__file__).parent / "Image" / "FourthTheme" / "8.jpg"
    nineth_image_path = Path(__file__).parent / "Image" / "FourthTheme" / "9.jpg"
    tenth_image_path = Path(__file__).parent / "Image" / "FourthTheme" / "10.jpg"
    eleventh_image_path = Path(__file__).parent / "Image" / "FourthTheme" / "11.jpg"
    tvelveth_image_path = Path(__file__).parent / "Image" / "FourthTheme" / "12.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEMES_NAMES[3]}"
    )

    await callback.message.answer(FOURTH_BLOCK[0])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(FOURTH_BLOCK[1])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(FOURTH_BLOCK[2])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(FOURTH_BLOCK[3])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(FOURTH_BLOCK[4])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await callback.message.answer(FOURTH_BLOCK[5])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))
    await callback.message.answer(FOURTH_BLOCK[6])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(nineth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tenth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eleventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tvelveth_image_path))

@dp.callback_query(F.data.startswith("teory_4"))
async def process_first_block_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "FifthTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "FifthTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "FifthTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "FifthTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "FifthTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "FifthTheme" / "6.jpg"
    seventh_image_path = Path(__file__).parent / "Image" / "FifthTheme" / "7.jpg"
    eighth_image_path = Path(__file__).parent / "Image" / "FifthTheme" / "8.jpg"
    nineth_image_path = Path(__file__).parent / "Image" / "FifthTheme" / "9.jpg"
    tenth_image_path = Path(__file__).parent / "Image" / "FifthTheme" / "10.jpg"
    eleventh_image_path = Path(__file__).parent / "Image" / "FifthTheme" / "11.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEMES_NAMES[4]}"
    )

    await callback.message.answer(FOURTH_BLOCK[0])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(FOURTH_BLOCK[1])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(FOURTH_BLOCK[2])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(FOURTH_BLOCK[3])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(nineth_image_path))
    await callback.message.answer(FOURTH_BLOCK[4])
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tenth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eleventh_image_path))


# Обработчик команды /practis
@dp.message(Command("practis"))
async def practis(message: Message):
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):  # Создаем 7 кнопок
        builder.add(
            InlineKeyboardButton(text=f"Практика {i}", callback_data=f"practis_{i}")
        )
    builder.adjust(1)  # Располагаем кнопки в один столбец
    await message.answer(
        "Выберите тему для практики:", reply_markup=builder.as_markup()
    )


# Обработчик нажатий на inline кнопки
@dp.callback_query(F.data.startswith("practis_"))
async def process_practis_callback(callback: CallbackQuery):
    topic_number = callback.data.split("_")[1]
    builder = InlineKeyboardBuilder()
    for i in range(1, 4):  # Создаем 3 дополнительные кнопки
        builder.add(
            InlineKeyboardButton(
                text=f"Задание {i}", callback_data=f"{callback.data}_task{i}"
            )
        )
    builder.adjust(1)  # Располагаем кнопки в один столбец
    await callback.message.edit_text(
        f"Вы выбрали Практику {topic_number}. Выберите задание:",
        reply_markup=builder.as_markup(),
    )
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
if __name__ == "__main__":
    asyncio.run(dp.run_polling(bot))
