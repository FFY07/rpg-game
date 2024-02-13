import pygame
import sys

import gui2.ui_functions as ui_functions
from scenes.scene import Scene
import resources2.images

class CreateChar(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        self.background = resources2.images.background_img
        
    def update(self, actions):
        pass
    
    def render(self, screen):
        self.game.canvas = self.background