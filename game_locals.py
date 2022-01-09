import pygame


# Инициализация PyGame и создание главного игрового окна.
def __init__():

    pygame.init()
    pygame.display.set_caption(head_main_screen)


# Загрузка изображений.
def load_image(path, is_alpha):

    if is_alpha:
        return pygame.image.load(path).convert_alpha()  # с прозрачным фоном
    else:
        return pygame.image.load(path).convert()  # без прозрачного фона


# Задание цветов.
BLACK = 0, 0, 0

# Переменные и константы для создания главного игрового окна.
screen_width = 1300  # ширина главного окна
screen_height = 770  # высота главного окна
screen_size = screen_width, screen_height  # габариты главного окна
head_main_screen = 'Танковая битва'  # заголовок главного окна

# Переменные и константы  фонового изображения.
pos_background_image = 0, 0

# Переменные и константы главного игрового цикла.
running = True  # условие выхода из цикла
FPS = 60
