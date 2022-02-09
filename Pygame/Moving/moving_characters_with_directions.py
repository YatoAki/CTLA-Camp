import pygame, sys

width, height = 624, 424
pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
pygame.display.set_caption('Moving a character with direction')

character = pygame.image.load('../images/cat.png')    #load the image into pygame
character_size = 24             #Image size 24 x 24
character_x, character_y = 1,1
character_speed = 10            #Set the speed for character

x_increase = 0      #Increase along x axis
y_increase = 0      #Increase along y axis

while True:

    pressed = pygame.key.get_pressed()

    #Code Below
    #Detect the pressed key and change the direction of the character

    if pressed[pygame.K_LEFT]:
        x_increase = -character_speed
        y_increase = 0
    elif pressed[pygame.K_RIGHT]:
        x_increase = character_speed
        y_increase = 0
    elif pressed[pygame.K_DOWN]:
        x_increase = 0
        y_increase = character_speed
    elif pressed[pygame.K_UP]:
        x_increase = 0
        y_increase = -character_speed

    ####

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #Add direction to character location

    character_x += x_increase
    character_y += y_increase

    ###

    screen.fill((255,255,255))
    screen.blit(character,(character_x,character_y))
    pygame.display.update()
    clock.tick(20)
