import random, pygame

from classes.unit import Unit

import resources.audio as audio
import gui.ui_functions as ui_functions

# Range of values
STRENGTH = (10, 10)
INTELLIGENCE = (20, 20)
DEFENCE = (80, 80)
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
        self.moves["Cannon (40)"] = self.cannon
        self.moves["Machine Gun (25)"] = self.machine_gun
        self.moves["Flamethrower (70)"] = self.flamethrower

    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 10
        self.defence += 6
        self.magic_resist += 2

    def cannon(self, target: object, target_team: list):
        """Loads a powerful cannon shell and fires it at a single target if loaded"""
        if self.is_target_hostile(target):
            mana_cost = 40

            if self.mana >= mana_cost:
                if not self.cannon_shells:
                    self.cannon_shells += 1
                    if self.game.sound:
                        pygame.mixer.find_channel().play(
                            self.game.audio_handler.tank_load_shell
                        )
                    self.game.sprites.add(ui_functions.HitImage("tank_charge", self, 2))
                    self.change_state("defend")

                # If we have cannon shells, proceed to fire
                else:
                    self.mana -= mana_cost
                    if self.game.sound:
                        pygame.mixer.find_channel().play(
                            self.game.audio_handler.tank_183mm
                        )
                    self.cannon_shells = 0

                    damage, crit = self.calc_damage(target, "magic", 4)

                    self.melee(target)
                    self.update_stats(target, damage, crit, "tank_cannon", 2)

                return True
            else:
                # Attack fail
                return False

    def machine_gun(self, target: object, target_team: list):
        if self.is_target_hostile(target):
            mana_cost = 25

            if self.mana >= mana_cost:
                self.mana -= mana_cost
                try:
                    # Selects 2 targets from the target team
                    target_list = random.sample(target_team, 2)
                except:
                    # in case there's only 1 target left
                    target_list = target_team

                for t in target_list:
                    damage, crit = self.calc_damage(t, "magic", 0.9)
                    self.update_stats(t, damage, crit, "tank_mg", 2)

                if self.game.sound:
                    pygame.mixer.find_channel().play(
                        self.game.audio_handler.tank_machine_gun
                    )

                return True

            else:
                # Attack fail
                return False

    def flamethrower(self, target: object, target_team: list):
        """Blasts a large amount of fire and burns all enemies for 3 turns"""
        if self.is_target_hostile(target):
            mana_cost = 70

            if self.mana >= mana_cost:
                self.mana -= mana_cost
                for t in target_team:
                    damage, crit = self.calc_damage(t, "magic", 1.5)
                    self.update_stats(t, damage, crit, "magma", 2)
                    t.burn_stacks.append([3, self.intelligence * 0.75])

                # Halves defence for 2 turns
                self.bonus_defence_stacks.append([2, -self.defence / 2])

                return True
