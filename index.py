import pygame
import time
import sys
from grid import Grid

pygame.init()

WIN_WIDTH = 300
WIN_HEIGHT = 600
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock() 

game_grid = Grid()
game_grid.print_grid()
#set colours of cell relative to index of 
game_grid.grid[0][0] = 1
game_grid.grid[3][5] = 4
game_grid.grid[17][8] = 7



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(dark_blue)
    game_grid.draw(screen)
    pygame.display.update()
    clock.tick(60)

