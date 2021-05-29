#Create your own shooter

from pygame import *
from random import *
clock = time.Clock()
FPS = 60
#create game window
window_width = 500
window_height = 700
window = display.set_mode((window_width,window_height))
#set scene background
background = transform.scale(image.load("galaxy.jpg"),(window_width,window_height))
#backgrounddos = transform.scale(image.load("C:\Users\AAL\Documents\Python\Test images"),(700,500))
#create 2 sprites and place them on the scene
sprite1 = transform.scale(image.load("ufo.png"),(100,100))
sprite2 = transform.scale(image.load("rocket.png"),(100,100))
font.init()
#handle "click on the "Close the window"" event 
mixer.init()
mixer.music.load("C:/Users/AAL/Documents/musiccc.mp3")
mixer.music.play()
#money = mixer.Sound("money.ogg")
#kick = mixer.Sound("kick.ogg")
font.init()
font1 = font.SysFont('Arial',36)
game = True

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.player_speed = player_speed

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x >= 0:
            self.rect.x -= 10
        if key_pressed[K_RIGHT] and self.rect.x <= 450:
            self.rect.x += 10
    def fire(self):
        bullet = Bullet("bullet.png",self.rect.centerx,self.rect.top,15)
        bullets.add(bullet)



lost = 0
class Enemy(GameSprite):
    def update(self):
        global lost
        if self.rect.y >= 0:
            self.rect.y += self.player_speed
        if self.rect.y >= 700:
            lost += 1
            self.player_speed = randint(2,7)
            self.rect.x = randint(0,400)
            self.rect.y = 0

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.player_speed
        if self.rect.y <= 0:
            self.kill()
            
def collision():
    pass



enemies = sprite.Group()

hero = Player("rocket.png",0,600,3)

enemy1 = Enemy("ufo.png",randint(0,400),0,randint(2,7))
enemy2 = Enemy("ufo.png",randint(0,400),0,randint(2,7))
enemy3 = Enemy("ufo.png",randint(0,400),0,randint(2,7))
enemy4 = Enemy("ufo.png",randint(0,400),0,randint(2,7))
enemy5 = Enemy("ufo.png",randint(0,400),0,randint(2,7))

enemies.add(enemy1)
enemies.add(enemy2)
enemies.add(enemy3)
enemies.add(enemy4)
enemies.add(enemy5)
win_points = 0
bullets = sprite.Group()

finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()
    
    if finish != True:
        hero.reset()
        hero.update()
        enemies.update()
        bullets.update()
        text_missed = font1.render("Missed: " + str(lost), 1, (255,255,255))
        bve_collide_list = sprite.groupcollide(bullets,enemies,True,True)
        evh_collide_list = sprite.spritecollide(hero,enemies,False)
        if len(evh_collide_list) or lost >= 3:
            text_lose = font1.render("YOU LOSE", 1, (255,255,255))
            window.blit(text_lose, (250,350))
        for i in range(len(bve_collide_list)):
            win_points += 1
            enemyx = Enemy("ufo.png",randint(0,400),0,randint(2,7))
            enemies.add(enemyx)
        if win_points >= 10:
            text_win = font1.render("YOU WIN",1,(255,255,255))
            window.blit(text_win,(250,350))
        text_hit = font1.render("Hit: " + str(win_points), 1, (255,255,255))
        display.update()
        window.blit(background,(0,0))
        window.blit(text_missed,(0,0))
        window.blit(text_hit,(0,50))
        enemies.draw(window)
        bullets.draw(window)
        

    clock.tick(FPS)
    