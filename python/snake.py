import pygame
import random



       



white = (250,250,250) #background color


pygame.init()#inicializa


display = pygame.display.set_mode((800,600))#set tamanho display

pygame.display.update() #atualiza do display


game_over = false #criando loop para o display ficar aberto

x1 = 300
y1 = 300

snake_lenght =1 

x1_change = 0
y1_change = 0

snake_list = []

clock = pygame.time.clock() #vel da cobra ? wt

foodx = round(random.randrange(0, 800 - 20) / 10.0) * 10.0

foody = round(random.randrange(0, 800 - 20) / 10.0) * 10.0

while not game_over:
    for event in pygame.event.get():#eventos ex: mouse se movendo
        print(event)
        if (event.type ==  pygame.quit) or ((x1>= 800) or (x1<=0)) or ((y1>= 600) or (y1<=0)): #apertar botao de fechar a janela ao chegar ao maximo da tela prog fecha
    
        if event.type ==  pygame.keydown: #apertar botao de fechar a janela
            game_over = True
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.k_right:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.k_up:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.k_down:
                x1_change = 0
                y1_change = 10
            else:
                pass
    
    x1 += x1_change
    y1 += y1_change

    display.fill(white)
    
    pygame.draw.rect(display,(25,55,25),[foodx,foody,10,10])#desenhe um retangulo cobra ooo
    head_snake =[]
    head_snake.append(x1) #kinda of tuple
    head_snake.append(y1)

    
    snake_list.append(head_snake)
    
    

    if len(snake_list) > snake_lenght:
        del snake_list[0]
    
    for x in snake_list[:-1]:
        if x == head_snake:
            game_over = true


    for x in snake_list:
        pygame.draw.rect(display,(255,0,0),[x[0],x[1],20,20])#desenhe um retangulo cobra ooo
    
    pygame.display.update()
    
    display.fill(white)
    if x1==foodx and y1 == foody:
        foodx = round(random.randrange(0, 800 - 20) / 10.0) * 10.0
        foody = round(random.randrange(0, 600 - 20) / 10.0) * 10.0
        print("got it")
        snake_lenght+=1
    clock.tick(30)





pygame.quit()

quit()

