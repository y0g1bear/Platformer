"""
platformer.py
Author: john
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1450
SCREEN_HEIGHT = 800

blueviolet = Color(0x8a2be2, 1.0)
hotpink = Color(0xff69b4, 1.0)
Aquamarine =Color(0x7fffd4, 1.0)
brown = Color(0xcd5c5c, 1.0)
green = Color(0x00ff7f, .5)
thist = Color(0xd8bfd8, 1.0)
white = Color(0xfafafa, 1.0)
noline = LineStyle(1,hotpink)

# Background
#black = Color(0, 1)
#noline = LineStyle(1, Aquamarine)
#bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, white)
#bg = Sprite(bg_asset, (0,0))
class stars(Sprite):
    loz = ImageAsset("grass-375586_960_720.jpg")
    height = 800
    width = 1450
    
    def __init__(self,position):
        super().__init__(stars.loz, position)
        self.scale = 1.5
    
class suasage(Sprite):
    """
    suasage
    """
    shumcks = ImageAsset("sausage-merguez.jpg")

    def __init__(self, position, invx, invy):
        super().__init__(suasage.shumcks, position)
        self.vx = invx
        self.vy = invy
        self.vr = 0
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        
        if self.y >= 700 or self.y <= 0:
                self.vy = self.vy*-1
                
        if self.x >= 1350 or self.x <= 0:
            self.vx = self.vx*-1
        self.scale = 0.2
class monkey(Sprite):
    """
    monkey
    """
    asset = ImageAsset("th.jfif")
    
    def __init__(self,position,invx,invy):
        super().__init__(monkey.asset, position)
        self.vx = invx
        self.vy = invy
        self.vr = 0
        sp.listenKeyEvent("keydown", "up arrow", self.up)
        sp.listenKeyEvent("keyup", "up arrow", self.up2)
        
        sp.listenKeyEvent("keydown", "right arrow", self.right)
        sp.listenKeyEvent("keyup", "right arrow", self.right2)
        
        sp.listenKeyEvent("keydown", "down arrow" , self.down)
        sp.listenKeyEvent("keyup", "down arrow", self.down2)
        
        sp.listenKeyEvent("keydown", "left arrow", self.left)
        sp.listenKeyEvent("keyup", "left arrow", self.left2)
        self.fxcenter = self.fycenter = 0.5
        self.up = 0
        self.down = 0
        self.right = 0
        self.left = 0
    def step(self):
        icecreamx = self.x
        icecreamy = self.y
        self.x += self.right - self.left
        self.y += self.down - self.up
        self.vy += 2
        self.rotation += self.vr
        
        
        if self.y >= 720  or self.y <= 0:
            self.y = icecreamy
                
        if self.x >= 1405 or self.x <= 0:
            self.x = icecreamx
            
        self.scale = 0.5  
        
        suasages = self.collidingWithSprites(suasage)
        if len(suasages) > 0:
            mysuasage = suasages[0]
            mysuasage.visible=False
            self.visible = False
            banana((mysuasage.x, mysuasage.y))
            
            

        
    def up(self, event):
        if self.visible == True:
            self.up = 30
    def up2(self, event):
        if self.visible == True:
            self.up = 0 
        
    def right(self, event):
        if self.visible == True:
            self.right = 30
    def right2 (self, event):
        if self.visible == True:
            self.right = 0
    
    def down(self, event):
        if self.visible == True:
            self.down = 30
    def down2(self, event):
        if self.visible == True:
            self.down = 0
    
    def left(self, event):
        if self.visible == True:
            self.left = 30
    def left2(self, event):
        if self.visible == True:
            self.left = 0
        
class banana(Sprite):
   asset = ImageAsset("banana.jfif")
   
   def __init__(self,pos):
       super().__init__(banana.asset,pos)

    

        

class wall(Sprite):
    lol = RectangleAsset(1450,40, noline, thist)
    
    def __init__(self):
        super().__init__(wall.lol, (5,750))

p = wall()     

class sp(App):
    """
    
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(1, Aquamarine)
        bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, white)
        bg = Sprite(bg_asset, (0,0))
        p = stars((0,0))
        self.s1 = suasage((600,0),8,8)
        self.s2 = suasage((1000,0),-8,5)
        self.s3 = suasage((450,450),5,8)
        self.s4 = suasage((600,100),10,8)
        self.s5 = suasage((300,100),11,10)
        l = monkey((50,50),0,0)
        
      
        p = wall() 
    def r(self.event):
        self.s1.visible == True
        self.s2.visible == True
        self.s3.visible == True
        self.s4.visible == True
        self.s5.visible == True

    def step(self):
        for ship in self.getSpritesbyClass(suasage):
            ship.step()


        for lol in self.getSpritesbyClass(monkey):
            lol.step()

myapp = sp(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
mapp.listenKeyEvent('r', keydown, shmucs)
