import pygame, random, math

from classes.unit import Unit
import gui.ui_functions as ui_functions

# Range of values
STRENGTH = (8, 8)
INTELLIGENCE = (20, 20)
DEFENCE = (80, 80)
MAGIC_RESIST = (100, 100)
race = "Human"


class Bandit(Unit):
    def __init__(self, name, team, game=None):
        super().__init__(name, team)
        self.game = game

        self.unit_class = "Bandit"
        self.race = race

        self.name = name
        self.team = team

        self.strength = random.randint(*STRENGTH)
        self.intelligence = random.randint(*INTELLIGENCE)
        self.defence = random.randint(*DEFENCE)
        self.magic_resist = random.randint(*MAGIC_RESIST)

        self.size_scale = 2.5

        if self.team == "enemy":
            self.direction = "left"

        self.load_animations()
        self.load_sounds()

        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.move_desc["Passive"] = "IDK write what Anyhow la"

        self.moves["Water Sword(15)"] = self.swordwater
        self.move_desc["Water Sword (15 MANA)"] = (
            "Enchance sword with water element, Attack and steal MANA from enemy"
        )

        self.moves["Fire Sword(30)"] = self.swordfire
        self.move_desc["Fire Sword (30 MANA)"] = (
            "Enchance sword with fire element, Attack and apply burn to enemy for 3 turns"
        )

    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 10
        self.defence += 5
        self.magic_resist += 2

    def swordwater(self, target: object, target_team: list):
        if self.is_target_hostile(target):
            mana_cost = 15
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                damage, crit = self.calc_damage(target, "magic", 1.2)
                damagemana = 25

                self.melee(target)
                self.update_stats(target, damage, crit, "unit/bandit/manasteal", 2)

                target.health -= damage

                if target.max_mana != 0.1:
                    target.mana -= damagemana
                    target.mana = max(0, target.mana)
                    self.mana += damagemana
                    if self.mana > self.max_mana:
                        self.mana = self.max_mana

                if self.game.sound:
                    self.play_sound(self.game.audio_handler.sword_sfx)
                    self.game.sprites.add(
                        ui_functions.HitImage("unit/tank/charge", self, 2)
                    )
                self.game.event_log.append(
                    f"{self.name} attack {target.name} for {int(damage)} and recover {damagemana}"
                )

                return True

    def swordfire(self, target: object, target_team: list):
        if self.is_target_hostile(target):
            mana_cost = 30
            if self.mana >= mana_cost:
                self.mana -= mana_cost

                target.burn_stacks.append([3, self.intelligence * 0.5])

                damage, crit = self.calc_damage(target, "physical", 2.5)

                self.melee(target)
                self.update_stats(target, damage, crit, "unit/bandit/statsteal", 2)

                if self.game.sound:
                    self.play_sound(self.game.audio_handler.sword_sfx)

                self.game.event_log.append(
                    f"{self.name} attack {target.name} for {int(damage)} and apply burn for 3 round"
                )

                return True
