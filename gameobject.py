import pygame

# typing
from pygame.sprite import AbstractGroup


class GameObject(pygame.sprite.Sprite):
    """
    Создание и отрисовка доп. объектов: ящиков, стен и др.
    """

    def __init__(self, group: AbstractGroup, object_dict: dict, color: str, object_type: str, x: int, y: int) -> None:
        super().__init__(group)

        self.image = object_dict[color]  # спрайт объекта
        self.rect = self.image.get_rect()

        self.type = object_type  # тип объекта (земля, стена...)
        if color.startswith('d_'):
            color = color.lstrip('d_')
        self.color = color  # цвет объекта
        self.set_pos((x, y))  # задание позиции объекту

    def set_pos(self, pos) -> None:
        """
        Задать новую позицию объекта.
        """
        self.rect.x, self.rect.y = pos[0] * 64, 64 + pos[1] * 64

    def get_pos(self) -> tuple:
        """
        Получить текущую позицию объекта.
        """
        return self.rect.x // 64, (self.rect.y - 64) // 64

    def get_color(self) -> str:
        """
        Получить цвет объекта.
        """
        return self.color

    def get_type(self) -> str:
        """
        Получить тип объекта (стена, ящик...).
        """
        return self.type
