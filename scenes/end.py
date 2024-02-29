import pygame

from scenes.scene import Scene
from scenes.credits import Credits

import resources.images as images


class GameOver(Scene):
    def __init__(self, game: object, victor: str):
        super().__init__(game)
        self.sprites = pygame.sprite.Group()
        self.victor = victor

        if self.victor == "player":
            self.result = images.victory_img

        else:
            self.result = images.defeat_img

    def update(self, actions):
        if actions["escape"] or actions["enter"]:

            # If this isn't set, the game will keep counting rounds
            self.game.rounds = 1
            next_scene = Credits(self.game)
            next_scene.start_scene()

        self.game.reset_keys()
        self.sprites.update()
        self.game.all_units.update()
        self.game.stat_guis.update()

    def render(self, screen):
        self.sprites.draw(screen)
        self.prev.render(screen)
        screen.blit(self.result, (self.xc, self.yc))
