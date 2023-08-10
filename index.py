import pygame
import sys
from game import Game
from Blocks import *
pygame.init()

WIN_WIDTH = 300
WIN_HEIGHT = 600
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock() 
game = Game()
block = IBlock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(dark_blue)  
    game.draw(screen)
    block.draw(screen)
    
    pygame.display.update()
    clock.tick(60)

