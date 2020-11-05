# - GAME.PY
import pygame  # -- import the pygame library
from pygame.locals import * # -- pygame.locals is a module that contains various pygame constants
pygame.init()  # -- initialize the pygame library

pygame.display.set_caption('Skynet Rebellion') # -- set the name of the window to 'Skynet Rebellion'
screen = pygame.display.set_mode([800, 600]) # -- create a screen with a resolution of 800 by 600

running = True # -- variable 'running' is used to stop the game if the user closes the window

# - PLAYER CLASS
# -- attributes: 
class Player(pygame.sprite.Sprite):
    # - Constructor method
    def __init__(self):
        super().__init__() # -- calling the methods of the superclass
        self.image = pygame.Surface([50, 100]) # -- create a new surface - 50 by 100px
        self.image.fill((255,255,255)) # -- fill the surface with white colour
        self.rect = self.image.get_rect() # -- catch the object which has the dimension of the image
        self.rect.x = 250 # -- set the x coordinate
        self.rect.y = 250 # -- set the y coordinate
    # - END Constructor method
# - END CLASS

player = Player() # -- Create an instance of the Player class

all_sprites_group = pygame.sprite.Group() # -- create a new sprite group
all_sprites_group.add(player) # -- add the player sprite into all_sprites_group

# - MAIN WHILE LOOP
# -- this is where the game is being executed
while running:
    
    # - FOR loop which listens to events
    for event in pygame.event.get():
        # -- if user quits the game
        if event.type == pygame.QUIT:
            running = False # -- set the variable running to False
        # - END IF
    # - END FOR

    screen.fill((0, 0, 0)) # -- fill the screen with white colour

    all_sprites_group.draw(screen) # -- Draw all the sprites on the screen

    pygame.display.flip() # -- Flip the display
    pygame.time.Clock().tick(60) # -- set the number of frames per second to 60
# - END WHILE

pygame.quit() # - Exit the game