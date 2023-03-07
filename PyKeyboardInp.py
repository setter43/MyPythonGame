import pygame
from pygame.locals import* #imports all key code

#initialize game window
pygame.init()

game_height = 700
game_width = 700
#create game window
screen = pygame.display.set_mode((game_width, game_height), 0, 32)

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

# Define movement speed
MOVEMENT_SPEED = 0.5

#game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        pressed = pygame.key.get_pressed()

    # Update position based on pressed keys
    if pressed[K_UP]:
        y -= MOVEMENT_SPEED
    if pressed[K_DOWN]:
        y += MOVEMENT_SPEED
    if pressed[K_LEFT]:
        x -= MOVEMENT_SPEED
    if pressed[K_RIGHT]:
        x += MOVEMENT_SPEED
    #clears game screens
    screen.fill((0,0,0))

    screen.blit(footballSprite,(x, y))
    pygame.display.update()
pygame.quit()
