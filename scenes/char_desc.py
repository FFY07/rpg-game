import pygame

import gui.ui_functions as ui_functions
from scenes.scene import Scene

import resources.images as images
import resources.fonts as fonts

desc_format = [20, "hightowertext", "grey27"]
name_format = [25, fonts.eagle_lake, "grey10"]


class CharDesc(Scene):
    def __init__(self, game, selected_unit: object):

        super().__init__(game)
        self.background = images.gamelog_background
        self.sprites = pygame.sprite.Group()

        # starting position
        self.position = 150

        self.selected_unit = selected_unit

        for name, desc in self.selected_unit.move_desc.items():
            self.load_section([name], name_format, 25)
            self.load_section([desc], desc_format, 50)

    def load_section(self, text_list, section_type, offset):
        for text in text_list:
            self.sprites.add(
                ui_functions.TextSprite(
                    text.strip(), *section_type, True, self.position
                )
            )
            self.position += offset

    def update(self, actions):

        if actions["escape"] or actions["space"]:
            for sprite in self.sprites:
                sprite.kill()

            self.game.reset_keys()
            self.exit_scene()

        self.game.reset_keys()
        self.game.all_units.update()

    def render(self, screen):

        self.prev.render(screen)

        screen.blit(
            pygame.transform.scale(self.background, (500, 650)),
            (self.xc - 250, self.yc - 300),
        )

        self.sprites.draw(screen)
