import pygame
import random 

import gui2.ui_functions as ui_functions
import classes.class_functions as cf

from scenes.scene import Scene
from scenes.play import Play

import resources2.images

class CreateCharSelect(Scene):
    def __init__(self, game: object, menu_id: int):
        super().__init__(game)
        self.sprites = pygame.sprite.Group()
        self.menu_id = menu_id
        self.gui_dict = {}
        


        # We need to output the result of text from self.game.text_buffer to some position in self.prev.some_list/dict
        
    def update(self, actions):
        for i, sprite in enumerate(self.prev.sprites.sprites()):
            if not sprite.name == "SELECTED" or sprite.name == "start":
                self.gui_dict[i] = sprite

        # print(self.gui_dict)
        for _, sprite in self.gui_dict.items():
            sprite.selected = False
            if self.game.text_ready:
                self.game.text_buffer = ""

        if self.prev.pointer == 0:
            for sprite in self.prev.sprites:
                if sprite.name == 'T0':
                    sprite.selected = True
        
        if self.prev.pointer == 1:
            for sprite in self.prev.sprites:
                if sprite.name == 'T1':
                    sprite.selected = True
                
        if self.prev.pointer == 2:
            for sprite in self.prev.sprites:
                if sprite.name == 'T2':
                    sprite.selected = True     

        if actions["enter"]:
            self.game.typing = True
               

        if actions["escape"]:
            self.exit_scene()
            
        self.prev.sprites.update()
        self.game.reset_keys()


    def render(self, screen):
        self.sprites.draw(screen)
        self.prev.render(screen)