from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from config import (
    PRACTICE_IMAGES_DIR,
    PARSE_MODE,
    PRACTICE_CALLBACK,
    BACK_TO_PRACTICE,
    TASK_CALLBACK,
    HINT_CALLBACK,
    ANSWER_CALLBACK,
    THEME_FOLDERS
)
from utils.keyboards import (
    create_themes_keyboard,
    create_back_keyboard,
    create_tasks_keyboard,
    create_hint_answer_keyboard
)
from typing import Dict, Any


# Константы для индексов
HINT_OFFSET = 0
ANSWER_OFFSET = 1
MAX_THEMES = 8
TASKS_PER_THEME = 5


async def practice_command(message: Message, data: Dict[str, Any]) -> None:
    """Обработчик команды /practice"""
    keyboard = create_themes_keyboard(data["pract_names"], PRACTICE_CALLBACK)
    await message.answer("Выберите тему для практики:", reply_markup=keyboard)


async def process_practice_theme(
    callback: CallbackQuery, 
    theme_idx: int, 
    data: Dict[str, Any]
) -> None:
    """Обработчик выбора темы практики"""
    keyboard = create_tasks_keyboard(theme_idx)
    await callback.message.answer(
        f"Вы выбрали практику по теме: \n{data['pract_names'][theme_idx]}",
        reply_markup=keyboard
    )
    await callback.answer()


async def process_practice_task(
    callback: CallbackQuery, 
    bot: Bot, 
    theme_idx: int, 
    task_idx: int
) -> None:
    """Обработчик выбора задания практики"""
    try:
        image_path = PRACTICE_IMAGES_DIR / THEME_FOLDERS[theme_idx] / f"{task_idx}.jpg"
        keyboard = create_hint_answer_keyboard(theme_idx, task_idx)
        
        await callback.message.answer(f"Вы выбрали задание {task_idx}")
        await bot.send_photo(
            chat_id=callback.message.chat.id,
            photo=FSInputFile(image_path),
            reply_markup=keyboard
        )
    except FileNotFoundError:
        await callback.message.answer("Изображение задания временно недоступно")
    finally:
        await callback.answer()


async def show_hint(
    callback: CallbackQuery, 
    theme_idx: int, 
    task_idx: int, 
    data: Dict[str, Any]
) -> None:
    """Показывает подсказку для задания"""
    try:
        hint_index = (task_idx - 1) * 2 + HINT_OFFSET
        await callback.message.answer(data["practice_blocks"][theme_idx][hint_index])
    finally:
        await callback.answer()


async def show_answer(
    callback: CallbackQuery, 
    theme_idx: int, 
    task_idx: int, 
    data: Dict[str, Any]
) -> None:
    """Показывает ответ для задания"""
    try:
        answer_index = (task_idx - 1) * 2 + ANSWER_OFFSET
        await callback.message.answer(data["practice_blocks"][theme_idx][answer_index])
    finally:
        await callback.answer()


async def back_to_practice(
    callback: CallbackQuery, 
    data: Dict[str, Any]
) -> None:
    """Обработчик возврата к списку тем практики"""
    keyboard = create_themes_keyboard(data["pract_names"], PRACTICE_CALLBACK)
    await callback.message.answer("Выберите тему для практики:", reply_markup=keyboard)
    await callback.answer()


def register_practice_handlers(
    dispatcher: Dispatcher, 
    bot_instance: Bot, 
    shared_data: Dict[str, Any]
) -> None:
    """Регистрация обработчиков для практики"""
    
    # Команда /practice
    @dispatcher.message(Command("practice"))
    async def practice_command_handler(message: Message):
        await practice_command(message, shared_data)

    # Регистрация обработчиков тем
    for theme_idx in range(MAX_THEMES):
        # Обработчик выбора темы
        @dispatcher.callback_query(F.data == f"{PRACTICE_CALLBACK}_{theme_idx}")
        async def theme_handler(callback: CallbackQuery, idx=theme_idx):
            await process_practice_theme(callback, idx, shared_data)

        # Регистрация обработчиков заданий
        for task_idx in range(1, TASKS_PER_THEME + 1):
            task_code = f"{theme_idx}{task_idx}"
            
            # Обработчик задания
            @dispatcher.callback_query(F.data == f"{TASK_CALLBACK}{task_code}")
            async def task_handler(callback: CallbackQuery, t=theme_idx, tk=task_idx):
                await process_practice_task(callback, bot_instance, t, tk)
            
            # Обработчик подсказки
            @dispatcher.callback_query(F.data == f"{HINT_CALLBACK}_{task_code}")
            async def hint_handler(callback: CallbackQuery, t=theme_idx, tk=task_idx):
                await show_hint(callback, t, tk, shared_data)
            
            # Обработчик ответа
            @dispatcher.callback_query(F.data == f"{ANSWER_CALLBACK}_{task_code}")
            async def answer_handler(callback: CallbackQuery, t=theme_idx, tk=task_idx):
                await show_answer(callback, t, tk, shared_data)

    # Обработчик возврата
    @dispatcher.callback_query(F.data == BACK_TO_PRACTICE)
    async def back_handler(callback: CallbackQuery):
        await back_to_practice(callback, shared_data)