import pygame

import gui2.ui_functions as ui_functions
from scenes.scene import Scene
import gui2.screen as scr
import resources2.images
from scenes.play import Play

#next_scene = Story(self.game)
#next_scene.start_scene()
story_header = [55, None, "yellow"]
story_color = [45, None, "white"]


class Story(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        self.background = resources2.images.story_background
        self.story = pygame.sprite.Group()
        
        # Can't go below integer so use fps to slow it down below 1
        self.game.fps = 45
        self.falling_speed = (0, -1.5)

        self.story_header = [
            ('Aventure to PSB Academy ', *story_header, True, scr.SCREEN_HEIGHT - 50),
            ('Stupid story sorry ', *story_header, True, scr.SCREEN_HEIGHT - 100),
            ]

        self.story_body = [

            ("Inside PSB Academy, something wasn't right.", *story_color, True, scr.SCREEN_HEIGHT + 100),
            ("The students were acting strangely", *story_color, True, scr.SCREEN_HEIGHT + 150),
            ("They doing bad things like being a freerider", *story_color, True, scr.SCREEN_HEIGHT + 200),
            ('Not doing their assigment', *story_color, True, scr.SCREEN_HEIGHT + 250),
            ('using Chatgpt to do all the quiz', *story_color, True, scr.SCREEN_HEIGHT + 300),
            ('You noticed and decided to stop it with friend', *story_color, True, scr.SCREEN_HEIGHT + 350), 
            ('as all of you went through the keep seeing all the bad stuff ', *story_color, True, scr.SCREEN_HEIGHT + 400),    
            ('happening because of the students being idiot.', *story_color, True, scr.SCREEN_HEIGHT + 450),   
            # ('Hall of Fame', *story_color, True, scr.SCREEN_HEIGHT + 250),


            ('PLease kill them', *story_color, True, scr.SCREEN_HEIGHT + 550), 
            ('Press Enter to Continue BTW', *story_color, True, scr.SCREEN_HEIGHT + 600), 
            ]
        
        # Add the sections you want to load into this list
        self.story_list = [self.story_header, self.story_body]
                    
        for section in self.story_list:
            for credit in section:
                credit_sprite = ui_functions.TextSprite(*credit, False, *self.falling_speed)
                self.story.add(credit_sprite)

    def update(self, actions):
        if actions["escape"]: 
            self.game.fps = 60
            self.exit_scene()
            
        if actions["enter"]:
            next_scene = Play(self.game)
            next_scene.start_scene()

        if actions["space"]:
            next_scene = Play(self.game)
            next_scene.start_scene()

        self.story.update()
        self.game.reset_keys()
        
        # Go back once credits are finished
        if len(self.story) == 0:
            self.game.fps = 60
            next_scene = Play(self.game)
            next_scene.start_scene()
        
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))
        self.story.draw(screen)
        