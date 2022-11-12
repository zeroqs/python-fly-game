from Bullet import Bullet
from constants import jet, sys, screen
import pygame

def events_handler(bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(jet, screen)
                bullets.add(bullet)
    keys = pygame.key.get_pressed()
    jet.move(keys)


def refresh_screen(bullets):
    for bullet in bullets.sprites():
        bullet.draw()
    jet.draw()
    pygame.display.flip()
    screen.fill((0, 0, 0))


def clear_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))