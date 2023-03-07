import pygame

pygame.init()#initialize game window
screen = pygame.display.set_mode((640,480), 0, 32)#create game window
pygame.display.set_caption("My Pygame")
screen.fill((0,0,0))#rgb value
game_over = False

#game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
pygame.quit()
