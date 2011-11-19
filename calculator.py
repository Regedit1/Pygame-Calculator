import pygame
import sys
from pygame.locals import *

pygame.init()

bg = "background.jpg"
screen = pygame.display.set_mode((400,400),0,32)
background = pygame.image.load(bg).convert()
pygame.display.set_caption("Calculator")
panel = pygame.image.load("panel.jpg").convert()



#Game loop
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    
    screen.blit(background, (0,0))
    background.blit(panel, (10,10))
    pygame.display.update()
    
