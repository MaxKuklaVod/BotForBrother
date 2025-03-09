from .common import register_common_handlers
from .theory import register_theory_handlers
from .practice import register_practice_handlers


def register_all_handlers(dp, bot, data):
    """Регистрирует все обработчики команд и колбэков"""
    register_common_handlers(dp)
    register_theory_handlers(dp, bot, data)
    register_practice_handlers(dp, bot, data)
