import random, pygame

from classes.unit import Unit

import gui.ui_functions as ui_functions

# Range of values
STRENGTH = (5, 5)
INTELLIGENCE = (20, 20)
DEFENCE = (65, 65)
MAGIC_RESIST = (85, 85)


class Necromancer(Unit):
    def __init__(self, name, team, game=None):
        super().__init__(name, team)
        self.game = game

        self.unit_class = "Necromancer"

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

        # self.load_sounds()

        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.cannon_shells = 0

        # Add moves to moves dictionary
        self.moves["Weaken (30)"] = self.weaken
        self.moves["Infect (20% HP)"] = self.infect
        self.moves["Doom (80)"] = self.doom

    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 8
        self.defence += 3
        self.magic_resist += 8

    def weaken(self, target: object, target_team: list):
        """Weaken enemy physical attacks and recover health"""
        mana_cost = 30
        if self.is_target_hostile(target):
            if self.mana >= mana_cost:
                self.mana -= mana_cost

                damage, crit = self.calc_damage(target, "magic", 1.25)
                self.update_stats(target, damage, crit, "unit/necromancer/doom", 1)
                target.bonus_strength_stacks.append([3, target.strength * 0.4])
                self.game.event_log.append(
                    f"{self.name} attacks {target.name} with weaken for {damage} damage!"
                )
                if crit:
                    self.game.event_log.append("It was a crit!")

                health_recovery = (self.max_health - self.health) * 0.5 + (
                    (self.intelligence + self.bonus_intelligence) / 100
                )
                print(health_recovery)
                self.health += health_recovery

                return True

    def infect(self, target: object, target_team: list):
        """Sacrifice health to restore mana"""
        health_cost = self.max_health * 0.2
        if self.health > health_cost:
            self.health -= health_cost

            # Mana recovery scales with intelligence
            mana_recovery = health_cost * 1 + (
                ((self.intelligence + self.bonus_intelligence)) / 100
            )
            self.mana += mana_recovery

            self.change_state("hurt")
            self.game.event_log.append(
                f"{self.name} sacrificed {health_cost} health for {mana_recovery} mana!"
            )

            return True

    def doom(self, target: object, target_team: list):
        """Summons powerful dark energy on all enemies and reduces their damage resistances for 5 turns"""
        if self.is_target_hostile(target):
            mana_cost = 80
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                for t in target_team:
                    damage, crit = self.calc_damage(t, "magic", 1.75)
                    self.update_stats(t, damage, crit, "unit/necromancer/doom", 2)
                    t.bonus_defence_stacks.append(
                        [5, -(self.intelligence + self.bonus_intelligence)]
                    )
                    t.bonus_magic_resist_stacks.append(
                        [5, -(self.intelligence + self.bonus_intelligence)]
                    )

                self.game.event_log.append(
                    f"{self.name} casts doom upon all enemies for ~{damage} damage and lowers their resistances!"
                )
                return True
