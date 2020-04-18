"""
Created by Benny Chase
Made with a Raspberry Pi 3B+, screenshots may malfunction on other devices. You should have Python 3.5 or higher installed, and you must have Pygame.
"""
# Imports
import pygame, sys, os, time
from pygame.locals import *

# Initiate everything
pygame.init()

winWidth = 960
winHeight = 720

halfWinWidth = winWidth / 2
halfWinHeight = winHeight / 2


DISPLAYSURF = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('Airfoil Model, press SPACE to take a picture')

# Set colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

DISPLAYSURF.fill(WHITE)

# Get input for values in equations
chord = input("What do you want the chord value to be? (use 'x' for example): ")
points = input("How many points should there be? (use 'x' for example): ")

"""
***Change the color value of line 25 to a custom color of the 'set colors' listed above (BLACK, WHITE...).***
"""
AIRFOILCOLOR = GREEN

# Equations
if chord == "x":
    chordValue = 1000
else:
    chordValue = chord

if points == "x":
    pointsValue = 100
else:
    pointsValue = points

COORDINATES = []

CENTER = halfWinWidth, halfWinHeight

QuarterChord = float(chordValue) / 4

for i in range(0, int(pointsValue) - 1):
    pass

COORDINATES = (50, halfWinHeight), (200, 600), (900, 600)

pygame.draw.polygon(DISPLAYSURF, AIRFOILCOLOR, (COORDINATES))

# Forever
while True:
    # Gets events
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                # Captures Screenshot when space is pressed, works on Raspberry Pi 3B+
                os.system("scrot")
                print("Screenshot Captured!")
        # Exits when you press the 'X'
        elif event.type == QUIT:
            print("exiting...")
            pygame.quit()
            sys.exit()
