##############################################
#   Assignment 2 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
##############################################

import pygame
from pygame import Surface
from Classes.Constants import Game, Bar, Color, Player

class VerticalBar(pygame.sprite.Sprite):
    def __init__(self, play_number, main_rect, len = 100):
        pygame.sprite.Sprite.__init__(self)

        self.play_number = play_number # Number of player: 1 - 2
        self.main_rect = main_rect # Position of bar
        self.len = len # Length of bar

        self.image = pygame.Surface([10, len])
        self.image.fill(Color.WHITE)
        self.rect = self.image.get_rect()

        self.speed = 6  # Speed of bar

        # Variable to check the condition is moving or not
        self.move_up = self.move_down = False
        self.isNotMoveUD = True
        self.isActive = True
        self.canCollide = True # Check if bar can collide ball

        # Specify the location of vertical bar
        if self.play_number == Player.PLAYER_1:
            self.rect.centerx = main_rect.left 
            self.rect.centerx += 50
        if self.play_number == Player.PLAYER_2:
            self.rect.centerx = main_rect.right
            self.rect.centerx -= 50
        self.rect.centery = main_rect.centery

    def move(self):
        if (self.isActive == True) and (self.move_up == True) and (self.rect.top > 50):
            self.rect.y -= self.speed
        elif (self.isActive == True) and (self.move_down == True) and (self.rect.bottom < Game.SCREEN_HEIGHT - 50):
            self.rect.y += self.speed
        elif self.isNotMoveUD == True:
            pass


class HorizontalBar(pygame.sprite.Sprite):
    def __init__(self, play_number, side, main_rect, len = 100):
        pygame.sprite.Sprite.__init__(self)

        self.play_number = play_number # Number of player: 1 - 2
        self.side = side # Side: top, bottom
        self.main_rect = main_rect # Position of bar
        self.len = len # Length of bar

        self.image = pygame.Surface([len, 10])
        self.image.fill(Color.GREEN)
        self.rect = self.image.get_rect()

        self.speed = 6  # Speed of bar

        # Variable to check the condition is moving or not
        self.move_left = self.move_right = False
        self.isNotMoveLR = True
        self.isActive = True
        self.canCollide = True # Check if bar can collide ball

        # Specify the location of vertical bar
        if self.play_number == Player.PLAYER_1:
            self.rect.centerx = main_rect.centerx
            self.rect.centerx *= 0.5

        if self.play_number == Player.PLAYER_2:
            self.rect.centerx = main_rect.centerx
            self.rect.centerx *= 1.5

        if (self.side == Bar.BAR_TOP):
            self.rect.centery = main_rect.top
            self.rect.centery += 50

        elif (self.side == Bar.BAR_BOTTOM):
            self.rect.centery = main_rect.bottom
            self.rect.centery -= 50
        

    def move(self):
        if self.play_number == Player.PLAYER_1:
            if (self.isActive == True) and (self.move_left == True) and (self.rect.left > 50):
                self.rect.x -= self.speed
            elif (self.isActive == True) and (self.move_right == True) and (self.rect.right < (Game.SCREEN_WIDTH / 2) - 10):
                self.rect.x += self.speed
            elif self.isNotMoveLR == True:
                pass
        
        if self.play_number == Player.PLAYER_2:
            if (self.isActive == True) and (self.move_left == True) and (self.rect.left > (Game.SCREEN_WIDTH / 2) + 12):
                self.rect.x -= self.speed
            elif (self.isActive == True) and (self.move_right == True) and (self.rect.right < Game.SCREEN_WIDTH - 50):
                self.rect.x += self.speed
            elif self.isNotMoveLR == True:
                pass