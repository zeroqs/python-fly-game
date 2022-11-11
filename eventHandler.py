from imports import pygame,sys,screen,jet


def event_handler():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        screen.fill((0, 0, 0))
        jet.draw()
        jet.move(keys)
        pygame.display.flip()
        pygame.time.Clock().tick(30)