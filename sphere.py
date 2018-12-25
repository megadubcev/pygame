import pygame


# инициализация pygame:
def draw1():
    screen.fill((0, 0, 0))
    for i in range(n):
        pygame.draw.ellipse(screen, pygame.Color("white"), (150 - (i + 1) * lenKv, 0, 2 * (i + 1) * lenKv, 300), 1)
        pygame.draw.ellipse(screen, pygame.Color("white"), (0, 150 - (i + 1) * lenKv, 300, 2 * (i + 1) * lenKv), 1)


pygame.init()
n = int(input())
size = width, height = 300, 300
lenKv = width / n / 2
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
draw1()
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()