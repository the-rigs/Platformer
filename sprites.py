# Sprite classes for platform game
import math
import pygame as pg
from settings import *
vec = pg.math.Vector2
plats = []
pow_block = []

import spritesheet
import random
sprite_sheet_image = pg.image.load('spritesheet2.png')
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
# size = 1
for x in range(21):
    for y in range(25):
        #426X629
        # if x == 6 and y==0:
        color_key  = WHITE
        if (x == 0 or x == 1) and (y ==9 or y ==10):
            color_key = BLACK
        if y == 0 and (x>14 and x < 18):
            # color_key = BLACK
            if x ==15:
                pow_block.append(sprite_sheet.get_image(x, y, 16, 16, color_key))
            pow_block.append(sprite_sheet.get_image(x, y, 16, 16,color_key))
        plats.append(sprite_sheet.get_image(x, y, 16, 16,color_key))
        image = sprite_sheet.get_image(x, y, 16, 16,color_key)


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        # self._layer = PLAYER_LAYER
        pg.sprite.Sprite.__init__(self)
        self.lives = 3
        self.game = game
        self.walking = False
        self.falling = False
        self.current_frame = 0
        self.last_update = 0
        self.jumping = False
        self.total_list = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        self.idle_r = []
        self.idle_l = []
        self.running_r = []
        self.running_l = []
        self.jump_r = []
        self.jump_l = []
        self.trans_list = []
        self.winning_list = []
        self.ladder_list = []
        self.hurt_list = []

        self.stand_list = []
        self.load_images()
        self.image = self.idle_r[0]
        self.rect = self.image.get_rect()
        self.rect.center = (35, HEIGHT - 40)
        self.pos = vec(BLOCK_SIZE*8, HEIGHT-80)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.inventory = []
        self.count = 0
        self.track = 0
        self.far = 0
        self.stop = False
        self.mushroom = False
        self.make_mush = True
        self.big = False
        self.jump_big = 1

    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def animate(self):
        now = pg.time.get_ticks()
        if abs(self.vel.x) > .01:
            self.walking = True
        else:
            self.walking = False
        # idling
        if not self.walking and not self.jumping:
            # if now - self.last_update > 180:
            #     self.last_update = now
            #     self.current_frame = (self.current_frame + 1) % len(self.idle_r)
                bottom = self.rect.bottom
                if self.vel.x < 0:
                    self.image = self.idle_l[0]
                else:
                    self.image = self.idle_r[0]

                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        if self.jumping:
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.jump_r)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.jump_r[self.current_frame]
                else:
                    self.image = self.jump_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        if self.walking and not self.jumping:
            if now - self.last_update > 50:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.running_r)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.running_r[self.current_frame]
                else:
                    self.image = self.running_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.jumping = False
            self.vel.y = -PLAYER_JUMP

    def load_images(self):
        ssi = pg.image.load('small_mario.png').convert_alpha()
        self.sprite_sheet = spritesheet.SpriteSheet(ssi)
        ssi2 = pg.image.load('big_mario.png').convert_alpha()
        self.sprite_sheet2 = spritesheet.SpriteSheet(ssi2)
        for x in range(14):
            for y in range(2):
                if y == 0 and x==0:
                    img = self.sprite_sheet.get_image(x, y, 15, 15, BLACK)
                    img = pg.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE))
                    self.idle_r.append(img)
                    img = pg.transform.flip(img, True, False)
                    img.set_colorkey(BLACK)
                    self.idle_l.append(img)
                if y == 0 and (x == 2 or x==4 or x == 6 ):
                    img = self.sprite_sheet.get_image(x, y, 15, 15, BLACK)
                    img = pg.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE))
                    self.running_r.append(img)
                    img = pg.transform.flip(img, True, False)
                    img.set_colorkey(BLACK)
                    self.running_l.append(img)
                if y == 0 and (x==10):
                    img = self.sprite_sheet.get_image(x, y, 15, 15, BLACK)
                    img = pg.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE))
                    self.jump_r.append(img)
                    img = pg.transform.flip(img, True, False)
                    img.set_colorkey(BLACK)
                    self.jump_l.append(img)
        # for x in range(6):
        #     for y in range(4):
        #         if y == 0 and x==0:
        #             img = self.sprite_sheet2.get_image(x, y, 28, 34, BLACK)
        #             img = pg.transform.scale(img, (52*SCALE, 68*SCALE))
        #             self.idle_r.append(img)
        #             img = pg.transform.flip(img, True, False)
        #             img.set_colorkey(BLACK)
        #             self.idle_l.append(img)
        #         if y == 0 and (x == 1 or x==2 or x == 3 ):
        #             img = self.sprite_sheet2.get_image(x, y, 28, 34, BLACK)
        #             img = pg.transform.scale(img, (52*SCALE, 68*SCALE))
        #             self.running_r.append(img)
        #             img = pg.transform.flip(img, True, False)
        #             img.set_colorkey(BLACK)
        #             self.running_l.append(img)
        #         if y == 0 and (x==5):
        #             img = self.sprite_sheet2.get_image(x, y, 28, 34, BLACK)
        #             img = pg.transform.scale(img, (58*SCALE, 68*SCALE))
        #             self.jump_r.append(img)
        #             img = pg.transform.flip(img, True, False)
        #             img.set_colorkey(BLACK)
        #             self.jump_l.append(img)


    def update(self):
        self.animate()
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_SPACE]:
            # print('jump')
            self.jump()
            self.jumping = True
        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel
        # wrap around the sides of the screen
        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, type):
        pg.sprite.Sprite.__init__(self)
        self.type = type
        self.x = x
        self.y = y
        self.current_frame = 0
        self.last_update = 0
        #floor
        if self.type == 0:
            self.image = plats[0]
        if self.type == 1:
            self.image = plats[0]
        #brick
        elif self.type ==2:
            self.image = plats[25]
        #question mark
        elif self.type ==3:
            self.quest = True
            self.image = pow_block[0]
        #tube
        elif self.type == 4:
            self.image = plats[10]
        elif self.type == 5:
            self.image = plats[9]
        elif self.type == 6:
            self.image = plats[35]
        elif self.type == 7:
            self.image = plats[34]
        elif self.type == 8:
            self.image = plats[1]
        self.rect = self.image.get_rect()
        self.rect.x = BLOCK_SIZE*x
        self.rect.y = HEIGHT-(36*(y+1))*SCALE
        self.quest = True
        self.lift = 0
        self.count = 1
        self.move = False
        self.track = 0
        self.down = False
    def animate(self):
        if self.quest == True:
            now = pg.time.get_ticks()
            if now - self.last_update > 130:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(pow_block)
                self.image = pow_block[self.current_frame]
        else:
            self.image = plats[450]
    def update(self):
        if self.type == 3:
            self.animate()
        if self.move:
            if self.down:
                self.rect.y += 10
                if self.rect.y > (HEIGHT - (36 * (self.y + 1)) * SCALE):
                    self.down = False
                    self.move = False
                    self.rect.y = HEIGHT - (36 * (self.y + 1)) * SCALE
            else:
                self.rect.y -= 10
                if self.rect.y < (HEIGHT - (36 * (self.y + 1)) * SCALE) - 20:
                    self.down = True

class Mushroom(pg.sprite.Sprite):
  def __init__(self,game, x,y):
    # self.groups = game.all_sprites, game.powerups
    pg.sprite.Sprite.__init__(self)
    self.game = game
    self.x = x
    self.y = y
    self.current_frame = 0
    self.last_update = 0
    self.image = pg.Surface((50, 50))
    self.image.fill(RED)
    #self.image = pow_block[0]
    #self.image = pg.transform.scale(self.image,(20,20))
    self.rect = self.image.get_rect()
    self.rect.bottom = y - 50
    self.pos = vec(x, y - 50)
    self.vel = vec(0, 0)
    self.acc = vec(0, 0)
    self.rect.x = x
    self.speedx = 3
    self.move_left = False

    # self.acc.x = PLAYER_ACC
    # self.rect.x = BLOCK_SIZE * self.x - 20
    # self.rect.y = HEIGHT - (36 * (self.y + 1)) * SCALE
  def animate(self):
      now = pg.time.get_ticks()
      if now - self.last_update > 135:
        self.last_update = now
        self.current_frame = (self.current_frame+1)%len(pow_block)
        self.image = pow_block[self.current_frame]
        self.image = pg.transform.scale(self.image,(20,20))
        # bottom = self.rect.bottom+2
        # self.rect = self.image.get_rect()
        # self.rect.bottom = bottom
  def update(self):
    # self.animate()
    #self.rect.x +=4
    self.acc = vec(0, PLAYER_GRAV)

    self.acc.x = MUSH_ACC
    if self.move_left:
        self.acc.x = -MUSH_ACC

    self.acc.x += self.vel.x * PLAYER_FRICTION
    # equations of motion
    self.vel += self.acc
    self.pos += self.vel+.5*self.acc
    self.rect.midbottom = self.pos

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
