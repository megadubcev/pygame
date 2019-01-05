import pygame

pygame.init()
size = width, height = 501, 501
screen = pygame.display.set_mode(size)
pygame.display.flip()
clock = pygame.time.Clock();
v = [0, 0]
r = 20
pos = [250, 250]
pos2 = pos


def draw():
    pygame.draw.circle(screen, pygame.Color("red"), pos, r)


def update():
    deltax = pos2[0] - pos[0]
    deltay = pos2[1] - pos[1]
    if deltax:
        v[0] = abs(deltax) // deltax * 50
    else:
        v[0] = 0
    if deltay:
        v[1] = abs(deltay) // deltay * 50
    else:
        v[1] = 0
    if not v[0]:
        v[1] *= 2
    if not v[1]:
        v[0] *= 2
    pos[0] += v[0] * tick // 1000
    pos[1] += v[1] * tick // 1000


running = True
while running:
    tick = clock.tick(50)
    screen.fill(pygame.Color("black"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos2 = event.pos

    update()
    draw()
    pygame.display.flip()
