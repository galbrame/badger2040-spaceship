import sys
import jpegdec

class Player():
    def __init__(self, display):
        self.jpeg = jpegdec.JPEG(display.display)
        test = self.jpeg.open_file("/space/spaceship.jpg")
        if test == 0:
            display.text("NO PIC!", 20, 20, scale=2)
        self.x = 0
        self.y = 0
        # width and height hard coded based on jpeg size
        self.width = 40
        self.height = 34
        
    def setPosition(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self):
        self.jpeg.decode(self.x, self.y)
        
        

class Sprite():
    def __init__(self, x, y, img, display):
        self.setPosition(x, y)
        self.img = img
        self.display = display
        
    def setPosition(self, x=None, y=None):
        if x != None:
            self.x = x
        if y != None:
            self.y = y
        
    def draw(self):
        if self.img != None:
            self.display.img(self.img.bitmap, w=self.img.width, h=self.img.height, x=int(self.x), y=int(self.y))
            
    def collision(self, obstacles):
        hit = False
        
        for obj in obstacles:
            if (self.x + self.img.width >= obj.x and obj.x + obj.img.width >= self.x and
                self.y + self.img.height >= obj.y and obj.y + obj.img.height >= self.y):
                hit = True
        
        return hit
