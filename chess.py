import pygame


# инициализация pygame:
def draw1():
    screen.fill((0, 0, 0))
    for i in range(0, n, 2):
        for j in range(n % 2, n, 2):
            screen.fill(pygame.Color('white'), pygame.Rect(i * lenKv, j * lenKv, lenKv, lenKv))
    for i in range(1, n, 2):
        for j in range((n + 1) % 2, n, 2):
            screen.fill(pygame.Color('white'), pygame.Rect(i * lenKv, j * lenKv, lenKv, lenKv))


pygame.init()
width, n = [int(x) for x in input().split()]
height = width
size = width, height
lenKv = width / n
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
draw1()
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()