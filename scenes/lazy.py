import pygame


import gui.ui_functions as ui_functions
from scenes.scene import Scene

import resources.images as images
from resources import fonts

class Lazy(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        # self.background = pygame.Surface(0, 0)
        self.background = images.char_select_menu
        self.lazysprites = pygame.sprite.Group()

        self.lazysprites.add(
            ui_functions.TextSprite(
                "ERROR 403 :( ",
                40,
                "Impact",
                "white",
                True,
                self.yc + 110,
                name="SELECTED",
            )
        )
        self.lazysprites.add(
            ui_functions.TextSprite(
                "Sorry, Desmond is lazy to do this feature",
                40,
                "Impact",
                "white",
                True,
                self.yc + 200 ,
                name="SELECTED",
            )
        )

        self.lazysprites.add(
            ui_functions.TextSprite(
                "and he most likely not going to do this",
                40,
                "Impact",
                "white",
                True,
                self.yc + 260,
                name="SELECTED",
            )
        )


    def update(self, actions):

        # if actions["enter"]:
        #     self.exit_scene()

        if actions["escape"]:
            self.exit_scene()

        if actions["space"]:
            self.exit_scene()



        self.game.reset_keys()
        self.lazysprites.update()

    def render(self, screen):
        screen.blit(
            pygame.transform.scale(
                self.background, (self.game.screen_width, self.game.screen_height)
            ),
            (0, 0),
        )
        self.lazysprites.draw(screen)

        for sprite in self.lazysprites.sprites():
            sprite.draw(screen)