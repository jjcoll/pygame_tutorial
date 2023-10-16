import pygame
from sys import exit
from displaying_images import test_surface

pygame.init()  # starts pygame engine

# creating display surface
screen = pygame.display.set_mode((800, 400))  # tuple with width and height of display window
pygame.display.set_caption('Runner')  # change the window title

# controlling the frame rate
clock = pygame.time.Clock()

while True:
    # look for all possible types of player events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pygame.QUIT is synonym of close button from window
            pygame.quit()  # opposite form pygame.init
            print('Pygame finished')
            exit()  # as we close pygame, we must close while loop
    # draw all our elements
    # update everything

    screen.blit(test_surface, (200, 100))  # put one surface in another surface

    pygame.display.update()  # updates display surface
    clock.tick(60)  # this tells python that while loop should not run faster, than 60 times per second
