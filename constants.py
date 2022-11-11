from imports import *

width, height = 1200, 800

screen = pygame.display.set_mode((width, height))
sprite = pygame.image.load("plane.png")

jet = Jet(screen, width, height, THECOLORS,sprite)