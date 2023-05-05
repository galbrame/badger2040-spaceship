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
    player = Player(display)
    asteroids = [Asteroid(display)]
    
    clearScreen()
    display.set_update_speed(badger2040.UPDATE_TURBO)
    display.update()
    
    while running:
        clearScreen()
        
        if display.pressed(badger2040.BUTTON_UP) and player.y > 0:
            player.setPosition(player.x, (player.y - 10))
        
        elif display.pressed(badger2040.BUTTON_DOWN) and player.y < displayHeight - player.height:
            player.setPosition(player.x, (player.y + 10))
        
        # quit game
        elif display.pressed(badger2040.BUTTON_A):
            running = False
            
        if random.randint(0, 100) > 90:
            asteroids.append(Asteroid(display))
            
        for a in asteroids:
            if a.onScreen():
                a.updateMovement()
                a.draw()
            else:
                score += 1
                asteroids.remove(a)
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
    
    
def updateScore(score):
    display.set_font("bitmap8")
    display.text("Score: " + str(score), 5, 5, scale=2)
    

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

