import pygame
import random

import gui2.ui_functions as ui_functions
import classes.class_functions as cf

from scenes.scene import Scene
from scenes.play import Play

import resources2.images as images


class CreateCharSelect(Scene):
    def __init__(self, game: object, menu_id: int):
        super().__init__(game)
        self.sprites = pygame.sprite.Group()
        self.background = images.char_select_background

        self.menu_id = menu_id
        self.gui_dict = {}

        self.chosen_name = "John Wick"
        self.chosen_class = "Knight"
        self.pointer = 0
        self.character_pointer = 0

        # Unnecessary
        self.class_list = cf.unit_list

        self.class_name = ui_functions.TextSprite(
            cf.unit_list[self.character_pointer],
            40,
            None,
            "white",
            True,
            100,
            "SELECTED",
        )
        self.sprites.add(self.class_name)

    def update(self, actions):
        for sprite in self.sprites:
            if sprite.name != "SELECTED":
                sprite.selected = False

        self.character_pointer = self.character_pointer % len(cf.unit_list)

        self.class_name.text = cf.unit_list[self.character_pointer]

        if actions["left"]:
            self.character_pointer += 1

        if actions["right"]:
            self.character_pointer -= 1

        if self.pointer == 1:
            # We need to output the result of text from self.game.text_buffer to some position in self.prev.some_list/dict
            self.chosen_character = (self.chosen_name, self.chosen_class)
            self.exit_scene()

        if actions["escape"]:
            self.exit_scene()

        self.sprites.update()
        self.game.reset_keys()

    def render(self, screen):
        screen.blit(
            pygame.transform.scale(
                self.background, (self.game.screen_width, self.game.screen_height)
            ),
            (0, 0),
        )
        self.sprites.draw(screen)
