#----------
# NOTES:
#
#    - written for badger OS version 0.0.2
#    - badger2040 appears to not like floats for screen coordinates
#    - (0,0) is the top left, (WIDTH, HEIGHT) is the bottom right of screen
#    - jpegs must be drawn last, or else other objects appear to not show up
#----------

import jpegdec
import random
import badger2040


#----------
# The Player "character" (the spaceship)
#
# Since jpegdec's getWidth() (or get_width() does not appear to work,
# we hardcode the size of the spaceship jpeg.
#----------
class Player():
    def __init__(self, display):
        # get a jpegdec instance
        self.jpeg = jpegdec.JPEG(display.display)
        # make sure it works
        test = self.jpeg.open_file("/space/spaceship.jpg")
        if test == 0:
            display.text("NO PIC!", 20, 20, scale=2)
        
        # set other parameters
        self.width = 40
        self.height = 34
        # center on the right side of the screen
        self.x = badger2040.WIDTH - (self.width + 5)
        self.y = int(badger2040.HEIGHT/2) - int(self.height/2)
        
        
    def setPosition(self, x, y):
        self.x = x
        self.y = y
        
        
    def draw(self):
        self.jpeg.decode(self.x, self.y)
        
        

#----------
# The game obstacles
#
# Random size, speed, and vector (moveX, moveY)
#----------
class Asteroid():
    def __init__(self, display):
        self.display = display
        self.radius = random.randint(2, 5)
        self.setPosition(self.radius, random.randint(self.radius, badger2040.HEIGHT))
        self.speed = random.randint(5, 20)
        self.moveX = int(badger2040.WIDTH/self.speed)
        self.moveY = int((random.randint(self.radius, badger2040.HEIGHT) - self.y)/self.speed)
        
        
    def setPosition(self, x, y):
        self.x = x
        self.y = y
        
        
    def updateMovement(self):
        self.setPosition(self.x + self.moveX, self.y + self.moveY)
        
    
    # Returns a boolean on whether object is still viewable
    def onScreen(self):
        return self.x < badger2040.WIDTH
        
        
    def draw(self):
        self.display.circle(self.x, self.y, self.radius)
        
        
    # Returns a boolean on whether Asteroid collided with Player
    def collision(self, player):
        hit = False
        
        if (self.x + self.radius) > player.x:
            if (self.y + self.radius) > player.y and (self.y + self.radius) < (player.y + player.height):
                hit = True
        
        return hit
