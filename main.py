import pygame, sys, particles, random

pygame.init()
p = particles.Source.Source(200, 150)
screan = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
Clock = pygame.time.Clock()
span = 2
e = False
while True:
    screan.fill('black')
    p.setSource(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    p.update(rects = [pygame.Rect(150, 150, 100, 100), pygame.Rect(70, 50, 20, 100), pygame.Rect(150, 70, 100, 20)], change = 0.1, b = 1, rand = 0.1)
    p.draw(screan,  (255, 0, 0))
    pygame.draw.rect(screan, (255, 255, 255),(150, 150, 100, 100))
    pygame.draw.rect(screan, (255, 255, 255),(70, 50, 20, 100))
    pygame.draw.rect(screan, (255, 255, 255),(150, 70, 100, 20))
    Clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            e = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            e = True
    if e:
        p.emmit(5, particles.Particle.Particle, size = 5, gravity = 0.1)
        p.emmit(0.5, particles.gravParticle.gravParticle, size = 5, gravity = 0)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        span += 0.01
    elif keys[pygame.K_DOWN]:
        span -= 0.01
    pygame.display.update()
 