# Sprite classes for platform game
import math
import pygame as pg
from settings import *
vec = pg.math.Vector2
plats = []
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

        plats.append(sprite_sheet.get_image(x, y, 16, 16,SCALE, color_key))
        image = sprite_sheet.get_image(x, y, 16, 16,SCALE, color_key)
        # image.set_colorkey(WHITE)

# class Player(pg.sprite.Sprite):
#     def __init__(self, game):
#         pg.sprite.Sprite.__init__(self)
#         self.game = game
#         self.width = 0
#         self.height = 0
#         self.idle_img = []
#         self.run_img_r = []
#         self.run_img_l = []
#         self.running = False
#         self.jumping = False
#         self.current_frame=0
#         self.load_images()
#         self.image = self.idle_img[0]
#         # self.image = pg.Surface((30, 40))
#         # self.image.fill(YELLOW)
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH / 2, HEIGHT / 2)
#         self.pos = vec(WIDTH / 2, HEIGHT / 2)
#         self.vel = vec(0, 0)
#         self.acc = vec(0, 0)
#         self.count = 0
#         self.track = 0
#         self.far = 0
#         self.stop = False
#         self.last_update = pg.time.get_ticks()
#     def animate(self):
#         now =pg.time.get_ticks()
#         if int(self.vel.x) != 0:
#             self.running = True
#             self.jumping  =False
#         else:
#             self.running = False
#         if not self.running and not self.jumping:
#             if now - self.last_update>125:
#                 self.last_update=now
#                 self.current_frame = (self.current_frame+1)%len(self.idle_img)
#                 self.image = self.idle_img[self.current_frame]
#                 self.rect = self.image.get_rect()
#         if self.jumping:
#             self.image = pg.image.load("idle3.png")
#             self.rect = self.image.get_rect()
#         if self.running:
#             if now - self.last_update>100:
#                 self.last_update=now
#                 self.current_frame = (self.current_frame+1)%len(self.run_img_r)
#                 if self.vel.x >0:
#                     self.image = self.run_img_r[self.current_frame]
#                 else:
#                     self.image = self.run_img_l[self.current_frame]
#                 self.rect = self.image.get_rect()
#     def load_images(self):
#         for i in range(1, 4):
#             filename = "idle{}.png".format(i)
#             img = pg.image.load(filename)
#             self.width = img.get_width()* SCALE
#             self.height = img.get_height()* SCALE
#             # img = pg.image.load(filename)
#
#             img = pg.transform.scale(img,(self.width,self.height))
#             self.idle_img.append(img)
#         for i in range(1, 7):
#             filename = "run{}.png".format(i)
#             img = pg.image.load(filename)
#             self.width = img.get_width() * SCALE
#             self.height = img.get_height() * SCALE
#             img = pg.transform.scale(img,(self.width,self.height))
#             self.run_img_r.append(img)
#         for frame in self.run_img_r:
#             self.run_img_l.append(pg.transform.flip(frame, True, False))
#
#     def jump(self):
#         # jump only if standing on a platform
#         self.rect.x += 1
#         hits = pg.sprite.spritecollide(self, self.game.platforms, False)
#         self.rect.x -= 1
#         if hits:
#             self.jumping = True
#             self.vel.y = -20
#
#     def update(self):
#         self.animate()
#         self.acc = vec(0, PLAYER_GRAV)
#         keys = pg.key.get_pressed()
#         if keys[pg.K_LEFT] :
#             self.acc.x = -PLAYER_ACC
#         if keys[pg.K_RIGHT] :
#             self.acc.x = PLAYER_ACC
#
#         # apply friction
#         self.acc.x += self.vel.x * PLAYER_FRICTION
#         # equations of motion
#         self.vel += self.acc
#         self.pos += self.vel + 0.5 * self.acc
#         self.rect.midbottom = self.pos
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
        self.grab_list = []
        self.blink_list_r = []
        self.blink_list_l = []
        self.fall_list_r = []
        self.fall_list_l = []
        self.jump_list_r = []
        self.jump_list_l = []
        self.trans_list = []
        self.winning_list = []
        self.ladder_list = []
        self.hurt_list = []
        self.running_list_r = []
        self.running_list_l = []
        self.stand_list = []
        self.load_images()
        self.image = self.blink_list_r[0]
        self.rect = self.image.get_rect()
        self.rect.center = (35, HEIGHT - 40)
        self.pos = vec(35, HEIGHT - 40)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.inventory = []
        self.count = 0
        self.track = 0
        self.far = 0
        self.stop = False

    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
                self.jumping = False

    def animate(self):
        now = pg.time.get_ticks()
        if abs(self.vel.x) > .01:
            self.walking = True
        else:
            self.walking = False
        # idling
        if not self.walking and not self.jumping:
            if now - self.last_update > 180:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.blink_list_r)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.blink_list_r[self.current_frame]
                else:
                    self.image = self.blink_list_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        if self.vel.y > 0.5:
            self.falling = True
            if now - self.last_update > 50:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.fall_list_r)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.fall_list_r[self.current_frame]
                else:
                    self.image = self.fall_list_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        if self.jumping:
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.jump_list_r)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.jump_list_r[self.current_frame]
                else:
                    self.image = self.jump_list_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        if self.walking and not self.jumping and not self.falling:
            if now - self.last_update > 50:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.running_list_r)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.running_list_r[self.current_frame]
                else:
                    self.image = self.running_list_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

    # def jump(self):
    #     # jump only if standing on a platform
    #     self.rect.x += 1
    #     hits = pg.sprite.spritecollide(self, self.game.platforms, False)
    #     self.rect.x -= 1
    #     if hits:
    #         self.jumping = False
    #         self.falling = False
    #         self.vel.y = -PLAYER_JUMP
    #     hits2 = pg.sprite.spritecollide(self, self.game.platforms1, False)
    #     if hits2:
    #         print('level 2 jump')
    #         self.jumping = False
    #         self.falling = False
    #         self.vel.y = -PLAYER_JUMP
    #     hits3 = pg.sprite.spritecollide(self, self.game.platforms2, False)
    #     if hits3:
    #         print('level 3 jump')
    #         self.jumping = False
    #         self.falling = False
    #         self.vel.y = -PLAYER_JUMP
    #     hits4 = pg.sprite.spritecollide(self, self.game.platforms3, False)
    #     if hits4:
    #         print('level 4 jump')
    #         self.jumping = False
    #         self.falling = False
    #         self.vel.y = -PLAYER_JUMP
    #     hits5 = pg.sprite.spritecollide(self, self.game.platforms4, False)
    #     if hits5:
    #         print('level 5 jump')
    #         self.jumping = False
    #         self.falling = False
    #         self.vel.y = -PLAYER_JUMP
    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.jumping = True
            self.vel.y = -20

    def load_images(self):
        size_ran = random.randrange(2, 8)
        divide = random.randrange(4, 8)
        size = size_ran / divide
        sprite_sheet_image = pg.image.load('mario.png').convert_alpha()
        self.sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
        size = 1
        for x in range(8):
            for y in range(8):
                if x == 0 and y < 3:
                    self.grab_list.append(self.sprite_sheet.get_image(x, y, 32, 40, size, BLACK))
                #   print(self.grab_list)
                elif x == 0 and y < 6 and y > 3:
                    img = self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK)
                    self.blink_list_r.append(img)
                    img = pg.transform.flip(img, True, False)
                    img.set_colorkey(BLACK)
                    self.blink_list_l.append(img)
                #   print(self.blink_list)
                elif x == 2 and y < 2:
                    img = self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK)
                    self.jump_list_r.append(img)
                    img = pg.transform.flip(img, True, False)
                    img.set_colorkey(BLACK)
                    self.jump_list_l.append(img)
                elif x == 0 and y >= 6 and y <= 7:
                    img = self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK)
                    self.fall_list_r.append(img)
                    img = pg.transform.flip(img, True, False)
                    img.set_colorkey(BLACK)
                    self.fall_list_l.append(img)
                elif x == 1 and y < 4:
                    self.ladder_list.append(self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK))
                elif x == 1 and y < 8:
                    self.hurt_list.append(self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK))
                elif x == 1 and y == 8:
                    self.stand_list.append(self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK))
                elif x == 2 and y < 5:
                    self.trans_list.append(self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK))
                elif x == 2 and y < 7:
                    self.winning_list.append(self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK))
                elif x == 5:
                    img = self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK)
                    self.running_list_r.append(img)
                    img = pg.transform.flip(img, True, False)
                    img.set_colorkey(BLACK)
                    self.running_list_l.append(img)

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
            # self.jumping = True
        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, type):
        pg.sprite.Sprite.__init__(self)
        self.type = type
        #floor
        if self.type == 0:
            self.image = plats[0]
        # elif self.type == 1:
        #     self.image = plats[28]
        #brick
        elif self.type ==2:
            self.image = plats[25]
        #question mark
        elif self.type ==3:
            self.image = plats[375]
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