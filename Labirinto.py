import pygame
import random
from Wall_Room import *
from Player_Item import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
# number of treasures
N = 3


def on_grid_random():
    x = random.randint(20, 740)
    y = random.randint(20, 540)
    return (x // 15 * 15, y // 15 * 15)


swallows = pygame.sprite.Group()



def main():
    """ Main Program """

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
        treasure = Treasure(on_grid_random()[0], on_grid_random()[1])
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

    clock = pygame.time.Clock()

    done = False
    count = 0
    while not done:

        swallow = Treasure(x=800, y=random.randrange(800))
        swallows.add(swallow)

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
            # Player collect treasure
            if pygame.sprite.collide_rect(player, treasure):
                # movingsprites.remove(treasure)
                treasure.rect.x = 700
                treasure.rect.y = 700
                # how many treasures were catch
                count += 1

            if count == N:
                current_room_no += 1
                current_room = rooms[current_room_no]
                player.rect.x = 400
                player.rect.y = 300
                count = 0
                for treasure in group_treasure:
                    treasure.rect.x = on_grid_random()[0]
                    treasure.rect.y = on_grid_random()[1]

        # --- Drawing ---
        screen.fill(BLACK)
        # count

        font = pygame.font.Font('freesansbold.ttf', 32)

        score = font.render("Restam: " + str(N - count), True, WHITE)
        screen.blit(score, (30, 30))

        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
