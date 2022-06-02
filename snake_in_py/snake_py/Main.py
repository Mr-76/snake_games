"""Main module

this module allows the user to run the snake game
it can be imported as a module as its done in the run.py file
in the snake_in_py folder

There are 6 functions defined in this file
they are main(),draw_food(),write_snake(),got_food(),set_food_pos()
and check_quit

"""
import sys
import random
import pygame
from .snake_classes import snake
from .map_class import Map_snake

def main():
    """Main function runs all the code """
    black = (0,0,0)
    block_sizes = 15
    game_map = Map_snake(800,600,(0,222,222)) #still need to chage class names
    player_snake = snake(1,(0,200,0))

    pygame.init()
    display = pygame.display.set_mode((game_map.get_screen_h(),
                                        game_map.get_screen_w()))#set tamanho display
    pygame.display.update()

    game_over = False

    player_snake.set_position((game_map.get_screen_h()/2),(game_map.get_screen_h()/2))

    clock = pygame.time.Clock()

    set_food_pos(game_map)

    while not game_over:
        for event in pygame.event.get():
            print(event)
            snake_x_y = player_snake.get_x_y_pos()

            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_snake.sub_pace(10,0)
                elif event.key == pygame.K_RIGHT:
                    player_snake.add_pace(10,0)
                elif event.key == pygame.K_UP:
                    player_snake.sub_pace(0,10)
                elif event.key == pygame.K_DOWN:
                    player_snake.add_pace(0,10)
                else:
                    pass

        if check_quit(event,game_map,snake_x_y):
            break

        display.fill(black)

        draw_food(display,game_map,block_sizes)

        player_snake.change_pos()

        game_over = player_snake.check_size_eat_self()

        snake_list = player_snake.get_pos_body()

        write_snake(snake_list,player_snake,block_sizes,display)

        pygame.display.update()

        display.fill(black)

        snake_x_y = player_snake.get_x_y_pos()

        got_food(snake_x_y,player_snake,game_map)

        clock.tick(20)


    pygame.quit()

    sys.exit()

def draw_food(display,game_map,block_sizes):
    """Function that drawns the food on the screen

    :param display: The pygame display object
    :type display: object
    :param game_map: Game map object that holds
        cordinates and other proprerties
    :type game_map: object
    :param block_sizes: the size of the food to be draw
    :type block_sizes: int
    """
    pygame.draw.rect(display,game_map.get_food_color(),
            [game_map.get_foodx(),game_map.get_foody(),block_sizes,block_sizes])


def write_snake(snake_list,player_snake,block_sizes,display):
    """Function to drawn the snake

    :param snake_list: The snake body, set of coordinates
        to be draw
    :type snake_list: list
    :param player_snake: The player snake obj
    :type player_snake: object
    :param block_sizes: the size of the snake to be draw
    :type block_sizes: int
    :param display: The pygame display object
    :type display: object
    """
    for pos in snake_list:
        pygame.draw.rect(display,player_snake.get_snake_color(),
                        [pos[0],pos[1],block_sizes,block_sizes])

def got_food(snake_x_y,player_snake,game_map):
    """ Function checks if the player got the food

    :param snake_x_y: the snake x and y coordinates
    :type snake_list: list
    :param player_snake: The player snake obj
    :type player_snake: object
    :param game_map: Game map object that holds
        cordinates and other proprerties
    :type game_map: object
    """
    if snake_x_y[0] == game_map.get_foodx() and snake_x_y[1] == game_map.get_foody():
        game_map.set_food_pos(
                        (round(random.randrange(0, game_map.get_screen_h() - 50) / 10.0) * 10.0),
                        (round(random.randrange(0, game_map.get_screen_w() - 50) / 10.0) * 10.0)
                        )
        print("got it")
        player_snake.snake_grow()
def set_food_pos(game_map):
    """ Function sets the food position

    :param game_map: Game map object that holds
        cordinates and other proprerties
    :type game_map: object
    """
    game_map.set_food_pos((round(random.randrange(0, game_map.get_screen_h() - 50) / 10.0) * 10.0),
                     (round(random.randrange(0, game_map.get_screen_w() - 50) / 10.0) * 10.0))

def check_quit(event,game_map,snake_x_y):
    """ Function checks if the game can quit
    :param event:  pygame type of event proprertie
    :type event: obj proprertie
    :param game_map: Game map object that holds
        cordinates and other propreties
    :type game_map: object
    :param snake_x_y: the snake x and y coordinates
    :type snake_list: list
    :returns: True or False based on the if statement checking
    :rtype: bool
    """
    if ((event.type ==  256) or (snake_x_y[0] in [game_map.get_screen_h(),0])
                             or(snake_x_y[1] in [game_map.get_screen_w(),0])):
        return True
    return False

if __name__== '__main__':
    main()
