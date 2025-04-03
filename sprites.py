# Sprite classes for platform game
import pygame as pg
from settings import *
import random
vec = pg.math.Vector2

import pygame as pg
from settings import *
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.width = 0
        self.height = 0
        self.track = 0
        self.far = 0
        self.stop = False
        self.idle_img= []
        self.run_img_r = []
        self.run_img_l = []
        self.running = False
        self.jumping = False
        self.scale = .2
        self.load_images()
        self.image = self.idle_img[0]
        # self.image = pg.Surface((30, 40))
        # self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (0, FLOOR)
        self.pos = vec(0, FLOOR)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.last_update = 0
        self.current_frame = 0
        self.count = 0
        self.track = 0
        self.far = 0
        self.stop = False

    def animate(self):
        now = pg.time.get_ticks()
        if int(self.vel.x) != 0 and not self.jumping :
            self.running = True
        else:
            self.running = False
        if not self.running:
            if now-self.last_update>125:
                self.last_update =now
                self.current_frame = (self.current_frame+1)%len(self.idle_img)
                self.image = self.idle_img[self.current_frame]
                self.rect= self.image.get_rect()
        if self.jumping:
            self.image = pg.image.load('idle3.png')
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.image = pg.transform.scale(self.image, (self.width * self.scale, self.height * self.scale))
            self.rect = self.image.get_rect()
        if self.running:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.run_img_r)
                if self.vel.x > 0:
                        self.image = self.run_img_r[self.current_frame]
                else:
                    self.image = self.run_img_l[self.current_frame]
                self.rect = self.image.get_rect()


    def load_images(self):
        for i in range(1,4):
            filename='idle{}.png'.format(i)
            img = pg.image.load(filename)
            self.width = img.get_width()
            self.height = img.get_height()
            img =pg.transform.scale(img,(self.width*self.scale,self.height*self.scale))
            self.idle_img.append(img)

        for i in range(1,7):
            filename='run{}.png'.format(i)
            img = pg.image.load(filename)
            self.width = img.get_width()
            self.height = img.get_height()
            img =pg.transform.scale(img,(self.width*self.scale,self.height*self.scale))
            self.run_img_r.append(img)

        for frame in self.run_img_r:
            self.run_img_l.append(pg.transform.flip(frame,True,False))
    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self , self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.jumping = True
            self.vel.y = -20

    def update(self):
        self.animate()
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

# class Platform(pg.sprite.Sprite):
#     def __init__(self, x, y, w, h, color):
#         pg.sprite.Sprite.__init__(self)
#         self.image = pg.Surface((w, h))
#         self.image.fill(color)
#         self.scale = .4
#         self.plat_img = []
#         self.load_images()
#         # self.image = random.choice(self.plat_img)
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#     def load_images(self):
#         for i in range(1,5):
#             filename='platform{}.png'.format(i)
#             img = pg.image.load(filename)
#             self.width = img.get_width()
#             self.height = img.get_height()
#             img =pg.transform.scale(img,(self.width*self.scale,self.height*self.scale))
#             self.plat_img.append(img)
class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, type):
        pg.sprite.Sprite.__init__(self)
        self.type = type
        if self.type == 1:
            self.image = pg.Surface((BLOCK_SIZE, BLOCK_SIZE))
            self.color = COLOR1
        elif self.type == 2:
            self.image = pg.Surface((BLOCK_SIZE, BLOCK_SIZE))
            self.color = COLOR2
        elif self.type ==0:
            self.image = pg.Surface((BLOCK_SIZE, BLOCK_SIZE))
            self.color = GREEN
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = BLOCK_SIZE*(x)
        self.rect.y = HEIGHT - BLOCK_SIZE*(y)