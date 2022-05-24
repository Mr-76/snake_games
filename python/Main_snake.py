import pygame
import random
from snake_classes import snake

snake_lenght = 1
white = (250,250,250) #background color
snake_color = (0,0,0)
snake_pace = 10

Snake = snake(snake_lenght,snake_color,snake_pace)

pygame.init()#inicializa

screen_h = 800
screen_w = 600

display = pygame.display.set_mode((screen_h,screen_w))#set tamanho display
pygame.display.update() #atualiza do display
game_over = False #criando loop para o display ficar aberto

Snake.set_position((screen_h/2),(screen_w/2))

clock = pygame.time.Clock() #vel da cobra ? wt

foodx = round(random.randrange(0, screen_h - 20) / 10.0) * 10.0
foody = round(random.randrange(0, screen_w - 20) / 10.0) * 10.0



while not game_over:
    for event in pygame.event.get():#eventos ex: mouse se movendo
        print(event)
        snake_x_y = Snake.get_x_y_pos() 
        if (event.type ==  pygame.quit) or ((snake_x_y[0]>= screen_h) or (snake_x_y[0]<=0)) or ((snake_x_y[1]>= screen_w) or (snake_x_y[1]<=0)):
            game_over = True
            
        if (event.type ==  pygame.KEYDOWN):
            if event.key == pygame.K_LEFT:
               Snake.sub_pace(10,0)#unprivate the method
               #_snake_x_add_pace not geting changed :()
               # Snake._snake_x_add_pace = -10
               # Snake._snake_y_add_pace = 0 
            elif event.key == pygame.K_RIGHT:
                Snake.add_pace(10,0)
            elif event.key == pygame.K_UP:
                Snake.sub_pace(0,10)
            elif event.key == pygame.K_DOWN:
                Snake.add_pace(0,10)
                print(Snake.get_pos_body())
            else:
                pass
    
    display.fill(white)
    
    pygame.draw.rect(display,(25,55,25),[foodx,foody,10,10])#desenhe um retangulo cobra ooo

    Snake.change_pos() #update snake position
    
    game_over = Snake.check_size_eat_self()

    snake_list = Snake.get_pos_body()
    for x in snake_list:
        pygame.draw.rect(display,(111,44,123),[x[0],x[1],20,20])#desenhe um retangulo cobra ooo
    pygame.display.update()
    display.fill(white)
    
    snake_x_y = Snake.get_x_y_pos()

    if snake_x_y[0]==foodx and snake_x_y[1] == foody:
        foodx = round(random.randrange(0, screen_h - 20) / 10.0) * 10.0
        foody = round(random.randrange(0, screen_w - 20) / 10.0) * 10.0
        print("got it")
        Snake.snake_grow()
    clock.tick(30)





pygame.quit()

quit()

