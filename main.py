import pygame
from sys import exit
from surfaces import *

pygame.init()
width = 800
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# create a font
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)  # font type and size
text = 'My Game'
anti_alias = False  # smooth text
text_sur = test_font.render(text, anti_alias, 'Black')

# import snail image
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_sur, (10, 10))


    screen.blit(snail_surface, (snail_x_pos, 270))

    snail_x_pos -= 2  # make snail move to the left
    if snail_x_pos < -100:
        snail_x_pos = 800

    pygame.display.update()
    clock.tick(60)