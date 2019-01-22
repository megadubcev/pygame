import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.flip()


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

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
                                  self.cell_size), self.board[i][j])

    def get_click(self, mouse_pos):
        self.get_cell(mouse_pos)


    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if x < self.left or y < self.top or x > self.left + self.width * self.cell_size or y > self.top + self.height * self.cell_size:
            print(None)
        else:
            j = (x - self.left) // self.cell_size
            i = (y - self.top) // self.cell_size
            print((j, i))



board = Board(5, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)

    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()