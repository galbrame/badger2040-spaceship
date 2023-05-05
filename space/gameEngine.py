import jpegdec
import random
import badger2040


class Player():
    def __init__(self, display):
        # width and height hard coded based on jpeg size
        self.width = 40
        self.height = 34
        self.jpeg = jpegdec.JPEG(display.display)
        test = self.jpeg.open_file("/space/spaceship.jpg")
        if test == 0:
            display.text("NO PIC!", 20, 20, scale=2)
        self.x = badger2040.WIDTH - (self.width + 5)
        self.y = int(badger2040.HEIGHT/2) - int(self.height/2)
        
        
    def setPosition(self, x, y):
        self.x = x
        self.y = y
        
        
    def draw(self):
        self.jpeg.decode(self.x, self.y)
        
        

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
        
        
    def onScreen(self):
        return self.x < badger2040.WIDTH
        
        
    def draw(self):
        self.display.circle(self.x, self.y, self.radius)
        
        
    def collision(self, player):
        hit = False
        
        if (self.x + self.radius) > player.x:
            if (self.y + self.radius) > player.y and (self.y + self.radius) < (player.y + player.height):
                hit = True
        
        return hit
