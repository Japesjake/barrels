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
        self.theta=180
        self.flying=False
    def blit(self):
        pg.draw.circle(surface,SILVER,(self.x,self.y),5)
    def draw(self):
        circle.blit()
        if self.x<=400 and self.flying:
            self.y=(self.x*round(m.tan(self.theta))-self.g*self.x^2)/(2*self.v^2*round(m.cos(self.theta))^2)
            self.x+=1
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

