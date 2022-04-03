from pygame import *
from time import clock


font.init()
font = font.SysFont('Arial', 40)
win = font.render('WIN GAMER 2', True, (255, 215, 0))
lose = font.render('WIN GAMER 1', True, (255, 215, 0))



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

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_SPACE] and self.rect.y < 375:
            self.rect.y += self.speed

    def update1(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 375 :
            self.rect.y += self.speed




class Ball(GameSprite):

    def __init__ (self, sprite1_image, sprite1_x,  sprite1_y, sprite1_speed, sprite1_vesota, sprite1_dlinna, sprite1_speed_x, sprite1_speed_y):
        super().__init__(sprite1_image, sprite1_x,  sprite1_y, sprite1_speed, sprite1_vesota, sprite1_dlinna)
        self.speed_y = sprite1_speed_y
        self.speed_x = sprite1_speed_x

    def update(self):
        self.rect.y -= self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y > 495:
            self.speed_y *= -1        
        if self.rect.y < 5:
            self.speed_y *= -1




win_h = 700
win_w = 500


window = display.set_mode((win_h, win_w))
display.set_caption('Ping-Pong')

clock = time.Clock()
FPS = 60

start_x = 350
start_y = 250

speed = 4
speed_x = 2
speed_y = 2

back_g = transform.scale(image.load("fon.png"), (700, 500))
sprite1 = Player(('roket.png'), 5, 350, 4, 150, 65)
sprite2 = Player(('roket.png'), 630, 350, 4, 150, 65)
ball = Ball(('ball.png'), start_x, start_y, speed, 70, 70, speed_x, speed_y)


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
        sprite2.update1()
        ball.reset()
        ball.update()


        if sprite.collide_rect(sprite1, ball) or sprite.collide_rect(sprite2, ball):
            ball.speed_x *=-1
            
        if ball.rect.y == 0 or ball.rect.y == 500:
            ball.speed_x *=-1

        if ball.rect.x == 0:
            window.blit(win, (200, 200))
            finish = True
        if ball.rect.x == 700:
            window.blit(lose, (200, 200))
            finish = True


    display.update()
        

    
