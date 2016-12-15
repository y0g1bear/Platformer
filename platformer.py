"""
platformer.py
Author: <your name here>
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

class suasage(Sprite):
    """
    suasage
    """
    asset = ImageAsset("sausage-merguez.jpg")

    def __init__(self, position, invx, invy):
        super().__init__(suasage.asset, position)
        self.vx = invx
        self.vy = invy
        self.vr = 0
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        
        if self.y >= 500 or self.y <= 0:
                self.vy = self.vy*-1
                
        if self.x >= 1100 or self.x <= 0:
            self.vx = self.vx*-1
            
class monkey(Sprite):
    """
    monkey
    """
    asset = ImageAsset("th.jfif")
    
    def __init__(self,position, invx,invy):
        super().__init__(monkey.asset, position)
        self.vx = invx
        self.vy = invy
        self.vr = 0
    
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        
        if self.y >= 500 or self.y <= 0:
                self.vy = self.vy*-1
                
        if self.x >= 1100 or self.x <= 0:
            self.vx = self.vx*-1
            
            
            
        

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
        s = suasage((0,0),8,8)
        s = suasage((1000,0),-8,5)
        s = suasage((450,450),5,8)
        s = suasage((36,100),10,8)
        l = monckey((50,50))
        p = wall() 
    
       

    def step(self):
        for ship in self.getSpritesbyClass(suasage):
            ship.step()

    def step(self):
        for lol in self.getSpritesbyClass(monkey):
            lol.step()

myapp = sp(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()