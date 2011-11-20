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
forn = "num"
func = " "
inputnum = 1  #checks to see if a funtion has been called
firstin = []
secondin = []
def funcornum(x,y): #tests to see if user input is a number or a function
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
            number = "1"
        elif y > 166 and y < 233:
            print 4
            number = "4"
        elif y > 233 and y < 300:
            print 7
            number = "7"
        elif y > 300 and y < 366:
            print 0
            number = "0"
        else:
            number = "none"
    elif x > 86 and x < 152:
        if y > 100 and y < 166:
            print 2
            number = "2"
        elif y > 166 and y < 233:
            print 5
            number = "5"
        elif y > 233 and y < 300:
            print 8
            number = "8"
        elif y > 300 and y < 366:
            print 0
            number = "0"
        else:
            number = "none"
    elif x > 152 and x < 220:
        if y > 100 and y < 166:
            print 3
            number = "3"
        elif y > 166 and y < 233:
            print 6
            number = "6"
        elif y > 233 and y < 300:
            print 9
            number = "9"
        elif y > 300 and y < 366:
            print "."
            number = "."
        else:
            number = "none"
        
    else:
        number =  "none"


    return number

def whichfunction(y):
    if y < 300:
        func = "+"
    elif y < 250:
        func = "*"
    elif y < 200:
        func = "-"
    elif y < 150:
        func = "/"
    return func
        
    

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
                number = whichnumber(x, y)
                if inputnum == 1:
                    firstin.append(number)
                    toprint = " ".join(firstin)
                    print toprint.replace(" ","")
                    
            if forn == "function":
                print "its a function"
                func = whichfunction(y)
                print func
        


    
    screen.blit(background, (0,0))
    background.blit(panel, (10,10))
    background.blit(numpad, (20,100))
    background.blit(function, (300,100))
    background.blit(equals, (280,320))
    background.blit(clearbutton, (320,10))
    pygame.display.update()
    
