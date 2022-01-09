import sys

from pygame.locals import *
from game_locals import *
from game_locals import __init__
from tanks import CreateTanks

main_screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

background_image = load_image('assets/sprites/background_image.png', False)

player_tank = CreateTanks()
player_tank = player_tank.create_tank(True, 'up')
rect_player_tank = player_tank.get_rect()
pos_player_tank = (screen_width / 2 - rect_player_tank.width / 2,
                   screen_height - rect_player_tank.height)


class TankBattle:

    __init__()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (
                event.type == KEYDOWN and event.key == K_ESCAPE
            ):
                running = False

        main_screen.fill(BLACK)
        main_screen.blit(background_image, pos_background_image)
        main_screen.blit(player_tank, pos_player_tank)
        pygame.display.update()

        clock.tick(FPS)

    sys.exit()
