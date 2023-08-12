from grid import Grid
from all_blocks import *
import random
import pygame

pygame.init()
title_font = pygame.font.Font(None, 40)
title_font2 = pygame.font.Font(None, 20)
#Game Over Serface
game_over_text = title_font.render("Game Over!", True, (255,255,255))
game_over_text2 = title_font2.render("Press any key to continue the game.", True, (255,255,255))
game_over_rect = pygame.Rect(40,240,250,100)

class Game:
    def __init__(self):
        self.grid = Grid()
        self.all_blocks = [I_block(), J_block(), L_block(), O_block(), S_block(), T_block(), Z_block()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

    #Updating Score
    def update_score(self, line):
        if line>=1:
            self.score+=line*10

    #COLLECTING A BLOCK
    def get_random_block(self):
        if len(self.all_blocks)==0:
            self.all_blocks = [I_block(), J_block(), L_block(), O_block(), S_block(), T_block(), Z_block()]
        block = random.choice(self.all_blocks)
        self.all_blocks.remove(block)
        return block

    #RESPONSE WITH KEY
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside()== False or self.block_fits()==False:
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits()==False:
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits()==False:
            self.current_block.move(-1, 0)

            # Lock the moving block to static
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            self.grid.grid[tile.row][tile.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()

        #GAME MAIN THEME: IF FULL ANY ROW THEN REMOVE
        rows_clear = self.reset_row()
        self.update_score(rows_clear)
        if self.block_fits()==False:
            self.game_over = True

    #After Game Over reseting the window
    def reset(self):
        self.grid.reset()
        self.all_blocks = [I_block(), J_block(), L_block(), O_block(), S_block(), T_block(), Z_block()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def is_full(self, row):
        for c in range(self.grid.num_cols):
            if self.grid.grid[row][c] == 0:
                return False
        return True

    def clear_row(self, row):
        for c in range(self.grid.num_cols):
            self.grid.grid[row][c] = 0

    def moving_down(self, row, complete):
        for c in range(self.grid.num_cols):
            self.grid.grid[row+complete][c] = self.grid.grid[row][c]
            self.grid.grid[row][c] = 0

    def reset_row(self):
        complete = 0
        for c in range(self.grid.num_rows -1,0,-1):
            if self.is_full(c):
                self.clear_row(c)
                complete+=1
            elif complete>0:
                self.moving_down(c, complete)
        return complete



    #If the block fit or not in the cell
    def block_fits(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            if self.grid.grid[tile.row][tile.column] != 0 :
                return False
        return True


    #OPERATION OF ROTATION
    def move_rotation(self):
        self.current_block.rotate()
        if self.block_inside() == False:
            #then undo the rotation:
            self.current_block.un_rotate()

    # CHECK OVERFLOW CONDITION
    def is_inside(self, row, column):
        if row >= 0 and row < 20 and column >= 0 and column < 10:
            return True
        return False

    def block_inside(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            if self.is_inside(tile.row, tile.column) == False:
                return False
        return True

    # draw the whole game
    def draw(self, display):
        self.grid.draw_grid(display)
        if self.game_over == False:
            self.current_block.draw(display,11,11)
            self.next_block.draw(display,270,300)
        elif self.game_over == True:
            self.next_block.draw(display, 270, 300)
            pygame.draw.rect(display, (59, 85, 162), game_over_rect, 0, 10)
            display.blit(game_over_text, (85, 265, 50, 50))
            display.blit(game_over_text2, (50, 300, 50, 50))

