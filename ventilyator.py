import pygame
import math

pygame.init()
size = width, height = 201, 201
screen = pygame.display.set_mode(size)
pygame.display.flip()
clock = pygame.time.Clock();


class Triangle:
    def __init__(self, rotation, r=70, color=pygame.Color('white'), v=0):
        self.rotation = rotation
        self.r = r
        self.color = color
        self.v = v

    def pos(self):
        return [(100, 100),
                (100 + math.cos(self.rotation) * self.r,
                 100 - math.sin(self.rotation) * self.r),
                (100 + math.cos(self.rotation + 30) * self.r,
                 100 - math.sin(self.rotation + 30) * self.r)]

    def draw(self):
        pygame.draw.circle(screen, pygame.Color('white'), (100, 100), 10, 0)
        pygame.draw.polygon(screen, self.color, [(100, 100),
                                                 (100 + math.cos(self.rotation/57) * self.r,
                                                  100 - math.sin(self.rotation/57) * self.r),
                                                 (100 + math.cos((self.rotation + 30)/57) * self.r,
                                                  100 - math.sin((self.rotation + 30)/57) * self.r)], 0)

    def update(self, tick):
        self.rotation += tick * self.v / 1000
        self.rotation %= 360


triangles = []
triangles.append(Triangle(75))
triangles.append(Triangle(195))
triangles.append(Triangle(315))

running = True
while running:
    tick = clock.tick(100)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for t in triangles:
                    t.v += 50
            elif event.button == 3:
                for t in triangles:
                    t.v -= 50

    for t in triangles:
        t.update(tick)
        t.draw()
    pygame.display.flip()
