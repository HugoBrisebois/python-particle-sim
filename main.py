from cmath import rect
from math import radians
import random
from turtle import circle, color, width
import random
import pygame

# Initialize the pygame window
pygame.init()
surface = pygame.display.set_mode((1080, 640))
clock = pygame.time.Clock()
running = True

# Color vars
color = (255, 192, 203)
red = (255, 0, 0)
blue = (0, 0, 128)
green = (0, 128, 0)



def Draw_Circle():
    
    # vars for the circle function
    radius = 5
    pos = []
    circle_pos = (500, 500)
    
    
    pygame.draw.circle(surface, color, circle_pos, radius, width=0)
    print("circle drawn")


while running:
    # poll for events
    # pygame.QUIT events means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.get_surface()
    
    # fill the screen with a color to wipe away anything from the last frame
    surface.fill("black")
    
    # render the physics engine
    
    # draw a circle
    Draw_Circle()
    
    
    
    # flip() the display to put the physics engine on screen
    pygame.display.flip()
    
        
    
    
pygame.quit()
    


