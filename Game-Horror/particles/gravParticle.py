import pygame
from particles.Particle import Particle

class gravParticle(Particle):
    def update(self, change, rand, rect):
        self.dy += self.gravity
        self.size -= change
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

        self.x += self.dx
        self.y += self.dy