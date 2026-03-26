from cmath import rect
from math import radians
from turtle import color, width

import pygame

# Initialize the pygame window
pygame.init()
surface = pygame.display.set_mode((1080, 640))
clock = pygame.time.Clock()
color = (255, 192, 203)
running = True

while running:
    # poll for events
    # pygame.QUIT events means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.get_surface()
    
    # fill the screen with a color to wipe away anything from the last frame
    surface.fill("purple")
    
    # render the physics engine
    pygame.draw.rect(surface, color, pygame.Rect(30,30,60,60))
    
    
    
    # flip() the display to put the physics engine on screen
    pygame.display.flip()
    pygame.time.wait(3000) # wait for 3 seconds
        
    
    
pygame.quit()
    


