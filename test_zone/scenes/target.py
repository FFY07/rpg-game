import pygame

from scenes.scene import Scene
from scenes.enemy_turn import EnemyTurn

from gui2 import ui_functions

import resources2.images as images


class ChooseTarget(Scene):
    def __init__(
        self,
        game: object,
        attacking_unit: pygame.sprite.Sprite,
        selected_move: object,
        anchor: object,
    ):
        super().__init__(game)
        self.effect_sprites = pygame.sprite.Group()
        self.anchor = anchor

        self.attacking_unit = attacking_unit
        self.selected_move = selected_move

        self.enemies = list(self.anchor.alive_enemy_dict.values())
        self.pointer = 0

        # Select starting target
        self.selected_unit = self.enemies[self.pointer]

        # Add pointer sprite
        self.sprites.add(ui_functions.TargetImage(self, images.enemy_target))

    def update(self, actions):
        self.enemies = list(self.anchor.alive_enemy_dict.values())
        self.pointer = self.pointer % len(self.enemies)

        self.selected_unit = self.enemies[self.pointer]

        if actions["up"]:
            self.pointer += 1

        if actions["down"]:
            self.pointer -= 1

        if actions["enter"]:
            for sprite in self.sprites.sprites():
                sprite.selected = False

            # Call the move method (method is tied to the unit already) onto the enemy self.unit and the anchor (play.py) alive enemy dictionary
            self.selected_move(self.selected_unit, self.enemies)
            next_scene = EnemyTurn(self.game, self.anchor)

            next_scene.start_scene()

        if actions["escape"]:
            self.sprites.empty()
            while self.game.stack[-1] != self.anchor:
                self.exit_scene()

        self.game.reset_keys()
        self.sprites.update()

        # If game breaks try putting this at the start of the loop
        self.game.all_units.update()

    def render(self, screen):
        self.anchor.render(screen)
        self.sprites.draw(screen)
