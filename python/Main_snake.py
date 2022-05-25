import pygame
import random
from snake_classes import snake
from map_class import Map_snake 
snake_lenght = 1
white = (250,250,250) #background color
snake_color = (0,200,0)
snake_pace = 10

screen_h = 800
screen_w = 600

block_sizes = 15
food_color = (255,0,0)
Map = Map_snake(screen_h,screen_w,food_color)
Snake = snake(snake_lenght,snake_color,snake_pace)

pygame.init()#inicializa
display = pygame.display.set_mode((Map.get_screen_h(),Map.get_screen_w()))#set tamanho display
pygame.display.update() #atualiza do display
game_over = False #criando loop para o display ficar aberto

Snake.set_position((Map.get_screen_h()/2),(Map.get_screen_h()/2))

clock = pygame.time.Clock() 


Map.set_food_pos((round(random.randrange(0, Map.get_screen_h() - 50) / 10.0) * 10.0),
                 (round(random.randrange(0, Map.get_screen_w() - 50) / 10.0) * 10.0))


while not game_over:
    for event in pygame.event.get():#eventos ex: mouse se movendo
        print(event)
        snake_x_y = Snake.get_x_y_pos() 
        if (event.type ==  pygame.KEYDOWN):
            if event.key == pygame.K_LEFT:
               Snake.sub_pace(10,0)
            elif event.key == pygame.K_RIGHT:
                Snake.add_pace(10,0)
            elif event.key == pygame.K_UP:
                Snake.sub_pace(0,10)
            elif event.key == pygame.K_DOWN:
                Snake.add_pace(0,10)
            else:
                pass
    
    if ((event.type ==  pygame.quit) or (snake_x_y[0] >= Map.get_screen_h()) 
                                     or (snake_x_y[0] <= 0) 
                                     or (snake_x_y[1] >= Map.get_screen_w()) 
                                     or (snake_x_y[1] <= 0)):
        game_over = True
        break



    if game_over == True:
        break


    display.fill(white)
    
    pygame.draw.rect(display,Map.get_food_color(),
            [Map.get_foodx(),Map.get_foody(),block_sizes,block_sizes])

    Snake.change_pos() 
    
    game_over = Snake.check_size_eat_self()

    snake_list = Snake.get_pos_body()
    
    for pos in snake_list:
        pygame.draw.rect(display,Snake.get_snake_color(),
                        [pos[0],pos[1],block_sizes,block_sizes])

    pygame.display.update()
    display.fill(white)
    
    snake_x_y = Snake.get_x_y_pos()

    if snake_x_y[0] == Map.get_foodx() and snake_x_y[1] == Map.get_foody():
        Map.set_food_pos((round(random.randrange(0, Map.get_screen_h() - 50) / 10.0) * 10.0),
                        (round(random.randrange(0, Map.get_screen_w() - 50) / 10.0) * 10.0))
        print("got it")
        Snake.snake_grow()
    clock.tick(20)


pygame.quit()

quit()

