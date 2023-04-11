import pygame
import random
import time
import light


class Particle:

    def __init__(self,
                 x,
                 y,
                 span,
                 size,
                 dx,
                 dy,
                 g,
                 light_type=light.lightCircle,
                 light_radius=5,
                 light_color=(50, 50, 50),
                 light_mask=0,
                 colorkey=(0, 0, 0),
                 light_size=(10, 10)):
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
        self.light_type = light_type
        if self.light_type == light.lightCircle:
            self.light = light_type(light_radius, light_color)

        elif self.light_type == light.lightMask:
            self.light = light_type(light_mask,
                                    size=light_size,
                                    colorkey=colorkey)

    def update(self, change, rand, rects, b, delta_time):
        self.dy += random.uniform(-rand, rand)
        self.dx += random.uniform(-rand, rand)
        self.size -= change * delta_time
        self.rect = pygame.Rect(self.x, self.y, self.size * 2, self.size * 2)

        self.x += self.dx * delta_time
        self.y += self.dy * delta_time

    def draw(self, screan, color):
        pygame.draw.circle(screan, color,
                           (self.rect.centerx, self.rect.centery), self.size)

    def draw_rect(self, screan, color):
        pygame.draw.rect(screan, color, self.rect)

    def draw_light(self, screan, size):
        if self.light_type == light.lightCircle:
            self.light.draw(screan,
                        self.x - self.light.rad,
                        self.y - self.light.rad,
                        size=self.size * size)
        elif self.light_type == light.lightMask:
            self.light.draw(screan,
                        self.x - self.light.sizex//2,
                        self.y - self.light.sizey//2,
                        size=self.size * size)

    def checkDeath(self):
        return time.time() > self.start_time + self.life_span
