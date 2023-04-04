import pygame
import random
import time

class Particle:

    def __init__(self, x, y, span, size, dx, dy, g):
        self.x = x
        self.y = y
        self.dy = dy
        self.dx = dx
        self.rect = pygame.Rect(x, y, size, size)
        self.life_span = span
        self.start_time = time.time()
        self.size = size
        self.dead = False
        self.gravity = g

    def update(self, change, rand, rects):
        self.dy += random.uniform(-rand, rand)
        self.dx += random.uniform(-rand, rand)
        self.size -= change
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        
        self.x += self.dx
        self.y += self.dy
        if self.size == 0:
            del self
            
    def draw(self, screan, color):
        pygame.draw.circle(screan, color, (self.x, self.y), self.size)

    def checkDeath(self):
        return time.time() > self.start_time + self.life_span