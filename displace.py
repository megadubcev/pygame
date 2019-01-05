import pygame

pygame.init()
size = width, height = 201, 201
screen = pygame.display.set_mode(size)
pygame.display.flip()
clock = pygame.time.Clock();


def draw():
    font = pygame.font.Font(None, 100)
    text = font.render(str(n), 1, pygame.Color("red"))
    screen.blit(text, (75, 75))


n = 1
running = True
while running:
    tick = clock.tick(30)
    screen.fill(pygame.Color("black"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == 1 and event.state == 6 and event.gain == 0:
            n += 1
    draw()
    pygame.display.flip()
