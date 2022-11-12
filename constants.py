from Jet import Jet
import pygame
import sys
from pygame.color import THECOLORS
width, height = 1200, 800

screen = pygame.display.set_mode((width, height))
sprite = pygame.image.load("plane.png")

jet = Jet(screen, width, height, sprite)