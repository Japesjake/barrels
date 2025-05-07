##Music by <a href="https://pixabay.com/users/djartmusic-46653586/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=301284">Krzysztof Szymanski</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=301284">Pixabay</a>
##<a href="https://www.flaticon.com/free-icons/music" title="music icons">Music icons created by Freepik - Flaticon</a>
##<a href="https://www.flaticon.com/free-icons/itunes" title="itunes icons">Itunes icons created by IconBaandar - Flaticon</a>
##<a href="https://www.flaticon.com/free-icons/bomb" title="bomb icons">Bomb icons created by Ylivdesign - Flaticon</a>
####version 1.11
import pygame as pg
import math as m
import random as rand
import time, os, pickle
#initializes game
if True:
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,50)
    pg.init()
    pg.mixer.init()
    music=pg.mixer.music.load("background.mp3")
    pg.mixer.music.play(-1)
    bam=pg.mixer.Sound('explosion.wav')
    game_over_sound=pg.mixer.Sound('game_over.mp3')
    WIDTH=800
    HEIGHT=800
    surface=pg.display.set_mode((WIDTH,HEIGHT))
    pg.display.set_caption("Barrels")
    SILVER=(192,192,192)
    RED=(255,0,0)
    GREEN=(0,255,0)
    YELLOW=(225,225,0)
    barrel_image=pg.image.load("barrel.png")
    barrel_image=pg.transform.scale(barrel_image,(100,100))
class Circle:
    def __init__(self,x,y,ret):
        self.ret=ret
        self.sx=x
        self.sy=HEIGHT-y
        self.x=x
        self.y=HEIGHT-y
        self.vx=10
        self.vy=10
        self.g=-1
        self.t=0
        self.launch=False
        pg.draw.circle(surface,SILVER,(self.x,self.y),5)
    def draw(self):
        if circle.launch==True:
            if self.ret.click==True:
                self.ret.y=HEIGHT-self.ret.y
                self.vy=(self.ret.y-self.sy)/10
                self.vx=(self.ret.x-self.sx)/10
            if self.vx>10:
                self.vx=10
            self.t+=0.1
            self.x=self.sx+self.vx*self.t
            self.y=HEIGHT-self.sy+self.vy*self.t+(0.5)*self.g*self.t**2
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
    def __init__(self,image):
        self.sx=rand.randint(50,WIDTH-100)
        self.sy=rand.randint(50,HEIGHT-100)
        self.x=self.sx
        self.y=self.sy
        self.reversed=False
        self.dx=self.sx+300
        self.dy=self.sy+300
        self.image=image
    def move(self,direction='horizontal',swap=False):
        if direction=='horizontal':
            if self.x>=self.sx and self.reversed==False:
                self.x+=.5
            if self.x<=self.dx+1 and self.x>=self.dx-1:
                self.reversed=True
            if self.reversed==True:
                self.x-=.5
            if self.x<=self.sx+1 and self.x>=self.sx-1:
                self.reversed=False
        if direction=='verticle':
            if self.y>=self.sy and self.reversed==False:
                self.y+=.5
            if self.y<=self.dy+1 and self.y>=self.dy-1:
                self.reversed=True
            if self.reversed==True:
                self.y-=.5
            if self.y<=self.sy+1 and self.y>=self.sy-1:
                self.reversed=False
        
    def draw(self):
        surface.blit(self.image,(self.x,self.y))
    def reset(self):
        self.sx=rand.randint(50,WIDTH-100)
        self.sy=rand.randint(50,HEIGHT-100)
class Explosion:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.image=pg.image.load("blast.png")
        self.image=pg.transform.scale(self.image,(100,100))
    def draw(self):
        surface.blit(self.image,(self.x,self.y))
class Button:
    def __init__(self,name,sizex,sizey,x,y):
        self.x=x
        self.y=y
        self.sizex=sizex
        self.sizey=sizey
        self.on=True
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
class Text:
    def __init__(self,text,color,x,y,obj=None,integer=False,type=None):
        self.text=text
        self.color=color
        self.x=x
        self.y=y
        self.font=pg.font.SysFont(None,24)
        self.obj=obj
        self.integer=integer
        self.type=type
    def draw(self):
        if self.integer==True:
            if self.type=='score': 
                self.img=self.font.render(self.text+str(self.obj.score),True,self.color)
            if self.type=='lives': 
                self.img=self.font.render(self.text+str(self.obj.lives),True,self.color)
            if self.type=='high_score':
                self.img=self.font.render(self.text+str(self.obj.high_score),True,self.color)
        else: self.img=self.font.render(self.text,True,self.color)
        surface.blit(self.img,(self.x,self.y))
class Game:
    def __init__(self):
        self.lives=10000
        self.collision=False
        self.running=True
        self.font=pg.font.SysFont(None,24)
        self.game_over_font=self.font.render('Game Over',True,RED)
        self.game_over=False
        self.high_score=self.load_score()
        self.score=0
        self.start=pg.time.get_ticks()
    def save_score(self):
        with open('high_score.p', 'wb') as file:
            pickle.dump(self.high_score, file)
    def load_score(self):
        with open('high_score.p', 'rb') as file:
            data = pickle.load(file)
            return data
class Bar:
    def __init__(self):
        self.width=20
    def draw(self):
        pg.draw.rect(surface,RED,(0,HEIGHT-20,self.width,20))
#creates objects
if True:
    reticle=Reticle(-1,-1)
    circle=Circle(200,400,reticle)
    barrel=Barrel(barrel_image)
    bar=Bar()
    restart=Button("restart.png",50,50,WIDTH/2-25,HEIGHT/2-25)
    mute=Button("note.png",50,50,WIDTH-50,0)
    game=Game()
    score=Text('Score: ',YELLOW,0,HEIGHT-100,game,True,'score')
    lives=Text('Lives: ',GREEN,0,HEIGHT-50,game,True,'lives')
    game_over=Text('Gameover',RED,WIDTH/2-40,HEIGHT/2-50,game,False)
    high_score=Text('HighScore: ',YELLOW,0,0,game,True,'high_score')
    explosion=Explosion(-100,-100)
while game.running:
    #event loop
    for event in pg.event.get():
        if event.type==pg.QUIT:
            game.save_score()
            game.running=False
        if event.type==pg.MOUSEBUTTONDOWN:
            if mute.is_moused()==False:
                circle.launch=True
            reticle.click=True
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:
                game.high_score=0
                print('KeyDown')
    #calculates bar
    bar.width=HEIGHT-reticle.y
    #resets circle
    if circle.launch==True and circle.t>80:
        circle.reset()
        circle.launch=False
        game.collision=False
    #detects collision, explodes barrel, and increases score
    if circle.x>=barrel.x and circle.x<=barrel.x+100 and circle.y>=barrel.y and circle.y<=barrel.y+100:
        game.collision=True
        game.start=pg.time.get_ticks()
        pg.mixer.Sound.play(bam)
        explosion=Explosion(barrel.x,barrel.y)
        # barrel.reset()
        barrel=Barrel(barrel_image)
        game.score+=1
        if game.high_score<game.score:
            game.high_score=game.score
    #restarts the game
    if restart.is_moused() and reticle.click and game.game_over==True:
        game.game_over=False
        circle.reset()
        barrel.reset()
        game.lives=3
        game.score=0
        if mute.on==True:
            pg.mixer.music.play()
    #toggles music
    if mute.is_moused() and reticle.click:
        if mute.on==True:
            pg.mixer.music.pause()
            mute.on=False
        else:
            pg.mixer.music.unpause()
            mute.on=True
    #saves score on game over
    if game.game_over==True:
        if game.score>game.high_score:
            game.save_score()
    #############clears surface and draws everything#############
    if True:
        surface.fill((0,0,0))
        score.draw()
        lives.draw()
        high_score.draw()
        mute.draw()
        if game.game_over==False:
            circle.draw()
            if game.score>=10:
                barrel.move('horizontal')
            if game.score>=20:
                barrel.move('verticle')
            if game.score>=3:
                pass
            barrel.draw()
            reticle.draw()
            bar.draw()
            if pg.time.get_ticks()-game.start<500:
                explosion.draw()
        else: 
            game_over.draw()
            restart.draw()
    #############################################################
    #resets click
    if reticle.click==True: 
        reticle.click=False
    #subtracts a life on a miss
    if game.collision==False and circle.launch==True and circle.t>80:
        game.lives-=1
        if game.lives==0:
            game.game_over=True
            pg.mixer.music.pause()
            game_over_sound.play()
            
    
    pg.display.update()