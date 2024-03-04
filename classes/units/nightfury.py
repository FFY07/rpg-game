import random

from classes.unit import Unit

import gui.ui_functions as ui_functions

# Range of values
STRENGTH = (30, 30)
INTELLIGENCE = (40, 40)
DEFENCE = (120, 120)
MAGIC_RESIST = (160, 160)

race = "Demon"


class NightFury(Unit):
    def __init__(self, name, team, game=None):
        super().__init__(name, team)
        self.game = game

        self.unit_class = "Nightfury"
        self.race = race

        self.name = name
        self.team = team

        self.strength = random.randint(*STRENGTH)
        self.intelligence = random.randint(*INTELLIGENCE)
        self.defence = random.randint(*DEFENCE)
        self.magic_resist = random.randint(*MAGIC_RESIST)

        self.size_scale = 0.8
        self.anim_speed = 60

        if self.team == "enemy":
            self.direction = "left"

        self.load_animations()

        self.load_sounds()

        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.cannon_shells = 0

        # Add moves to moves dictionary
        self.move_desc["Passive"] = "Secret unit with bonus mana regen"
        self.mana_regen_stacks.append([-1, 10])

        # Remove the basic attack
        self.moves.pop("Basic Attack")

        self.moves["lazy"] = self.lazy
        self.moves["Plasma (40)"] = self.plasma
        self.moves["Divebomb (75)"] = self.divebomb
        self.moves["Tackle (20)"] = self.tackle

    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 10
        self.intelligence += 12
        self.defence += 10
        self.magic_resist += 12

    def lazy(self, target: object, target_team: list):
        """Does literally nothing"""
        self.game.event_log.append(f"{self.name} was too lazy to do anything")
        self.play_sound(self.game.audio_handler.nightfury_lazy)
        self.change_state("defend")

        self.exp += self.level_exp_dict[self.level] * 0.01

        return True

    def plasma(self, target: object, target_team: list):
        """Scree"""
        if self.is_target_hostile(target):
            mana_cost = 40

            # If we have cannon shells, proceed to fire
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                self.play_sound(self.game.audio_handler.nightfury_plasma)
                self.cannon_shells = 0

                damage, crit = self.calc_damage(target, "magic", 3.5)

                self.melee(target)
                self.update_stats(target, damage, crit, "unit/tank/cannon", 2)
                self.game.event_log.append(
                    f"{self.name} fires plasma {target.name} for {int(damage)} damage!"
                )
                if crit:
                    self.game.event_log.append("It was a crit!")

                return True

    def divebomb(self, target: object, target_team: list):
        """Divebombs all enemies and burns them for one round"""
        if self.is_target_hostile(target):
            mana_cost = 75

            if self.mana >= mana_cost:
                self.mana -= mana_cost
                for t in target_team:
                    damage, crit = self.calc_damage(t, "magic", 0.8)
                    self.update_stats(t, damage, crit, "unit/necromancer/doom", 2)
                    t.burn_stacks.append([1, self.intelligence * 0.7])

                self.game.event_log.append(
                    f"{self.name} divebombs all enemies with plasma for {int(damage)} damage!"
                )
                if crit:
                    self.game.event_log.append("It was a crit!")

                self.play_sound(self.game.audio_handler.nightfury_divebomb)

                return True

    def tackle(self, target: object, target_team: list):
        """Scree"""
        if self.is_target_hostile(target):
            mana_cost = 30

            # If we have cannon shells, proceed to fire
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                self.play_sound(self.game.audio_handler.nightfury_tackle)
                self.cannon_shells = 0

                damage, crit = self.calc_damage(target, "physical", 1)

                self.melee(target)
                self.update_stats(target, damage, crit, "misc/physical/slash2", 2)
                self.game.event_log.append(
                    f"{self.name} slashes {target.name} for {int(damage)} damage!"
                )
                if crit:
                    self.game.event_log.append("It was a crit!")

                return True
