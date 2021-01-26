import pygame

# Allow to use functinos and variables in the pygame.locals
# without having to add pygame.locals prefix (optiona;)
from pygame.locals import *


# This line is compulsory to add anything you want to use the Pygame 
# library. Must be added before any other pygame functions to avoid
# initialization error
pygame.init()


# Game loop is where all the game events occur, update and get drawn
# to the screen. The game loop begins and the program keeps looping over
# and over until an event of type QUIT occurs

# Game loop begins
while True:
    # Code
    # Code

    pygame.display.update()

    # Quitting the game loop
    # Every game loop must have an end point, else your game will 
    # run indefinetly
    for event in pygame.event.get():
        # The type attribute tells us what kind of event the
        # object represents

        if event.type == QUIT:
            # We call both pygame.quit() and sys.exit() to close
            # the pygame window and the python script respectively.
            # Simply using sys.exit() can cause IDE to hang due to a bug
            pygame.quit()
            sys.exit()
            # Side note: If you didn’t import everything from pygame.locals 
            # as we did you would have to use pygame.locals.QUIT instead of QUIT.

    # Low resolution projects are much easier to manage
    # High resolution game requires time and effort due to the complexity
    # in creating and managing it

    # For every game, we create a window of a fixed size by passing a tuple 
    # of width and height
    DISPLAYSURF = pygame.display.set_mode((300,300))

    # Individually accessing co-ordinates
    # Place both the X and Y values in a tuple, first int is X and second is Y
    pygame.draw.circle(DISPLAYSURF, BLACK, (200,50), 30)

    # More on this link
    # https://coderslegacy.com/python/python-pygame-tutorial/