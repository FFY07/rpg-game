import pygame

import gui.ui_functions as ui_functions
from scenes.scene import Scene

import resources.images as images
from resources import audio
from classes.units.toothless import Toothless

class Lazy(Scene):
    def __init__(self, game: object):
       
        super().__init__(game)
        # self.background = pygame.Surface(0, 0)
        self.background = images.char_select_menu
        self.sprites = pygame.sprite.Group()
        self.lazysprites = pygame.sprite.Group()

        pygame.mixer.music.load(audio.easter)
        pygame.mixer.music.play(-1, 0, 500)

        self.lazysprites.add(Toothless(self.xc, self.yc + 200))

        self.sprites.add(
            ui_functions.TextSprite(
                "ERROR 403 :( ",
                40,
                "Impact",
                "white",
                True,
                self.yc - 260,
                name="SELECTED",
            )
        )
        self.sprites.add(
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

        self.sprites.add(
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

        if actions["escape"] or actions["space"] :
            for sprite in self.sprites:
                sprite.kill()
            for sprite in self.lazysprites:
                sprite.kill()

            self.exit_scene()
            pygame.mixer.music.load(audio.battle_alt)
            pygame.mixer.music.play(-1, 0, 1000)


        self.game.reset_keys()
        self.sprites.update()
        
        self.lazysprites.update(0.25)

    def render(self, screen):
        screen.blit(
            pygame.transform.scale(
                self.background, (self.game.screen_width, self.game.screen_height)
            ),
            (0, 0),
        )

        self.sprites.draw(screen)
        self.lazysprites.draw(screen)