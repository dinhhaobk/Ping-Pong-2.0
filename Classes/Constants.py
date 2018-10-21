##############################################
#	Assignment 2 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
##############################################

# Game constants
class Game:
    SCREEN_WIDTH = 1300
    SCREEN_HEIGHT = 700
    FPS = 60

# Ball direction constants
class Direction:
    UP_LEFT = 0
    DOWN_LEFT = 1
    UP_RIGHT = 2
    DOWN_RIGHT = 3
        
# Bar constants
class Bar:
    BAR_LEFT = 0
    BAR_RIGHT = 1
    BAR_TOP = 2 
    BAR_BOTTOM = 3

# Player constants
class Player:
    PLAYER_1 = 1
    PLAYER_2 = 2

# Object constants
class Face:
    FACE_TOP = 0
    FACE_BOTTOM = 1
    FACE_LEFT = 2
    FACE_RIGHT = 3

# Time constants

# Font constants

# Text constants

# Color constants
class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    AQUA = (128, 255, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 128, 0)
    GRAY = (64, 64, 64)

# Sound constants
class Music:
    BG_MUSIC = "./Sound/background.ogg"
    HIT_SOUND = "./Sound/hit.wav"