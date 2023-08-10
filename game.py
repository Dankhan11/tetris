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

    def draw(self, screen):
        self.current_block.draw(screen)
        self.grid.draw(screen)
        
      