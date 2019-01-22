import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.flip()


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.colors = [pygame.Color("black"), pygame.Color("red"), pygame.Color("blue")]

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, pygame.Color("white"),
                                 (self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size,
                                  self.cell_size), 1)
    def render2(self):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, self.colors[self.board[i][j]],
                                 (self.left + j * self.cell_size + 1, self.top + i * self.cell_size + 1, self.cell_size -2,
                                  self.cell_size -2), 0)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if x < self.left or y < self.top or x > self.left + self.width * self.cell_size or y > self.top + self.height * self.cell_size:
            return None
        j = (x - self.left) // self.cell_size
        i = (y - self.top) // self.cell_size
        return [i, j]

    def on_click(self, cell_coords):
        self.board[cell_coords[0]][cell_coords[1]] = (self.board[cell_coords[0]][cell_coords[1]] + 1) % 3


board = Board(5, 7)


def render2(self):
    for i in range(self.height):
        for j in range(self.width):
            pygame.draw.rect(screen, pygame.Color("white"),
                             (self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size,
                              self.cell_size), 1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)

    screen.fill((0, 0, 0))
    board.render()
    board.render2()
    pygame.display.flip()
