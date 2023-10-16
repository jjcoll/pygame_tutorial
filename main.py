import pygame
from sys import exit
from surfaces import *


pygame.init()
width = 800
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Runner')

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))



    pygame.display.update()
    clock.tick(60)