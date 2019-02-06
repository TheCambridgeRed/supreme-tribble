import pygame
import os
import handle_keys


def main():
    pygame.init()
    clock = pygame.time.Clock()

    player_x = 20
    player_y = 380

    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540

    PLAYER_SPEED = 5

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pygame')

    bg = pygame.image.load(os.path.join('data', 'bg.png'))
    player = pygame.image.load(os.path.join('data', 'char.png'))
    player.set_colorkey((255, 255, 255))
    player_rect = player.get_rect()

    running = True
    jumping = False
    jump_count = 10
    neg = 1

    while running:

        screen.blit(bg, (0, 0))
        screen.blit(player, (player_x, player_y))

        pygame.display.flip()

        keys_dict = handle_keys.handle_keys(PLAYER_SPEED)
        if not keys_dict['keep_running']:
            running = False

        if keys_dict['jump']:
            jumping = True

        if jumping:
            if jump_count == 0:
                neg *= -1

            if jump_count < -10:
                jump_count = 10
                jumping = False
                neg = 1
            else:
                player_y -= (jump_count ** 2) * 0.4 * neg
                jump_count -= 1

        if (not player_x + keys_dict['x'] < 0 and
                not player_x + keys_dict['x'] >
                SCREEN_WIDTH - player_rect.width):
            player_x += keys_dict['x']
        if (not player_y + keys_dict['y'] < 0 and
                not player_y + keys_dict['y'] >
                SCREEN_HEIGHT - player_rect.height):
            player_y += keys_dict['y']

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
