import pygame
from Labirinto import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)

swallows = pygame.sprite.Group()
class Treasure(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """
 
    def __init__(self, x, y):
        """ Constructor function """
        # Call the parent's constructor
        super().__init__()
        #self.treasure_list = pygame.sprite.Group()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(YELLOW)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    
    def position(self, walls):

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls,False)
        for block in block_hit_list:
            self.rect.top = block.rect.bottom
