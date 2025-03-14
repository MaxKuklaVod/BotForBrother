from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command


WELCOME_MESSAGE = (
    "Привет! Я бот для обучения. Используйте /help, "
    "чтобы узнать список команд."
)
HELP_MESSAGE = (
    "Список команд:\n"
    "/start - Начать общение\n"
    "/help - Показать список команд\n"
    "/theory - Теоретическая часть\n"
    "/practice - Практическая часть"
)


async def send_welcome(message: Message) -> None:
    """Обработчик команды /start"""
    await message.answer(WELCOME_MESSAGE)


async def help_command(message: Message) -> None:
    """Обработчик команды /help"""
    await message.answer(HELP_MESSAGE)


def register_common_handlers(dispatcher: Dispatcher) -> None:
    """Регистрирует обработчики базовых команд
    
    Args:
        dispatcher: Объект Dispatcher для регистрации хэндлеров
    """
    dispatcher.message.register(send_welcome, Command("start"))
    dispatcher.message.register(help_command, Command("help"))