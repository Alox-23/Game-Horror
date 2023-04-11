import pygame
from light.lightCircle import lightCircle

class lightMask(lightCircle):
	def __init__(self, mask, size = (50, 50), colorkey = (0,0,0)):
		self.size = size
		self.sizex = size[0]
		self.sizey = size[1]
		self.img = mask
		self.img = pygame.transform.scale(self.img, size)
		self.img.set_colorkey(colorkey)