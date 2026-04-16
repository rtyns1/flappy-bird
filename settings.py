
import pygame


#settings.py is a config file used to store global variables and constants.
#Screen dimensions,target frame rates, color presets, asset info like filepaths for images, sounds and fonts,
#For mine, i shall start with screen dimensions.

GAME_WIDTH = 400
GAME_HEIGHT = 600
#Starting point X--> horizontal coordinate where bird appears when the game being.
# Starting position is fixed because the bird does not move horizontally.
#The pipes move right to left, creating the illusion of forward movement, the bird only moves up when flapping, or down due to g.
BIRD_X = GAME_WIDTH /2# horizontal starting position of bird
BIRD_Y = GAME_HEIGHT /2#vertical starting position of bird
BIRD_SIZE = 30 # means 30*30 pixel square
GRAVITY = 0.5 #.5 here means the birds downwards speed increases by 0.5 pixel per frame
#Screen is 600 pixels tall, so .5 is appropriate
JUMP_STRENGTH= -0.9 #when you flap, birds velocity instantly becomes -9, negative means up
# so u flap, it moves up 9 pixels, then gravity slowly pulls it back down.
#The jump needs to be strong enough to overcome gravity and actually go up, but not too strong
#If jump is -9 and gravity is 0.5, the bird goes up about 18 frames before starting to fall again

PIPE_WIDTH= 80
PIPE_GAP = 200 # 200 pixels of empty space btwn top pipe and bottom pipe
PIPE_SPACING = 300 # one pipe apart to the next is 300 pixels, meaning u can only see one pipe pair on screen at a time.
PIPE_SPEED = 3 # moves left 3 pixels per frame, at 6- fps that is 180 pixels per second.
#Screen is 400 pixels wide so pipe takes about 2.2 seconds to travel from right to left edge.

SKY_BLUE = (135, 206, 235)
GROUND_BROWN = (139, 206, 235)
BIRD_YELLOW = (255, 255, 0)
PIPE_GREEN = (0, 255, 0)
WHITE= (255, 255, 255)

#Now why are constants important and why would we want them in a separate fie of their own?
"""

"""



