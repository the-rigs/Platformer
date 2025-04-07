TITLE = "Jumpy!"
SCALE = (1)
WIDTH = 576
HEIGHT = 540
FPS = 60
FONT_NAME = 'arial'


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
COLOR1 = RED
COLOR2 = BLUE

# Player properties
PLAYER_ACC = 0.8
PLAYER_FRICTION = -0.12
PLAYER_GRAV = .3


BLOCK_SIZE = 36*SCALE

SCREEN_1 = 16
WALL_LIST=[(-14,4,99)]
PLATFORM_LIST = [(17,5,2),
                 (21,5,1),
                 (22,5,2),
                 (23,5,1),
                 (23,9,1),
                 (24,5,2),
                 (25,5,1),
                 (78,5,1),
                 (79,5,1),
                 (80,5,1),
                 (81,10,1),(82,10,1),(83,10,1),(84,10,1),(85,10,1),(86,10,1),(87,10,1),(88,10,1),
                 (91,10,1),(92,10,1),(93,10,1),(94,10,2),(94,5,1),
                 (100,5,1),(101,5,1),
                 (106,5,2),(109,5,2),(109,10,2),(112,5,2),
                 (118,5,1),
                 (121,10,1),(122,10,1),(123,10,1),
                 (128,10,1),(129,10,2),(129,5,1),(130,10,2),(130,5,1),(131,10,1),
                 (134,2,1),(135,2,1),(135,3,1),(136,2,1),(136,3,1),(136,4,1),(137,2,1),(137,3,1),(137,4,1),(137,5,1),
                 (140,2,1),(140,3,1),(140,4,1),(140,5,1),(141,2,1),(141,3,1),(141,4,1),(142,2,1),(142,3,1),(143,2,1),
                 ]
for i in range(-20,192):
    var = (i,0,0)
    var2 = (i,1,0)
    PLATFORM_LIST.append(var)
    PLATFORM_LIST.append(var2)
    #tube loop
    start = 29
    tube_h = 2
    for i in range(1, tube_h+1):
        var = (start, i + 1, 0)
        var2 = (start + 1, i + 1, 0)
        PLATFORM_LIST.append(var)
        PLATFORM_LIST.append(var2)
    start = 39
    tube_h = 3
    for i in range(1,tube_h+1):
        var = (start,i+1,0)
        var2 = (start+1,i+1,0)
        PLATFORM_LIST.append(var)
        PLATFORM_LIST.append(var2)
    start = 47
    tube_h = 4
    for i in range(1, tube_h+1):
        var = (start, i + 1, 0)
        var2 = (start + 1, i + 1, 0)
        PLATFORM_LIST.append(var)
        PLATFORM_LIST.append(var2)
    start = 58
    tube_h = 4
    for i in range(1, tube_h+1):
        var = (start, i + 1, 0)
        var2 = (start + 1, i + 1, 0)
        PLATFORM_LIST.append(var)
        PLATFORM_LIST.append(var2)
