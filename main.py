#imports pygame module and constants
import pygame
import constants
from character import Character

#initializes pygame
pygame.init()

#calls the screen size from the constants file
screen = pygame.display.set_mode((constants.SCREEN_WITDH, constants.SCREEN_HEIGHT))

#sets screen name in left corner
pygame.display.set_caption("Dungeon Crawler")

#create clock for maintaining frame rate
clock = pygame.time.Clock()

#define player movement variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

#helper function to scale image
def scale_image(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))

# load character images
mob_animations = []
mob_types = ["elf", "imp", "skeleton", "goblin", "muddy", "tiny_zombie", "big_demon"]

animation_types = ["idle", "run"]
for mob in mob_types:
    #load images
    animation_list = []
    for animation in animation_types:
        #reset temporary list of images
        temp_list = []
        for i in range(4):
            img = pygame.image.load(f"assets/images/characters/{mob}/{animation}/{i}.png").convert_alpha()
            img = scale_image(img, constants.SCALE)
            temp_list.append(img)
        animation_list.append(temp_list)
    mob_animations.append(animation_list)

#create player
player = Character(100, 100, mob_animations, 0)

#main game loop
run = True
while run:

    #controll frame rate
    clock.tick(constants.FPS)

    screen.fill(constants.BG)

    #calculate player movement
    dx = 0
    dy = 0
    if moving_right == True:
        dx = constants.SPEED
    if moving_left == True:
        dx = -constants.SPEED
    if moving_up == True:
        dy = -constants.SPEED
    if moving_down == True:
        dy = constants.SPEED

    #move player
    player.move(dx, dy)

    #update player
    player.update()

    #draw player on screen
    player.draw(screen)

    #even handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #take keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True
        #keyboard button release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False

    pygame.display.update()

pygame.quit()