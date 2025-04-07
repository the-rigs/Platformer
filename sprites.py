# Sprite classes for platform game
import pygame as pg
from settings import *
vec = pg.math.Vector2
import spritesheet

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
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
            # img = pg.transform.scale(img,(self.width,self.height))
            self.idle_img.append(img)
        for i in range(1, 7):
            filename = "run{}.png".format(i)
            img = pg.image.load(filename)
            # img = pg.transform.scale(img,(self.width,self.height))
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
            print(self.vel.x, self.acc)
        if keys[pg.K_RIGHT] :
            self.acc.x = PLAYER_ACC
            print(self.vel.x, self.acc)

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
        self.plats = []
        self.load_images()
        if self.type == 1:
            # self.image = pg.Surface((BLOCK_SIZE, BLOCK_SIZE))
            self.image = self.plats[0]
            self.color = COLOR1
        elif self.type == 2:
            self.image = pg.Surface((BLOCK_SIZE, BLOCK_SIZE))
            self.color = COLOR2
        elif self.type ==0:
            self.image = pg.Surface((BLOCK_SIZE, BLOCK_SIZE))
            self.color = GREEN
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = BLOCK_SIZE*x
        self.rect.y = HEIGHT-(36*(y+1))*SCALE

    def load_images(self):
        sprite_sheet_image = pg.image.load('spritesheet.png').convert_alpha()
        self.sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
        # size = 1
        for x in range(25):
            for y in range(36):
                #426X629
                # if x == 6 and y==0:
                self.plats.append(self.sprite_sheet.get_image(x, y, 17.04, 17.47,SCALE, BLACK))

                self.image = self.sprite_sheet.get_image(x, y, 17.04, 17.47,SCALE, BLACK)
                self.image.set_colorkey(BLACK)
                # #   print(self.grab_list)
                # elif x == 0 and y < 6 and y > 3:
                #     # self.blink_list.append(self.sprite_sheet.get_image(x,y,32, 40, size, BLACK))
                #     img = self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK)
                #     self.blink_list_r.append(img)
                #     img = pg.transform.flip(img, True, False)
                #     img.set_colorkey(BLACK)
                #     self.blink_list_l.append(img)
                # #   print(self.blink_list)
                # elif x == 2 and y < 2:
                #     # self.jump_list.append(self.sprite_sheet.get_image(y,x,32, 40, size, BLACK))
                #     img = self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK)
                #     self.jump_list_r.append(img)
                #     img = pg.transform.flip(img, True, False)
                #     img.set_colorkey(BLACK)
                #     self.jump_list_l.append(img)
                # elif x == 0 and y >= 6 and y <= 7:
                #     # self.fall_list.append(self.sprite_sheet.get_image(y,x,32, 40, size, BLACK))
                #     img = self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK)
                #     self.fall_list_r.append(img)
                #     img = pg.transform.flip(img, True, False)
                #     img.set_colorkey(BLACK)
                #     self.fall_list_l.append(img)
                # elif x == 1 and y < 4:
                #     self.ladder_list.append(self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK))
                # elif x == 1 and y < 8:
                #     self.hurt_list.append(self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK))
                # elif x == 1 and y == 8:
                #     self.stand_list.append(self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK))
                # elif x == 2 and y < 5:
                #     self.trans_list.append(self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK))
                # elif x == 2 and y < 7:
                #     self.winning_list.append(self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK))
                # elif x == 5:
                #     img = self.sprite_sheet.get_image(y, x, 32, 40, size, BLACK)
                #     self.running_list_r.append(img)
                #     img = pg.transform.flip(img, True, False)
                #     img.set_colorkey(BLACK)
                #     self.running_list_l.append(img)

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