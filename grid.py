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
    
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False   
    
    def is_row_full(self,row):
        #loop through columns in each row checking if it is full 
        for column in range(self.num_columns):
            if self.grid[row][column] == 0: #if empty
                return False
        return True
                
                
    def clear_row(self,row):
        for column in range(self.num_columns):
            self.grid[row][column] = 0
                       

             
        
    def draw(self,screen):
        
        #iterate through grid changing colour checking value of cell in grid
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size + 1,row*self.cell_size + 1,self.cell_size -1 ,self.cell_size -1 )
                pygame.draw.rect(screen,self.color[cell_value],cell_rect )
                
    def is_inside(self, row, column):
        if row >=0 and row< self.num_rows and column >= 0 and column <self.num_columns:
            return True
        else:
            return False