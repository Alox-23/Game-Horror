import pygame, time, sys, particles, random

pygame.init()
p = particles.Source.Source(200, 150)
screan = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')
Clock = pygame.time.Clock()
span = 2
rects = [
    pygame.Rect(random.randint(0, 800), random.uniform(0, 600), random.randint(10, 100), random.randint(10, 100)) for i in range(100)
]
last_time = time.time()
FPS = 60
tFPS = 60
e = False
while True:
    dt = time.time() - last_time
    dt *= tFPS
    print(dt)
    last_time= time.time()
    screan.fill('black')
    p.setSource(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    p.update(rects = rects, change = 0.00, b = 1, rand = 0.1, delta_time = dt)
    p.draw(screan,  (255, 0, 0))
    pygame.display.set_caption(str(int(Clock.get_fps())))
    for i in rects:
        pygame.draw.rect(screan, (255, 255, 255), i)
    Clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            e = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            e = True
    if e:
        p.emmit(1, particles.pycParticle.pycParticle, amount = 1,size = 1, gravity = 0.1, dx = random.uniform(-2, 2), dy = random.uniform(-2, 0))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        FPS += 0.1
    elif keys[pygame.K_DOWN]:
        FPS -= 0.1
    pygame.display.update()
 