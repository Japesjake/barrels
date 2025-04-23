import pygame as pg
import math as m
pg.init()
surface=pg.display.set_mode((800,800))
pg.display.set_caption("Barrels")

SILVER=(192,192,192)
class Circle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.v=1
        self.g=1
        self.theta=135
        self.flying=False
        self.blit()
    def blit(self):
        pg.draw.circle(surface,SILVER,(self.x,self.y),5)
    def draw(self):
        if True:
            self.y=(round(self.x)*round(m.tan(self.theta))-self.g*round(self.x)^2)/(2*self.v^2*round(m.cos(self.theta))^2)
            self.x=(round(self.y)*round(m.tan(self.theta))-self.g*round(self.y)^2)/(2*self.v^2*round(m.cos(self.theta))^2)
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

