import pygame, sys, Labirinto

from pygame.constants import K_a, K_d, K_s, K_w

class Funcoes_game():

    def __init__(self) -> None:
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.PURPLE = (255, 0, 255)
        self.YELLOW = (255, 255, 0)
        self.ORANGE = (255, 153, 51)
        # number of treasures
        self.N = 3

        self.TEXT_SIZE = 12

    def checar_eventos(self, player):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == K_a:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT or event.key == K_d:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP or event.key == K_w:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN or event.key == K_s:
                    player.changespeed(0, 5)
                if event.key == pygame.K_ESCAPE:
                    done = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == K_a:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT or event.key == K_d:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP or event.key == K_w:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN or event.key == K_s:
                    player.changespeed(0, -5)

    def checar_colisoes(self, player, done):       
        

        for event in pygame.event.get():
                if event.type == pygame.QUIT:                    
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        player.gameover = False
                        Labirinto.main()

                    if event.key == pygame.K_ESCAPE:
                        done = True
                        player.gameover = False
                        pygame.quit()