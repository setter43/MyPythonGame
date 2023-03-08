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

#Define Clock / FPS
clock = pygame.time.Clock()

#game loop
while not game_over:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        #else if Sprite moves with mouse
        elif event.type == pygame.MOUSEMOTION :
            x, y = event.pos
            x -= footballWidth/2
            y -= footballHeight/2
    pressed = pygame.key.get_pressed()

    # Update position based on pressed keys
    if pressed[K_UP]:
        y -= MOVEMENT_SPEED*dt
    if pressed[K_DOWN]:
        y += MOVEMENT_SPEED*dt
    if pressed[K_LEFT]:
        x -= MOVEMENT_SPEED*dt
    if pressed[K_RIGHT]:
        x += MOVEMENT_SPEED*dt
    if pressed[K_SPACE]:
        x, y = (0, 0)

    if x > (screen.get_width()- footballWidth):
        x = screen.get_width() - footballWidth
    if x < 0:
        x = 0
    
    if y > (screen.get_height()- footballHeight):
        y = screen.get_height() - footballHeight
    if y < 0:
        y = 0
    #clears game screens
    screen.fill((0,0,0))

    screen.blit(footballSprite,(x, y))
    pygame.display.update()
pygame.quit()
