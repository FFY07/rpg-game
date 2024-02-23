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

        # Unnecessary
        self.class_list = cf.unit_list

        self.class_name = ui_functions.TextSprite(
            self.prev.class_list[0], 40, None, "white", True, 100, "SELECTED"
        )
        self.sprites.add(self.class_name)

    def update(self, actions):
        for sprite in self.sprites:
            if sprite.name != "SELECTED":
                sprite.selected = False

        if self.pointer == 1:
            # We need to output the result of text from self.game.text_buffer to some position in self.prev.some_list/dict
            self.chosen_character = (self.chosen_name, self.chosen_class)
            self.exit_scene()

        if actions["escape"]:
            self.exit_scene()

        self.sprites.update()
        self.game.reset_keys()

    def render(self, screen):
        self.sprites.draw(screen)
