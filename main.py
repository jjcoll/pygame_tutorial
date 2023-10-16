import pygame
from sys import exit
from surfaces import *
from rectangles import *

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
snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 600
snail_rectangle = snail_surface.get_rect(bottomright = (600, 300))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface.convert(), (0, 0))
    screen.blit(ground_surface.convert(), (0, 300))
    screen.blit(text_sur, (10, 10))
    screen.blit(player_surface.convert_alpha(), player_rectangle)
    screen.blit(snail_surface.convert_alpha(), snail_rectangle)

    snail_rectangle.x -= 2
    if snail_rectangle.right < 0:
        snail_rectangle.left = 800


    pygame.display.update()
    clock.tick(60)
