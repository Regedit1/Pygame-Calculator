import pygame
import sys
from pygame.locals import *

pygame.init()

bg = "background.jpg"
screen = pygame.display.set_mode((400,400),0,32)
background = pygame.image.load(bg).convert()
pygame.display.set_caption("Calculator")
panel = pygame.image.load("panel.jpg").convert()
numpad = pygame.image.load("numpad.jpg").convert()
function = pygame.image.load("functions.jpg").convert()
forn = "num"
def funcornum(x,y):
    if x > 20 and x < 220 and y > 100 and y < 366:
        print "number"
        forn = "number"
    elif x > 300 and x < 350 and y > 100 and y < 300:
        print "function"
        forn = "function"
    else:
        forn = "neither"
    return forn

def whichnumber(x, y):
    print "testing for number:"
    if x > 20 and x < 86:
        if y > 100 and y < 166:
            print 1
            number = 1
        if y > 166 and y < 233:
            print 4
            number = 4
        if y > 233 and y < 300:
            print 7
            number = 7
        else:
            number = "none"
    else:
        number =  "none"


    return number


#Game loop
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            x , y = pygame.mouse.get_pos()
            forn = funcornum(x , y)
            if forn == "number":
                whichnumber(x, y)
        


    
    screen.blit(background, (0,0))
    background.blit(panel, (10,10))
    background.blit(numpad, (20,100))
    background.blit(function, (300,100))
    pygame.display.update()
    
