import pygame
import os

import handle_keys
import denizen


def main():
    pygame.init()
    clock = pygame.time.Clock()

    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540
    GROUND_LEVEL = 450

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pygame')
    logo = pygame.image.load(os.path.join('data', 'logo.png'))
    pygame.display.set_icon(logo)

    bg = pygame.image.load(os.path.join('data', 'bg.png'))
    player_sprite = pygame.image.load(os.path.join('data', 'char.png'))
    player_sprite.set_colorkey((255, 255, 255))
    player_rect = player_sprite.get_rect()

    player_x = 20
    player_y = GROUND_LEVEL - player_rect.height

    player_1 = denizen.Player(player_x, player_y,    # location
                              0, 0,                  # velocities (x and y)
                              0, 0,                  # acceleration (x and y)
                              player_sprite, player_rect)

    running = True

    while running:
        keys_dict = handle_keys.handle_keys()
        if not keys_dict['keep_running']:
            running = False

        # handle edges of the screen
        if player_1.x + player_rect.width + player_1.vel_x < 0:
            player_1.x = SCREEN_WIDTH
        elif player_1.x + player_1.vel_x > SCREEN_WIDTH:
            player_1.x = 0 - player_rect.width

        # stop the player if they're on the ground, otherwise accelerate down
        if player_1.y + player_1.rect.height >= GROUND_LEVEL:
            player_1.y = GROUND_LEVEL - player_1.rect.height
            player_1.vel_y = 0
            y_target = 0
        else:
            y_target = 12

        if (keys_dict['jump']
                and player_1.y + player_1.rect.height == GROUND_LEVEL):
            player_1.jump()

        player_1.accelerate_x(5, keys_dict['x'])
        player_1.accelerate_y(y_target)

        player_1.calculate_position()

        screen.blit(bg, (0, 0))
        player_1.draw_to(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
