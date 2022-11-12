import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, jet, screen):
        super(Bullet, self).__init__()

        self.screen = screen
        self.width = 2
        self.height = 5
        self.bullet_x = jet.x + 25
        self.bullet_x_second = jet.x + 65
        self.bullet_y = jet.y + 60
        self.rect = pygame.Rect(self.bullet_x, self.bullet_y, self.width, self.height)
        self.rect_second = pygame.Rect(self.bullet_x_second, self.bullet_y, self.width, self.height)


    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect_second)

    def update(self):
        self.bullet_y -= 15
        self.rect.y = self.bullet_y
        self.rect_second.y = self.bullet_y

