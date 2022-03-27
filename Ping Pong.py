from pygame import *
from time import *


font.init()
font = font.SysFont('Arial', 40)
win = font.render('YOU WIN', True, (255, 215, 0))
lose = font.render('YOU LOSE', True, (225, 0, 0))


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
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.x < win_h - 80:
            self.rect.x += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.y = start_y
        self.rect.x = start_x
        if self.rect.y < 495 and self.rect.x < 695:
            self.rect.y += self.speed
            self.rect.X += self.speed
        if self.rect.y < 495 and self.rect.x > 5:
            self.rect.y += self.speed
            self.rect.X -= self.speed
        if self.rect.y > 5 and self.rect.x > 5:
            self.rect.y -= self.speed
            self.rect.X -= self.speed
        if self.rect.y > 5 and self.rect.x < 695:
            self.rect.y -= self.speed
            self.rect.X += self.speed




'''class Enemy(GameSprite):
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

        keys_pressed = key.get_pressed()'''



win_h = 700
win_w = 500


window = display.set_mode((win_h, win_w))
display.set_caption('Ping-Pong')

clock = time.Clock()
FPS = 60

start_x = 350
start_y = 250

speed = 1

back_g = transform.scale(image.load("fon.png"), (700, 500))
sprite1 = Player(('roket.png'), 5, 350, 2, 150, 65)
sprite1 = Player(('roket.png'), 630, 350, 2, 150, 65)
ball = Ball(('ball.png'), start_x, start_y, speed, 70, 70)


finish = False


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            

    if finish != True:
    
        window.blit(back_g, (0, 0))
        sprite1.reset()
        sprite1.update()
        sprite2.reset()
        sprite2.update()
        ball.reset()
        ball.update()


        if sprite.spritecollide(sprite1, ball) or sprite.spritecollide(sprite1, ball):
            speed *=-1
            
        if ball.rect.y == 0 or ball.rect.y == 500:
            speed *=-1

        if ball.rect.x == 0:
            window.blit(win, (200, 200))
            finish = True
        if ball.rect.x == 700:
            window.blit(lose, (200, 200))
            finish = True








        
        


    display.update()
        

    
