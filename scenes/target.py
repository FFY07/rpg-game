import pygame

from scenes.scene import Scene
from scenes.enemy_turn import EnemyTurn

from gui import ui_functions

import resources.images as images
import resources.audio as audio


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
        self.hostile = True

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
        self.players = list(self.anchor.alive_player_dict.values())

        if self.hostile:
            self.target_team = self.enemies

        # Check if we're targeting friendly or enemy team
        else:
            self.target_team = self.players

        self.pointer = self.pointer % len(self.target_team)

        self.selected_unit = self.target_team[self.pointer]

        if actions["down"]:
            self.pointer += 1

        if actions["up"]:
            self.pointer -= 1

        if actions["left"]:
            self.hostile = False

        if actions["right"]:
            self.hostile = True

        if actions["enter"]:
            for sprite in self.sprites.sprites():
                sprite.selected = False

            # Call the move method (method is tied to the unit already) onto the enemy self.unit and the anchor (play.py) alive enemy dictionary
            if self.selected_move(self.selected_unit, self.target_team):
                next_scene = EnemyTurn(self.game, self.anchor)
                next_scene.start_scene()

            else:
                print("not enough mana/invalid target!")
                if self.game.sound:
                    pygame.mixer.find_channel().play(self.game.audio_handler.oom_sfx)
                self.sprites.empty()
                while self.game.stack[-1] != self.anchor:
                    self.exit_scene()

        if actions["escape"]:
            self.sprites.empty()
            while self.game.stack[-1] != self.anchor:
                self.exit_scene()

        self.game.reset_keys()
        self.sprites.update()

        # If game breaks try putting this at the start of the loop
        self.game.all_units.update()
        self.game.stat_guis.update()

    def render(self, screen):
        self.anchor.render(screen)
        self.sprites.draw(screen)
