##############################################
#   Assignment 2 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
##############################################

import pygame
import random
import sys
from pygame import *
from random import randint
from Classes.Constants import Game, Bar, Face, Player, Color, Music
from Classes.Ball import Ball
from Classes.Bar import VerticalBar, HorizontalBar
from Classes.Object import Object

class PingPong:
    def __init__(self):
        self.screen = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT), 0, 32)
        pygame.display.set_caption("Ping Pong 2.0 - Assignment 2 - Group 4")
        # Initialize the main surface
        self.main_rect = self.screen.get_rect()

        # Initialize the score surface
        #self.score_surface = pygame.Surface([SCREEN_WIDTH, 100])
        #self.score_rect = self.score_surface.get_rect()

        self.basic_font = pygame.font.SysFont("Helvetica", 60)
        self.game_over_font_big = pygame.font.SysFont("VNI-Tekon", 120)
        self.game_over_font_small = pygame.font.SysFont("VNI-Tekon", 80)

        # Initialize Ball - Bar - Object
        self.ball = Ball(Color.WHITE, self.main_rect)
        
        self.bar_left = VerticalBar(Player.PLAYER_1, self.main_rect)
        self.bar_right = VerticalBar(Player.PLAYER_2, self.main_rect)

        self.bar_top1 = HorizontalBar(Player.PLAYER_1, Bar.BAR_TOP, self.main_rect)
        self.bar_top2 = HorizontalBar(Player.PLAYER_2, Bar.BAR_TOP, self.main_rect)
        self.bar_bot1 = HorizontalBar(Player.PLAYER_1, Bar.BAR_BOTTOM, self.main_rect)
        self.bar_bot2 = HorizontalBar(Player.PLAYER_2, Bar.BAR_BOTTOM, self.main_rect)

        self.object = Object(self.main_rect)

        self.all_sprites = pygame.sprite.RenderPlain(self.ball, self.bar_left, self.bar_right, self.bar_top1, self.bar_top2, self.bar_bot1, self.bar_bot2, self.object)

        self.score1 = 0
        self.score2 = 0

        self.background = pygame.image.load("./Image/menu_bg.png")
        self.background2 = pygame.image.load("./Image/end_bg.png")

    def draw_line(self):
        netx = self.main_rect.centerx

        net_rect0 = pygame.Rect(netx, 25, 5, 50)
        net_rect1 = pygame.Rect(netx, 125, 5, 50)
        net_rect2 = pygame.Rect(netx, 225, 5, 50)
        net_rect3 = pygame.Rect(netx, 325, 5, 50)
        net_rect4 = pygame.Rect(netx, 425, 5, 50)
        net_rect6 = pygame.Rect(netx, 625, 5, 50)
        
        pygame.draw.rect(self.screen, Color.WHITE, (net_rect0.left, net_rect0.top, net_rect0.width, net_rect0.height))
        pygame.draw.rect(self.screen, Color.WHITE, (net_rect1.left, net_rect1.top, net_rect1.width, net_rect1.height))
        pygame.draw.rect(self.screen, Color.WHITE, (net_rect2.left, net_rect2.top, net_rect2.width, net_rect2.height))
        pygame.draw.rect(self.screen, Color.WHITE, (net_rect3.left, net_rect3.top, net_rect3.width, net_rect3.height))
        pygame.draw.rect(self.screen, Color.WHITE, (net_rect4.left, net_rect4.top, net_rect4.width, net_rect4.height))
        pygame.draw.rect(self.screen, Color.WHITE, (net_rect6.left, net_rect6.top, net_rect6.width, net_rect6.height))

    def ball_collide_bar(self):
        # Handle direction for ball with bar
        if pygame.sprite.collide_rect(self.ball, self.bar_left):    
            self.ball.handle_collision_bar(Bar.BAR_LEFT)
        elif pygame.sprite.collide_rect(self.ball, self.bar_right):
            self.ball.handle_collision_bar(Bar.BAR_RIGHT)
        elif pygame.sprite.collide_rect(self.ball, self.bar_top1):
            self.ball.handle_collision_bar(Bar.BAR_TOP)
        elif pygame.sprite.collide_rect(self.ball, self.bar_top2):
            self.ball.handle_collision_bar(Bar.BAR_TOP)
        elif pygame.sprite.collide_rect(self.ball, self.bar_bot1):
            self.ball.handle_collision_bar(Bar.BAR_BOTTOM)
        elif pygame.sprite.collide_rect(self.ball, self.bar_bot2):
            self.ball.handle_collision_bar(Bar.BAR_BOTTOM)

        # Handle direction for ball with object
        elif pygame.sprite.collide_rect(self.ball, self.object):
            if self.ball.rect.centerx >= self.object.rect.centerx:
                if abs(self.ball.rect.centery - self.object.rect.centery) <= (self.ball.radius + (self.object.len_y / 2)):
                    self.ball.handle_collision_object(Face.FACE_RIGHT)
                else:
                    if self.ball.rect.centery >= self.object.rect.centery:
                        self.ball.handle_collision_object(Face.FACE_BOTTOM)
                    else:
                        self.ball.handle_collision_object(Face.FACE_TOP)
            else:
                if abs(self.ball.rect.centery - self.object.rect.centery) <= (self.ball.radius + (self.object.len_y / 2)):
                    self.ball.handle_collision_object(Face.FACE_LEFT)
                else:
                    if self.ball.rect.centery >= self.object.rect.centery:
                        self.ball.handle_collision_object(Face.FACE_BOTTOM)
                    else:
                        self.ball.handle_collision_object(Face.FACE_TOP)  

            self.all_sprites.remove(self.object)
            self.object = Object(self.main_rect)
            self.all_sprites.add(self.object)

    def start(self):
        delay_start = True
        collide_time = 250
        delta = 0

        play_time = 60 # Time to play game

        loop_menu = True
        loop_game = True
        loop_end = True

        clock = 0

        # Menu scene
        while loop_menu:      
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        loop_menu = False

            self.screen.blit(self.background, (0, 0))
            pygame.display.update()

        # Main scene
        while loop_game:
            # Check if ball is out the screen or not
            if self.ball.rect.x > Game.SCREEN_WIDTH:
                self.score1 += self.ball.get_score()
                self.ball.reset_normal() 
                self.ball.direction = randint(0, 1)
                delay_start = 0            

            elif self.ball.rect.right < 0:
                self.score2 += self.ball.get_score()  
                self.ball.reset_normal()    
                self.ball.direction = randint(2, 3)  
                delay_start = 0 

            elif self.ball.rect.y > Game.SCREEN_HEIGHT:
                if self.ball.rect.x > Game.SCREEN_WIDTH / 2:
                    self.score1 += self.ball.get_score()
                    self.ball.reset_normal()
                    self.ball.direction = randint(0, 1)
                    delay_start = 0

                elif self.ball.rect.x < Game.SCREEN_WIDTH / 2:
                    self.score2 += self.ball.get_score()
                    self.ball.reset_normal()
                    self.ball.direction = randint(2, 3)
                    delay_start = 0

            elif self.ball.rect.bottom < 0:
                if self.ball.rect.x > Game.SCREEN_WIDTH / 2: 
                    self.score1 += self.ball.get_score()
                    self.ball.reset_normal()
                    self.ball.direction = randint(0, 1)
                    delay_start = 0 

                elif self.ball.rect.x < Game.SCREEN_WIDTH / 2:
                    self.score2 += self.ball.get_score()
                    self.ball.reset_normal()
                    self.ball.direction = randint(2, 3)
                    delay_start = 0 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Player begin moving
                if event.type == KEYDOWN:   
                    # Player 1 moving           
                    if event.key == K_w: # Player 1 move up
                        self.bar_left.move_up = True
                        self.bar_left.move_down = False
                        self.bar_left.isNotMoveUD = False

                        self.bar_left.image.fill(Color.GREEN)
                        self.bar_top1.image.fill(Color.WHITE)
                        self.bar_bot1.image.fill(Color.WHITE)

                    elif event.key == K_s: # Player 1 move down
                        self.bar_left.move_up = False
                        self.bar_left.move_down = True
                        self.bar_left.isNotMoveUD = False

                        self.bar_left.image.fill(Color.GREEN)
                        self.bar_top1.image.fill(Color.WHITE)
                        self.bar_bot1.image.fill(Color.WHITE)
                    
                    elif event.key == K_a: # Player 1 move left
                        self.bar_top1.move_left = True
                        self.bar_top1.move_right = False
                        self.bar_top1.isNotMoveLR = False

                        self.bar_bot1.move_left = True
                        self.bar_bot1.move_right = False
                        self.bar_bot1.isNotMoveLR = False

                        self.bar_left.image.fill(Color.WHITE)
                        self.bar_top1.image.fill(Color.GREEN)
                        self.bar_bot1.image.fill(Color.GREEN)

                    elif event.key == K_d: # Player 1 move right
                        self.bar_top1.move_left = False
                        self.bar_top1.move_right = True
                        self.bar_top1.isNotMoveLR = False

                        self.bar_bot1.move_left = False
                        self.bar_bot1.move_right = True
                        self.bar_bot1.isNotMoveLR = False
                        
                        self.bar_left.image.fill(Color.WHITE)
                        self.bar_top1.image.fill(Color.GREEN)
                        self.bar_bot1.image.fill(Color.GREEN)

                    # Player 2 moving
                    elif event.key == K_UP:
                        self.bar_right.move_up = True
                        self.bar_left.move_down = False
                        self.bar_left.isNotMoveUD = False

                        self.bar_right.image.fill(Color.GREEN)
                        self.bar_top2.image.fill(Color.WHITE)
                        self.bar_bot2.image.fill(Color.WHITE)

                    elif event.key == K_DOWN:
                        self.bar_right.move_up = False
                        self.bar_right.move_down = True
                        self.bar_right.isNotMoveUD = False

                        self.bar_right.image.fill(Color.GREEN)
                        self.bar_top2.image.fill(Color.WHITE)
                        self.bar_bot2.image.fill(Color.WHITE)
                    
                    elif event.key == K_LEFT:
                        self.bar_top2.move_left = True
                        self.bar_top2.move_right = False
                        self.bar_top2.isNotMoveLR = False

                        self.bar_bot2.move_left = True
                        self.bar_bot2.move_right = False
                        self.bar_bot2.isNotMoveLR = False

                        self.bar_right.image.fill(Color.WHITE)
                        self.bar_top2.image.fill(Color.GREEN)
                        self.bar_bot2.image.fill(Color.GREEN)

                    elif event.key == K_RIGHT:
                        self.bar_top2.move_left = False
                        self.bar_top2.move_right = True
                        self.bar_top2.isNotMoveLR = False

                        self.bar_bot2.move_left = False
                        self.bar_bot2.move_right = True
                        self.bar_bot2.isNotMoveLR = False

                        self.bar_right.image.fill(Color.WHITE)
                        self.bar_top2.image.fill(Color.GREEN)
                        self.bar_bot2.image.fill(Color.GREEN)                      

                # Player stop moving
                elif event.type == KEYUP:
                    if event.key == K_w or event.key == K_s:
                        self.bar_left.move_up = self.bar_left.move_down = False
                        self.bar_left.isNotMoveUD = True
                    
                    if event.key == K_a or event.key == K_d:
                        self.bar_top1.move_left = self.bar_top1.move_right = False
                        self.bar_top1.isNotMoveLR = True

                        self.bar_bot1.move_left = self.bar_bot1.move_right = False
                        self.bar_bot1.isNotMoveLR = True

                    elif event.key == K_UP or event.key == K_DOWN:
                        self.bar_right.move_up = self.bar_right.move_down = False
                        self.bar_right.isNotMoveUD = True

                    elif event.key == K_LEFT or event.key == K_RIGHT: 
                        self.bar_top2.move_left = self.bar_top2.move_right = False
                        self.bar_top2.isNotMoveLR = True

                        self.bar_bot2.move_left = self.bar_bot2.move_right = False
                        self.bar_bot2.isNotMoveLR = True

            # Name - Score of player
            name_board = self.basic_font.render("Player 1                          Player 2", True, Color.AQUA) 
            name_board_rect = name_board.get_rect()
            name_board_rect.centerx = self.main_rect.centerx
            name_board_rect.centery = self.main_rect.centery - 80
            score_board = self.basic_font.render(str(self.score1) + "                                      " + str(self.score2), True, Color.AQUA) 
            score_board_rect = score_board.get_rect()
            score_board_rect.centerx = self.main_rect.centerx 
            score_board_rect.centery = self.main_rect.centery

            # Time to play game
            time_board = self.basic_font.render(str(int(play_time)), True, Color.AQUA)
            time_board_rect = time_board.get_rect()
            time_board_rect.centerx = self.main_rect.centerx
            time_board_rect.centery = self.main_rect.centery + 200

            self.screen.fill(Color.GRAY)
            self.draw_line()
            self.screen.blit(name_board, name_board_rect)
            self.screen.blit(score_board, score_board_rect)
            self.screen.blit(time_board, time_board_rect)

            self.all_sprites.draw(self.screen)
            
            self.ball.move()

            self.bar_left.move()
            self.bar_right.move()
            self.bar_top1.move()
            self.bar_top2.move()
            self.bar_bot1.move()
            self.bar_bot2.move()

            self.ball_collide_bar()
            
            pygame.display.update()
            
            # Set the ball can collide after 0.5s
            collide_time -= delta
            if collide_time <= 0:
                self.ball.canCollide = True
                collide_time = 250
            
            if delay_start == False:
                play_time -= delta / 1000
                delta = clock.tick(Game.FPS)

            # Delay 1s when the ball restarts
            elif delay_start == True:
                pygame.time.delay(1000)          
                delay_start = False
                clock = pygame.time.Clock()

            if play_time <= 0:
                loop_game = False
    
        # Finish scene
        while loop_end:     
            for event in pygame.event.get():
                if event.type == QUIT:
                    loop_end = False

            self.screen.blit(self.background2, (0, 0))

            game_over = self.game_over_font_big.render("GAME OVER", True, Color.WHITE)
            if self.score1 > self.score2:    
                game_over1 = self.game_over_font_small.render("Player 1 Wins!", True, Color.WHITE)
            elif self.score1 < self.score2:
                game_over1 = self.game_over_font_small.render("Player 2 Wins!", True, Color.WHITE)
            else:
                game_over1 = self.game_over_font_small.render("DRAW!", True, Color.WHITE)

            game_over_rect = game_over.get_rect()
            game_over_rect.centerx = self.main_rect.centerx
            game_over_rect.centery = self.main_rect.centery - 80
            game_over1_rect = game_over1.get_rect()
            game_over1_rect.centerx = game_over_rect.centerx
            game_over1_rect.centery = game_over_rect.centery + 120

            self.screen.blit(game_over, game_over_rect)
            self.screen.blit(game_over1, game_over1_rect)

            pygame.display.update()


###########################################################################
# Initialize the game
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()

# Start game - Run main loop
myGame = PingPong()
myGame.start()

# Exit game if the main loop ends
pygame.quit()