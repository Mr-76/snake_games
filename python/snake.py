import pygame
import random
white = (0,0,0)
pygame.init()#inicializa

display = pygame.display.set_mode((800,600))#set tamanho display

pygame.display.update() #atualiza do display


game_over = False #criando loop para o display ficar aberto

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0


clock = pygame.time.Clock() #vel da cobra ? wt

foodx = round(random.randrange(0, 800 - 20) / 10.0) * 10.0

foody = round(random.randrange(0, 800 - 20) / 10.0) * 10.0

while not game_over:
    for event in pygame.event.get():#eventos ex: mouse se movendo
        print(event)
        if (event.type ==  pygame.QUIT) or ((x1>= 800) or (x1<=0)) or ((y1>= 600) or (y1<=0)): #apertar botao de fechar a janela ao chegar ao maximo da tela prog fecha
            game_over = True
    
        if event.type ==  pygame.KEYDOWN: #apertar botao de fechar a janela
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
            else:
                pass
    
    x1 += x1_change
    y1 += y1_change

    display.fill(white)
    
    pygame.draw.rect(display,(255,0,0),[x1,y1,20,20])#desenhe um retangulo cobra OOO
    pygame.draw.rect(display,(25,55,25),[foodx,foody,10,10])#desenhe um retangulo cobra OOO

    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()

