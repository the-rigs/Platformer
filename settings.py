TITLE = "Jumpy!"
SCALE = (1/2)
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
PLATFORM_LIST = [(17,5,3),
                 (21,5,2),
                 (22,5,3),
                 (23,5,2),
                 (23,9,3),
                 (24,5,3),
                 (25,5,2),
                 (78,5,2),
                 (79,5,2),
                 (80,5,2),
                 (81,10,2),(82,10,2),(83,10,2),(84,10,2),(85,10,2),(86,10,2),(87,10,2),(88,10,2),
                 (91,10,2),(92,10,2),(93,10,2),(94,10,3),(94,5,2),
                 (100,5,2),(101,5,2),
                 (106,5,3),(109,5,3),(109,10,3),(112,5,3),
                 (118,5,2),
                 (121,10,2),(122,10,2),(123,10,2),
                 (128,10,2),(129,10,3),(129,5,2),(130,10,3),(130,5,2),(131,10,2),
                 (134,2,8),(135,2,8),(135,3,8),(136,2,8),(136,3,8),(136,4,8),(137,2,8),(137,3,8),(137,4,8),(137,5,8),
                 (140,2,8),(140,3,8),(140,4,8),(140,5,8),(141,2,8),(141,3,8),(141,4,8),(142,2,8),(142,3,8),(143,2,8),
                 ]
for i in range(-20,192):
    var = (i,0,1)
    var2 = (i,1,0)
    PLATFORM_LIST.append(var)
    PLATFORM_LIST.append(var2)
    #tube loop
    start = 29
    tube_h = 2
    typeT = 5
    for i in range(1, tube_h+1):
        if i != tube_h:
            typet = 5
        else:
            typeT = typeT - 1
        var = (start, i + 1, typeT )
        var2 = (start + 1, i + 1, typeT+2)

        PLATFORM_LIST.append(var)
        PLATFORM_LIST.append(var2)
    start = 39
    tube_h = 3
    typeT = 5
    for i in range(1,tube_h+1):
        if i != tube_h:
            typet = 5
        else:
            typeT = typeT - 1
        var = (start, i + 1, typeT)
        var2 = (start + 1, i + 1, typeT + 2)

        PLATFORM_LIST.append(var)
        PLATFORM_LIST.append(var2)
    start = 47
    tube_h = 4
    typeT = 5
    for i in range(1, tube_h+1):
        if i != tube_h:
            typet = 5
        else:
            typeT = typeT - 1
        var = (start, i + 1, typeT)
        var2 = (start + 1, i + 1, typeT + 2)
        PLATFORM_LIST.append(var)
        PLATFORM_LIST.append(var2)
    start = 58
    tube_h = 4
    typeT = 5
    for i in range(1, tube_h + 1):
        if i != tube_h:
            typet = 5
        else:
            typeT = typeT - 1
        var = (start, i + 1, typeT)
        var2 = (start + 1, i + 1, typeT + 2)
        PLATFORM_LIST.append(var)
        PLATFORM_LIST.append(var2)