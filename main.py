import pygame

# Initialize the pygame window
pygame.init()

def window() -> None:
    pygame.display.set_mode((800, 600))
    # pygame.display.init() is redundant; set_mode initializes it

