import asyncio
from aiogram import Bot, Dispatcher
from config import API_TOKEN
from handlers import register_all_handlers
from data.loader import load_all_data

async def main():
    # Загрузка данных
    data = load_all_data()
    
    # Инициализация бота и диспетчера
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    
    # Регистрация обработчиков
    register_all_handlers(dp, bot, data)
    
    # Запуск бота
    print("Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())