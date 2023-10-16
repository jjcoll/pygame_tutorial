# rectangles help precise positioning on surfaces
# they help detect collisions

import pygame

player_surface = pygame.image.load('graphics/player/player_walk_1.png')
# for a surface, we always grap topleft point for a rectangle we can use any point
player_rectangle = player_surface.get_rect(midbottom = (60, 300))  # creates rectangle around player surface
