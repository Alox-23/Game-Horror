"""
    -----------------------------------
    |                                 |
    |       WARNING THIS FILE IS FOR  |
    |           TESTING PURUSES!      |
    |                                 |
    -----------------------------------
"""
import pygame
print("light init")

class light:
    def circle(self, radius, color):
        img = pygame.Surface((radius * 2 + 0.1, radius * 2+ 0.1))
        pygame.draw.circle(img, color, (radius, radius), radius)
        img.set_colorkey((0, 0, 0))
        return img