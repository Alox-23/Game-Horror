import pygame
import random
import time
import light

class Particle:

    def __init__(self, x, y, span, size, dx, dy, g):
        self.x = x
        self.y = y
        self.dy = dy
        self.dx = dx
        self.gravity = g
        self.rect = pygame.Rect(x, y, size, size)
        self.life_span = span
        self.start_time = time.time()
        self.size = size
        self.dead = False
        self.light = light.light()

    def update(self, change, rand, rects, b, delta_time):
        self.dy += random.uniform(-rand, rand)
        self.dx += random.uniform(-rand, rand)
        self.size -= change
        self.rect = pygame.Rect(self.x, self.y, self.size*2, self.size*2)
        
        self.x += self.dx * delta_time
        self.y += self.dy * delta_time
        if self.size == 0:
            del self
            
    def draw(self, screan, color):
        pygame.draw.circle(screan, color,(self.rect.centerx, self.rect.centery), self.size)

    def draw_rect(self, screan, color):
        pygame.draw.rect(screan, color,self.rect)

    def draw_light(self, screan, color, light_size):
        r = self.size * light_size
        if r > 0:
            screan.blit(self.light.circle(r, color), (self.x-r//2, self.y-r //2), special_flags = pygame.BLEND_RGB_ADD)

    def checkDeath(self):
        return time.time() > self.start_time + self.life_span