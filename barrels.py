import pygame as pg
import math as m
import time, os
start_time=time.time()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,100)
pg.init()
WIDTH=800
HEIGHT=800
surface=pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Barrels")

SILVER=(192,192,192)
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
        self.theta=45
        self.launch=False
        pg.draw.circle(surface,SILVER,(self.x,self.y),5)
    def draw(self):
        if circle.launch==True:
            # self.vy=self.sy+self.ret.x
            self.t+=0.1
            self.x=self.sx+self.vx*self.t
            self.y=self.sy+self.vy*self.t+(0.5)*self.g*self.t**2
            self.y=HEIGHT-self.y
        pg.draw.circle(surface,SILVER,(self.x,self.y),5)
class Reticle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        self.x,self.y=pg.mouse.get_pos()
        pg.draw.line(surface,(255,0,0),(self.x,self.y-10),(self.x,self.y+10))
        pg.draw.line(surface,(255,0,0),(self.x-10,self.y),(self.x+10,self.y))
reticle=Reticle(-1,-1)
circle=Circle(400,400,reticle)

running=True
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.MOUSEBUTTONDOWN:
            circle.launch=True
    if circle.launch==True and circle.t>=50:
        circle.x=circle.sx
        circle.y=circle.sy
        circle.t=0
        circle.launch=False
    surface.fill((0,0,0))
    circle.draw()
    # reticle.draw()
    pg.display.update()