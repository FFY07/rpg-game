import pygame

import gui.ui_functions as ui_functions
from scenes.scene import Scene

import resources.images as images
class GameLog(Scene):
    def __init__(self, game):

        super().__init__(game)

        self.gamelog = images.gamelog_background
        self.sprites = pygame.sprite.Group()

        self.position = self.yc - 200

        self.sprites.add(
            ui_functions.TextSprite(
                "Game History ",
                25,
                "Impact",
                "black",
                True,
                self.yc - 230,
                name="SELECTED",
            )
        )

        for i , line in enumerate(self.game.event_log):
            self.load_section(f"{self.game.event_log[-i]}", 35)

            print(self.sprites)

    def load_section(self, text_list, offset):
        for text in text_list:
            self.sprites.add(
                ui_functions.TextSprite(
                    text, 20, None, self.position, False,
                )
            )

    def update(self, actions):

        # if actions["enter"]:
        #     self.exit_scene()

        if actions["escape"] or actions["space"]:
            for sprite in self.sprites:
                sprite.kill()

            self.exit_scene()

        self.game.reset_keys()
        self.game.all_units.update()


    def render(self, screen):

        self.prev.render(screen)

        screen.blit(
            pygame.transform.scale(
                self.gamelog, (500, 650)
            ),
            (self.xc -250, self.yc -300),
        )


        self.sprites.draw(screen)