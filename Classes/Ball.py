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
from random import randint
from math import sin,cos
from Classes.Constants import Color, Direction, Bar, Face
from Classes.Sound import Sound

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, main_rect, radius = 25):
        pygame.sprite.Sprite.__init__(self)

        self.color = color # Color of ball  
        self.main_rect = main_rect # Position of ball
        self.radius = radius # Radius of ball

    	# Draw the ball (circle)
        self.image = pygame.Surface([2 * radius, 2 * radius])
        self.image.set_colorkey(Color.BLACK)
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)
        self.rect = self.image.get_bounding_rect()
        self.rect.centerx = main_rect.centerx
        self.rect.centery = main_rect.centery

        self.direction = randint(0, 3) # Direction of ball
        self.speed = 3 # Speed of ball
        self.angle = randint(0, 90)

        self.canCollide  = True # Check ball can collide bar or not
        #self.last = pygame.time.get_ticks()

        self.sound = Sound() # Initialize sound for ball
        self.sound.playBgMusic()

    def move(self):
        if self.direction == Direction.UP_LEFT:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
        elif self.direction == Direction.UP_RIGHT:
            self.rect.x += self.speed
            self.rect.y -= self.speed
        elif self.direction == Direction.DOWN_LEFT:
            self.rect.x -= self.speed
            self.rect.y += self.speed
        elif self.direction == Direction.DOWN_RIGHT:
            self.rect.x += self.speed
            self.rect.y += self.speed

    # Handle ball with bar
    def handle_collision_bar(self, side):
        if self.canCollide == True:
            # Handle direction
            if side == Bar.BAR_LEFT:
                if self.direction == Direction.UP_LEFT:
                    self.direction = Direction.UP_RIGHT
                elif self.direction == Direction.DOWN_LEFT:
                    self.direction = Direction.DOWN_RIGHT             

            elif side == Bar.BAR_RIGHT:
                if self.direction == Direction.UP_RIGHT:
                    self.direction = Direction.UP_LEFT
                elif self.direction == Direction.DOWN_RIGHT:
                    self.direction = Direction.DOWN_LEFT  

            elif side == Bar.BAR_TOP:
                if self.direction == Direction.UP_LEFT:
                    self.direction = Direction.DOWN_LEFT
                elif self.direction == Direction.UP_RIGHT:
                    self.direction = Direction.DOWN_RIGHT 

            elif side == Bar.BAR_BOTTOM:
                if self.direction == Direction.DOWN_LEFT:
                    self.direction = Direction.UP_LEFT
                elif self.direction == Direction.DOWN_RIGHT:
                    self.direction = Direction.UP_RIGHT

            # Handle radius - color - speed
            if self.radius <= 10:
                if self.color != Color.RED:
                    self.radius = 25
                self.speed += 1
                if self.speed == 4:
                    self.draw_circle(Color.YELLOW)
                elif self.speed == 5:
                    self.draw_circle(Color.ORANGE)
                elif self.speed >= 6:
                    self.draw_circle(Color.RED)
            else:
                self.radius -= 3
                self.draw_circle(self.color)

            #Play hit sound
            self.sound.stopHitSound()
            self.sound.playHitSound()
            self.canCollide = False

    # Handle ball with object
    def handle_collision_object(self, face):
        if self.canCollide == True:
            # Handle direction
            if face == Face.FACE_RIGHT:
                if self.direction == Direction.UP_LEFT:
                    self.direction = Direction.UP_RIGHT
                elif self.direction == Direction.DOWN_LEFT:
                    self.direction = Direction.DOWN_RIGHT             

            elif face == Face.FACE_LEFT:
                if self.direction == Direction.UP_RIGHT:
                    self.direction = Direction.UP_LEFT
                elif self.direction == Direction.DOWN_RIGHT:
                    self.direction = Direction.DOWN_LEFT  

            elif face == Face.FACE_BOTTOM:
                if self.direction == Direction.UP_LEFT:
                    self.direction = Direction.DOWN_LEFT
                elif self.direction == Direction.UP_RIGHT:
                    self.direction = Direction.DOWN_RIGHT 

            elif face == Face.FACE_TOP:
                if self.direction == Direction.DOWN_LEFT:
                    self.direction = Direction.UP_LEFT
                elif self.direction == Direction.DOWN_RIGHT:
                    self.direction = Direction.UP_RIGHT

            #Play hit sound
            self.sound.stopHitSound()
            self.sound.playHitSound()

    def draw_circle(self, color):
        new_pos_x = self.rect.centerx
        new_pos_y = self.rect.centery
        self.image.fill(Color.BLACK)
        self.image = pygame.Surface([2 * self.radius, 2 * self.radius])
        self.image.set_colorkey(Color.BLACK)
        self.color = color
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_bounding_rect()
        self.rect.centerx = new_pos_x
        self.rect.centery = new_pos_y

    def reset_normal(self):
        self.image.fill(Color.BLACK)
        self.radius = 25
        self.color = Color.WHITE
        self.image = pygame.Surface([2 * self.radius, 2 * self.radius])
        self.image.set_colorkey(Color.BLACK)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_bounding_rect()
        self.rect.centerx = self.main_rect.centerx
        self.rect.centery = self.main_rect.centery

        self.speed = 3
        self.canCollide = True

    # Get score of player (based on color)
    def get_score(self):
        if self.color == Color.WHITE:
            return 1
        elif self.color == Color.YELLOW:
            return 2
        elif self.color == Color.ORANGE:
            return 3
        elif self.color == Color.RED:
            return 4