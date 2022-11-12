import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, jet, screen):
        super(Bullet, self).__init__()

        self.screen = screen
        self.width = 2
        self.height = 5
        self.bullet_x = jet.x
        self.bullet_y = jet.y
        self.rect = pygame.Rect(self.bullet_x, self.bullet_y, self.width, self.height)


    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)

    def update(self):
        self.bullet_y -= 15
        self.rect.y = self.bullet_y

