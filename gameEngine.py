class Img():
    def __init__(self, path):
        with open(path, "rb") as f:
            img_format = f.readline()
            
            if img_format != b'p4\n':
                print("Image must be .pbm format")
                exit()
                
            dimensions = f.readline()
            w, h = [int(x) for x in dimensions.split(b' ')]
            bmp = bytearray(r.read())
        
        self.bitmap = bmp
        self.width = w
        self.height = h
        

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
        if self.image != None:
            self.display.image(self.img.bitmap, w=self.img.width, h=self.img.height, x=int(self.x), y=int(self.y))
            
    def collision(self, obstacles):
        hit = False
        
        for obj in obstacles:
            if (self.x + self.img.width >= obj.x and obj.x + obj.img.width >= self.x and
                self.y + self.img.height >= obj.y and obj.y + obj.img.height >= self.y):
                hit = True
        
        return hit