import pygame as pg
pg.init()
surface=pg.display.set_mode((800,800))
pg.display.set_caption("Barrels")


def shoot():
    print('ok')
SILVER=(192,192,192)
class Circle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def blit(self):
        pg.draw.circle(surface,SILVER,(self.x,self.y),5)
circle=Circle(200,600)

running=True
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                shoot()
        circle.blit()
        pg.display.update()

