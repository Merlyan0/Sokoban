# импорт дополнительных объектов
from objects import back_small, restart, background2

# импорт дополнительных функций
from functions import *

# импорт моделей для создания меню, игрока, карты
from menu import Menu
from player import Player
from map import Map


class Game:
    """
    Основной класс игры.
    """

    def __init__(self, height: int, weight: int, fps: int) -> None:
        self.__size = self.height, self.weight = height, weight  # разрешение экрана
        self.__fps = fps  # fps

        pygame.init()

        self.__screen = pygame.display.set_mode(self.__size)  # отрисовка рабочего окна
        pygame.display.set_caption('SOKOBAN')  # изменение названия окна
        self.__clock = pygame.time.Clock()  # fps

        # группы спрайтов
        self.players = pygame.sprite.Group()  # игроки

        # экземпляры классов
        self.menu = Menu(self.__screen)  # меню
        self.player = Player(self.players, 1, 1)  # игрок
        self.map = Map('assets/maps', 'level1.txt', 'green')  # карта уровня

        # шрифты
        self.font = pygame.font.Font('assets/fonts/main.ttf', 27)
        self.font_level = pygame.font.Font('assets/fonts/main.ttf', 36)
        self.font_subtitle = pygame.font.SysFont('Times new Roman', 36)

        # переменные цикла
        self.loop = True
        self.finished_loop = True

        # звуки
        self.level_finished_sound = pygame.mixer.Sound(os.path.join('assets/sound', 'level_finished.wav'))
        self.level_finished_sound.set_volume(0.1)

        # создание базы данных
        create_connection()

    def run(self) -> None:
        """
        Основной цикл игры.
        """
        self.play_music()

        while self.loop:
            self.check_events()  # проверка событий

            self.__screen.fill('white')

            self.players.update()  # обновление игрока
            if self.map.check_installed():  # проверка выигрыша
                self.say_win()

            self.draw()  # рисование объектов

            pygame.display.flip()
            self.__clock.tick(60)

    def draw(self) -> None:
        """
        Прорисовка уровня.
        """
        self.render_level_menu()  # верхнее меню уровня
        self.map.ground_group.draw(self.__screen)  # земля
        self.map.crates_group.draw(self.__screen)  # ящики
        self.map.install_locations_group.draw(self.__screen)  # места для установки ящиков
        self.map.blocks_group.draw(self.__screen)  # стены
        self.players.draw(self.__screen)  # игроки

    def render_level_menu(self) -> None:
        """
        Прорисовка верхнего меню уровня.
        """
        # прямоугольник-фон
        pygame.draw.rect(self.__screen, '#cab19b', (0, 0, 1500, 100))

        # информационные данные
        level = self.font.render(f'УРОВЕНЬ: {self.map.level}', False, '#808080')
        moves = self.font.render(f'ХОДОВ: {self.player.get_moves()}', False, '#808080')
        crates = self.font.render(f'УСТАНОВЛЕНО ЯЩИКОВ: {len(self.map.installed_crates)} '
                                  f'/ {len(self.map.install_locations_list)}', False, '#808080')

        # отрисовка
        self.__screen.blit(level, (10, 24))
        self.__screen.blit(moves, (280, 24))
        self.__screen.blit(crates, (560, 24))
        self.__screen.blit(back_small, (1330, -3))
        self.__screen.blit(restart, (1170, -3))

    def check_events(self) -> None:
        """
        Проверка текущих событий.
        """
        for event in pygame.event.get():
            # выход
            if event.type == pygame.QUIT:
                sys.exit()

            # нажатие на клавишу клавиатуры
            if event.type == pygame.KEYDOWN:
                pos = self.player.get_pos()

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.crate_motion(pos, 0, -1)
                    self.players.update(up=True, permission=self.map.check_free(pos[0], pos[1] - 1))

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.crate_motion(pos, 0, 1)
                    self.players.update(down=True, permission=self.map.check_free(pos[0], pos[1] + 1))

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.crate_motion(pos, -1, 0)
                    self.players.update(left=True, permission=self.map.check_free(pos[0] - 1, pos[1]))

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.crate_motion(pos, 1, 0)
                    self.players.update(right=True, permission=self.map.check_free(pos[0] + 1, pos[1]))

            # нажатие на кнопку мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                # перезапуск уровня
                if 1176 <= event.pos[0] <= 1329 and 7 <= event.pos[1] <= 57:
                    self.menu.selected_sound.play()
                    self.init_level('assets/maps', f'level{self.map.level}.txt', (1, 1))
                # выход из уровня
                elif 1335 <= event.pos[0] <= 1489 and 7 <= event.pos[1] <= 57:
                    self.menu.selected_sound.play()
                    self.loop = False
                    self.menu.loop_levels = True
                    self.menu.play_music()
                    self.run_menu()

    def run_menu(self) -> None:
        """
        Запустить меню.
        """
        self.menu.run_menu_main()

    def say_win(self) -> None:
        """
        Вывести меню завершения уровня.
        """
        # база данных
        a = create_connection()
        update_db(a[0], a[1], int(self.map.level), int(self.player.moves))

        # обновление переменных цикла
        self.loop = False
        self.finished_loop = True

        # звук
        self.level_finished_sound.play()

        while self.finished_loop:
            self.check_events_finish()

            self.__screen.fill('white')

            # отрисовка 1
            self.draw()
            self.__screen.blit(background2, (400, 200))

            # рендер надписей
            level = self.font.render(f'LEVEL {self.map.level} FINISHED!', False, '#808080')
            moves = self.font.render(f'ходов сделано: ', False, '#808080')
            moves2 = self.font.render(f'{self.player.get_moves()}', False, '#808080')

            crates = self.font.render(f'установлено ящиков:', False, '#808080')
            crates2 = self.font.render(f'{len(self.map.installed_crates)} / '
                                       f'{len(self.map.install_locations_list)}', False, '#808080')
            next_b = self.font.render(f'NEXT', False, '#808080')

            # отрисовка 2
            self.__screen.blit(level, (565, 250))
            self.__screen.blit(moves, (500, 350))
            self.__screen.blit(moves2, (500, 410))
            self.__screen.blit(crates, (500, 470))
            self.__screen.blit(crates2, (500, 530))
            self.__screen.blit(next_b, (680, 770))

            pygame.display.flip()
            self.__clock.tick(60)

    def check_events_finish(self) -> None:
        """
        Проверка событий после завершения уровня.
        """
        for event in pygame.event.get():
            # выход
            if event.type == pygame.QUIT:
                sys.exit()

            # нажатие мышью
            if event.type == pygame.MOUSEBUTTONDOWN:
                # следующий уровень
                if 590 <= event.pos[0] <= 888 and 698 <= event.pos[1] <= 824:
                    lvl = int(self.map.level) + 1
                    if lvl != 5:
                        self.finished_loop = False
                        self.loop = True
                        self.init_level('assets/maps', f'level{lvl}.txt', (1, 1))
                    else:
                        self.loop = False
                        self.finished_loop = False
                        self.menu.loop_levels = True
                        self.menu.play_music()
                        self.run_menu()

    def crate_motion(self, pos: tuple, x: int, y: int) -> None:
        """
        Перемещение ящиков с заменой их позиции на карте.
        """
        a = self.map.move_crate((pos[0] + x, pos[1] + y), x, y)
        if a != (-1, -1):
            self.map.change_sprite_pos((pos[0] + x, pos[1] + y), a)
            value = self.map.map[pos[1] + y][pos[0] + x]
            self.map.change_map((pos[0] + x, pos[1] + y), 0)
            self.map.change_map((pos[0] + 2 * x, pos[1] + 2 * y), value)

    def init_level(self, path: str, name: str, player_pos: tuple) -> None:
        """
        Смена уровня.
        """
        self.map.update_map(path, name, 'green')
        self.player.set_moves(0)
        self.player.set_pos(player_pos[0], player_pos[1])

    @staticmethod
    def play_music() -> None:
        """
        Запустить проигрывание музыки.
        """
        pygame.mixer.music.unload()
        pygame.mixer.music.load(os.path.join('assets/sound/music', 'main.mp3'))
        pygame.mixer.music.set_volume(0.03)
        pygame.mixer.music.play(loops=-1)


if __name__ == '__main__':
    game = Game(1500, 1000, 60)
    game.menu.set_game(game)
    game.run_menu()
