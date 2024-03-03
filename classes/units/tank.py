import random, pygame

from classes.unit import Unit

import gui.ui_functions as ui_functions

# Range of values
STRENGTH = (8, 8)
INTELLIGENCE = (22, 22)
DEFENCE = (100, 100)
MAGIC_RESIST = (80, 80)
race = "Machine"


class Tank(Unit):
    def __init__(self, name, team, game=None):
        super().__init__(name, team)
        self.game = game

        self.unit_class = "Tank"
        self.race = race

        self.name = name
        self.team = team

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
        self.move_desc["Passive"] = "You say you wanted a Tanker right?"

        self.moves["Cannon (40)"] = self.cannon
        self.move_desc["Cannon (40 MANA)"] = (
            "Loads a powerful tank shell and fires it at a single target if loaded"
        )

        self.moves["Machine Gun (25)"] = self.machine_gun
        self.move_desc["Machine Gun (25 MANA)"] = "Randomly shoot 1-2 enemies"

        self.moves["Flamethrower (70)"] = self.flamethrower
        self.move_desc["Flamethrower (70 MANA)"] = (
            "Blasts a large amount of fire and burns all enemies for 3 turns"
        )

    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 10
        self.defence += 8
        self.magic_resist += 2

    def cannon(self, target: object, target_team: list):
        """Loads a powerful tank shell and fires it at a single target if loaded"""
        if self.is_target_hostile(target):
            mana_cost = 40

            if not self.cannon_shells:
                self.cannon_shells += 1
                self.play_sound(self.game.audio_handler.tank_load_shell)

                self.game.sprites.add(
                    ui_functions.HitImage("unit/tank/charge", self, 2)
                )
                self.change_state("defend")
                self.game.event_log.append(f"{self.name} has loaded a shell!")

                # Load the shell
                return True

            else:
                # If we have cannon shells, proceed to fire
                if self.mana >= mana_cost:
                    self.mana -= mana_cost
                    self.play_sound(self.game.audio_handler.tank_183mm)
                    self.cannon_shells = 0

                    damage, crit = self.calc_damage(target, "magic", 4)

                    self.melee(target)
                    self.update_stats(target, damage, crit, "unit/tank/cannon", 2)
                    self.game.event_log.append(
                        f"{self.name} fires a shell at {target.name} for {int(damage)} damage!"
                    )
                    if crit:
                        self.game.event_log.append("It was a crit!")

                    return True

                else:
                    # fail because of no mana (optional to return False since it will already return None by default)
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
                    damage, crit = self.calc_damage(t, "magic", 1.1)
                    self.update_stats(t, damage, crit, "unit/tank/mg", 2)
                    self.game.event_log.append(
                        f"{self.name} hits {t.name} with a machine gun for {int(damage)} damage!"
                    )
                    if crit:
                        self.game.event_log.append("It was a crit!")

                self.play_sound(self.game.audio_handler.tank_machine_gun)

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
                    damage, crit = self.calc_damage(t, "magic", 0.8)
                    self.update_stats(t, damage, crit, "misc/magic/magma", 2)
                    t.burn_stacks.append([3, self.intelligence * 0.4])

                self.game.event_log.append(
                    f"{self.name} has burned all enemies for {int(damage)} damage!"
                )
                if crit:
                    self.game.event_log.append("It was a crit!")

                # Halves defence for 2 turns
                self.bonus_defence_stacks.append([2, -self.defence / 2])
                self.game.event_log.append(f"{self.name}'s defence has been reduced!")

                return True
