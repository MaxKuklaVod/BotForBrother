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
    THEME_FOLDERS,
)
from utils.keyboards import (
    create_themes_keyboard,
    create_back_keyboard,
    create_tasks_keyboard,
    create_hint_answer_keyboard,
)


async def practice_command(message: Message, data):
    """Обработчик команды /practice"""
    keyboard = create_themes_keyboard(data["pract_names"], PRACTICE_CALLBACK)
    await message.answer("Выберите тему для практики:", reply_markup=keyboard)


async def process_practice_theme(callback: CallbackQuery, theme_idx: int, data):
    """Обработчик выбора темы практики"""
    keyboard = create_tasks_keyboard(theme_idx)
    await callback.message.answer(
        f"Вы выбрали практику по теме: \n{data['pract_names'][theme_idx]}",
        reply_markup=keyboard,
    )
    await callback.answer()


async def process_practice_task(
    callback: CallbackQuery, bot: Bot, theme_idx: int, task_idx: int
):
    """Обработчик выбора задания практики"""
    # Путь к изображению задания
    image_path = PRACTICE_IMAGES_DIR / THEME_FOLDERS[theme_idx] / f"{task_idx}.jpg"

    # Подготовка клавиатуры с кнопками подсказки и ответа
    keyboard = create_hint_answer_keyboard(theme_idx, task_idx)

    # Отправка сообщения и изображения
    await callback.message.answer(f"Вы выбрали задание {task_idx}")
    await bot.send_photo(
        chat_id=callback.message.chat.id,
        photo=FSInputFile(image_path),
        reply_markup=keyboard,
    )
    await callback.answer()


async def show_hint(callback: CallbackQuery, theme_idx: int, task_idx: int, data):
    """Показывает подсказку для задания"""
    hint_index = (task_idx - 1) * 2  # Индекс подсказки в массиве
    await callback.message.answer(data["practice_blocks"][theme_idx][hint_index])
    await callback.answer()


async def show_answer(callback: CallbackQuery, theme_idx: int, task_idx: int, data):
    """Показывает ответ для задания"""
    answer_index = (task_idx - 1) * 2 + 1  # Индекс ответа в массиве
    await callback.message.answer(data["practice_blocks"][theme_idx][answer_index])
    await callback.answer()


async def back_to_practice(callback: CallbackQuery, data):
    """Обработчик возврата к списку тем практики"""
    keyboard = create_themes_keyboard(data["pract_names"], PRACTICE_CALLBACK)
    await callback.message.answer("Выберите тему для практики:", reply_markup=keyboard)
    await callback.answer()


def register_practice_handlers(dp: Dispatcher, bot: Bot, data):
    """Регистрирует обработчики команд и колбэков для практики"""
    
    # Правильный обработчик команды /practice
    async def practice_command_handler(message: Message):
        await practice_command(message, data)
    
    dp.message.register(practice_command_handler, Command("practice"))
    
    # Регистрация обработчиков выбора темы практики
    for theme_idx in range(8):  # Предполагаем, что у нас 8 тем практики
        # Создаем замыкание для сохранения текущего значения theme_idx
        theme_idx_value = theme_idx  # Важно: создаем локальную копию
        
        async def theme_handler(callback: CallbackQuery, idx=theme_idx_value):
            await process_practice_theme(callback, idx, data)
        
        dp.callback_query.register(
            theme_handler, 
            F.data == f"{PRACTICE_CALLBACK}_{theme_idx}"
        )
    
    # Регистрация обработчиков для заданий, подсказок и ответов
    for theme_idx in range(8):
        for task_idx in range(1, 6):  # Предполагаем, что у нас 5 заданий в каждой теме
            task_code = f"{theme_idx}{task_idx}"
            
            # Создаем локальные копии индексов для использования в замыканиях
            t_idx, tk_idx = theme_idx, task_idx
            
            # Обработчик выбора задания
            async def task_handler(callback: CallbackQuery, t=t_idx, tk=tk_idx):
                await process_practice_task(callback, bot, t, tk)
            
            # Обработчик показа подсказки
            async def hint_handler(callback: CallbackQuery, t=t_idx, tk=tk_idx):
                await show_hint(callback, t, tk, data)
            
            # Обработчик показа ответа
            async def answer_handler(callback: CallbackQuery, t=t_idx, tk=tk_idx):
                await show_answer(callback, t, tk, data)
            
            # Регистрация обработчиков
            dp.callback_query.register(
                task_handler, 
                F.data == f"{TASK_CALLBACK}{task_code}"
            )
            
            dp.callback_query.register(
                hint_handler, 
                F.data == f"{HINT_CALLBACK}_{task_code}"
            )
            
            dp.callback_query.register(
                answer_handler, 
                F.data == f"{ANSWER_CALLBACK}_{task_code}"
            )
    
    # Обработчик возврата к выбору темы практики
    async def back_handler(callback: CallbackQuery):
        await back_to_practice(callback, data)
    
    dp.callback_query.register(back_handler, F.data == BACK_TO_PRACTICE)