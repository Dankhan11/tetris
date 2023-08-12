import pygame
from colours import Colours
from position import Position

class Block:
    def __init__(self,id):
        self.id = id 
        self.cells = {} # used to store occupied cells for each rotated block 
        self.cell_size = 30
        self.rotation_state = 0
        #store row and column offset 
        self.row_offset = 0
        self.column_offset = 0 
        
        self.colours = Colours.get_cell_colours()
               
    def move(self, rows, column):
        self.row_offset += rows
        self.column_offset += column
        
        
        #retreives the cells array based on the rotation state
    def get_cell_position(self):
        tiles = self.cells[self.rotation_state]
        #empty array to store the moved tiles 
        moved_tiles = []
        
        #update position of tiles 
        for position in tiles:
            position = Position(position.row +self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles
    
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0
            
    def undo_rotation(self):
        if self.rotation_state < 0:
            self.rotation_state = len(self.cells)      
        self.rotation_state -= 1  
            
    def draw(self, screen):
        tiles = self.get_cell_position() #retreives the cells array based on the rotation state
        
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1,
                                    self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colours[self.id], tile_rect)
       
   
            
        
    