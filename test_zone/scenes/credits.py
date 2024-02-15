import pygame
import sys

import gui2.ui_functions as ui_functions
from scenes.scene import Scene
import gui2.screen as scr
import resources2.images

credit_section = [40, None, "yellow"]
credit_title = [35, None, "white"]
credit_desc = [35, None, "green"]
credit_name = [30, "segoeuiemoji", "white"]

class Credits(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        self.background = resources2.images.credits_background
        self.credits = pygame.sprite.Group()
        
        self.clock = pygame.time.Clock()
        self.clock.tick(30)
        self.falling_speed = (0, -1)

        self.credits_header = [
            ('[ Credits ]', *credit_section, True, scr.SCREEN_HEIGHT - 50),
            ('PSB INTRODUCTION TO PROGRAMMING ASSIGNMENT', *credit_desc, True, scr.SCREEN_HEIGHT),
            ('GAME CREATED BY (GROUP A1) ', *credit_desc, True, scr.SCREEN_HEIGHT + 50)
            ]

        self.credits_body = [
            ('[ Members ]', *credit_section, True, scr.SCREEN_HEIGHT + 150),
            
            ('Group Leader', *credit_title, True, scr.SCREEN_HEIGHT + 200),
            ('Desmond Foo Fong Yoong', *credit_name, True, scr.SCREEN_HEIGHT + 250),
            ('Group Members', *credit_title, True, scr.SCREEN_HEIGHT + 300),
            ('Haarith Bin Naguri Ibrahim', *credit_name, True, scr.SCREEN_HEIGHT + 350),
            ('[Didn\'t Even Test The Game]', *credit_section, True, scr.SCREEN_HEIGHT + 450),
            ('P.S. If you see your name here,', *credit_desc, True, scr.SCREEN_HEIGHT + 500),
            ('just message Desmond and he\'ll move it back ^_^ — RZ', *credit_desc, True, scr.SCREEN_HEIGHT + 550),
            ('Haohong Luo ', *credit_name, True, scr.SCREEN_HEIGHT + 650),
            ('Xu Xiang (Ye Xuxiang) Yap ', *credit_name, True, scr.SCREEN_HEIGHT + 700),
            ('Yi Soon Pong ', *credit_name, True, scr.SCREEN_HEIGHT + 750),
            ('Qiao Er Kang', *credit_name, True, scr.SCREEN_HEIGHT + 800)
            ]

        self.credits_footer = [
            ('THANKS FOR PLAYING', *credit_section, True, scr.SCREEN_HEIGHT + 950),
            (' ', *credit_section, True, scr.SCREEN_HEIGHT + 1000) # padding
            ]

        # Add the sections you want to load into this list
        self.credits_list = [self.credits_header, self.credits_body, self.credits_footer]
                    
        for section in self.credits_list:
            for credit in section:
                credit_sprite = ui_functions.TextSprite(*credit, False, *self.falling_speed)
                self.credits.add(credit_sprite)

    def update(self, actions):
        if actions["escape"] or actions["enter"]:
            self.clock.tick(self.game.fps)
            self.exit_scene()
            
        self.credits.update()
        self.game.reset_keys()
        
        # Go back once credits are finished
        if len(self.credits) == 0:
            self.clock.tick(self.game.fps)
            self.exit_scene()
        
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))
        self.credits.draw(self.game.canvas)
        