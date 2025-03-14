from pathlib import Path
import json
from typing import Dict, List, Tuple

from config import THEORY_DIR, PRACTICE_DIR, THEMES_DIR


def load_json(file_path: Path) -> Dict:
    """Загружает данные из JSON-файла
    
    Args:
        file_path: Путь к файлу
        
    Returns:
        Словарь с данными из JSON
    """
    with open(file_path, encoding="utf-8") as file:
        return json.load(file)


def load_block_data(directory: Path, block_names: List[str]) -> Dict[str, Dict]:
    """Загружает данные для набора блоков
    
    Args:
        directory: Директория с файлами блоков
        block_names: Список названий блоков
        
    Returns:
        Словарь с данными блоков
    """
    return {
        name: load_json(directory / f"{name}block.json")
        for name in block_names
    }


THEORY_BLOCK_NAMES = ["first", "second", "third", "fourth", "fifth", "sixth"]

# Исправленный THEORY_KEY_MAP
THEORY_KEY_MAP = {
    "first": ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth"],
    "second": ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth"],
    "third": ["first", "second", "third"],
    "fourth": ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"],
    "fifth": ["first", "second", "third", "fourth", "fifth"],
    "sixth": ["first", "second", "third", "fourth", "fifth", "sixth"]
}

def load_theory_data() -> List[List[Dict]]:
    """Загружает и формирует блоки теоретических данных
    
    Returns:
        Список списков теоретических блоков
    """
    theory_blocks = load_block_data(THEORY_DIR, THEORY_BLOCK_NAMES)
    
    return [
        [block_data[key] for key in THEORY_KEY_MAP[block_name]]
        for block_name, block_data in theory_blocks.items()
    ]


PRACTICE_BLOCK_NAMES = [
    "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth"
]
PRACTICE_KEYS = [
    f"{num}_{type_}" 
    for num in ("first", "second", "third", "fourth", "fifth")
    for type_ in ("hint", "answer")
]

def load_practice_data() -> List[List[Dict]]:
    """Загружает и формирует блоки практических данных
    
    Returns:
        Список списков практических блоков
    """
    practice_blocks = load_block_data(PRACTICE_DIR, PRACTICE_BLOCK_NAMES)
    
    return [
        [block_data[key] for key in PRACTICE_KEYS]
        for block_data in practice_blocks.values()
    ]


def load_theme_names() -> Tuple[List[str], List[str]]:
    """Загружает названия тем
    
    Returns:
        Кортеж (список названий теории, список названий практики)
    """
    theory_themes = load_json(THEMES_DIR / "theor_names.json")
    practice_themes = load_json(THEMES_DIR / "pract_names.json")
    
    return (
        [theory_themes[f"{name}_theme"] for name in THEORY_BLOCK_NAMES],
        [practice_themes[f"{name}_theme"] for name in PRACTICE_BLOCK_NAMES]
    )


def load_all_data() -> Dict[str, List]:
    """Загружает все данные для приложения
    
    Returns:
        Словарь с теорией, практикой и названиями тем
    """
    return {
        "theory_blocks": load_theory_data(),
        "practice_blocks": load_practice_data(),
        "theor_names": load_theme_names()[0],
        "pract_names": load_theme_names()[1]
    }