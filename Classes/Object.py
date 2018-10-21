##############################################
#	Assignment 2 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
##############################################

import pygame
from pygame import Surface
from random import randint
from Classes.Constants import Color

class Object(pygame.sprite.Sprite):
    def __init__(self, second_rect):
        pygame.sprite.Sprite.__init__(self)

        self.second_rect = second_rect
        self.len_x = randint(90, 120)
        self.len_y = randint(90, 120)

        self.image = pygame.Surface([self.len_x, self.len_y])
        self.image.fill(Color.BLUE)
        self.rect = self.image.get_rect()

        x = randint(0, 1)
        y = randint(0, 1)
        if x == 0:
            self.rect.centerx = self.second_rect.centerx - randint(90, 120)
        else:
            self.rect.centerx = self.second_rect.centerx + randint(90, 120)

        if y == 0:
                self.rect.centery = self.second_rect.centery - randint(90, 120)
        else:
            self.rect.centery = self.second_rect.centery + randint(90, 120)