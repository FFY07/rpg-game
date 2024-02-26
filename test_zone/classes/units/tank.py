import random, pygame

from classes.unit import Unit

import resources2.audio as audio
import gui2.ui_functions as ui_functions

# Range of values
STRENGTH = (2, 2)
INTELLIGENCE = (17, 17)
DEFENCE = (60, 60)
MAGIC_RESIST = (30, 30)


class Tank(Unit):
    def __init__(self, name, team, id_no=0, game=None):
        super().__init__(name, team, id_no)
        self.game = game

        self.unit_class = "Tank"

        self.name = name
        self.team = team
        self.id = id_no

        self.strength = random.randint(*STRENGTH)
        self.intelligence = random.randint(*INTELLIGENCE)
        self.defence = random.randint(*DEFENCE)
        self.magic_resist = random.randint(*MAGIC_RESIST)

        self.size_scale = 3.5

        if self.team == "enemy":
            self.direction = "left"

        self.load_animations()

        self.load_sounds()

        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.cannon_shells = 0

        # Add moves to moves dictionary
        self.moves["Cannon (30)"] = self.cannon
        self.moves["Machine Gun (15)"] = self.machine_gun

    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 10
        self.defence += 5
        self.magic_resist += 2

    def cannon(self, target: object, target_team: list):
        if self.is_target_hostile(target):
            mana_cost = 30

            if self.mana >= mana_cost:
                if not self.cannon_shells:
                    self.cannon_shells += 1
                    if self.game.sound:
                        pygame.mixer.Sound.play(self.game.audio_handler.tank_load_shell)
                        self.game.sprites.add(
                            ui_functions.HitImage("tank_charge", self, 2)
                        )

                # If we have cannon shells, proceed to fire
                else:
                    self.mana -= mana_cost
                    if self.game.sound:
                        pygame.mixer.Sound.play(self.game.audio_handler.tank_183mm)
                    self.cannon_shells = 0

                    damage = self.calc_damage(target, "magic", 5)

                    self.melee(target)
                    self.update_stats(target, damage, "tank_cannon", 2)

                return True
            else:
                # Attack fail
                return False

    def machine_gun(self, target: object, target_team: list):
        if self.is_target_hostile(target):
            mana_cost = 15

            if self.mana >= mana_cost:
                self.mana -= mana_cost
                try:
                    # Selects 2 targets from the target team
                    target_list = random.sample(target_team, 2)
                except:
                    # in case there's only 1 target left
                    target_list = target_team

                for t in target_list:
                    damage = self.calc_damage(t, "magic", 1.5)
                    self.update_stats(t, damage, "tank_mg", 2)

                if self.game.sound:
                    pygame.mixer.Sound.play(self.game.audio_handler.tank_machine_gun)

                return True

            else:
                # Attack fail
                return False
