import json
from config import THEORY_DIR, PRACTICE_DIR, THEMES_DIR


def load_json(file_path):
    """Загружает данные из JSON файла"""
    with open(file_path, encoding="utf-8") as f:
        return json.loads(f.read())


def load_theory_data():
    """Загружает данные теории"""
    # Названия блоков теории
    theory_blocks = {}
    for name in ["first", "second", "third", "fourth", "fifth", "sixth"]:
        file_path = THEORY_DIR / f"{name}block.json"
        theory_blocks[name] = load_json(file_path)

    # Ключи для каждого блока теории
    keys_map = {
        "first": [
            "first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
        ],
        "second": [
            "first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
        ],
        "third": ["first", "second", "third"],
        "fourth": ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"],
        "fifth": ["first", "second", "third", "fourth", "fifth"],
        "sixth": ["first", "second", "third", "fourth", "fifth", "sixth"],
    }

    # Формирование блоков теории
    blocks = []
    for name, keys in keys_map.items():
        blocks.append([theory_blocks[name][key] for key in keys])

    return blocks


def load_practice_data():
    """Загружает данные практики"""
    # Названия блоков практики
    practice_blocks = {}
    for name in [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
    ]:
        file_path = PRACTICE_DIR / f"{name}block.json"
        practice_blocks[name] = load_json(file_path)

    # Формирование блоков практики
    practice_keys = [
        "first_hint",
        "first_answer",
        "second_hint",
        "second_answer",
        "third_hint",
        "third_answer",
        "fourth_hint",
        "fourth_answer",
        "fifth_hint",
        "fifth_answer",
    ]

    blocks = []
    for name in [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
    ]:
        blocks.append([practice_blocks[name][key] for key in practice_keys])

    return blocks


def load_theme_names():
    """Загружает названия тем"""
    # Загрузка названий тем
    theor_names_data = load_json(THEMES_DIR / "theor_names.json")
    pract_names_data = load_json(THEMES_DIR / "pract_names.json")

    # Формирование списков с названиями тем
    theor_names = [
        theor_names_data[f"{key}_theme"]
        for key in ["first", "second", "third", "fourth", "fifth", "sixth"]
    ]
    pract_names = [
        pract_names_data[f"{key}_theme"]
        for key in [
            "first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
        ]
    ]

    return theor_names, pract_names


def load_data():
    """Загружает все данные для бота"""
    theory_blocks = load_theory_data()
    practice_blocks = load_practice_data()
    theor_names, pract_names = load_theme_names()

    return {
        "theory_blocks": theory_blocks,
        "practice_blocks": practice_blocks,
        "theor_names": theor_names,
        "pract_names": pract_names,
    }
