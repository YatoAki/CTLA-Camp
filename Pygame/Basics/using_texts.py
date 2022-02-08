import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('Using texts')

font = pygame.font.SysFont('arial',100)         #Load font style into pygame
text = font.render('Hello',True,(255,255,255))  #Load text from font

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(text,(200,100))                 #blit the text
    pygame.display.update()
