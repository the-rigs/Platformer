import pygame as pg
import random
from settings import *
from sprites import *

# class Game:
#     def __init__(self):
#         # initialize game window, etc
#         pg.init()
#         pg.mixer.init()
#         self.screen = pg.display.set_mode((WIDTH, HEIGHT))
#         pg.display.set_caption(TITLE)
#         self.clock = pg.time.Clock()
#         self.running = True
#
#     def new(self):
#         # start a new game
#         self.all_sprites = pg.sprite.Group()
#         self.platforms = pg.sprite.Group()
#         self.player = Player(self)
#         self.all_sprites.add(self.player)
#         for plat in PLATFORM_LIST:
#             p = Platform(*plat)
#             self.all_sprites.add(p)
#             self.platforms.add(p)
#         self.run()
#
#     def run(self):
#         # Game Loop
#         self.playing = True
#         while self.playing:
#             self.clock.tick(FPS)
#             self.events()
#             self.update()
#             self.draw()
#
#     def update(self):
#         # Game Loop - Update
#         self.all_sprites.update()
#         # check if player hits a platform - only if falling
#         if self.player.vel.y > 0:
#             hits = pg.sprite.spritecollide(self.player, self.platforms, False)
#             if hits:
#                 self.player.jumping = False
#                 self.player.pos.y = hits[0].rect.top
#                 self.player.vel.y = 0
#         #if player reaches top 1/4 of screen
#         if self.player.rect.top<=HEIGHT//4:
#             self.player.pos.y += abs(self.player.vel.y)
#             for plat in self.platforms:
#                 plat.rect.y+=abs(self.player.vel.y)
#                 if plat.rect.top >=HEIGHT:
#                     plat.kill()
#         #spawn new platforms average of 5
#         while len(self.platforms)<6:
#             width = random.randrange(50,101)
#             x =random.randrange(0,WIDTH-width)
#             y = random.randrange(-75, -30)
#             p = Platform(x,y,width,20, COLOR1)
#             self.platforms.add(p)
#             self.all_sprites.add(p)
#         #die
#         if self.player.rect.top>HEIGHT:
#             for sprite in self.all_sprites:
#                 sprite.rect.y -= max(self.player.vel.y, 10)
#                 # sprite.kill()
#                 if  sprite.rect.bottom<0:
#                     sprite.kill()
#         #restart game
#         if len(self.platforms) == 0:
#             self.playing = False
#
#     def events(self):
#         # Game Loop - events
#         for event in pg.event.get():
#             # check for closing window
#             if event.type == pg.QUIT:
#                 if self.playing:
#                     self.playing = False
#                 self.running = False
#             if event.type == pg.KEYDOWN:
#                 if event.key == pg.K_SPACE:
#                     self.player.jump()
#
#     def draw(self):
#         # Game Loop - draw
#         self.screen.fill(BLACK)
#         self.all_sprites.draw(self.screen)
#         # *after* drawing everything, flip the display
#         pg.display.flip()
#
#     def show_start_screen(self):
#         # game splash/start screen
#         pass
#
#     def show_go_screen(self):
#         # game over/continue
#         pass
#
# g = Game()
# g.show_start_screen()
# while g.running:
#     g.new()
#     g.show_go_screen()
#
# pg.quit()


import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.floors = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        # floor = Platform(0,HEIGHT-40,WIDTH,40, RED)
        # self.all_sprites.add(floor)
        # self.floors.add(floor)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        print("track",self.player.track)
        print("far",self.player.far)
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
            hit_floor = pg.sprite.spritecollide(self.player,self.floors,False)
            if hit_floor:
                self.player.pos.y = hit_floor[0].rect.top
                self.player.vel.y = 0
        #if player reaches to 1/4 of screen
        if self.player.vel.x >.05:
            self.player.track +=1
        if self.player.vel.x <-.05:

            self.player.track -=1
        if self.player.track > self.player.far:
            self.player.far = self.player.track
        if self.player.track <-50:
            self.player.stop = True
        if self.player.stop:
            self.player.vel.x = 0
        if self.player.rect.right>= 3*WIDTH/4:
            if self.player.vel.x>.05:
                self.player.count +=1

            self.player.pos.x -= abs(self.player.vel.x)
            for plat in self.platforms:
                plat.rect.x -= abs(self.player.vel.x)
                # if self.player.count > 50:
                #     height = random.randrange(100, 251)
                #     x = random.randrange(WIDTH + 50, WIDTH + 150)
                #     width = x - WIDTH
                #     #     y = random.randrange(-75,-30)
                #     p = Platform(x, HEIGHT - height, width, height)
                #     self.platforms.add(p)
                #     self.all_sprites.add(p)
                #     self.player.count=0
                # if plat.rect.right<=0:
                #     height = random.randrange(100, 251)
                #     x = random.randrange(WIDTH+50,WIDTH+150)
                #     width = x-WIDTH
                #     #     y = random.randrange(-75,-30)
                #     p = Platform(x,HEIGHT-height,width,height)
                #     self.platforms.add(p)
                #     self.all_sprites.add(p)
        if self.player.vel.x <-.05:
            self.player.count -=1
            if self.player.count <0:
                self.player.count=0
        if self.player.rect.left <= WIDTH/4:
            self.player.pos.x += abs(self.player.vel.x)
            for plat in self.platforms:
                plat.rect.x += abs(self.player.vel.x)


                #     plat.kill()

        #spawn new platforms average of 5
        # while len(self.platforms) < 6:
        #     width = random.randrange(50,101)
        #     x = random.randrange(0,WIDTH-width)
        #     y = random.randrange(-75,-30)
        #     p = Platform(x,y,width,20)
        #     self.platforms.add(p)
        #     self.all_sprites.add(p)

        #die
        # if self.player.rect.top> HEIGHT:
        #     for sprite in self.all_sprites:
        #         sprite.rect.y -= max(self.player.vel.y, 10)
        #         if sprite.rect.bottom <0:
        #             sprite.kill()
        # if len(self.platforms) == 0:
        #     self.playing = False







    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(LIGHTBLUE)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()