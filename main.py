import pygame

# physics engine
import pymunk

# initialize the physics engine


# define global variables
display = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
space = pymunk.Space()
FPS = 50

body = pymunk.Body()
body.position = 400, 400
shape = pymunk.Circle(body, 10)
spcae.add(body, shape)


# Initialize the pygame window
pygame.init()

def sim():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill display with the color white
        display.fill((255,255,255))
        pygame..draw.circle()


        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

sim()
pygame.quit()



