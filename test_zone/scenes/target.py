import pygame

from scenes.scene import Scene
from scenes.enemy_turn import EnemyTurn

from gui2 import ui_functions

import resources2.images as images


class ChooseTarget(Scene):
    def __init__(self, game: object, selected_unit: pygame.sprite.Sprite):
        super().__init__(game)
        self.effect_sprites = pygame.sprite.Group()

        self.attacking_unit = selected_unit

        self.all_enemies = []

        # Add all enemy sprites to a list
        for unit in self.game.enemies.sprites():
            self.all_enemies.append(unit)

        self.selected_unit = self.all_enemies[0]

        # Add pointer sprite
        self.sprites.add(ui_functions.TargetImage(self, images.enemy_target))
        self.pointer = 1
        print("test")

    def update(self, actions):
        self.game.all_units.update()
        # Remove dead sprites from list
        for i, sprite in enumerate(self.all_enemies):
            if not sprite.alive:
                self.all_enemies.pop(i)

        self.pointer = self.pointer % len(self.all_enemies)

        self.selected_unit = self.all_enemies[self.pointer]

        if actions["up"]:
            self.pointer += 1

        if actions["down"]:
            self.pointer -= 1

        if actions["enter"]:
            for sprite in self.sprites.sprites():
                sprite.selected = False

            # Move select screen not written yet under attack.py
            self.attacking_unit.basic_attack(
                self.selected_unit, self.anchor.alive_enemy_dict
            )
            next_scene = EnemyTurn(self.game)

            # Number of times the enemy can attack
            next_scene.attacks = 1

            next_scene.anchor = self.anchor
            next_scene.start_scene()

        if actions["escape"]:
            self.sprites.empty()
            while self.game.stack[-1] != self.anchor:
                self.exit_scene()

        self.game.reset_keys()
        self.sprites.update()

    def render(self, screen):
        self.anchor.render(screen)
        self.sprites.draw(screen)
