import pygame
from sys import exit

# absolutely required before running any other code
# basically just starts pygames
pygame.init()
# gotta set the width and height for set_mode() in the way (x,y)
screen = pygame.display.set_mode((800, 400))
# makes title for the screen of the game
# can also change icons
pygame.display.set_caption("Learning PyGame")

# need to normalize framerate so that animation speed is the same across different computers| Keep frame rate constant
# need to create ceiling and floor for frame rate
clock = pygame.time.Clock()

# need tupil w width and height for just a square: pygame.Surface((100, 200))
# for an image use pygame.image.load(file path) and blit it in in the while loop

# steps to create text 1) create font(text size and style) 2) write text on surface 3) blit the text surface
# 1) font = pygame.font.Font(font, size) (can use ttf file in font) 2)text_surface = font.render(text, AA(antialias or not), color)
# antialist(smooth edges of text) either True or False (True for everything but pixel art)

test_surface = pygame.Surface((100, 200))
# change color of test surface
test_surface.fill('Red')

# game is going to run from inside the while True loop
# draw all elements
# update everything
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # need to break or else throws error cause video system is unintialized in the rest of the while loop
            pygame.quit()
            exit()

    # To display anything in PyGames, must put it on a surface
    # regular surface(image/text/color) needs to be put on a display surface to be displayed
    # display surface always shown, never hide, must be unique
    # can have as many regular surface as want, displayed only when connected to display surface

    # putting one surface on another surface, need surface and position
    screen.blit(test_surface, (200, 100))

    # updates display surface screen
    pygame.display.update()
    # tells that the loop shouldnt run faster than 60 times per second
    clock.tick(60)
