from pygame import *
from random import randint



font.init()
font = font.Font(None, 50)
win = font.render('YOU WIN', True, (255, 215, 0))
lose = font.render('YOU LOSE', True, (225, 0, 0))

lost = 0
sb = 0


class GameSprite(sprite.Sprite):
    def __init__(self, sprite1_image, sprite1_x,  sprite1_y, sprite1_speed, sprite1_vesota, sprite1_dlinna):
        super().__init__()
        self.image = transform.scale(image.load(sprite1_image), (sprite1_dlinna, sprite1_vesota))
        self.speed = sprite1_speed
        self.vesota = sprite1_vesota
        self.dlinna = sprite1_dlinna
        self.rect = self.image.get_rect()
        self.rect.x = sprite1_x
        self.rect.y = sprite1_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):    
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y += self.speed

        if keys_pressed[K_DOWN] and self.rect.xy < win_w - 8:
            self.rect.y -= self.speed

    '''def fire(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE]:
            Sprite_x = self.rect.centerx
            Sprite_y = self.rect.top
            sprite6 = Bullet(('bullet.png'), Sprite_x, Sprite_y, 5, 30, 10  )
            bullets.add(sprite6)




class Bullet(GameSprite):
    def update(self):
        global sb
        if self.rect.y > 0:
            self.direction = 'up'
        if self.rect.y < 0:
            self.rect.y = self.rect.top
        if self.direction == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed'''
def update(self):
        self.rect.y = start_y
        self.rect.x = start_x
        self.direction = 'down'
        self.direction = 'right'
        if self.rect.y > 5 and self.rect.x > 5:
            self.direction = 'down'
            self.direction = 'right'
        if self.rect.y > 5 and self.rect.x > 694:
            self.direction = 'down'
            self.direction = 'left'
        if self.rect.y > 494 and self.rect.x > 695:
            self.direction = 'up'
            self.direction = 'left'
        if self.rect.y > 495 and self.rect.x > 5:
            self.direction = 'up'
            self.direction = 'right'

class Enemy(GameSprite):
    def update(self):
        global lost
        if self.rect.y < 625:
            self.direction = 'down'
        
        if self.rect.y > 626:
            self.rect.y = 0
            self.rect.x = randint(50, 645)
            self.speed = randint(1, 4)
            lost = lost + 1
        if self.direction == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

        keys_pressed = key.get_pressed()
    def retry(self):
        global sb
        if sb == 4 or sb == 6 or sb == 8:
            S_x = randint(50, 645)
            S_x1 = randint(50, 645)
            sprite2 = Enemy(('asteroid.png'), S_x, 100, 2, 65, 65)
            sprite3 = Enemy(('ufo.png'), S_x1, 100, 3, 65, 65)
            monsters.add(sprite2)
            monsters.add(sprite3)
            sb +=1



win_h = 700
win_w = 500


window = display.set_mode((win_h, win_w))
display.set_caption('Шутер')

clock = time.Clock()
FPS = 60

speed

back_g = transform.scale(image.load("galaxy.jpg"), (700, 500))
sprite1 = Player(('rocket.png'), 350, 430, 5, 65, 65)
sprite2 = Enemy(('asteroid.png'), 50, 100, 2, 65, 65)
sprite3 = Enemy(('ufo.png'), 230, 100, 3, 65, 65)
sprite4 = Enemy(('asteroid.png'), 496, 100, 1, 65, 65)
sprite5 = Enemy(('ufo.png'), 650, 100, 4, 65, 65)


monsters = sprite.Group()
monsters.add(sprite2)
monsters.add(sprite3)
monsters.add(sprite4)
monsters.add(sprite5)

bullets = sprite.Group()

finish = False


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            

    if finish != True:
        
        schet1 = font.render('Пропущено: ' + str(lost), True, (225, 20, 150))
        schet2 = font.render('Счет: ' + str(sb), True, (225, 20, 150))


        window.blit(back_g, (0, 0))
        sprite1.reset()
        sprite1.update()
        monsters.draw(window)
        monsters.update()
        sprite2.retry()
        sprite3.retry()
        sprite1.fire()
        bullets.draw(window)
        bullets.update()

        if sprite.spritecollide(sprite1, monsters, False, False):
            window.blit(lose, (200, 200))
            finish = True
            

        if sprite.groupcollide(monsters, bullets, True, True):
            sb = sb + 1
            
            
        if sb == 11:
            window.blit(win, (200, 200))
            finish = True


        window.blit(schet2, (5, 5))
        window.blit(schet1, (5, 35))
        
        

    clock.tick(FPS)
    display.update()
        

    
