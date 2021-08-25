import pygame, random, time, funcoes_game, star, personagem, sys
from Wall_Room import*
from Player_Item import*

clock = pygame.time.Clock()

def on_grid_random():
    x = random.randint(40, 740)
    y = random.randint(40, 540)
    return (x//15 * 15, y//15 *15)

def main():
    """ Main Program """   
    
    # Call this function so the Pygame library can initialize itself
    pygame.init()
    funcoes = funcoes_game.Funcoes_game()
 
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
 
    # Set the title of the window
    pygame.display.set_caption('Labirinto')
 
    # Create the player paddle object
    player = personagem.Player(45, 45)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
    

    group_treasure = pygame.sprite.Group()

    for item in range(funcoes.N):
        treasure = Treasure(on_grid_random()[0],on_grid_random()[1])
        group_treasure.add(treasure)
        movingsprites.add(treasure)
    
    Star = star.star(
        on_grid_random()[0]+random.randint(-120, 120),on_grid_random()[1]+random.randint(-120, 120))
    movingsprites.add(Star)
    
 
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
    startTime = time.time()    
    collision_time = 0    
    
    while not done:

        #End game if player collise a wall   
        
        while player.gameover and not player.collision_imune:
            
            screen.fill(WHITE)
            font = pygame.font.Font('freesansbold.ttf', funcoes.TEXT_SIZE) 
            gameoverText = font.render("GAME OVER, para jogar novamente aperte C, para sair aperte Esc", True, BLACK)
            gameoverText_rect = gameoverText.get_rect(center=(800/2, 600/2))
            screen.blit(gameoverText, (gameoverText_rect))
    
            pygame.display.update()

            funcoes.checar_colisoes(player, done)


        #end game if complete all levels
        while end:
            screen.fill(WHITE)
            font = pygame.font.Font('freesansbold.ttf', funcoes.TEXT_SIZE-2)
            #theEndText = font.render("para jogar novamente aperte C, para sair aperte Esc", True, BLACK)
            #screen.blit(theEndText, (250,270))
            timerText = font.render(f"Parabéns, você conclui o desafio em: {round(endTime - startTime, 1)}s. Para jogar novamente aperte C, para sair aperte Esc", True, BLACK)
            timerText_rect = timerText.get_rect(center=(800/2, 600/2))
            screen.blit(timerText, (timerText_rect))
            pygame.display.update()
            
            funcoes.checar_colisoes(player, done)

        # --- Event Processing ---
 
        funcoes.checar_eventos(player)

 
        # --- Game Logic ---
        player.move(current_room.wall_list)
        Star.position(current_room.wall_list)
        
        #if player collect immune item it can collide with a wall
        if pygame.sprite.collide_rect(player, Star):
            player.collision_imune = True
            collision_time = pygame.time.get_ticks()
            Star.rect.x = 700
            Star.rect.y = 700
        if pygame.time.get_ticks() - collision_time > 3000:
            player.collision_imune = False
        
        for treasure in group_treasure:
            treasure.position(current_room.wall_list)
            #Player collect treasure
            if pygame.sprite.collide_rect(player, treasure):
                 #movingsprites.remove(treasure)
                treasure.rect.x = 700
                treasure.rect.y = 700
                #how many treasures were catch
                count +=1
          
           
            if count == funcoes.N:
                if current_room_no <= funcoes.N-1:
                    current_room_no += 1
                    if current_room_no == funcoes.N:
                        endTime = time.time()
                        end = True
                    else:
                        current_room = rooms[current_room_no]
                    
                if current_room_no == funcoes.N:
                    end = True
                    
                player.rect.x = 400
                player.rect.y = 300
                count=0
                Star.rect.x = on_grid_random()[0]+random.randint(-120, 120)
                Star.rect.y = on_grid_random()[1]+random.randint(-120, 120)
                for treasure in group_treasure:
                    treasure.rect.x = on_grid_random()[0]
                    treasure.rect.y = on_grid_random()[1]


        # --- Drawing ---
        screen.fill(BLACK)
        #count
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        font = pygame.font.Font('freesansbold.ttf', 14)

        score = font.render("Restam: " + str(funcoes.N - count), True, WHITE)
        screen.blit(score, (30,5))

        temp = font.render("Timer: " + str(round(time.time() - startTime, 1)), True, WHITE)
        screen.blit(temp, (700,5))
        
        #text that show if player is immune
        if player.collision_imune:
            imuneText = font.render("Você está imune", True, WHITE)
            imuneText_rect = imuneText.get_rect(center=(800/2, 600/2))
            screen.blit(imuneText, (imuneText_rect))
            pygame.display.update()
            player.gameover = False

        pygame.display.flip()
 
        clock.tick(60)

        
 
    pygame.quit()
 
if __name__ == "__main__":
    main()