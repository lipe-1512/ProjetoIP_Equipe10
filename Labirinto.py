import pygame
import random
from Wall_Room import*
from Player_Item import*
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
# number of treasures
N = 3

TEXT_SIZE = 12
 
clock = pygame.time.Clock()

#bool for gameover event
gameover = False

class Player(pygame.sprite.Sprite):
    global gameover
    """ This class represents the bar at the bottom that the
    player controls """
 
    # Set speed vector
    change_x = 0
    change_y = 0
 
    def __init__(self, x, y):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y
 
    def move(self, walls):
        global gameover
        """ Find a new position for the player """
 
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            gameover = True
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
         # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            gameover = True
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

def on_grid_random():
    x = random.randint(30, 740)
    y = random.randint(30, 540)
    return (x//15 * 15, y//15 *15)

def main():
    """ Main Program """
    global N
    global gameover
    
    # Call this function so the Pygame library can initialize itself
    pygame.init()
 
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
 
    # Set the title of the window
    pygame.display.set_caption('Labirinto')
 
    # Create the player paddle object
    player = Player(45, 45)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    group_treasure = pygame.sprite.Group()

    for item in range(N):
        treasure = Treasure(on_grid_random()[0],on_grid_random()[1])
        group_treasure.add(treasure)
        movingsprites.add(treasure)
    
 
    rooms = []
 
    room = Room1()
    rooms.append(room)
 
    room = Room2()
    rooms.append(room)
 
    room = Room3()
    rooms.append(room)
 
    current_room_no = 0
    current_room = rooms[current_room_no]
 

 
    done = False
    count = 0
    end = False
    
    while not done:

        #End game if player collise a wall   
        while gameover:
            screen.fill(WHITE)
            font = pygame.font.Font('freesansbold.ttf', TEXT_SIZE) 
            gameoverText = font.render("GAME OVER, para jogar novamente aperte C, para sair aperte Esc", True, BLACK)
            screen.blit(gameoverText, (250,270))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameover = False
                        main()

                    if event.key == pygame.K_ESCAPE:
                        done = True
                        gameover = False
                        pygame.quit()


        #end game if complete all levels
        while end:
            screen.fill(WHITE)
            font = pygame.font.Font('freesansbold.ttf', TEXT_SIZE)
            theEndText = font.render("FIM, para jogar novamente aperte C, para sair aperte Esc", True, BLACK)
            screen.blit(theEndText, (250,270))
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        main()

                    if event.key == pygame.K_ESCAPE:
                        done = True
                        end = False
                        pygame.quit()

        # --- Event Processing ---
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
                if event.key == pygame.K_ESCAPE:
                    done = True
                   
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)

 
        # --- Game Logic ---
        player.move(current_room.wall_list)

        for treasure in group_treasure:
            treasure.position(current_room.wall_list)
            #Player collect treasure
            if pygame.sprite.collide_rect(player, treasure):
                 #movingsprites.remove(treasure)
                treasure.rect.x = 700
                treasure.rect.y = 700
                #how many treasures were catch
                count +=1
          
           
            if count == N:
                print(current_room_no, N)
                if current_room_no <= N-1:
                    current_room_no += 1
                    if current_room_no == N:
                        end = True
                    else:
                        current_room = rooms[current_room_no]
                    
                if current_room_no == N:
                    end = True
                    
                player.rect.x = 400
                player.rect.y = 300
                count=0
                for treasure in group_treasure:
                    treasure.rect.x = on_grid_random()[0]
                    treasure.rect.y = on_grid_random()[1]


        # --- Drawing ---
     
        screen.fill(BLACK)
            #count

        font = pygame.font.Font('freesansbold.ttf', 32)

        score = font.render("Restam: " + str(N - count), True, WHITE)
        screen.blit(score, (30,30))

        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        pygame.display.flip()
 
        clock.tick(60)

        
 
    pygame.quit()
 
if __name__ == "__main__":
    main()