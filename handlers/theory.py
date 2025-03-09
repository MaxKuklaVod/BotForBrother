from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from config import THEORY_IMAGES_DIR, PARSE_MODE, THEORY_CALLBACK, BACK_TO_THEORY
from utils.keyboards import create_themes_keyboard, create_back_keyboard

async def theory_command(message: Message, data):
    """Обработчик команды /theory"""
    keyboard = create_themes_keyboard(data["theor_names"], THEORY_CALLBACK)
    await message.answer(
        "Выберите тему для изучения теории:", reply_markup=keyboard
    )

async def process_first_block_theory(callback: CallbackQuery, bot: Bot, data):
    """Обработчик для первого блока теории"""
    theor_names = data["theor_names"]
    block = data["theory_blocks"][0]
    
    # Пути к изображениям
    image_paths = [
        THEORY_IMAGES_DIR / "FirstTheme" / f"{i}.jpg"
        for i in range(1, 14)
    ]
    
    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{theor_names[0]}"
    )
    
    # Последовательность вывода для первого блока
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[0]))
    await callback.message.answer(block[0], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[1]))
    await callback.message.answer(block[1], parse_mode=PARSE_MODE)
    await callback.message.answer(block[2], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[2]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[3]))
    await callback.message.answer(block[3], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[4]))
    await callback.message.answer(block[4], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[5]))
    await callback.message.answer(block[5], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[6]))
    await callback.message.answer(block[6], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[7]))
    await callback.message.answer(block[7], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[8]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[9]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[10]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[11]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[12]))
    
    # Кнопка возврата
    keyboard = create_back_keyboard(BACK_TO_THEORY)
    await callback.message.answer("Конец темы", reply_markup=keyboard)

async def process_second_block_theory(callback: CallbackQuery, bot: Bot, data):
    """Обработчик для второго блока теории"""
    theor_names = data["theor_names"]
    block = data["theory_blocks"][1]
    
    # Пути к изображениям
    image_paths = [
        THEORY_IMAGES_DIR / "SecondTheme" / f"{i}.jpg"
        for i in range(1, 11)
    ]
    
    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{theor_names[1]}"
    )
    
    # Последовательность вывода для второго блока
    await callback.message.answer(block[0], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[0]))
    await callback.message.answer(block[1], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[1]))
    await callback.message.answer(block[2], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[2]))
    await callback.message.answer(block[3], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[3]))
    await callback.message.answer(block[4], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[4]))
    await callback.message.answer(block[5], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[5]))
    await callback.message.answer(block[6], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[6]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[7]))
    await callback.message.answer(block[7], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[8]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[9]))
    
    # Кнопка возврата
    keyboard = create_back_keyboard(BACK_TO_THEORY)
    await callback.message.answer("Конец темы", reply_markup=keyboard)

async def process_third_block_theory(callback: CallbackQuery, bot: Bot, data):
    """Обработчик для третьего блока теории"""
    theor_names = data["theor_names"]
    block = data["theory_blocks"][2]
    
    # Пути к изображениям
    image_paths = [
        THEORY_IMAGES_DIR / "ThirdTheme" / f"{i}.jpg"
        for i in range(1, 9)
    ]
    
    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{theor_names[2]}"
    )
    
    # Последовательность вывода для третьего блока
    await callback.message.answer(block[0], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[0]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[1]))
    await callback.message.answer(block[1], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[2]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[3]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[4]))
    await callback.message.answer(block[2], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[5]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[6]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[7]))
    
    # Кнопка возврата
    keyboard = create_back_keyboard(BACK_TO_THEORY)
    await callback.message.answer("Конец темы", reply_markup=keyboard)

async def process_fourth_block_theory(callback: CallbackQuery, bot: Bot, data):
    """Обработчик для четвертого блока теории"""
    theor_names = data["theor_names"]
    block = data["theory_blocks"][3]
    
    # Пути к изображениям
    image_paths = [
        THEORY_IMAGES_DIR / "FourthTheme" / f"{i}.jpg"
        for i in range(1, 13)
    ]
    
    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{theor_names[3]}"
    )
    
    # Последовательность вывода для четвертого блока
    await callback.message.answer(block[0], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[0]))
    await callback.message.answer(block[1], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[1]))
    await callback.message.answer(block[2], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[2]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[3]))
    await callback.message.answer(block[3], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[4]))
    await callback.message.answer(block[4], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[5]))
    await callback.message.answer(block[5], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[6]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[7]))
    await callback.message.answer(block[6], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[8]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[9]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[10]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[11]))
    
    # Кнопка возврата
    keyboard = create_back_keyboard(BACK_TO_THEORY)
    await callback.message.answer("Конец темы", reply_markup=keyboard)

async def process_fifth_block_theory(callback: CallbackQuery, bot: Bot, data):
    """Обработчик для пятого блока теории"""
    theor_names = data["theor_names"]
    block = data["theory_blocks"][4]
    
    # Пути к изображениям
    image_paths = [
        THEORY_IMAGES_DIR / "FifthTheme" / f"{i}.jpg"
        for i in range(1, 7)
    ]
    
    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{theor_names[4]}"
    )
    
    # Последовательность вывода для пятого блока
    await callback.message.answer(block[0], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[0]))
    await callback.message.answer(block[1], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[1]))
    await callback.message.answer(block[2], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[2]))
    await callback.message.answer(block[3], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[3]))
    await callback.message.answer(block[4], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[4]))
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[5]))
    
    # Кнопка возврата
    keyboard = create_back_keyboard(BACK_TO_THEORY)
    await callback.message.answer("Конец темы", reply_markup=keyboard)

async def process_sixth_block_theory(callback: CallbackQuery, bot: Bot, data):
    """Обработчик для шестого блока теории"""
    theor_names = data["theor_names"]
    block = data["theory_blocks"][5]
    
    # Пути к изображениям
    image_paths = [
        THEORY_IMAGES_DIR / "SixthTheme" / f"{i}.jpg"
        for i in range(1, 8)
    ]
    
    await callback.message.answer(
        f"Вы выбрали теорию по теме: \n{theor_names[5]}"
    )
    
    # Последовательность вывода для шестого блока
    await callback.message.answer(block[0], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[0]))
    await callback.message.answer(block[1], parse_mode=PARSE_MODE)
    await callback.message.answer(block[2], parse_mode=PARSE_MODE)
    await callback.message.answer(block[3], parse_mode=PARSE_MODE)
    await callback.message.answer(block[4], parse_mode=PARSE_MODE)
    await bot.send_photo(chat_id=callback.message.chat.id, photo=FSInputFile(image_paths[1]))
    await callback.message.answer(block[5], parse_mode=PARSE_MODE)
    
    # Кнопка возврата
    keyboard = create_back_keyboard(BACK_TO_THEORY)
    await callback.message.answer("Конец темы", reply_markup=keyboard)

async def back_to_theory(callback: CallbackQuery, data):
    """Обработчик возврата к списку тем теории"""
    keyboard = create_themes_keyboard(data["theor_names"], THEORY_CALLBACK)
    await callback.message.answer(
        "Выберите тему для изучения теории:", reply_markup=keyboard
    )


def register_theory_handlers(dp: Dispatcher, bot: Bot, data):
    """Регистрирует обработчики команд и колбэков для теории"""
    
    # Правильный способ регистрации для асинхронных обработчиков с параметрами
    # Создаем отдельные функции-обертки для каждого обработчика
    
    # Регистрация команды /theory
    async def theory_command_handler(message: Message):
        await theory_command(message, data)
    
    dp.message.register(theory_command_handler, Command("theory"))
    
    # Регистрация обработчиков для блоков теории
    async def first_block_handler(callback: CallbackQuery):
        await process_first_block_theory(callback, bot, data)
    
    async def second_block_handler(callback: CallbackQuery):
        await process_second_block_theory(callback, bot, data)
    
    async def third_block_handler(callback: CallbackQuery):
        await process_third_block_theory(callback, bot, data)
    
    async def fourth_block_handler(callback: CallbackQuery):
        await process_fourth_block_theory(callback, bot, data)
    
    async def fifth_block_handler(callback: CallbackQuery):
        await process_fifth_block_theory(callback, bot, data)
    
    async def sixth_block_handler(callback: CallbackQuery):
        await process_sixth_block_theory(callback, bot, data)
    
    async def back_handler(callback: CallbackQuery):
        await back_to_theory(callback, data)
    
    # Регистрация обработчиков выбора блоков теории
    dp.callback_query.register(first_block_handler, F.data == f"{THEORY_CALLBACK}_0")
    dp.callback_query.register(second_block_handler, F.data == f"{THEORY_CALLBACK}_1")
    dp.callback_query.register(third_block_handler, F.data == f"{THEORY_CALLBACK}_2")
    dp.callback_query.register(fourth_block_handler, F.data == f"{THEORY_CALLBACK}_3")
    dp.callback_query.register(fifth_block_handler, F.data == f"{THEORY_CALLBACK}_4")
    dp.callback_query.register(sixth_block_handler, F.data == f"{THEORY_CALLBACK}_5")
    
    # Регистрация обработчика возврата
    dp.callback_query.register(back_handler, F.data == BACK_TO_THEORY)