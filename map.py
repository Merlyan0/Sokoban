# импорт модели объекта
from gameobject import GameObject

# импорт дополнительных объектов
from objects import *

# импорт дополнительных функций
from functions import *


class Map:
    """
    Инициализация и логика работы карты уровня.
    """

    def __init__(self, path: str, name: str, ground_color: str) -> None:
        self.map = load_map(path, name)  # загрузка карты из текстового фала
        self.height, self.width, self.tile_size = 0, 0, 0  # инициализация переменных
        self.level = 1  # текущий уровень

        # спрайты
        self.crates = crates  # ящики
        self.install_locations = install_locations  # места для установки ящиков
        self.blocks = blocks  # стены
        self.ground = ground  # земля

        # группы спрайтов
        self.crates_group = pygame.sprite.Group()  # ящики
        self.install_locations_group = pygame.sprite.Group()  # места для установки ящиков
        self.blocks_group = pygame.sprite.Group()  # стены
        self.ground_group = pygame.sprite.Group()  # земля

        # соотнесение чисел в текстовом файле карты уровня и объектов в игре
        self.number_guide = \
            {1: [self.blocks_group, self.blocks, 'gray', 'block'],  # стены: 1-4
             2: [self.blocks_group, self.blocks, 'brown', 'block'],
             3: [self.blocks_group, self.blocks, 'red', 'block'],
             4: [self.blocks_group, self.blocks, 'd_red', 'block'],

             5: [self.crates_group, self.crates, 'gray', 'crate'],  # ящики: 5-14
             6: [self.crates_group, self.crates, 'brown', 'crate'],
             7: [self.crates_group, self.crates, 'red', 'crate'],
             8: [self.crates_group, self.crates, 'blue', 'crate'],
             9: [self.crates_group, self.crates, 'green', 'crate'],
             10: [self.crates_group, self.crates, 'd_gray', 'crate'],
             11: [self.crates_group, self.crates, 'd_brown', 'crate'],
             12: [self.crates_group, self.crates, 'd_red', 'crate'],
             13: [self.crates_group, self.crates, 'd_blue', 'crate'],
             14: [self.crates_group, self.crates, 'd_green', 'crate'],

             15: [self.install_locations_group, self.install_locations, 'gray', 'install'],  # установка ящиков: 15-19
             16: [self.install_locations_group, self.install_locations, 'brown', 'install'],
             17: [self.install_locations_group, self.install_locations, 'red', 'install'],
             18: [self.install_locations_group, self.install_locations, 'blue', 'install'],
             19: [self.install_locations_group, self.install_locations, 'green', 'install']}

        # список размещенных на карте объектов (их классы) кроме земли и мест для установки ящиков
        self.objects_list = list()

        # список координат каждого места для установки ящика
        self.install_locations_list = list()

        # список уже установленных ящиков
        self.installed_crates = list()

        self.update_map(path, name, ground_color)

        # звуки
        self.crate_installed_sound = pygame.mixer.Sound(os.path.join('assets/sound', 'installed.wav'))
        self.crate_installed_sound.set_volume(0.2)

    def kill_sprites(self) -> None:
        """
        Удалить все спрайты.
        """
        for i in self.crates_group:
            i.kill()
        for i in self.install_locations_group:
            i.kill()
        for i in self.blocks_group:
            i.kill()
        for i in self.ground_group:
            i.kill()

    def update_map(self, path: str, name: str, ground_color: str) -> None:
        """
        Обновить карту (перейти на другой уровень).
        """
        self.map = load_map(path, name)
        self.level = name.split('.')[0][-1]
        self.kill_sprites()
        self.objects_list = list()
        self.install_locations_list = list()
        self.init_map(ground_color)

    def init_map(self, ground_color: str) -> None:
        """
        Инициализировать новую карту: создать все спрайты.
        """
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.tile_size = 64

        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] != 0:
                    a = self.number_guide[self.map[y][x]]
                    if a[3] == 'install':
                        GameObject(a[0], a[1], a[2], a[3], x, y)
                        self.install_locations_list.append([(x, y), a[2]])
                        self.change_map((x, y), 0)
                    else:
                        self.objects_list.append(GameObject(a[0], a[1], a[2], a[3], x, y))
                GameObject(self.ground_group, self.ground, ground_color, 'ground', x, y)

    def change_map(self, pos: tuple, value: int) -> None:
        """
        Изменение значения в позиции *pos* на *value* в главной переменной класса.
        """
        self.map[pos[1]][pos[0]] = value

    def change_sprite_pos(self, pos1: tuple, pos2: tuple) -> None:
        """
        Изменить позицию у определенного спрайта на карте.
        """
        for i in self.objects_list:
            if i.get_pos() == pos1:
                i.set_pos(pos2)

    def get_sprite_type(self, pos: tuple) -> str:
        """
        Получить тип спрайта (земля, стена...).
        """
        for i in self.objects_list:
            if i.get_pos() == pos:
                return i.get_type()

    def check_free(self, x: int, y: int) -> bool:
        """
        Проверяет, свободен ли заданный участок
        """
        if self.map[y][x] == 0:
            return True
        return False

    def move_crate(self, crate_pos: tuple, x: int, y: int) -> tuple:
        """
        Возвращает координаты перемещенного ящика, если возможно совершить это действие.
        """
        if self.get_sprite_type((crate_pos[0], crate_pos[1])) == 'crate':
            if self.check_free(crate_pos[0] + x, crate_pos[1] + y):
                return crate_pos[0] + x, crate_pos[1] + y
        return -1, -1

    def check_installed(self) -> bool:
        """
        Добавляет все ящики, расположенные на правильных местах, в список. Возвращает True, если ВСЕ ящики расположены
        на правильных местах.
        """
        a = len(self.installed_crates)
        self.installed_crates = list()
        for i in self.objects_list:
            for j in self.install_locations_list:
                if i.get_pos() == j[0] and i.get_color() == j[1]:
                    self.installed_crates.append(i)
        if len(self.installed_crates) > a:
            self.crate_installed_sound.play()
        if len(self.installed_crates) == len(self.install_locations_list):
            return True
        return False
