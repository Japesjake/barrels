import pygame as pg
import math as m
import time, os
start_time=time.time()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,100)
pg.init()
surface=pg.display.set_mode((800,800))
pg.display.set_caption("Barrels")

SILVER=(192,192,192)
class Circle:
    def __init__(self,x,y):
        self.sx=x
        self.sy=y
        self.x=x
        self.y=y
        self.v=10
        self.g=-0.1
        self.t=0
        self.theta=60
        self.a=0
        self.flying=False
        self.blit()
        pg.display.update()
    def blit(self):
        pg.draw.circle(surface,SILVER,(self.x,self.y),5)
    def draw(self):
        if True:
            # self.y=(round(self.x)*round(m.tan(self.theta))-self.g*round(self.x)^2)/(2*self.v^2*round(m.cos(self.theta))^2)
            # self.x=(round(self.y)*round(m.tan(self.theta))-self.g*round(self.y)^2)/(2*self.v^2*round(m.cos(self.theta))^2)
            self.t+=1
            # self.y=self.sx+self.v*self.t*m.cos(self.theta)
            # self.x=self.sy+self.v*self.t*m.sin(self.theta)
            # self.y=(self.sx+self.v*self.t)+(0.5*self.g*(self.t^2))
            # self.y=(self.v*m.sin(self.theta)*self.t)-(0.5*self.g*(self.t^2))
            # self.x=self.v*m.cos(self.theta)*self.t

            self.x=self.v*self.t+(0.5)*self.a*self.t**2
            # make sure to add starting location to left of self.x on the left side.
            self.y=self.x*m.tan(self.theta)-self.g*self.x**2/2*(self.v^2)*(m.cos(self.theta)**2)

            circle.blit()

circle=Circle(400,400)

running=True
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                circle.flying=True
    circle.draw()
    pg.display.update()

