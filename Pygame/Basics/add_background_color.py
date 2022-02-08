import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("add background color")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0,52,54))      #fill the screen with color
    pygame.display.update()     #update the display
