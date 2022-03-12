import pygame

# импорт дополнительных объектов
from objects import players

# typing
from pygame.sprite import AbstractGroup


class Player(pygame.sprite.Sprite):
    """
    Создание, отрисовка и управление главным персонажем.
    """

    def __init__(self, group: AbstractGroup, x: int, y: int) -> None:
        pygame.init()

        super().__init__(group)

        self.players = players  # словарь со всеми спрайтами игрока

        self.image = self.players['down']  # текущий кадр
        self.rect = self.image.get_rect()

        self.current_direct = 'down'  # текущее направление движения
        self.set_pos(x, y)  # координаты начального спавна

        self.moves = 0  # количество ходов

    def update(self, up=False, down=False, right=False, left=False, permission=False) -> None:
        """
        Обновление позиции персонажа.
        """
        # определение нового направления движения для персонажа
        if up:
            self.current_direct = 'up'
        elif down:
            self.current_direct = 'down'
        elif right:
            self.current_direct = 'right'
        elif left:
            self.current_direct = 'left'

        # движение персонажа, если получено разрешение от Logic (если в этом направлении земля)
        if permission:
            if up:
                self.rect.y -= 64
            elif down:
                self.rect.y += 64
            elif right:
                self.rect.x += 64
            elif left:
                self.rect.x -= 64
            self.add_move()

        self.image = self.players[self.current_direct]  # обновление спрайта

    def get_pos(self) -> tuple:
        """
        Получить позицию персонажа относительно карты.
        """
        return self.rect.x // 64, (self.rect.y - 64) // 64

    def set_pos(self, x: int, y: int) -> None:
        """
        Задать позицию персонажа относительно карты.
        """
        self.rect.x, self.rect.y = x * 64, 64 + y * 64

    def get_moves(self) -> int:
        """
        Получить количество ходов.
        """
        return self.moves

    def set_moves(self, value: int) -> None:
        """
        Задать количество ходов.
        """
        self.moves = value

    def add_move(self) -> None:
        """
        Добавить один ход в переменную.
        """
        self.moves += 1
