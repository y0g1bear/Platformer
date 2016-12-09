"""
platformer.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000

blueviolet = Color(0x8a2be2, 1.0)
hotpink = Color(0xff69b4, 1.0)
Aquamarine =Color(0x7fffd4, 1.0)
brown = Color(0xcd5c5c, 1.0)
green = Color(0x00ff7f, .5)
thist = Color(0xd8bfd8, 1.0)
white = Color(0xfafafa, 1.0)
noline = LineStyle(1,white)

# Background
black = Color(0, 1)
noline = LineStyle(1, Aquamarine)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, white)
bg = Sprite(bg_asset, (0,0))

class suasage(Sprite):
    """
    suasage
    """
    asset = ImageAsset("sausage-merguez.jpg")

    def __init__(self, position):
        super().__init__(suasage.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        
  
s = suasage((100,100))

class wall(Sprite):
    lol = RectangleAsset(1500,40, noline, thist)
    
    def __init__(self):
        super().__init__(wall.lol, (5,600))
p = wall()     

class sp(App):
    """
    
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg = Sprite(bg_asset, (0,0))
       
       

    def step(self):
        for ship in self.getSpritesbyClass(suasage):
            ship.step()
            if self.y >= 1000:
                self.vy = self.vy*-1
                self.vx = self.vx*-1
                print("it works")

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run(s.step)