import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Add background image")

bg_image = pygame.image.load('../images/background.jpg') #load the image into pygame
bg_image = pygame.transform.scale(bg_image,(600,400))   #adjust image size to fit into pygame window

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(bg_image,(0,0))                         #show the image
    pygame.display.update()
