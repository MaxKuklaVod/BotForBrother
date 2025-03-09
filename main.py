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

# Функция для загрузки JSON файлов
def load_json(file_path):
    with open(file_path, encoding="utf-8") as f:
        return json.loads(f.read())

# Загрузка файлов теории
theory_blocks = {}
for name in ["first", "second", "third", "fourth", "fifth", "sixth"]:
    file_path = Path(__file__).parent / "Json" / "Theory" / f"{name}block.json"
    theory_blocks[name] = load_json(file_path)

# Загрузка файлов практики
practice_blocks = {}
for name in ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth"]:
    file_path = Path(__file__).parent / "Json" / "Practices" / f"{name}block.json"
    practice_blocks[name] = load_json(file_path)

# Загрузка названий тем
theor_names = load_json(Path(__file__).parent / "Json" / "Themes" / "theor_names.json")
pract_names = load_json(Path(__file__).parent / "Json" / "Themes" / "pract_names.json")

# Формирование блоков теории
FIRST_BLOCK_THEORY = [theory_blocks["first"][key] for key in ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth"]]
SECOND_BLOCK_THEORY = [theory_blocks["second"][key] for key in ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth"]]
THIRD_BLOCK_THEORY = [theory_blocks["third"][key] for key in ["first", "second", "third"]]
FOURTH_BLOCK_THEORY = [theory_blocks["fourth"][key] for key in ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]]
FIFTH_BLOCK_THEORY = [theory_blocks["fifth"][key] for key in ["first", "second", "third", "fourth", "fifth"]]
SIXTH_BLOCK_THEORY = [theory_blocks["sixth"][key] for key in ["first", "second", "third", "fourth", "fifth", "sixth"]]

# Формирование блоков практики
practice_keys = ["first_hint", "first_answer", "second_hint", "second_answer", "third_hint", 
                "third_answer", "fourth_hint", "fourth_answer", "fifth_hint", "fifth_answer"]

FIRST_BLOCK_PRACTICE = [practice_blocks["first"][key] for key in practice_keys]
SECOND_BLOCK_PRACTICE = [practice_blocks["second"][key] for key in practice_keys]
THIRD_BLOCK_PRACTICE = [practice_blocks["third"][key] for key in practice_keys]
FOURTH_BLOCK_PRACTICE = [practice_blocks["fourth"][key] for key in practice_keys]
FIFTH_BLOCK_PRACTICE = [practice_blocks["fifth"][key] for key in practice_keys]
SIXTH_BLOCK_PRACTICE = [practice_blocks["sixth"][key] for key in practice_keys]
SEVENTH_BLOCK_PRACTICE = [practice_blocks["seventh"][key] for key in practice_keys]
EIGHTH_BLOCK_PRACTICE = [practice_blocks["eighth"][key] for key in practice_keys]

PRACTICE_BLOCKS = [
    FIRST_BLOCK_PRACTICE,
    SECOND_BLOCK_PRACTICE,
    THIRD_BLOCK_PRACTICE,
    FOURTH_BLOCK_PRACTICE,
    FIFTH_BLOCK_PRACTICE,
    SIXTH_BLOCK_PRACTICE,
    SEVENTH_BLOCK_PRACTICE,
    EIGHTH_BLOCK_PRACTICE
]

# Формирование списков с названиями тем
THEOR_NAMES = [theor_names[f"{key}_theme"] for key in ["first", "second", "third", "fourth", "fifth", "sixth"]]
PRACT_NAMES = [pract_names[f"{key}_theme"] for key in ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth"]]

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
        "/theory - Теоретическая часть\n"
        "/practice - Практическая часть"
    )

# Обработчик команды /theory
@dp.message(Command("theory"))
async def theory(message: Message):
    builder = InlineKeyboardBuilder()
    for i in range(0, 6):
        builder.add(InlineKeyboardButton(text=f"{THEOR_NAMES[i]}", callback_data=f"theory_{i}"))
    builder.adjust(1)  # Располагаем кнопки в один столбец
    await message.answer(
        "Выберите тему для изучения теории:", reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data.startswith("theory_0"))
async def process_first_block_theory_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "Theory" / "FirstTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "Theory" / "FirstTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "Theory" / "FirstTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "Theory" / "FirstTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "Theory" / "FirstTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "Theory" / "FirstTheme" / "6.jpg"
    seventh_image_path = Path(__file__).parent / "Image" / "Theory" / "FirstTheme" / "7.jpg"
    eighth_image_path = Path(__file__).parent / "Image" / "Theory" / "FirstTheme" / "8.jpg"
    nineth_image_path = Path(__file__).parent / "Image" / "Theory" / "FirstTheme" / "9.jpg"
    tenth_image_path = Path(__file__).parent / "Image" / "Theory" / "FirstTheme" / "10.jpg"
    eleventh_image_path = Path(__file__).parent / "Image" / "Theory" / "FirstTheme" / "11.jpg"
    twelveth_image_path = Path(__file__).parent / "Image" / "Theory" / "FirstTheme" / "12.jpg"
    thirteenth_image_path = Path(__file__).parent / "Image" / "Theory" / "FirstTheme" / "13.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEOR_NAMES[0]}"
    )

    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(FIRST_BLOCK_THEORY[0], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(FIRST_BLOCK_THEORY[1], parse_mode="Markdown")
    await callback.message.answer(FIRST_BLOCK_THEORY[2], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(FIRST_BLOCK_THEORY[3], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(FIRST_BLOCK_THEORY[4], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await callback.message.answer(FIRST_BLOCK_THEORY[5], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await callback.message.answer(FIRST_BLOCK_THEORY[6], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))
    await callback.message.answer(FIRST_BLOCK_THEORY[7], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(nineth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tenth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eleventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(twelveth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(thirteenth_image_path))

    # Добавляем кнопку для перехода к выбору темы
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Вернуться к выбору темы", callback_data="back_to_theory"))
    await callback.message.answer("Конец темы", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("theory_1"))
async def process_second_block_theory_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "Theory" / "SecondTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "Theory" / "SecondTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "Theory" / "SecondTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "Theory" / "SecondTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "Theory" / "SecondTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "Theory" / "SecondTheme" / "6.jpg"
    seventh_image_path = Path(__file__).parent / "Image" / "Theory" / "SecondTheme" / "7.jpg"
    eighth_image_path = Path(__file__).parent / "Image" / "Theory" / "SecondTheme" / "8.jpg"
    nineth_image_path = Path(__file__).parent / "Image" / "Theory" / "SecondTheme" / "9.jpg"
    tenth_image_path = Path(__file__).parent / "Image" / "Theory" / "SecondTheme" / "10.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEOR_NAMES[1]}"
    )

    # Отправляем текст и изображения в правильной последовательности
    await callback.message.answer(SECOND_BLOCK_THEORY[0], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(SECOND_BLOCK_THEORY[1], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(SECOND_BLOCK_THEORY[2], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await callback.message.answer(SECOND_BLOCK_THEORY[3], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(SECOND_BLOCK_THEORY[4], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(SECOND_BLOCK_THEORY[5], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await callback.message.answer(SECOND_BLOCK_THEORY[6], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))
    await callback.message.answer(SECOND_BLOCK_THEORY[7], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(nineth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tenth_image_path))

    # Добавляем кнопку для перехода к выбору темы
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Вернуться к выбору темы", callback_data="back_to_theory"))
    await callback.message.answer("Конец темы", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("theory_2"))
async def process_third_block_theory_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "Theory" / "ThirdTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "Theory" / "ThirdTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "Theory" / "ThirdTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "Theory" / "ThirdTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "Theory" / "ThirdTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "Theory" / "ThirdTheme" / "6.jpg"
    seventh_image_path = Path(__file__).parent / "Image" / "Theory" / "ThirdTheme" / "7.jpg"
    eighth_image_path = Path(__file__).parent / "Image" / "Theory" / "ThirdTheme" / "8.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEOR_NAMES[2]}"
    )

    # Отправляем текст и изображения в правильной последовательности
    await callback.message.answer(THIRD_BLOCK_THEORY[0], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(THIRD_BLOCK_THEORY[1], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(THIRD_BLOCK_THEORY[2], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))

    # Добавляем кнопку для перехода к выбору темы
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Вернуться к выбору темы", callback_data="back_to_theory"))
    await callback.message.answer("Конец темы", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("theory_3"))
async def process_fourth_block_theory_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "Theory" / "FourthTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "Theory" / "FourthTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "Theory" / "FourthTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "Theory" / "FourthTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "Theory" / "FourthTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "Theory" / "FourthTheme" / "6.jpg"
    seventh_image_path = Path(__file__).parent / "Image" / "Theory" / "FourthTheme" / "7.jpg"
    eighth_image_path = Path(__file__).parent / "Image" / "Theory" / "FourthTheme" / "8.jpg"
    nineth_image_path = Path(__file__).parent / "Image" / "Theory" / "FourthTheme" / "9.jpg"
    tenth_image_path = Path(__file__).parent / "Image" / "Theory" / "FourthTheme" / "10.jpg"
    eleventh_image_path = Path(__file__).parent / "Image" / "Theory" / "FourthTheme" / "11.jpg"
    twelveth_image_path = Path(__file__).parent / "Image" / "Theory" / "FourthTheme" / "12.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEOR_NAMES[3]}"
    )

    await callback.message.answer(FOURTH_BLOCK_THEORY[0], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(FOURTH_BLOCK_THEORY[1], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(FOURTH_BLOCK_THEORY[2], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(FOURTH_BLOCK_THEORY[3], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(FOURTH_BLOCK_THEORY[4], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await callback.message.answer(FOURTH_BLOCK_THEORY[5], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eighth_image_path))
    await callback.message.answer(FOURTH_BLOCK_THEORY[6], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(nineth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(tenth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(eleventh_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(twelveth_image_path))

    # Добавляем кнопку для перехода к выбору темы
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Вернуться к выбору темы", callback_data="back_to_theory"))
    await callback.message.answer("Конец темы", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("theory_4"))
async def process_fifth_block_theory_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "Theory" / "FifthTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "Theory" / "FifthTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "Theory" / "FifthTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "Theory" / "FifthTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "Theory" / "FifthTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "Theory" / "FifthTheme" / "6.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEOR_NAMES[4]}"
    )

    await callback.message.answer(FIFTH_BLOCK_THEORY[0], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(FIFTH_BLOCK_THEORY[1], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(FIFTH_BLOCK_THEORY[2], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await callback.message.answer(FIFTH_BLOCK_THEORY[3], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(FIFTH_BLOCK_THEORY[4], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))

    # Добавляем кнопку для перехода к выбору темы
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Вернуться к выбору темы", callback_data="back_to_theory"))
    await callback.message.answer("Конец темы", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("theory_5"))
async def process_sixth_block_theory_callback(callback: CallbackQuery):
    # Путь к локальному изображению
    first_image_path = Path(__file__).parent / "Image" / "Theory" / "SixthTheme" / "1.jpg"
    second_image_path = Path(__file__).parent / "Image" / "Theory" / "SixthTheme" / "2.jpg"
    third_image_path = Path(__file__).parent / "Image" / "Theory" / "SixthTheme" / "3.jpg"
    fourth_image_path = Path(__file__).parent / "Image" / "Theory" / "SixthTheme" / "4.jpg"
    fifth_image_path = Path(__file__).parent / "Image" / "Theory" / "SixthTheme" / "5.jpg"
    sixth_image_path = Path(__file__).parent / "Image" / "Theory" / "SixthTheme" / "6.jpg"
    seventh_image_path = Path(__file__).parent / "Image" / "Theory" / "SixthTheme" / "7.jpg"

    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{THEOR_NAMES[5]}"
    )

    await callback.message.answer(SIXTH_BLOCK_THEORY[0], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(first_image_path))
    await callback.message.answer(SIXTH_BLOCK_THEORY[1], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(second_image_path))
    await callback.message.answer(SIXTH_BLOCK_THEORY[2], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(third_image_path))
    await callback.message.answer(SIXTH_BLOCK_THEORY[3], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fourth_image_path))
    await callback.message.answer(SIXTH_BLOCK_THEORY[4], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(fifth_image_path))
    await callback.message.answer(SIXTH_BLOCK_THEORY[5], parse_mode="Markdown")
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(sixth_image_path))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(seventh_image_path))

    # Добавляем кнопку для перехода к выбору темы
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Вернуться к выбору темы", callback_data="back_to_theory"))
    await callback.message.answer("Конец темы", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("back_to_theory"))
async def process_back_to_theory_callback(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(0, 6):
        builder.add(InlineKeyboardButton(text=f"{THEOR_NAMES[i]}", callback_data=f"theory_{i}"))
    builder.adjust(1)
    await callback.message.answer(
        "Выберите тему для изучения теории:", reply_markup=builder.as_markup()
    )

# Обработчик команды /practice
@dp.message(Command("practice"))
async def practice(message: Message):
    builder = InlineKeyboardBuilder()
    for i in range(0, 8):
        builder.add(InlineKeyboardButton(text=f"{PRACT_NAMES[i]}", callback_data=f"practice_{i}"))
    builder.adjust(1)  # Располагаем кнопки в один столбец
    await message.answer(
        "Выберите тему для практики:", reply_markup=builder.as_markup()
    )

# Функция для создания обработчиков выбора темы практики
def register_practice_theme_handlers():
    # Обработчики выбора темы практики
    for theme_idx in range(8):
        @dp.callback_query(F.data == f"practice_{theme_idx}")
        async def process_practice_theme_callback(callback: CallbackQuery, theme=theme_idx):
            builder = InlineKeyboardBuilder()
            for i in range(1, 6):
                builder.add(
                    InlineKeyboardButton(
                        text=f"Задание {i}", 
                        callback_data=f"_task{theme}{i}"
                    )
                )
            builder.adjust(1)
            await callback.message.answer(
                f"Вы выбрали практику по теме: \n{PRACT_NAMES[theme]}", 
                reply_markup=builder.as_markup()
            )
            await callback.answer()

# Функция для создания обработчиков выбора задания
def register_practice_task_handlers():
    # Создаем обработчики для всех тем и заданий
    for theme_idx in range(8):
        for task_idx in range(1, 6):
            task_code = f"{theme_idx}{task_idx}"
            
            # Обработчик выбора задания
            @dp.callback_query(F.data == f"_task{task_code}")
            async def process_task_callback(callback: CallbackQuery, theme=theme_idx, task=task_idx, code=task_code):
                # Путь к изображению задания
                task_image_path = Path(__file__).parent / "Image" / "Practices" / f"{get_theme_folder(theme)}" / f"{task}.jpg"
                builder = InlineKeyboardBuilder()
                builder.add(
                    InlineKeyboardButton(text="Подсказка", callback_data=f"hint_{code}"),
                    InlineKeyboardButton(text="Решение", callback_data=f"answer_{code}"),
                )
                await callback.message.answer(f"Вы выбрали задание {task}")
                await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(task_image_path), reply_markup=builder.as_markup())
                await callback.answer()
            
            # Обработчик показа подсказки
            @dp.callback_query(F.data == f"hint_{task_code}")
            async def process_hint_callback(callback: CallbackQuery, theme=theme_idx, task=task_idx):
                hint_index = (task - 1) * 2  # Индекс подсказки в массиве
                await callback.message.answer(PRACTICE_BLOCKS[theme][hint_index])
                await callback.answer()
            
            # Обработчик показа решения
            @dp.callback_query(F.data == f"answer_{task_code}")
            async def process_answer_callback(callback: CallbackQuery, theme=theme_idx, task=task_idx):
                answer_index = (task - 1) * 2 + 1  # Индекс ответа в массиве
                await callback.message.answer(PRACTICE_BLOCKS[theme][answer_index])
                await callback.answer()

# Вспомогательная функция для определения папки темы
def get_theme_folder(theme_idx):
    themes = ["FirstTheme", "SecondTheme", "ThirdTheme", "FourthTheme", 
              "FifthTheme", "SixthTheme", "SeventhTheme", "EighthTheme"]
    return themes[theme_idx]

# Регистрируем все обработчики практических заданий
register_practice_theme_handlers()
register_practice_task_handlers()

# Обработчик для возврата к выбору темы практики
@dp.callback_query(F.data == "back_to_practice")
async def process_back_to_practice_callback(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i in range(0, 8):
        builder.add(InlineKeyboardButton(text=f"{PRACT_NAMES[i]}", callback_data=f"practice_{i}"))
    builder.adjust(1)
    await callback.message.answer(
        "Выберите тему для практики:", reply_markup=builder.as_markup()
    )
    await callback.answer()

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())