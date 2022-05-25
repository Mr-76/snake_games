import pygame
import random
from .snake_classes import snake
from .map_class import Map_snake 

def main():
    black = (0,0,0)
    block_sizes = 15
    Map = Map_snake(800,600,(0,222,222))
    Snake = snake(1,(0,200,0))

    pygame.init()
    display = pygame.display.set_mode((Map.get_screen_h(),Map.get_screen_w()))#set tamanho display
    pygame.display.update() 
    
    game_over = False 
    
    Snake.set_position((Map.get_screen_h()/2),(Map.get_screen_h()/2))
    
    clock = pygame.time.Clock() 
    
    set_food_pos(Map)
    
    while not game_over:
        for event in pygame.event.get():
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
        
        if(check_quit(event,pygame,Map,snake_x_y)):
            break
        
        display.fill(black)
        
        draw_food(display,Map,block_sizes)
        
        Snake.change_pos() 
        
        game_over = Snake.check_size_eat_self()

        snake_list = Snake.get_pos_body()
        
        write_snake(snake_list,Snake,block_sizes,display)

        pygame.display.update()
        
        display.fill(black)
        
        snake_x_y = Snake.get_x_y_pos()
        
        got_food(snake_x_y,Snake,Map)
        
        clock.tick(20)


    pygame.quit()

    quit()

def draw_food(display,Map,block_sizes):
    pygame.draw.rect(display,Map.get_food_color(),
            [Map.get_foodx(),Map.get_foody(),block_sizes,block_sizes])


def write_snake(snake_list,Snake,block_sizes,display):
        for pos in snake_list:
            pygame.draw.rect(display,Snake.get_snake_color(),
                            [pos[0],pos[1],block_sizes,block_sizes])

def got_food(snake_x_y,Snake,Map):
            if snake_x_y[0] == Map.get_foodx() and snake_x_y[1] == Map.get_foody():
                Map.set_food_pos((round(random.randrange(0, Map.get_screen_h() - 50) / 10.0) * 10.0),
                                (round(random.randrange(0, Map.get_screen_w() - 50) / 10.0) * 10.0))
                print("got it")
                Snake.snake_grow()
def set_food_pos(Map):
    Map.set_food_pos((round(random.randrange(0, Map.get_screen_h() - 50) / 10.0) * 10.0),
                     (round(random.randrange(0, Map.get_screen_w() - 50) / 10.0) * 10.0))

def check_quit(event,pygame,Map,snake_x_y):
    if ((event.type ==  pygame.quit) or (snake_x_y[0] >= Map.get_screen_h()) 
                                     or (snake_x_y[0] <= 0) 
                                     or (snake_x_y[1] >= Map.get_screen_w()) 
                                     or (snake_x_y[1] <= 0)):
        
        return True
    else:
        return False

if (__name__== '__main__'):
    main()
