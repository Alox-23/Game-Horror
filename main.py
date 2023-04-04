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
    p.update(rects = [pygame.Rect(150, 150, 100, 10)], change = 0.0)
    p.draw(screan,  (255, 0, 0))
    pygame.draw.rect(screan, (255, 255, 255),(150, 150, 100, 100), )
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
        p.emmit(5, particles.pycParticle.pycParticle, dx = 0, size = 5)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        span += 0.01
    elif keys[pygame.K_DOWN]:
        span -= 0.01
    pygame.display.update()
 