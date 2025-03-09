from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import TASK_CALLBACK, HINT_CALLBACK, ANSWER_CALLBACK


def create_themes_keyboard(themes, callback_prefix):
    """Создаёт клавиатуру с темами"""
    builder = InlineKeyboardBuilder()
    for i, theme in enumerate(themes):
        builder.add(
            InlineKeyboardButton(text=theme, callback_data=f"{callback_prefix}_{i}")
        )
    builder.adjust(1)  # Размещаем кнопки в один столбец
    return builder.as_markup()


def create_back_keyboard(callback_data):
    """Создаёт клавиатуру с кнопкой возврата"""
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="Вернуться к выбору темы", callback_data=callback_data
        )
    )
    return builder.as_markup()


def create_tasks_keyboard(theme_idx):
    """Создаёт клавиатуру с заданиями для темы"""
    builder = InlineKeyboardBuilder()
    for i in range(1, 6):
        builder.add(
            InlineKeyboardButton(
                text=f"Задание {i}", callback_data=f"{TASK_CALLBACK}{theme_idx}{i}"
            )
        )
    builder.adjust(1)  # Размещаем кнопки в один столбец
    return builder.as_markup()


def create_hint_answer_keyboard(theme_idx, task_idx):
    """Создаёт клавиатуру с кнопками подсказки и ответа"""
    builder = InlineKeyboardBuilder()
    task_code = f"{theme_idx}{task_idx}"
    builder.add(
        InlineKeyboardButton(
            text="Подсказка", callback_data=f"{HINT_CALLBACK}_{task_code}"
        ),
        InlineKeyboardButton(
            text="Решение", callback_data=f"{ANSWER_CALLBACK}_{task_code}"
        ),
    )
    return builder.as_markup()
