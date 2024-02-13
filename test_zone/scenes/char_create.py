import pygame
import sys

import gui2.ui_functions as ui_functions
from scenes.scene import Scene
import scenes
import resources2.images

class CreateChar(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        self.background = resources2.images.background_img
        
    def update(self, actions):
        if actions["escape"]:
            self.exit_scene()
            
        # You better reset the keys or the next scene will get mad at you
        self.game.reset_keys()
    
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))