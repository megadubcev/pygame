import pygame

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.flip()
clock = pygame.time.Clock();


class Rect:
    def __init__(self, pos, pos2, color=pygame.Color('white'), v=(0, 0)):
        self.x = pos[0]
        self.y = pos[1]
        self.x2 = pos2[0]
        self.y2 = pos2[1]
        self.color = color

    def pos(self):
        return int(self.x), int(self.y), int(self.x2 - self.x), int(self.y2 - self.y)
        ptint

    def draw(self):
        pygame.draw.rect(screen, self.color, self.pos(), 2)
        # print(self.pos())


rects = []
rect = None
running = True
while running:
    tick = clock.tick(100)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            rect = Rect(event.pos, event.pos)
            rects.append(rect)
        if event.type == pygame.MOUSEBUTTONUP:
            rect = None
        if rect and event.type == pygame.MOUSEMOTION:
            rect.x2, rect.y2 = event.pos
        if event.type == pygame.KEYDOWN:
            if event.key == 122 and event.mod == 64:
                del rects[len(rects) - 1]
    for r in rects:
        r.draw()
    pygame.display.flip()
