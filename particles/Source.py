import pygame
import particles.Particle
import random
import time


class Source:

    def __init__(self, x=0, y=0):
        self.particles = []
        self.x = x
        self.y = y
		
    def emmit(self, life_span, particle, size = 3, amount = 1, dx = 0, dy = 0, gravity = 0.1):
        for i in range(amount):
            self.particles.append(particle(self.x, self.y, life_span, size, dx, dy, gravity))
		
    def update(self, rand = 0.2, change = 0.1, rects = [], b = 2, delta_time = 1):
        for part_num, part in enumerate(self.particles):
            part.update(change, rand, rects, b, delta_time)
            if part.checkDeath():
                del self.particles[part_num]
    def setSource(self, x, y):
        self.x, self.y = x, y

    def draw_rand(self, screan):
        for particle in self.particles:
            particle.draw(screan, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))

    def draw_light(self, screan, color, light_size):
        for particle in self.particles:
            particle.draw_light(screan, color, light_size = light_size)

    def draw(self, screan, color):
        for particle in self.particles:
            particle.draw(screan, color)

    def draw_rect(self, screan, color):
        for particle in self.particles:
            particle.draw_rect(screan, color)

    def print_length(self):
        print(len(self.particles))
