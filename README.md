# Sokoban
<p align="center">
<img src="https://img.shields.io/badge/made%20by-merlyan0-blue.svg" >
<img src="https://img.shields.io/github/last-commit/Merlyan0/Sokoban" >
<img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" >
<img src="https://img.shields.io/github/languages/top/Merlyan0/Sokoban" >
</p>

![Логотип игры](https://github.com/Merlyan0/Sokoban/blob/579092766dc8aae3314a25cdefa2d44bed664d66/assets/sprites/titles/title.png)
## Описание
Проект реализован на языке программирования Python, использована библиотека PyGame. Содержит 4 базовых уровня, проходить которые можно в любом порядке. Использована современная красочная графика: 10 видов ящиков, 5 видов мест для установки ящиков, 4 вида стен, 3 вида блока земли. Ведется подсчет сделанных ходов и после завершения уровня этот результат записывается в базу данных.

<img src="https://media.giphy.com/media/sdq45lX96O5vFbJcOH/giphy.gif" width="70%"></p>

## Запуск игры
**Важно:** разрешение экрана должно быть не менее 1920x1080 (при масштабе 100%), иначе окно с игрой будет обрезано
### Запуск исходного кода с помощью виртуального окружения
1. Скачайте весь проект целиком
2. Настройте виртуальное окружение. **Рекомендуется использовать Python версии 3.8!**
3. Установите необходимые библиотеки, используя requirements.txt
4. Запустите главный файл игры - *game.py*
### Запуск с помощью .exe файла
1. Скачайте файл *game.exe*, находящийся в репозитории
2. Запустите его

## Как играть?
### Управление
Навигация по меню осуществляется мышью. Управлять персонажем можно стрелками или клавишами w, a, s, d.
### Правила и принципы игры
Герой (Кладовщик) находится на поле, разделенном на квадратные клетки, и должен подвинуть каждый ящик на обозначенное место.

*Важные дополнения:*
* Тянуть ящики нельзя, можно только толкать
* Ящики можно толкать только по одному
* Нельзя проходить сквозь стены или толкать сквозь них ящики
* Для ящика каждого цвета - свое место

## Структура проекта
* *assets* - папка со спрайтами, картами и музыкой
* *functions.py* - дополнительные функции, необходимые для работы проекта
* **game.py** - главный файл с главным классом игры
* *gameobject.py* - класс каждого объекта игры: земли, стены и пр.
* *map.py* - инициализация, отрисовка и проверка событий на карте
* *menu.py* - главное меню
* *objects.py* - файл со всеми загруженными в проект ассетами
* *player.py* - класс главного героя - игрока

## Графика
#### Ящики
<p align="center">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/crates/crate1.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/crates/crate2.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/crates/crate3.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/crates/crate4.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/crates/crate5.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/crates/crate6.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/crates/crate7.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/crates/crate8.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/crates/crate9.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/crates/crate10.png">
</p>

#### Земля
<p align="center">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/ground/ground1.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/ground/ground2.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/ground/ground3.png">
</p>

#### Стены
<p align="center">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/blocks/block1.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/blocks/block2.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/blocks/block3.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/blocks/block4.png">
</p>

#### Места для установки ящиков
<p align="center">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/install_locations/install1.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/install_locations/install2.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/install_locations/install3.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/install_locations/install4.png">
<img src="https://github.com/Merlyan0/Sokoban/blob/9827b50bb2638d929ccaf932174a68a3c4d3f0e3/assets/sprites/objects/install_locations/install5.png">
</p>

## Источники
### Графика
Основа: [Kenney - Sokoban](https://www.kenney.nl/assets/sokoban/) </br>
Фон 1: [krot.info - 13 фон](https://krot.info/fony/33126-pikselnyj-fon-37-foto.html) </br>
Фон 2: [OpenGameArt - UI FOR 2D GAME](https://opengameart.org/content/ui-for-2d-game/) </br>
Кнопки: [itch.io - Joseth](https://joseth-sc.itch.io/gui-design-for-games/) </br>
### Музыка и звуки
Главный саундтрек: [OpenGameArt - Puzzle Game 3](https://opengameart.org/content/puzzle-game-3/) </br>
Музыка в меню: [OpenGameArt - KB - Game Intro Menu Music](https://opengameart.org/content/kb-game-intro-menu-music/) </br>
Звук помещения ящика на специальное место: [OpenGameArt - Completion sound](https://opengameart.org/content/completion-sound/) </br>
Звук завершения текуего уровня: [OpenGameArt - Victory!](https://opengameart.org/content/victory-2/) </br>
Звук нажатия на кнопку: [OpenGameArt - 8bit Menu Select](https://opengameart.org/content/8bit-menu-select/) </br>
