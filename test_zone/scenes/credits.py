import pygame

import gui2.ui_functions as ui_functions
from scenes.scene import Scene
import gui2.screen as scr
import resources2.images

credit_section = [55, None, "yellow"]
credit_title = [45, None, "white"]
credit_desc = [45, None, "green"]
credit_name = [35, "segoeuiemoji", "white"]

class Credits(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        self.background = resources2.images.credits_background
        self.credits = pygame.sprite.Group()
        
        # Can't go below integer so use fps to slow it down below 1
        self.game.fps = 45
        self.falling_speed = (0, -2)

        self.credits_header = [
            ('[ Credits ]', *credit_section, True, scr.SCREEN_HEIGHT - 50),
            ('PSB INTRODUCTION TO PROGRAMMING ASSIGNMENT', *credit_desc, True, scr.SCREEN_HEIGHT),
            ('GAME CREATED BY (GROUP A1) ', *credit_desc, True, scr.SCREEN_HEIGHT + 50)
            ]

        self.credits_body = [
            ('[ Members ]', *credit_section, True, scr.SCREEN_HEIGHT + 400),
            
            ('Group Leader', *credit_title, True, scr.SCREEN_HEIGHT + 450),
            ('Desmond Foo Fong Yoong 👑', *credit_name, True, scr.SCREEN_HEIGHT + 500),
            ('Group Members', *credit_title, True, scr.SCREEN_HEIGHT + 650),
            ('Haarith Bin Naguri Ibrahim', *credit_name, True, scr.SCREEN_HEIGHT + 700),
            
            
            ('[ 0 Lines Contributed ]', *credit_section, True, scr.SCREEN_HEIGHT + 850),
            
            ('MOVE YOUR NAME OUT IF YOU SEE IT BELOW', *credit_desc, True, scr.SCREEN_HEIGHT + 900),
            ('THIS IS YOUR LAST CHANCE', *credit_section, True, scr.SCREEN_HEIGHT + 950),
            ('— RZ (17/2/2024)', 45, None, "grey", True, scr.SCREEN_HEIGHT + 1000),

            ('Desmond was planning to give everyone the same grade,', 30, "segoeuiemoji", "grey", True, scr.SCREEN_HEIGHT + 1100),
            ('but I want the lecturer to see this first...', 30, "segoeuiemoji", "grey", True, scr.SCREEN_HEIGHT + 1150),
            
            
            ('Why is your name still here?', *credit_title, True, scr.SCREEN_HEIGHT + 1500),
            ('Haohong Luo', *credit_name, True, scr.SCREEN_HEIGHT + 1550),
            ('Xu Xiang (Ye Xuxiang) Yap', *credit_name, True, scr.SCREEN_HEIGHT + 1600),
            ('Yi Soon Pong', *credit_name, True, scr.SCREEN_HEIGHT + 1650),
            ('Qiao Er Kang', *credit_name, True, scr.SCREEN_HEIGHT + 1700),
            ('(More proof on GitHub)', 35, "segoeuiemoji", "grey", True, scr.SCREEN_HEIGHT + 1950),
            ]
        

        self.credits_footer = [
            ('THANKS FOR PLAYING', *credit_section, True, scr.SCREEN_HEIGHT + 2250),
            (' ', *credit_section, True, scr.SCREEN_HEIGHT + 2300) # padding
            ]

        # Add the sections you want to load into this list
        self.credits_list = [self.credits_header, self.credits_body, self.credits_footer]
                    
        for section in self.credits_list:
            for credit in section:
                credit_sprite = ui_functions.TextSprite(*credit, False, *self.falling_speed)
                self.credits.add(credit_sprite)

    def update(self, actions):
        if actions["escape"] or actions["enter"]:
            self.game.fps = 60
            self.exit_scene()
            
        self.credits.update()
        self.game.reset_keys()
        
        # Go back once credits are finished
        if len(self.credits) == 0:
            self.game.fps = 60
            self.exit_scene()
        
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))
        self.credits.draw(screen)
        