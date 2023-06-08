from pygame import *
from random import choice
from time import sleep


class GameSprite(sprite.Sprite):
    def __init__(self, texture, xpos, ypos, width, height, speed):
        super().__init__()
        self.texture = transform.scale(image.load(texture), (width, height))
        self.speed = speed
        self.rect = self.texture.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
    
    def show(self):
        screen.blit(self.texture, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, xpos, ypos):
        super().__init__('C:/Users/gamin/white.jpg', xpos, ypos, 10, 100, 5)
    
    def move(self, distance):
        self.rect.y -= distance


class Ball(GameSprite):
    def __init__(self, xpos, ypos):
        super().__init__('C:/Users/gamin/white.jpg', xpos, ypos, 20, 20, 5)
        self.velocityX = choice([-1, 1])
        self.velocityY = choice([-1, 1])
    
    def update_velocity(self):
        if self.rect.y < 20 or self.rect.y > 460:
            self.velocityY *= -1
        
        if sprite.collide_rect(player1, self) or sprite.collide_rect(player2, self):
            self.velocityX *= -1
    
    def move(self):
        self.rect.x += self.speed * self.velocityX
        self.rect.y += self.speed * self.velocityY


init()

screen = display.set_mode((700, 500))
clock = time.Clock()
font = font.Font(None, 50)

player1 = Player(50, 200)
player2 = Player(640, 200)
ball = Ball(330, 230)

lose1 = font.render('LEFT GUY LOST!', True, (180, 0, 0))
lose2 = font.render('RIGHT GUY LOST!', True, (180, 0, 0))

loss = False
game = True

while game:    
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    keys = key.get_pressed()
    
    if keys[K_w] and player1.rect.y > 20:
        player1.move(player1.speed)
    if keys[K_s] and player1.rect.y < 380:
        player1.move(-player1.speed)

    if keys[K_UP] and player2.rect.y > 20:
        player2.move(player2.speed)
    if keys[K_DOWN] and player2.rect.y < 380:
        player2.move(-player2.speed)
    
    ball.move()
    ball.update_velocity()
    
    screen.fill((20, 100, 200))
    player1.show()
    player2.show()
    ball.show()

    if ball.rect.x <= 0:
        screen.blit(lose1, (200, 225))
        loss = True
    elif ball.rect.x >= 680:
        screen.blit(lose2, (190, 225)) 
        loss = True
    
    if loss:
        player1_speed = player1.speed
        player2_speed = player2.speed
        ball_speed = ball.speed

        player1.speed = 0
        player2.speed = 0
        ball.speed = 0

        display.update()
        sleep(1)
        loss = False

        player1.rect.x = 50
        player1.rect.y = 200
        player1.speed = player1_speed

        player2.rect.x = 640
        player2.rect.y = 200
        player2.speed = player2_speed

        ball.rect.x = 330
        ball.rect.y = 230
        ball.speed = ball_speed

    clock.tick(60)
    display.update()
