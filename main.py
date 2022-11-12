import pygame
from events_handler import *
from pygame.sprite import Group

def run():
    pygame.init()
    pygame.display.set_caption("Jet fly")
    bullets = Group()
    while True:
        events_handler(bullets)
        bullets.update()
        refresh_screen(bullets)
        pygame.time.Clock().tick(30)


if __name__ == '__main__':
    run()
