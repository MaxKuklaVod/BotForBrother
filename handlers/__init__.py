from aiogram import Dispatcher
from aiogram import Bot
from typing import Any, Dict

from .common import register_common_handlers
from .theory import register_theory_handlers
from .practice import register_practice_handlers


def register_all_handlers(dispatcher: Dispatcher, bot_instance: Bot, shared_data: Dict[str, Any]) -> None:
    """
    Регистрирует все обработчики команд и колбэков
    
    Args:
        dispatcher: Объект Dispatcher для регистрации хэндлеров
        bot_instance: Экземпляр бота для взаимодействия с API
        shared_data: Общие данные, используемые в обработчиках
    """
    register_common_handlers(dispatcher)
    register_theory_handlers(dispatcher, bot_instance, shared_data)
    register_practice_handlers(dispatcher, bot_instance, shared_data)