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
        self.font_name = pg.font.match_font(FONT_NAME)
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.floors = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for wall in WALL_LIST:
            w = Wall(*wall)
            self.all_sprites.add(w)
            self.walls.add(w)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
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
        if self.player.vel.y < 0:

            # for p in self.platforms:
            #     print('test')
            #     if p.type == 3:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            for p in hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.top:
                        lowest = hit
                        if self.player.pos.x < lowest.rect.right + 10 and self.player.pos.x > lowest.rect.left - 10:
                            print("this is it")
                            self.player.jumping = False

                            self.player.vel.y = abs(self.player.vel.y)
        ###############################################################
                        if self.player.rect.bottom  < lowest.rect.top:
                            print("working on")
                            self.player.rect.bottom = lowest.rect.top
                            self.player.vel.y = 0
                            self.player.jumping = False
                            self.player.falling = False
                            if p.type == 2 and p.type == 3:
                                #self.player.vel.y *= -1
                                self.player.jumping = False
                        if p.type == 3:
                            print('type3')
                            p.quest = False
                            #self.player.vel.y = 0
                            #self.player.vel.y = abs(self.player.vel.y)
                            self.player.vel.y *= -1
                            self.player.jumping = False
                        if p.type == 2:
                            print('type2')
                            p.move = True
                            #self.player.vel.y = abs(self.player.vel.y)
                            #self.player.vel.y *= -1
                            self.player.jumping = False
                            while p.count <101:
                                print(p.count)
                                if p.count <=51:
                                    # p.lift = -10
                                    p.rect.y -=1
                                    print(p.rect.y)
                                else:
                                    print('working')
                                    print(p.rect.y)
                                    p.rect.y +=1
                                    # p.lift = 10
                                p.count += 1
                            if p.count ==10:
                                p.count = 0
                                p.lift = 0
                            # if  p.move:
                            #     p.lift = -1
                            #     p.track = 1
                            #     p.move = False
                            #             # print('Hit')
        ####################################################################


                    # if self.player.pos.y == hits[0].rect.bottom:
            # if hits:
            #     for h in self.platforms:
            #         if self.player.rect.top >= h.rect.bottom:
            #             h.kill()
            #             print('hit')
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            for h in hits:
                if h.type == 0:

                    self.player.jumping = False
                    self.player.falling = False
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0

                else:
                    lowest = hits[0]
                    for hit in hits:
                        if hit.rect.bottom > lowest.rect.top:
                            lowest = hit
                    if self.player.pos.x < lowest.rect.right + 10 and self.player.pos.x > lowest.rect.left - 10:

                        if self.player.rect.bottom-5 < lowest.rect.top - 20:

                            self.player.rect.bottom = lowest.rect.top
                            self.player.vel.y = 0
                            self.player.jumping = False
                            self.player.falling = False
            hit_floor = pg.sprite.spritecollide(self.player,self.floors,False)
            if hit_floor:
                # self.player.jumping = False
                self.player.pos.y = hit_floor[0].rect.top
                self.player.vel.y = 0
            hit_plat_L = pg.sprite.spritecollide(self.player,self.walls,False)
            if hit_plat_L:
                #if self.player.rect.left <= hit_plat_L[0].rect.left:
                self.player.stop=True
                self.player.pos.x += 6
                # print(self.player.pos.x)
        if self.player.stop:
            self.player.acc = 0
        if self.player.rect.right>= WIDTH/2:
            if self.player.vel.x>.05:
                self.player.count +=1

            self.player.pos.x -= abs(self.player.vel.x)
            for plat in self.platforms:
                plat.rect.x -= abs(self.player.vel.x)
            for wall in self.walls:
                    wall.rect.x -= abs(self.player.vel.x)
        # if self.player.vel.x <-.05:
        #     self.player.count -=1
        #     if self.player.count <0:
        #         self.player.count=0
        if self.player.rect.left <= WIDTH/8:
            self.player.pos.x += abs(self.player.vel.x)
            for plat in self.platforms:
                plat.rect.x += abs(self.player.vel.x)
            for wall in self.walls:
                wall.rect.x += abs(self.player.vel.x)
    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            # if event.type == pg.KEYUP:
            #     if event.key == pg.K_SPACE:
            #         self.player.jump_cut()
                    # self.player.jump()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(LIGHTBLUE)
        self.all_sprites.draw(self.screen)
        for i in range(1,14):
            self.draw_text(str(i-1), 22, WHITE, SCREEN_1/2*(2*i-3)*BLOCK_SIZE, HEIGHT/2)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()