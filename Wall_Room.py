import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)


class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """
 
    def __init__(self, x, y, width, height, color):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x



class Room(object):
    """ Base class for all rooms. """

    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


class Room1(Room):
    """This creates all the walls in room 1"""

    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 600, WHITE],
                 [780, 0, 20, 600, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 500, BLUE],
                 [330, 80, 20, 380, BLUE],
                 [130, 80, 20, 200, BLUE],
                 [150, 260, 180, 20, BLUE],
                 [240, 20, 20, 150, BLUE],
                 [450, 80, 330, 20, BLUE],
                 [450, 100, 20, 150, BLUE],
                 [450, 250, 170, 20, BLUE],
                 [620, 250, 20, 150, BLUE],
                 [20, 370, 170, 20, BLUE],
                 [190, 370, 20, 150, BLUE],
                 [460, 350, 20, 230, BLUE]
                 ]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room2(Room):
    """This creates all the walls in room 2"""

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 600, RED],
                 [780, 0, 20, 600, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [330, 230, 120, 20, RED],
                 [330, 250, 20, 100, RED],
                 [330, 350, 120, 20, RED],
                 [450, 290, 330, 20, RED],
                 [220, 95, 20, 420, RED],
                 [240, 160, 370, 20, RED],
                 [340, 95, 365, 20, RED],
                 [700, 95, 20, 195, RED],
                 [240, 440, 370, 20, RED],
                 [670, 400, 20, 180, RED],
                 [410, 510, 20, 70, RED],
                 [20, 120, 120, 20, RED],
                 [100, 210, 120, 20, RED],
                 [20, 300, 120, 20, RED],
                 [100, 390, 120, 20, RED],
                 [20, 480, 120, 20, RED]
                 ]


        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room3(Room):
    """This creates all the walls in room 3"""

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 600, PURPLE],
                 [780, 0, 20, 600, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE],
                 [330, 85, 20, 410, PURPLE],
                 [130, 85, 200, 20, PURPLE],
                 [130, 475, 200, 20, PURPLE],
                 [130, 105, 20, 135, PURPLE],
                 [130, 340, 20, 135, PURPLE],
                 [150, 340, 120, 20, PURPLE],
                 [250, 360, 20, 60, PURPLE],
                 [150, 220, 120, 20, PURPLE],
                 [250, 160, 20, 60, PURPLE],
                 [450, 85, 20, 410, PURPLE],
                 [470, 85, 200, 20, PURPLE],
                 [470, 475, 200, 20, PURPLE],
                 [530, 340, 120, 20, PURPLE],
                 [530, 220, 120, 20, PURPLE],
                 [650, 105, 20, 135, PURPLE],
                 [650, 340, 20, 135, PURPLE],
                 [530, 160, 20, 60, PURPLE],
                 [530, 360, 20, 60, PURPLE],
                 [390, 20, 20, 100, PURPLE],
                 [390, 460, 20, 120, PURPLE],
                 [20, 145, 60, 20, PURPLE],
                 [20, 405, 60, 20, PURPLE],
                 [720, 145, 60, 20, PURPLE],
                 [720, 405, 60, 20, PURPLE]
                 ]
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
   
