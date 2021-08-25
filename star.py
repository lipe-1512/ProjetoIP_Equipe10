import pygame, funcoes_game

class star(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """ Constructor function """
        # Call the parent's constructor
        super().__init__()
        #self.treasure_list = pygame.sprite.Group()

        funcoes = funcoes_game.Funcoes_game()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(funcoes.ORANGE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    
    def position(self, walls):

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls,False)
        for block in block_hit_list:
            self.rect.top = block.rect.bottom