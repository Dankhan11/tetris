import pygame
from colours import Colours
class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_columns = 10
        self.cell_size = 30 
        
        #list comprehension to make the grid 
        self.grid = [[0 for j in range(self.num_columns)] for i in range(self.num_rows)]
        self.color = Colours.get_cell_colours()
        
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                print(self.grid[row][column], end = " ")
            print()
    
    
        
    def draw(self,screen):
        
        #iterate through grid changing colour checking value of cell in grid
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size + 1,row*self.cell_size + 1,self.cell_size -1 ,self.cell_size -1 )
                pygame.draw.rect(screen,self.color[cell_value],cell_rect )
                