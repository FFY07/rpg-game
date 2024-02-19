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
        self.pointer = 0
        self.menu_id = menu_id
        print("welcome to the selection screen you are stuck here now haha jk press escape")        
        # We need to output the result of text from self.game.text_buffer to some position in self.prev.some_list/dict
        
    def update(self, actions):
        if actions["escape"]:
            self.exit_scene()
        self.game.reset_keys()
    #     for sprite in self.sprites.sprites():
    #         sprite.selected = False

    #     self.pointer = self.pointer % (len(self.gui_dict))

    #     if self.pointer == 0:
    #         for sprite in self.sprites.sprites():
    #             if sprite.name == self.pointer:
    #                 sprite.selected = True
        
    #             if actions["enter"]:
    #                 self.selecting = True

    #     if self.pointer == 1:
    #         for sprite in self.sprites.sprites():
    #             if sprite.name == self.pointer:
    #                 sprite.selected = True
        
    #             if actions["enter"]:
    #                 self.selecting = True
                    
    #     if self.pointer == 2:
    #         for sprite in self.sprites.sprites():
    #             if sprite.name == self.pointer:
    #                 sprite.selected = True
        
    #             if actions["enter"]:
    #                 self.selecting = True
                    
    #     if self.pointer == 3:
    #         for sprite in self.sprites.sprites():
    #             if sprite.name == "start":
    #                 sprite.selected = True
        
    #             if actions["enter"]:
    #                 next_scene = Play(self.game)
    #                 next_scene.start_scene()
        
    #     self.selected_name_dict[self.pointer] = self.game.text_buffer
    #     self.text_buffer = ""

    #     if actions["escape"]:
    #         self.exit_scene()
        
    #     if actions['space']:
    #         next_scene = Play(self.game)
    #         next_scene.start_scene()

    #     # if actions["enter"]:            
    #     #     next_scene = Play(self.game)
    #     #     next_scene.start_scene()
        
    #     if actions['up']:
    #         self.pointer -= 1 

    #     if actions['down']:
    #         print('check')
    #         self.pointer += 1

    #     self.game.reset_keys()
    #     self.sprites.update()
    
    # def render(self, screen):
    #     self.sprites.draw(screen)

    #     for sprite in self.sprites.sprites():
    #         sprite.draw(screen)