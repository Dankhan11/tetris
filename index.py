import pygame
import sys
from game import Game
from Blocks import *
pygame.init()


title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("SCORE", True, (255, 255, 255))

WIN_WIDTH = 500
WIN_HEIGHT = 600
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock() 
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:    
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
            
            
                
            
    #drawing         
    screen.fill(dark_blue)  
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)

