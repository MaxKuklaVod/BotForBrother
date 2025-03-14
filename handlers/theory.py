from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from config import (
    THEORY_IMAGES_DIR,
    PARSE_MODE,
    THEORY_CALLBACK,
    BACK_TO_THEORY
)
from utils.keyboards import create_themes_keyboard, create_back_keyboard
from typing import Dict, Any


async def theory_command(message: Message, data: Dict[str, Any]) -> None:
    """Обработчик команды /theory"""
    keyboard = create_themes_keyboard(data["theor_names"], THEORY_CALLBACK)
    await message.answer(
        "Выберите тему для изучения теории:", reply_markup=keyboard
    )


async def process_block_theory(
    callback: CallbackQuery,
    bot: Bot,
    data: Dict[str, Any],
    block_index: int,
    theme_folder: str,
    image_count: int,
    sequence: list
) -> None:
    """Универсальный обработчик блоков теории
    
    Args:
        block_index: Индекс блока в data["theory_blocks"]
        theme_folder: Название папки с изображениями
        image_count: Количество изображений
        sequence: Последовательность вывода (0 - текст, 1 - фото)
    """
    theor_name = data["theor_names"][block_index]
    block = data["theory_blocks"][block_index]
    image_paths = [
        THEORY_IMAGES_DIR / theme_folder / f"{i}.jpg"
        for i in range(1, image_count + 1)
    ]
    
    await callback.message.answer(f"Вы выбрали теорию по теме:\n{theor_name}")
    
    text_index = 0
    image_index = 0
    
    for element in sequence:
        try:
            if element == 0:
                await callback.message.answer(
                    block[text_index], parse_mode=PARSE_MODE
                )
                text_index += 1
            elif element == 1:
                await bot.send_photo(
                    chat_id=callback.message.chat.id,
                    photo=FSInputFile(image_paths[image_index])
                )
                image_index += 1
        except IndexError:
            await callback.message.answer("Ошибка в последовательности блока")
            break
    
    keyboard = create_back_keyboard(BACK_TO_THEORY)
    await callback.message.answer("Конец темы", reply_markup=keyboard)
    await callback.answer()


async def back_to_theory(callback: CallbackQuery, data: Dict[str, Any]) -> None:
    """Обработчик возврата к списку тем теории"""
    keyboard = create_themes_keyboard(data["theor_names"], THEORY_CALLBACK)
    await callback.message.answer(
        "Выберите тему для изучения теории:", reply_markup=keyboard
    )
    await callback.answer()


def register_theory_handlers(
    dispatcher: Dispatcher,
    bot_instance: Bot,
    shared_data: Dict[str, Any]
) -> None:
    """Регистрация обработчиков для теории"""
    
    # Команда /theory
    @dispatcher.message(Command("theory"))
    async def theory_handler(message: Message):
        await theory_command(message, shared_data)

    # Конфигурация блоков теории
    THEORY_BLOCKS_CONFIG = [
        {
            "index": 0,
            "theme_folder": "FirstTheme",
            "image_count": 13,
            "sequence": [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1]
        },
        {
            "index": 1,
            "theme_folder": "SecondTheme",
            "image_count": 10,
            "sequence": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1]
        },
        {
            "index": 2,
            "theme_folder": "ThirdTheme",
            "image_count": 8,
            "sequence": [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
        },
        {
            "index": 3,
            "theme_folder": "FourthTheme",
            "image_count": 12,
            "sequence": [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1]
        },
        {
            "index": 4,
            "theme_folder": "FifthTheme",
            "image_count": 6,
            "sequence": [0, 1, 0, 1, 0, 1, 0, 1, 1, 1]
        },
        {
            "index": 5,
            "theme_folder": "SixthTheme",
            "image_count": 7,
            "sequence": [0, 0, 0, 0, 0, 1, 0, 0]
        }
    ]

    # Регистрация обработчиков для каждого блока
    for block_config in THEORY_BLOCKS_CONFIG:
        idx = block_config["index"]
        
        @dispatcher.callback_query(F.data == f"{THEORY_CALLBACK}_{idx}")
        async def block_handler(callback: CallbackQuery, bc=block_config):
            await process_block_theory(
                callback,
                bot_instance,
                shared_data,
                bc["index"],
                bc["theme_folder"],
                bc["image_count"],
                bc["sequence"]
            )

    # Обработчик возврата
    @dispatcher.callback_query(F.data == BACK_TO_THEORY)
    async def back_handler(callback: CallbackQuery):
        await back_to_theory(callback, shared_data)