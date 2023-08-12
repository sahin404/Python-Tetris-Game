import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.color_house()

    def reset(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0

    #DRAW THE GAME INTERFACE
    def draw_grid(self, display):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                cell_value = self.grid[i][j]
                cell_rect = pygame.Rect(j*self.cell_size+11, i*self.cell_size+11, self.cell_size-1, self.cell_size-1)
                pygame.draw.rect(display, self.colors[cell_value],cell_rect)
