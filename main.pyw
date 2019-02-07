import pygame
import os

import handle_keys
from denizen import Player


def main():
    # pygame stuff
    pygame.init()
    clock = pygame.time.Clock()

    # constants
    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540
    GROUND_LEVEL = 450

    # set up
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Supreme Tribble')
    logo = pygame.image.load(os.path.join('data', 'logo.png'))
    pygame.display.set_icon(logo)

    # load bg image
    bg = pygame.image.load(os.path.join('data', 'bg.png'))

    # load player_sprite, get rect for player
    player_sprite = pygame.image.load(os.path.join('data', 'char.png'))
    player_sprite.set_colorkey((255, 255, 255))
    player_rect = player_sprite.get_rect()

    # player initial positions
    player_x = 20
    player_y = GROUND_LEVEL - player_rect.height

    # set up player_object
    player = Player(player_x, player_y, 0, 0, 10, 12, 0,
                    0, False, player_sprite, player_rect)

    # add player to list to be drawn
    chars = [player]

    # start main loop
    running = True

    while running:
        # get the keys pressed
        keys_dict = handle_keys.handle_keys()
        if not keys_dict['keep_running']:
            running = False

        # stop the player if they're on the ground, otherwise accelerate down
        y_target = player.is_falling(GROUND_LEVEL)

        # if user jumps, make appropriate checks and jump
        if keys_dict['jump']:
            player.jump(GROUND_LEVEL)

        player.calculate_position(keys_dict['x'], y_target)

        # handle edges of the screen
        if player.x + player_rect.width + player.vel_x < 0:
            player.x = SCREEN_WIDTH
        elif player.x + player.vel_x > SCREEN_WIDTH:
            player.x = 0 - player_rect.width

        draw_all(screen, bg, chars)
        clock.tick(60)

    pygame.quit()


def draw_all(screen, backdrop, chars_list):
    screen.blit(backdrop, (0, 0))
    for char in chars_list:
        char.draw_to(screen)
    pygame.display.flip()


if __name__ == '__main__':
    main()
