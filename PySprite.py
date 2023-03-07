import pygame

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

#game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(footballSprite,(screen.get_width()/2 -footballWidth/2, screen.get_height()/2 -footballHeight/2))
    pygame.display.update()
pygame.quit()
