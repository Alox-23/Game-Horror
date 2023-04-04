import pygame
from particles.gravParticle import gravParticle
import math

class pycParticle(gravParticle):
    def checkCollide(self, rects):
        hit = False
        for rect in rects:
            if pygame.Rect.colliderect(self.rect, rect):
                hit = True
                if self.dy > 0:
                    self.dy = -self.dy // 2
                if self.dx > 0:
                    self.dx = -self.dx
                if self.rect.bottom == rect.top:
                    self.dy = -self.dy
                if self.rect.top == rect.bottom:
                    self.dy = self.dy
                if self.rect.right == rect.left:
                    self.dx = -self.dx
                if self.rect.left == rect.right:
                    self.dx = self.dx
        return hit

    def update(self, change, rand, rects):
        self.dy += self.gravity
        self.size -= change
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

        self.checkCollide(rects)
        self.x += self.dx
        self.y += self.dy