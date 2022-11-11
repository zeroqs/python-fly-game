from eventHandler import event_handler
from imports import pygame


def run():
    pygame.init()
    pygame.display.set_caption("Jet fly")
    event_handler()


run()
