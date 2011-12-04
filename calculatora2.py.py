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
equals = pygame.image.load("equals.jpg").convert()
clearbutton = pygame.image.load("clearbutton.jpg").convert()

inputone = []
inputtwo = []
whichinput = 1

def whichbutton(x,y):
    if x > 20 and x < 86:
        if y > 100 and y < 166:
            
            pressed = "1"
        elif y > 166 and y < 233:
            
            pressed = "4"
        elif y > 233 and y < 300:
            
            pressed = "7"
        elif y > 300 and y < 366:
            
            pressed = "0"
        else:
            pressed = "none"
    elif x > 86 and x < 152:
        if y > 100 and y < 166:
            
            pressed = "2"
        elif y > 166 and y < 233:
            
            pressed = "5"
        elif y > 233 and y < 300:
            
            pressed = "8"
        elif y > 300 and y < 366:
            
            pressed = "0"
        else:
            pressed = "none"
    elif x > 152 and x < 220:
        if y > 100 and y < 166:
            
            pressed = "3"
        elif y > 166 and y < 233:
            
            pressed = "6"
        elif y > 233 and y < 300:
            
            pressed = "9"
        elif y > 300 and y < 366:
            
            pressed = "."
        else:
            pressed = "none"
    elif y > 250 and y < 300:
        pressed = " / "
    elif y > 200 and y < 250:
        pressed = " - "
    elif y > 150 and y < 200:
        pressed = " * "
    elif y > 100 and y < 150:
        pressed = " + "
    elif y > 10 and y < 50 and x > 320 and x < 370:
        pressed = "Clear"
    if y > 320 and y < 386 and x > 280 and x < 346:
        pressed = "Calc"
    print pressed
    return pressed

def numberpressed(button):
    if button == "1" or button == "2" or button == "3" or button == "4" or button == "5" or button == "6" or button == "7" or button == "8" or button == "9" or button == "0" or button == ".":
        if whichinput == 1:
            inputone.append(button)
        elif whichinput == 2:
            inputtwo.append(button)

def functionpressed(button):
    if button == " / ":
        whichinput = 2
        operator = " / "
        if whichinput == 1:
            whichinput = 2
        
    if button == " - ":
        whichinput = 2
        operator = " - "
        if whichinput == 1:
            whichinput = 2
        
    if button == " + ":
        whichinput = 2
        operator = " + "
        if whichinput == 1:
            whichinput = 2
        
    if button == " * ":
        whichinput = 2
        operator = " * "
        if whichinput == 1:
            whichinput = 2

    return whichinput
        
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            x , y = pygame.mouse.get_pos()
            button = whichbutton(x , y)
            numberpressed(button)
            whichinput = functionpressed(button)
            if whichinput == 1:
                print inputone
            elif whichinput == 2:
                print inputtwp
           
            


    screen.blit(background, (0,0))
    background.blit(panel, (10,10))
    background.blit(numpad, (20,100))
    background.blit(function, (300,100))
    background.blit(equals, (280,320))
    background.blit(clearbutton, (320,10))
    pygame.display.update()
