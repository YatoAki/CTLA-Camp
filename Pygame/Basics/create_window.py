import pygame, sys

pygame.init()

#setting display width & height
screen = pygame.display.set_mode((600,400))

#setting display name
pygame.display.set_caption("Create Pygame Window")

#lets keep the window going
while True:
    for event in pygame.event.get():        #Check what user is doing
        if event.type == pygame.QUIT:
            sys.exit()                      #Close the program

    #update the display
    pygame.display.update()
