import pygame

pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
pygame.display.flip()
clock = pygame.time.Clock();
posrect = (0, 0, 100, 100)


def draw():
    pygame.draw.rect(screen, pygame.Color("green"), posrect, 0)


draw()
running = True
mouse = False
while running:
    tick = clock.tick(100)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] >= posrect[0] and event.pos[1] >= posrect[1] and \
                event.pos[0] <= posrect[0] + posrect[2] and event.pos[1] <= posrect[1] + posrect[3]:
            mouse = True
            pos0 = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse = False

        elif event.type == pygame.MOUSEMOTION and mouse:
            pos1 = event.pos
            posrect = (posrect[0] + pos1[0] - pos0[0], posrect[1] + pos1[1] - pos0[1], 100, 100)
            pos0 = pos1
        draw()

        pygame.display.flip()
