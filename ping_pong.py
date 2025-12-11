from pygame import *
import random


init()

back = (21, 21, 21)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))


game = True
finish = False

clock = time.Clock()
FPS = 60
score1 = 0
score2 = 0

win_score = 5 


speed_x = 3
speed_y = 3

mixer.init()
mixer.music.load("Flat lay of ping pong paddles with ball _ Free Photo_files\8-bit-background-music-for-arcade-game-come-on-mario-164702(1).mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.4)

hit_sound = mixer.Sound("Flat lay of ping pong paddles with ball _ Free Photo_files\cinematic-hit-159487.mp3")

def reset_ball():
    ball.rect.x = 200
    ball.rect.y = 200
    global speed_x, speed_y
    speed_x = random.choice([-3, 3])
    speed_y = random.choice([-3, 3])

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed 
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed    

racket1 = Player("racket1.png", 30, 200, 4, 50, 150)
racket2 = Player("racket2.png", 520, 200, 4, 50, 150)
ball = Player("ball2.png", 200, 200, 4, 50, 50)



font.init()
font = font.Font(None, 35)
lose1 = font.render("PLAYER 1 LOST!", True, (180, 0, 0))
lose2 = font.render("PLAYER 2 LOST!", True, (180, 0, 0))
win1 = font.render("PLAYER 1 WIN!", True, (0, 255, 0))
win2 = font.render("PLAYER 2 WIN!", True, (0, 255, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.reset()
        racket2.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1 
            hit_sound.set_volume(0.2)
            hit_sound.play()

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1 

        if ball.rect.x < 0:
            score2 += 1
            reset_ball()


        if ball.rect.x > win_width:
            score1 += 1
            reset_ball()

        score1_text = font.render(str(score1), True, (255,255,255))
        window.blit(score1_text, (150, 30))

        score2_text = font.render(str(score2), True, (255,255,255))
        window.blit(score2_text, (420, 30))

        if score1 >= win_score:
            finish = True
            window.blit(win1, (180, 200))

        if score2 >= win_score:
            finish = True
            window.blit(win2, (180, 200))

        racket1.update_l()
        racket2.update_r()

    display.update()
    clock.tick(FPS)
