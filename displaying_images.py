import pygame
"""
To display images we need a surface
Display surface -> the game window. Anything displayed goes here
regular surface -> single image (something imported, rendered text or plain color) needs to be put on display surface
to be visible

Imagine you placing several surface on the display surface
-- we can only have one display surface, and it is always visible
-- we can have many regular surfaces and only displayed when attached to display surface
"""

test_surface = pygame.Surface((100, 200))
test_surface.fill('red')

test_surface_img = pygame.image.load('graphics/Sky.png')