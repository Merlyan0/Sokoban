import os
import sys

from functions import load_image


"""
LOADING
"""
# нахождение файлов, распакованных во временную папку (для .exe)
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

# игрок
up = load_image("assets/sprites/player", "up.png")
down = load_image("assets/sprites/player", "down.png")
right = load_image("assets/sprites/player", "right.png")
left = load_image("assets/sprites/player", "left.png")

# ящики
crate_gray = load_image('assets/sprites/objects/crates', 'crate1.png')
crate_brown = load_image('assets/sprites/objects/crates', 'crate2.png')
crate_red = load_image('assets/sprites/objects/crates', 'crate3.png')
crate_blue = load_image('assets/sprites/objects/crates', 'crate4.png')
crate_green = load_image('assets/sprites/objects/crates', 'crate5.png')
crate_d_gray = load_image('assets/sprites/objects/crates', 'crate6.png')
crate_d_brown = load_image('assets/sprites/objects/crates', 'crate7.png')
crate_d_red = load_image('assets/sprites/objects/crates', 'crate8.png')
crate_d_blue = load_image('assets/sprites/objects/crates', 'crate9.png')
crate_d_green = load_image('assets/sprites/objects/crates', 'crate10.png')

# места для установки ящиков
install_gray = load_image('assets/sprites/objects/install_locations', 'install1.png')
install_brown = load_image('assets/sprites/objects/install_locations', 'install2.png')
install_red = load_image('assets/sprites/objects/install_locations', 'install3.png')
install_blue = load_image('assets/sprites/objects/install_locations', 'install4.png')
install_green = load_image('assets/sprites/objects/install_locations', 'install5.png')

# стены
block_gray = load_image('assets/sprites/objects/blocks', 'block1.png')
block_brown = load_image('assets/sprites/objects/blocks', 'block2.png')
block_red = load_image('assets/sprites/objects/blocks', 'block3.png')
block_d_red = load_image('assets/sprites/objects/blocks', 'block4.png')

# земля
ground_gray = load_image('assets/sprites/objects/ground', 'ground1.png')
ground_brown = load_image('assets/sprites/objects/ground', 'ground2.png')
ground_green = load_image('assets/sprites/objects/ground', 'ground3.png')

# меню: основное
background = load_image('assets/sprites/backgrounds', 'background1.jpg')
title = load_image('assets/sprites/titles', 'title.png', -1)
play_button = load_image('assets/sprites/buttons', 'play.png', -1)
help_button = load_image('assets/sprites/buttons', 'help.png', -1)
score_button = load_image('assets/sprites/buttons', 'score.png', -1)
exit_button = load_image('assets/sprites/buttons', 'exit.png', -1)
back = load_image('assets/sprites/buttons', 'back.png', -1)
score = load_image('assets/sprites/titles', 'score.png', -1)
help_t = load_image('assets/sprites/titles', 'help.png', -1)

# меню завершения уровня
back_small = load_image('assets/sprites/buttons', 'back_small.png', -1)
restart = load_image('assets/sprites/buttons', 'restart.png', -1)
background2 = load_image('assets/sprites/backgrounds', 'background2.png', -1)

# меню: уровни
levels = load_image('assets/sprites/titles', 'levels.png', -1)
level1 = load_image('assets/sprites/buttons', 'level1.png', -1)
level2 = load_image('assets/sprites/buttons', 'level2.png', -1)
level3 = load_image('assets/sprites/buttons', 'level3.png', -1)
level4 = load_image('assets/sprites/buttons', 'level4.png', -1)


"""
OBJECTS
"""
# игрок
players = {'down': down,
           'up': up,
           'right': right,
           'left': left}
# ящики
crates = {'gray': crate_gray,
          'brown': crate_brown,
          'red': crate_red,
          'blue': crate_blue,
          'green': crate_green,
          'd_gray': crate_d_gray,
          'd_brown': crate_d_brown,
          'd_red': crate_d_red,
          'd_blue': crate_d_blue,
          'd_green': crate_d_green}

# места для установки ящиков
install_locations = {'gray': install_gray,
                     'brown': install_brown,
                     'red': install_red,
                     'blue': install_blue,
                     'green': install_green}

# стены
blocks = {'gray': block_gray,
          'brown': block_brown,
          'red': block_red,
          'd_red': block_d_red}

# земля
ground = {'gray': ground_gray,
          'brown': ground_brown,
          'green': ground_green}
