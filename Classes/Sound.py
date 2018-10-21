##############################################
#	Assignment 2 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
##############################################

import pygame
from pygame import mixer
from Classes.Constants import Music

class Sound:
    def __init__(self):
        self.bgMusic = pygame.mixer.music.load(Music.BG_MUSIC)
        self.hitSound = pygame.mixer.Sound(Music.HIT_SOUND)       

    def playBgMusic(self):
        pygame.mixer.music.play(0)

    def playHitSound(self):
        self.hitSound.play()

    def stopHitSound(self):
        self.hitSound.stop()