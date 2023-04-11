import pygame

class lightCircle:
    def __init__(self, radius, color, size):
        self.rad = radius
        self.size = size
        self.img = pygame.Surface((radius * 2 + 0.1, radius * 2+ 0.1))
        pygame.draw.circle(self.img, color, (radius, radius), radius)
        self.img.set_colorkey((0, 0, 0))

    def draw(self,screan, x, y, size):
	    screan.blit(pygame.transform.scale(self.img, self.size), (x, y), special_flags = pygame.BLEND_RGB_ADD)
		