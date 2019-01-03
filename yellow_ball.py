import pygame

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.flip()
clock = pygame.time.Clock();


def draw():
    pygame.draw.circle(screen, pygame.Color("yellow"), pos, r)


ball = False
running = True
while running:
    tick = clock.tick(30)
    screen.fill(pygame.Color("blue"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            ball = True
            r = 0

    if ball:
        r += tick // 10
        draw()
    pygame.display.flip()
