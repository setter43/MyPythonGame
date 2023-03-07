import pygame
from pygame.locals import* #imports all key code

pygame.init()#initialize game window

game_height = 700
game_width = 700
screen = pygame.display.set_mode((game_width, game_height), 0, 32)#create game window

#import sprite
footballSprite = pygame.image.load('./img/football.png')
#resize sprite
footballSprite = pygame.transform.scale(footballSprite, (25, 25))
footballWidth = footballSprite.get_width()
footballHeight = footballSprite.get_height()
pygame.display.set_caption("My Pygame Sprites")
screen.fill((0,0,0))#rgb value
game_over = False

x, y = (0, 0)

#game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        pressed = pygame.key.get_pressed()
    if pressed[K_UP]:#Standing for Key Press is UP Arrow
            y -= 0.5
    if pressed[K_DOWN]:
        y += 0.5
    if pressed[K_LEFT]:
        x -= 0.5
    if pressed[K_RIGHT]:
        x += 0.5
    screen.fill((0,0,0))#clears game screens
    screen.blit(footballSprite,(x, y))
    pygame.display.update()
pygame.quit()
