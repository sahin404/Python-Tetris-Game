import pygame
from position import Position
from colors import Colors


class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.row_offset = 0
        self.column_offset = 0
        self.colors = Colors.color_house()
    #rotation method
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == 4:
            self.rotation_state = 0
        return self.rotation_state

    #If the Rotation is Overflow condition then Undo the previous rotation
    def un_rotate(self):
        self.rotation_state -= 1
        return self.rotation_state

    #Adding, PROCESSING AND PRINTING THE NEW POSITION OF BLOCK
    def move(self, rows, columns):
        self.row_offset = self.row_offset + rows
        self.column_offset = self.column_offset + columns

    def get_cell_position(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row+self.row_offset, position.column+self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def draw(self, display, x,y):
        tiles = self.get_cell_position()
        for tile in tiles:
            create_rect = pygame.Rect(tile.column*self.cell_size+x,tile.row*self.cell_size+y, self.cell_size-1, self.cell_size-1)
            pygame.draw.rect(display, self.colors[self.id], create_rect)



