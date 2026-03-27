from ast import Pass

import pygame

# Initialize the pygame window
pygame.init()

# define width of screen
width = 1000
# define height of screen
height = 600
screen_res = (width, height)

screen = pygame.display.set_mode(screen_res)

# define colors
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 180,0)
blue = (0,0, 180)

# define speed of ball
# speed = [X direction speed, Y direction speed]
speed = [0.5, 0.5]

    # define ball
ball_obj = pygame.draw.circle(surface=screen, color=red, center=[25, 25], radius=5)


class Ball:
    def __init__(self, x,y, radius, speed_x, speed_y, color):
        # initialize a ball with position, size and speed
        self.rect = pygame.draw.circle(surface= screen, color=color, center=[x,y], radius=radius)
        self.speed = [speed_x, speed_y]
        self.radius = radius
        self.color = color
    
    def move(self):
        # move the ball
        self.rect = self.rect.move(self.speed)
        
    def check_bound(self, width, height):
        # check if ball hits walls and reverse direction
        if self.rect.left <= 0 or self.rect.right >= width:
            self.speed[0] = -self.speed[0]  # Fixed: was -speed[0]
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speed[1] = -self.speed[1]
            
    def draw(self, surface):
        # draw the ball on screen
        pygame.draw.circle(surface=surface, color=self.color, center=self.rect.center, radius=self.radius, width=0)  # Fixed: was Surface=


balls = [
    Ball(100, 100, 5, 1, 1, red),
    Ball(300, 200, 5, -0.7, 1, blue),
    Ball(500, 400, 5, 1, -0.8, green),
    Ball(200, 150, 5, 2, 1.5, red),
    Ball(700, 300, 5, -1.2, -0.9, blue),
    Ball(800, 100, 5, 0.8, 2, green),
    Ball(150, 450, 5, -1.5, 0.7, red),
    Ball(600, 250, 5, 1.3, -1.2, blue),
    Ball(350, 50, 5, -0.9, 1.8, green),
    Ball(900, 500, 5, 2.1, -0.5, red),
    Ball(50, 300, 5, -1.8, 1.1, blue),
    Ball(750, 450, 5, 1.4, -1.6, green),
    Ball(450, 350, 5, -0.6, 2.2, red),
    Ball(250, 80, 5, 1.7, 0.8, blue),
    Ball(650, 180, 5, -2, -1.3, green),
    Ball(120, 520, 5, 1.1, -1.9, red),
    Ball(850, 220, 5, -1.4, 1.6, blue),
    Ball(550, 120, 5, 1.9, 0.4, green),
    Ball(320, 480, 5, -0.8, -2.1, red),
    Ball(780, 380, 5, 1.6, 1.3, blue),
]


# game loop
while True:
    # event loop
    for event in pygame.event.get():
        # check if a user wants to exit the game or not
        if event.type == pygame.QUIT:
            exit()

    # fill black color on screen
    screen.fill(black)

    # update and draw all balls
    for ball in balls:
        ball.move()
        ball.check_bound(width,height)
        ball.draw(screen)

    # update screen
    pygame.display.flip()


pygame.quit()



