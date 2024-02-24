import pygame, random

from scenes.scene import Scene

from gui2 import ui_functions

import resources2.images as images


class EnemyTurn(Scene):
    def __init__(self, game: object, anchor: object):
        super().__init__(game)
        self.sprites = pygame.sprite.Group()
        self.effect_sprites = pygame.sprite.Group()

        self.anchor = anchor

        self.alive_players = []
        self.alive_enemies = []

        # Number of times the enemy can attack
        self.attacks = 1

        # Delay before the enemy starts attacking
        self.wait = 1000
        self.start_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()

        for sprite in self.alive_enemies:
            print(sprite.health, sprite.alive)

    def update(self, actions):
        self.update_alive_dict()

        # If either team is dead, go back to play screen
        if self.alive_enemy_dict and self.alive_player_dict:

            # Delay before attacking which is actually useless code because we added a new check for player team idle below
            if self.current_time - self.start_time > self.wait and self.attacks:
                self.target_team_ready = True
                self.attacker = random.choice(list(self.alive_enemy_dict.values()))
                self.target = random.choice(list(self.alive_player_dict.values()))

                # If player character is not idle, wait until it is (where it will get deactivated on top)

                # bandaid fix for currently attacking sprites to never be attacked
                for sprite in list(self.alive_player_dict.values()):
                    if sprite.state != "idle":
                        self.target_team_ready = False

                if self.target_team_ready:
                    self.target.deactivate()  # Timing issue (force deactivate)

                    # Enemy chooses a random move to attack with
                    self.attacker_attack = random.choice(
                        list(self.attacker.moves.values())
                    )
                    self.attacker_attack(
                        self.target, list(self.alive_player_dict.values())
                    )
                    self.attacks -= 1
                    self.start_time = pygame.time.get_ticks()

            # Check if we still have to wait for everyone's animations to finish
            # And if the enemy still has attacks left
            if self.attacks:
                self.waiting = True
            else:
                self.waiting = False
        else:
            self.waiting = False

        # Check if any sprites are still in their active animations
        for sprite in self.game.all_units.sprites():
            if not sprite.state == "idle" and not sprite.state == "death":
                self.waiting = True

            else:
                sprite.deactivate()

        if not self.waiting:
            for sprite in self.game.all_units.sprites():
                sprite.deactivate()

            while self.game.stack[-1] != self.anchor:
                self.exit_scene()

        self.current_time = pygame.time.get_ticks()
        self.sprites.update()
        self.game.all_units.update()

    def render(self, screen):
        self.anchor.render(screen)
        self.sprites.draw(screen)
