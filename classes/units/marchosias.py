import pygame, random, math

from classes.unit import Unit
import gui.ui_functions as ui_functions

# Range of values
STRENGTH = (0, 0)
INTELLIGENCE = (40, 40)
DEFENCE = (80, 80)
MAGIC_RESIST = (80, 80)
race = "Demon"


class Marchosias(Unit):
    def __init__(self, name, team, game=None):
        super().__init__(name, team)
        self.game = game

        self.unit_class = "Marchosias"
        self.race = race

        self.name = name
        self.team = team

        self.strength = random.randint(*STRENGTH)
        self.intelligence = random.randint(*INTELLIGENCE)
        self.defence = random.randint(*DEFENCE)
        self.magic_resist = random.randint(*MAGIC_RESIST)

        self.size_scale = 1

        if self.team == "enemy":
            self.direction = "left"

        self.load_animations()
        self.load_sounds()

        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.move_desc["Passive "] = (
            " Using INT on every skill( include basic attack) "
        )
        
        self.moves["Hell fire(25)"] = self.hellfire
        self.move_desc["Hell fire(25 MANA)"] = (
            "Blasts fire on enemies and burn for 3 turns"
        )


    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 10
        self.defence += 5
        self.magic_resist += 2

    def basic_attack(self, target: object, target_team: list):

        if self.is_target_hostile(target):

            damage, crit = self.calc_damage(target, "magic", 0.45)
                
            # Melee is optional and only for direct attacks
            self.melee(target)
            self.update_stats(target, damage, crit, "misc/physical/slash1", 50)

            # Add mana when attacking
            if self.mana < self.max_mana:
                self.mana += 10
                if self.mana > self.max_mana:
                    self.mana = self.max_mana

            self.play_sound(self.default_attack_sfx)

            return True
        

    def hellfire(self, target: object, target_team: list):
        """Blasts fire on enemies and burn for 3 turns"""
        if self.is_target_hostile(target):
            mana_cost = 25

            if self.mana >= mana_cost:
                self.mana -= mana_cost

                target.burn_stacks.append([3, self.intelligence * 0.375])

                damage, crit = self.calc_damage(target, "magic", 0.4)

                # self.melee(target)
                self.update_stats(target, damage, crit, "unit/marchosias/fire", 2)

                # Halves defence for 2 turns
                self.bonus_defence_stacks.append([2, -self.defence / 2])
                self.game.event_log.append(f"{self.name} use hell fire")

                return True
