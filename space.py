#----------
# SPACESHIP is a terrible use of the badger medium, due to the low refresh rate
# and slow button responses, but was fun to make (and show off) none the less.
# - ENJOY! :)
#
# NOTES:
#
#    - written for badger OS version 0.0.2
#    - badger2040 appears to not like floats for screen coordinates
#    - (0,0) is the top left, (WIDTH, HEIGHT) is the bottom right of screen
#    - jpegs must be drawn last, or else other objects appear to not show up
#----------

import badger2040
import random
from space.gameEngine import *

#----------
# Globals
#----------

display = badger2040.Badger2040()
badger2040.system_speed(badger2040.SYSTEM_FAST)

displayWidth = badger2040.WIDTH
displayHeight = badger2040.HEIGHT


#----------
# Clear the screen
#----------
def clearScreen():
    display.set_pen(15)
    display.clear()
    display.set_pen(0)
    

#----------
# Game loop
#
# Returns score (int) for printing "Game Over" screen
#----------
def runGame():
    score = 0
    running = True
    player = Player(display)
    asteroids = [Asteroid(display)]
    
    clearScreen()
    display.set_update_speed(badger2040.UPDATE_TURBO)
    display.update()
    
    while running:
        clearScreen()
        
        # move up
        if display.pressed(badger2040.BUTTON_UP) and player.y > 0:
            player.setPosition(player.x, (player.y - 10))
        
        # move down
        elif display.pressed(badger2040.BUTTON_DOWN) and player.y < displayHeight - player.height:
            player.setPosition(player.x, (player.y + 10))
        
        # quit game
        elif display.pressed(badger2040.BUTTON_A):
            running = False
            
        # add asteroids approximately 10% of the time
        if random.randint(0, 100) > 90:
            asteroids.append(Asteroid(display))
        
        for a in asteroids:
            # move and draw asteroids
            if a.onScreen():
                a.updateMovement()
                a.draw()
            # if asteroid off screen, points for you!
            else:
                score += 1
                asteroids.remove(a)
                # and if we happen have no asteroids left, add one
                if (len(asteroids) == 0):
                    asteroids.append(Asteroid(display))
            
        updateScore(score)
        player.draw() #jpeg must always be drawn last for rest to show up
        display.update()
        
        for a in asteroids:
            if a.collision(player):
                running = False
    
    return score
    

#----------
# Title screen
#----------
def displayTitle():
    clearScreen()
    display.set_font("bitmap14_outline")
    display.text("Spaceship!", 20, 20, scale=2)
    display.set_font("bitmap8")
    display.text("Press UP to start", 20, 60, scale=2)
    display.text("Press A and C to quit", 20, 90, scale=2)
    display.set_update_speed(badger2040.UPDATE_FAST)
    display.update()
    
    
#----------
# Game Over screen
#----------
def gameOver(score):
    clearScreen()
    display.set_font("bitmap14_outline")
    display.text("Game Over!", 20, 20, scale=2)
    display.set_font("bitmap8")
    display.text("Score: " + str(score), 190, 25, scale=2)
    display.text("Press UP to start over", 20, 60, scale=2)
    display.text("Press A and C to quit", 20, 90, scale=2)
    display.set_update_speed(badger2040.UPDATE_FAST)
    display.update()
    
    
#----------
# Add the score to the top left of screen
#----------
def updateScore(score):
    display.set_font("bitmap8")
    display.text("Score: " + str(score), 5, 5, scale=2)
    # display.update() will be called when game screen ready to
    # be re-drawn
    

#----------
# Main Program Loop
#----------
displayTitle()

while True:
    #play the game
    if display.pressed(badger2040.BUTTON_UP):
        score = runGame() #loops until player gets hit
        clearScreen()
        display.update()
        gameOver(score)
    
    # User can press A+C to return to badger launcher, as per
    # normal use