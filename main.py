#imports pygame module and constants
import pygame
import constants

#initializes pygame
pygame.init()

#calls the screen size from the constants file
screen = pygame.display.set_mode((constants.SCREEN_WITDH, constants.SCREEN_HEIGHT))

#sets screen name in left corner
pygame.display.set_caption("Dungeon Crawler")

#main game loop
run = True
while run:

    #even handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()