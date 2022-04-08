import os
import sys
from pathlib import Path

import pygame

# работа с БД
import sqlite3

# typing
from typing import Union
from pygame.surface import Surface, SurfaceType

pygame.init()
pygame.display.set_mode((1500, 1000))


def load_image(path: str, name: str, color_key: int = None) -> Union[Surface, SurfaceType]:
    """
    Загрузка в pygame изображения с возможностью задания цветового ключа.
    """
    fullname = os.path.join(path, name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)  # загрузка изображения с помощью pygame
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)  # применение цветового ключа для изображения
    else:
        image = image.convert_alpha()
    return image


def load_map(path: str, name: str) -> list:
    """
    Возвращает карту, загруженную из текстового файла в программу, в виде списка.
    """
    fullname = Path(os.path.join(path, name))
    if not os.path.isfile(fullname):
        print(f"Файл '{fullname}' не найден")
        sys.exit()
    with open(fullname) as input_file:
        level_map = [list(map(int, line.split())) for line in input_file]
    return level_map


"""
РАБОТА С БД ↓
"""


def create_connection() -> tuple:
    """
    Возвращает соединение к базе данных и курсор.
    """
    conn = sqlite3.connect('score.sqlite')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS score(
       level INT,
       value INT);
    """)
    conn.commit()
    return conn, cur


def update_db(conn, cur, level: int, value: int) -> None:
    """
    Добавить новое значение в базу данных.
    """
    cur.execute(f"""INSERT INTO score(level, value) 
           VALUES({level}, {value});""")
    conn.commit()


def get_scores(cur) -> tuple:
    """
    Возвращает последние значения для каждого уровня из базы данных.
    """
    cur.execute("SELECT * FROM score WHERE level=1;")
    a = cur.fetchall()
    if len(a) != 0:
        a = a[-1][1]
    else:
        a = 0

    cur.execute("SELECT * FROM score WHERE level=2;")
    b = cur.fetchall()
    if len(b) != 0:
        b = b[-1][1]
    else:
        b = 0

    cur.execute("SELECT * FROM score WHERE level=3;")
    c = cur.fetchall()
    if len(c) != 0:
        c = c[-1][1]
    else:
        c = 0

    cur.execute("SELECT * FROM score WHERE level=4;")
    d = cur.fetchall()
    if len(d) != 0:
        d = d[-1][1]
    else:
        d = 0

    return a, b, c, d
