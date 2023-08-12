from grid import Grid
from Blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), ZBlock(), OBlock(), SBlock(), TBlock(), LBlock()]

        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
    
    
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), ZBlock(), OBlock(), SBlock(), TBlock(), LBlock()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
       
    def move_left(self):
        self.current_block.move(0,-1)
        if self.block_inside() == False or self.block_fits() == False:  
            self.current_block.move(0,1)
            
            
        
    def move_right(self):
        self.current_block.move(0,1)
        if self.block_inside() == False or self.block_fits == False:
            self.current_block.move(0,-1)
            
        #downward movement for block - chekcing if block fits or not
    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1,0)
            self.lock_block()
        
     
     #indicate that block has reached its final position 
    def lock_block(self):
        tiles = self.current_block.get_cell_position()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
            
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
                
        
          #check if block is still within the grid boundaries
    def block_inside(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
    
    def block_fits(self):
        tiles = self.current_block.get_cell_position()
        #check if any of the cells are occupied
        for tile in tiles:
           if self.grid.is_empty(tile.row,tile.column) == False:
               return False
        return True
    
    def move_row_down(self, row, num_rows):
       for column in range(self.num_columns):
           #copies value of original row to the new row
           self.grid[row+num_rows][column] = self.grid[row][column]
           self.grid[row][column] = 0
           
    def clear_full_row(self):
        completed = 0
        for row in range(self.num_rows -1, 0, -1):#iterates through rows in reverse 
            if self.is_row_full(row):
                self.clear_full_row(row)
                completed += 1
        
           
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
        
    
    