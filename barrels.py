##Restart icon created by logisstudio - Flaticon
##https://www.flaticon.com/free-icons/restart
import pygame as pg
import math as m
import random as rand
import time, os
#initializes game
if True:
    start_time=time.time()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,100)
    pg.init()
    WIDTH=800
    HEIGHT=800
    surface=pg.display.set_mode((WIDTH,HEIGHT))
    pg.display.set_caption("Barrels")
    SILVER=(192,192,192)
    RED=(255,0,0)
    GREEN=(0,255,0)
    YELLOW=(225,225,0)
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
        self.click=False
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
class Button:
    def __init__(self,name,sizex,sizey,x,y):
        self.x=x
        self.y=y
        self.sizex=sizex
        self.sizey=sizey
        self.image=pg.image.load(name)
        self.image=pg.transform.scale(self.image,(sizex,sizey))
    def draw(self):
        surface.blit(self.image,(self.x,self.y))
    def is_moused(self):
        self.mouse=pg.mouse.get_pos()
        self.mousex,self.mousey=self.mouse
  
        if self.mousex>=self.x and self.mousey>=self.y:
            if self.mousex<=self.x+self.sizex and self.mousey<=self.y+self.sizex:
                return True
        return False
        
class Game:
    def __init__(self):
        self.lives=3
        self.collision=False
        self.running=True
        self.font=pg.font.SysFont(None,24)
        self.game_over_font=self.font.render('Game Over',True,RED)
        self.game_over=False
        self.score=0
    def draw_game_over(self):
        surface.blit(self.game_over_font,(WIDTH/2-50,HEIGHT/2-50))
    def draw_score(self):
        self.score_font=self.font.render("Score: "+str(self.score),True,YELLOW)
        surface.blit(self.score_font,(0,HEIGHT-100))
    def draw_lives(self):
        self.lives_font=self.font.render("Lives: "+str(self.lives),True,GREEN)
        surface.blit(self.lives_font,(0,HEIGHT-50))
class Bar:
    def __init__(self):
        self.width=20
    def draw(self):
        pg.draw.rect(surface,RED,(0,HEIGHT-20,self.width,20))
#creates objects
if True:
    reticle=Reticle(-1,-1)
    circle=Circle(200,400,reticle)
    barrel=Barrel(300,700)
    bar=Bar()
    restart=Button("restart.png",50,50,WIDTH/2-25,HEIGHT/2-25)
    game=Game()
while game.running:
    #event loop
    for event in pg.event.get():
        if event.type==pg.QUIT:
            game.running=False
        if event.type==pg.MOUSEBUTTONDOWN:
            circle.launch=True
            reticle.click=True
    #calculates bar
    bar.width=HEIGHT-reticle.y
    #resets circle at time t
    if circle.launch==True and circle.t>80:
        circle.reset()
        circle.launch=False
        game.collision=False
    #detects collision increases score
    if circle.x>=barrel.x and circle.x<=barrel.x+100 and circle.y>=barrel.y and circle.y<=barrel.y+100:
        game.collision=True
        barrel.reset()
        game.score+=1
    
    if restart.is_moused() and reticle.click and game.game_over==True:
        game.game_over=False
        circle.reset()
        barrel.reset()
        game.lives=3
        game.score=0
    if reticle.click==True: 
        reticle.click=False
    #clears board and draws everything
    if True:
        surface.fill((0,0,0))
        game.draw_lives()
        game.draw_score()
        if game.game_over==False:
            circle.draw()
            barrel.draw()
            reticle.draw()
            bar.draw()
        else: 
            game.draw_game_over()
            restart.draw()
    #subtracts a life on a miss
    if game.collision==False and circle.launch==True and circle.t>80:
        game.lives-=1
        if game.lives==0:
            game.game_over=True
    
    pg.display.update()