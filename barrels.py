import pygame as pg
import math as m
import random as rand
import time, os
start_time=time.time()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,100)
pg.init()
WIDTH=800
HEIGHT=800
surface=pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Barrels")
SILVER=(192,192,192)
RED=(255,0,0)
class Circle:
    def __init__(self,x,y,ret):
        self.ret=ret
        self.sx=x
        self.sy=y
        self.x=x
        self.y=y
        self.vx=10
        self.vy=10
        self.g=-1
        self.t=0
        self.launch=False
        pg.draw.circle(surface,SILVER,(self.x,self.y),5)
    def draw(self):
        if circle.launch==True:
            self.ret.y=HEIGHT-self.ret.y
            self.vy=(self.ret.y-self.sy)/10
            self.vx=(self.ret.x-self.sx)/10
            if self.vx>10:
                self.vx=10
            self.t+=0.1
            self.x=self.sx+self.vx*self.t
            self.y=self.sy+self.vy*self.t+(0.5)*self.g*self.t**2
            self.y=HEIGHT-self.y
        pg.draw.circle(surface,SILVER,(self.x,self.y),5)
    def reset(self):
        circle.x=circle.sx
        circle.y=circle.sy
        circle.t=0
        circle.launch=False
class Reticle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        self.x,self.y=pg.mouse.get_pos()
        pg.draw.line(surface,(255,0,0),(self.x,self.y-10),(self.x,self.y+10))
        pg.draw.line(surface,(255,0,0),(self.x-10,self.y),(self.x+10,self.y))
class Barrel:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.image=pg.image.load("barrel.png")
        self.image=pg.transform.scale(self.image,(100,100))
    def draw(self):
        surface.blit(self.image,(self.x,self.y))
    def reset(self):
        self.x=rand.randint(50,WIDTH-100)
        self.y=rand.randint(50,HEIGHT-100)
class Game:
    def __init__(self):
        self.lives=3
        self.collision=False
        self.running=True
        self.font=pg.font.SysFont(None,24)
        self.img=self.font.render('Game Over',True,RED)
        self.game_over=False
    def draw(self):
        surface.blit(self.img,(WIDTH/2-50,HEIGHT/2-50))
class Bar:
    def __init__(self):
        rect=pg.Rect()
reticle=Reticle(-1,-1)
circle=Circle(200,400,reticle)
barrel=Barrel(300,700)
game=Game()
while game.running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            game.running=False
        if event.type==pg.MOUSEBUTTONDOWN:
            circle.launch=True
    if circle.launch==True and circle.t>=50:##lower 50
        circle.reset()
        circle.launch=False
        game.collision=False
    surface.fill((0,0,0))
    if game.game_over==False:
        circle.draw()
        barrel.draw()
        reticle.draw()
    else: game.draw()

    #detect collision
    if circle.x>=barrel.x and circle.x<=barrel.x+100 and circle.y>=barrel.y and circle.y<=barrel.y+100:
        game.collision=True
        barrel.reset()
    if game.collision==False and circle.launch==True and circle.t>50:
        game.lives-=1
        if game.lives==0:
            game.game_over=True

    
    pg.display.update()