import os
from pathlib import Path

# Токен API
API_TOKEN = os.getenv("BOT_TOKEN")

# Пути к директориям
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "Json"
IMAGE_DIR = BASE_DIR / "Image"

# Пути к данным
THEORY_DIR = DATA_DIR / "Theory"
PRACTICE_DIR = DATA_DIR / "Practices"
THEMES_DIR = DATA_DIR / "Themes"

# Изображения
THEORY_IMAGES_DIR = IMAGE_DIR / "Theory"
PRACTICE_IMAGES_DIR = IMAGE_DIR / "Practices"

# Префиксы для callback-данных
THEORY_CALLBACK = "theory"
PRACTICE_CALLBACK = "practice"
TASK_CALLBACK = "_task"
HINT_CALLBACK = "hint"
ANSWER_CALLBACK = "answer"
BACK_TO_THEORY = "back_to_theory"
BACK_TO_PRACTICE = "back_to_practice"

# Настройки формата вывода
PARSE_MODE = "Markdown"

# Имена тем для папок с изображениями
THEME_FOLDERS = [
    "FirstTheme",
    "SecondTheme",
    "ThirdTheme",
    "FourthTheme",
    "FifthTheme",
    "SixthTheme",
    "SeventhTheme",
    "EighthTheme",
]
