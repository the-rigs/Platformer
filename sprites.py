# Sprite classes for platform game
import math
import pygame as pg
from settings import *
vec = pg.math.Vector2
plats = []
import spritesheet
sprite_sheet_image = pg.image.load('spritesheet.png')
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
# size = 1
for x in range(25):
    for y in range(32):
        #426X629
        # if x == 6 and y==0:
        plats.append(sprite_sheet.get_image(x, y, 17.04, 17.03,SCALE, BLACK))

        image = sprite_sheet.get_image(x, y, 17.04, 17.03,SCALE, BLACK)
        image.set_colorkey(BLACK)

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.width = 0
        self.height = 0
        self.idle_img = []
        self.run_img_r = []
        self.run_img_l = []
        self.running = False
        self.jumping = False
        self.current_frame=0
        self.load_images()
        self.image = self.idle_img[0]
        # self.image = pg.Surface((30, 40))
        # self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.count = 0
        self.track = 0
        self.far = 0
        self.stop = False
        self.last_update = pg.time.get_ticks()
    def animate(self):
        now =pg.time.get_ticks()
        if int(self.vel.x) != 0:
            self.running = True
            self.jumping  =False
        else:
            self.running = False
        if not self.running and not self.jumping:
            if now - self.last_update>125:
                self.last_update=now
                self.current_frame = (self.current_frame+1)%len(self.idle_img)
                self.image = self.idle_img[self.current_frame]
                self.rect = self.image.get_rect()
        if self.jumping:
            self.image = pg.image.load("idle3.png")
            self.rect = self.image.get_rect()
        if self.running:
            if now - self.last_update>100:
                self.last_update=now
                self.current_frame = (self.current_frame+1)%len(self.run_img_r)
                if self.vel.x >0:
                    self.image = self.run_img_r[self.current_frame]
                else:
                    self.image = self.run_img_l[self.current_frame]
                self.rect = self.image.get_rect()
    def load_images(self):
        for i in range(1, 4):
            filename = "idle{}.png".format(i)
            img = pg.image.load(filename)
            self.width = img.get_width()* SCALE
            self.height = img.get_height()* SCALE
            # img = pg.image.load(filename)

            img = pg.transform.scale(img,(self.width,self.height))
            self.idle_img.append(img)
        for i in range(1, 7):
            filename = "run{}.png".format(i)
            img = pg.image.load(filename)
            self.width = img.get_width() * SCALE
            self.height = img.get_height() * SCALE
            img = pg.transform.scale(img,(self.width,self.height))
            self.run_img_r.append(img)
        for frame in self.run_img_r:
            self.run_img_l.append(pg.transform.flip(frame, True, False))

    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.jumping = True
            self.vel.y = -20

    def update(self):
        self.animate()
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] :
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT] :
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, type):
        pg.sprite.Sprite.__init__(self)
        self.type = type
        if self.type == 0:
            self.image = plats[49]
        elif self.type == 1:
            self.image = plats[50]
        elif self.type ==2:
            self.image = plats[160]
        elif self.type ==3:
            self.image = plats[0]
        elif self.type == 4:
            self.image = plats[13]
        elif self.type == 5:
            self.image = plats[14]
        elif self.type == 6:
            self.image = plats[45]
        elif self.type == 7:
            self.image = plats[46]
        elif self.type == 8:
            self.image = plats[136]

        self.rect = self.image.get_rect()
        self.rect.x = BLOCK_SIZE*x
        self.rect.y = HEIGHT-(36*(y+1))*SCALE

class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, type):
        pg.sprite.Sprite.__init__(self)
        self.type = type
        if self.type == 99:
            self.image = pg.Surface((BLOCK_SIZE, BLOCK_SIZE*y*4))
            self.color = LIGHTBLUE
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = BLOCK_SIZE*(SCREEN_1+x)