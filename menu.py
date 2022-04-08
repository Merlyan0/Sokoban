from os import path
import pygame

# импорт дополнительных функций
from functions import get_scores, create_connection

# импорт дополнительных объектов
from objects import background, play_button, score_button, exit_button, help_button, title, levels, \
    level1, back, level2, level3, level4, score, help_t


class Menu:
    """
    Класс главного меню игры.
    """

    def __init__(self, screen) -> None:
        pygame.init()
        self.__screen = screen  # экран
        self.game = None  # экземляр главного класса игры

        # циклы
        self.loop_main = True  # главный
        self.loop_levels = True  # меню с уровнями
        self.loop_help = True  # меню с помощью
        self.loop_score = True  # меню с последними результатами игрока

        # звуки
        self.selected_sound = pygame.mixer.Sound(path.join('assets/sound', 'menu_selected.wav'))
        self.selected_sound.set_volume(0.2)

        # музыка
        self.play_music()

        # инициализация переменных с правилами
        self.rule1, self.rule2, self.rule3, self.rule4 = None, None, None, None

    def set_game(self, game) -> None:
        """
        Установить экземляр главного класса игры.
        """
        self.game = game
        self.render_rules()

    def render_rules(self) -> None:
        """
        Рендер текста правил игры.
        """
        self.rule1 = self.game.font_subtitle.render(f'Игроку необходимо расставить ящики '
                                                    f'по обозначенным местам лабиринта ', False, '#808080')

        self.rule2 = self.game.font_subtitle.render(f'(обратите внимание: для ящиков '
                                                    f'разных цветов - разные места!).', False, '#808080')

        self.rule3 = self.game.font_subtitle.render(f'Кладовщик одновременно может двигать '
                                                    f'только один ящик, толкая вперёд.', False, '#808080')

        self.rule4 = self.game.font_subtitle.render(f'Нельзя перемещать ящики сквозь стены.', False, '#808080')

    def run_menu_main(self) -> None:
        """
        Запуск главного меню.
        """
        while self.loop_main:
            self.check_events_main()

            self.__screen.fill('white')

            objects = [(background, (0, 0)),
                       (title, (400, -70)),
                       (play_button, (400, 100)),
                       (help_button, (400, 310)),
                       (score_button, (400, 520)),
                       (exit_button, (400, 740))]

            for i in objects:
                self.__screen.blit(i[0], (i[1][0], i[1][1]))

            pygame.display.flip()

    def run_menu_levels(self) -> None:
        """
        Запуск меню выбора уровня.
        """
        while self.loop_levels:
            self.check_events_levels()

            self.__screen.fill('white')

            objects = [(background, (0, 0)),
                       (levels, (400, -50)),
                       (level1, (40, 170)),
                       (level2, (270, 170)),
                       (level3, (500, 170)),
                       (level4, (730, 170)),
                       (back, (400, 700))]

            for i in objects:
                self.__screen.blit(i[0], (i[1][0], i[1][1]))

            pygame.display.flip()

    def run_menu_help(self) -> None:
        """
        Запуск меню с правилами игры.
        """
        while self.loop_help:
            self.check_events_help()

            self.__screen.fill('white')

            objects = [(help_t, (380, -30)),
                       (self.rule1, (30, 240)),
                       (self.rule2, (30, 320)),
                       (self.rule3, (30, 400)),
                       (self.rule4, (30, 480)),
                       (back, (400, 700))]

            self.__screen.blit(background, (0, 0))

            pygame.draw.rect(self.__screen, '#cab19b', (10, 200, 1400, 400))
            pygame.draw.rect(self.__screen, 'gray', (10, 200, 1400, 400), 15)

            for i in objects:
                self.__screen.blit(i[0], (i[1][0], i[1][1]))

            pygame.display.flip()

    def run_menu_score(self) -> None:
        """
        Запуск меню с результатами пользователя.
        """
        while self.loop_score:
            self.check_events_score()

            # получение результатов из базы данных и рендер текста
            a = get_scores(create_connection()[1])
            self.__screen.fill('white')

            lvl1 = self.game.font_level.render(f'Уровень 1:', False, '#808080')
            if a[0] == 0:
                lvl1_2 = self.game.font_subtitle.render(f'ещё не пройден', False, '#808080')
            else:
                lvl1_2 = self.game.font_subtitle.render(f'{a[0]} ходов сделано', False, '#808080')

            lvl2 = self.game.font_level.render(f'Уровень 2:', False, '#808080')
            if a[1] == 0:
                lvl2_2 = self.game.font_subtitle.render(f'ещё не пройден', False, '#808080')
            else:
                lvl2_2 = self.game.font_subtitle.render(f'{a[1]} ходов сделано', False, '#808080')

            lvl3 = self.game.font_level.render(f'Уровень 3:', False, '#808080')
            if a[2] == 0:
                lvl3_2 = self.game.font_subtitle.render(f'ещё не пройден', False, '#808080')
            else:
                lvl3_2 = self.game.font_subtitle.render(f'{a[2]} ходов сделано', False, '#808080')

            lvl4 = self.game.font_level.render(f'Уровень 4:', False, '#808080')
            if a[3] == 0:
                lvl4_2 = self.game.font_subtitle.render(f'ещё не пройден', False, '#808080')
            else:
                lvl4_2 = self.game.font_subtitle.render(f'{a[3]} ходов сделано', False, '#808080')

            objects = [(score, (380, -30)),
                       (lvl1, (30, 230)),
                       (lvl1_2, (300, 223)),
                       (lvl2, (30, 310)),
                       (lvl2_2, (300, 303)),
                       (lvl3, (30, 390)),
                       (lvl3_2, (300, 383)),
                       (lvl4, (30, 470)),
                       (lvl4_2, (300, 463)),
                       (back, (400, 700))]

            self.__screen.blit(background, (0, 0))

            pygame.draw.rect(self.__screen, '#cab19b', (10, 180, 1400, 400))
            pygame.draw.rect(self.__screen, 'gray', (10, 180, 1400, 400), 15)

            for i in objects:
                self.__screen.blit(i[0], (i[1][0], i[1][1]))

            pygame.display.flip()

    def check_events_main(self) -> None:
        """
        Проверка событий для главного меню.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # кнопка play
                if 419 <= event.pos[0] <= 1035 and 135 <= event.pos[1] <= 345:
                    self.selected_sound.play()
                    self.loop_levels = True
                    self.loop_help = False
                    self.loop_score = False
                    self.loop_main = False
                    self.run_menu_levels()
                # кнопка help
                elif 419 <= event.pos[0] <= 1035 and 350 <= event.pos[1] <= 550:
                    self.selected_sound.play()
                    self.loop_levels = False
                    self.loop_help = True
                    self.loop_score = False
                    self.loop_main = False
                    self.run_menu_help()
                # кнопка score
                elif 419 <= event.pos[0] <= 1035 and 561 <= event.pos[1] <= 766:
                    self.selected_sound.play()
                    self.loop_levels = False
                    self.loop_help = False
                    self.loop_score = True
                    self.loop_main = False
                    self.run_menu_score()
                # кнопка exit
                elif 419 <= event.pos[0] <= 1035 and 777 <= event.pos[1] <= 985:
                    self.selected_sound.play()
                    pygame.quit()
                    exit()

    def check_events_levels(self) -> None:
        """
        Проверка событий для меню с уровнями.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # кнопка 1
                if 63 <= event.pos[0] <= 252 and 212 <= event.pos[1] <= 413:
                    self.change_level(1, (1, 1))
                # кнопка 2
                elif 293 <= event.pos[0] <= 485 and 212 <= event.pos[1] <= 413:
                    self.change_level(2, (1, 1))
                # кнопка 3
                elif 522 <= event.pos[0] <= 715 and 212 <= event.pos[1] <= 413:
                    self.change_level(3, (1, 1))
                # кнопка 4
                elif 750 <= event.pos[0] <= 947 and 212 <= event.pos[1] <= 413:
                    self.change_level(4, (1, 1))
                # кнопка back
                elif 419 <= event.pos[0] <= 1034 and 738 <= event.pos[1] <= 944:
                    self.selected_sound.play()
                    self.loop_levels = False
                    self.loop_help = False
                    self.loop_score = False
                    self.loop_main = True
                    self.run_menu_main()

    def check_events_help(self) -> None:
        """
        Проверка событий для меню с правилами игры.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # кнопка back
                if 419 <= event.pos[0] <= 1034 and 738 <= event.pos[1] <= 944:
                    self.selected_sound.play()
                    self.loop_levels = False
                    self.loop_help = False
                    self.loop_score = False
                    self.loop_main = True
                    self.run_menu_main()

    def check_events_score(self) -> None:
        """
        Проверка событий для меню с результатами.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # кнопка back
                if 419 <= event.pos[0] <= 1034 and 738 <= event.pos[1] <= 944:
                    self.selected_sound.play()
                    self.loop_levels = False
                    self.loop_help = False
                    self.loop_score = False
                    self.loop_main = True
                    self.run_menu_main()

    def change_level(self, level_number: int, player_pos: tuple) -> None:
        """
        Изменить текущий уровень в главном классе.
        """
        self.selected_sound.play()
        self.game.init_level('assets/maps', f'level{level_number}.txt', player_pos)
        pygame.mixer.music.stop()
        self.game.loop = True
        self.loop_levels = False
        self.loop_main = False
        self.loop_score = False
        self.loop_help = False
        self.game.run()

    @staticmethod
    def play_music() -> None:
        """
        Запустить проигрывание музыки.
        """
        pygame.mixer.music.unload()
        pygame.mixer.music.load(path.join('assets/sound/music', 'menu.mp3'))
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(loops=-1)
