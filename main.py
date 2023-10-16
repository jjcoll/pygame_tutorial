import pygame
from sys import exit
from surfaces import *
from rectangles import *
from quotes import get_quote

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

text_sur_2 = test_font.render('You have lost', anti_alias, 'Red')
text_rect_2 = text_sur_2.get_rect(center = (400, 200))

# import snail image
snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 600
snail_rectangle = snail_surface.get_rect(bottomright = (600, 300))

# # speech box
# speech_surf = pygame.image.load('graphics/speech_box.png')
# speech_rect = speech_surf.get_rect(center = (400, 200))
# speech_font = pygame.font.Font('font/Pixeltype.ttf', 40)

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


    if not snail_rectangle.colliderect(player_rectangle):
        snail_rectangle.x -= 2
        if snail_rectangle.right < 0:
            snail_rectangle.left = 800
    else:
        screen.blit(text_sur_2, text_rect_2)

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rectangle.collidepoint((mouse_pos)):
    #     if pygame.mouse.get_pressed()[0] == True:
    #         speech_rect.bottomleft = player_rectangle.topright
    #         screen.blit(speech_surf, speech_rect)
    #         speech_text_sur = speech_font.render(get_quote(), False, 'Black')
    #         speech_text_rec = speech_text_sur.get_rect(center = speech_rect.center)
    #         screen.blit(speech_text_sur, speech_text_rec)
    #
    #         print('pressed')



    pygame.display.update()
    clock.tick(60)
