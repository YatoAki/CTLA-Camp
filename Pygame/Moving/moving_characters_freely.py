import pygame, sys

width, height = 624, 424
pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()     #To set FPS
pygame.display.set_caption("Moving a character freely")


character = pygame.image.load('../images/happy.png')    #load the image into pygame
character_size = 24             #Image size 24 x 24
character_x, character_y = 0,0
character_speed = 10            #Set the speed for character

while True:
    pressed = pygame.key.get_pressed()

    #Code Below
    #Detect the pressed key and change the location of the character

    if pressed[pygame.K_LEFT]:
        character_x -= character_speed if character_x > 0 else 0
    elif pressed[pygame.K_RIGHT]:
        character_x += character_speed if character_x + character_speed <= width - character_size else 0
    if pressed[pygame.K_DOWN]:
        character_y += character_speed if character_y + character_speed <= height - character_size else 0
    elif pressed[pygame.K_UP]:
        character_y -= character_speed if character_y > 0 else 0

    ####

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255,255,255))
    screen.blit(character,(character_x,character_y))
    pygame.display.update()
    clock.tick(20) #Setting FPS
