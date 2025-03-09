from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command


async def send_welcome(message: Message):
    """Обработчик команды /start"""
    await message.answer(
        "Привет! Я бот для обучения. Используйте /help, чтобы узнать список команд."
    )


async def help_command(message: Message):
    """Обработчик команды /help"""
    await message.answer(
        "Список команд:\n"
        "/start - Начать общение\n"
        "/help - Показать список команд\n"
        "/theory - Теоретическая часть\n"
        "/practice - Практическая часть"
    )


def register_common_handlers(dp: Dispatcher):
    """Регистрирует обработчики базовых команд"""
    dp.message.register(send_welcome, Command("start"))
    dp.message.register(help_command, Command("help"))
