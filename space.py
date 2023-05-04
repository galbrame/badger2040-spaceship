import badger2040
import time
import random
import io
from machine import Pin
from space.gameEngine import *

#----------
# Globals
#----------

display = badger2040.Badger2040()
badger2040.system_speed(badger2040.SYSTEM_FAST)

displayWidth = badger2040.WIDTH
displayHeight = badger2040.HEIGHT

player = Player(display)


#----------
# Clear the screen
#----------
def clearScreen():
    display.set_pen(15)
    display.clear()
    display.set_pen(0)
    

#----------
# Main Game Loop
#----------
def runGame():
    score = 0
    running = True
    
    clearScreen()
    display.set_update_speed(badger2040.UPDATE_TURBO)
    display.update()
    
    player.setPosition(displayWidth - (player.width + 5), int(displayHeight/2) - int(player.height/2))
    
    while running:
        clearScreen()
        
        if display.pressed(badger2040.BUTTON_UP) and player.y > 0:
            player.setPosition(player.x, (player.y - 10))
        
        elif display.pressed(badger2040.BUTTON_DOWN) and player.y < displayHeight - player.height:
            player.setPosition(player.x, (player.y + 10))
        
        # quit game
        elif display.pressed(badger2040.BUTTON_A):
            running = False
            
        player.draw()
        display.update()
    

#----------
# Title screen
#----------
def displayTitle():
    clearScreen()
    display.set_font("bitmap14_outline")
    display.text("Spaceship!", 20, 20, scale=2)
    display.set_font("bitmap8")
    display.text("Press UP to start", 20, 60, scale=2)
    display.text("Hold C and press A to quit", 20, 90, scale=2)
    display.set_update_speed(badger2040.UPDATE_FAST)
    display.update()
    
    

#----------
# Main Program Loop
#----------
displayTitle()

while True:
    #play the game
    if display.pressed(badger2040.BUTTON_UP):
        runGame() #loops until player gets hit
        clearScreen()
        display.update()
        displayTitle() #show the title screen if player dies
    
    #quit game
    elif display.pressed(badger2040.BUTTON_A):
        clearScreen()
        display.set_update_speed(badger2040.UPDATE_FAST)
        display.update()
        display.halt()

