import pygame


def handle_keys():
    events_dict = {'keep_running': True,
                   'x': 0,
                   'y': 0,
                   'jump': False}
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            events_dict['keep_running'] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                events_dict['keep_running'] = False
            if event.key == pygame.K_SPACE:
                events_dict['jump'] = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        events_dict['x'] = -1
    if keys[pygame.K_RIGHT]:
        events_dict['x'] = 1

    return events_dict
