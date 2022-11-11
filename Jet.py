import pygame


class Jet:
    def __init__(self, screen, width, height, THECOLORS, sprite):
        self.end_width = width - 100
        self.end_height = height - 100
        self.sprite = sprite
        self.screen = screen
        self.color = THECOLORS['orange']
        self.x = width // 2
        self.y = height - 100

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= 15
        elif keys[pygame.K_RIGHT] and self.x <= self.end_width:
            self.x += 15
        elif keys[pygame.K_UP] and self.y > 0:
            self.y -= 10
        elif keys[pygame.K_DOWN] and self.y <= self.end_height:
            self.y += 10