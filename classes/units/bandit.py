import pygame, random, math

from classes.unit import Unit
import gui.ui_functions as ui_functions

# Range of values
STRENGTH = (8, 8)
INTELLIGENCE = (20, 20)
DEFENCE = (40, 40)
MAGIC_RESIST = (50, 50)


class Bandit(Unit):
    def __init__(self, name, team, game=None):
        super().__init__(name, team)
        self.game = game

        self.unit_class = "Bandit"

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

        self.moves["Water Sword(15)"] = self.swordwater
        self.moves["Fire Sword(30)"] = self.swordfire
        self.moves["Molotov (15)"] = self.molotov
        # self.moves["Underwear Theft (10)"] = self.stealunderwear

    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 10
        self.defence += 5
        self.magic_resist += 2

    def swordwater(self, target: object, target_team: list):
        if self.is_target_hostile(target) :
            mana_cost = 15
            if self.mana > mana_cost:
                self.mana -= mana_cost
                damage, crit = self.calc_damage(target, "magic", 1.2)
                damagemana = 25

                self.melee(target)
                self.update_stats(target, damage, crit, "manasteal", 2)

                target.health -= damage

                if target.max_mana != 0.1:
                    target.mana -= (damagemana)
                    target.mana = max(0, target.mana)
                    self.mana += damagemana
                    if self.mana > self.max_mana:
                        self.mana = self.max_mana


                if self.game.sound:
                    pygame.mixer.Sound.play(self.default_attack_sfx)
                    self.game.sprites.add(ui_functions.HitImage("tank_charge", self, 2))

                return True

    def swordfire(self, target: object, target_team: list):
        if self.is_target_hostile(target):
            mana_cost = 30
            if self.mana > mana_cost:
                self.mana -= mana_cost

                target.burn_stacks.append([3, self.intelligence * 0.25])

                damage, crit = self.calc_damage(target, "physical", 2.5)

                self.melee(target)
                self.update_stats(target, damage, crit, "statsteal", 2)

                if self.game.sound:
                    pygame.mixer.Sound.play(self.default_attack_sfx)

                return True

    def molotov(self, target: object, target_team: list):
        if self.is_target_hostile(target):
            mana_cost = 15
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                target.burn_stacks.append([3, self.intelligence])

                damage, crit = self.calc_damage(target, "magic", 0.1)
                self.melee(target)
                self.update_stats(target, damage, crit, "magma", 2)

                return True

    # def stealunderwear(self, target: object, target_team: list):
    #     if self.is_target_hostile(target):
    #         mana_cost = 10
    #         if self.mana > mana_cost:
    #             self.mana -= mana_cost
    #             damage, crit = self.calc_damage(target, "physical", 999)

    #             if self.strength >= 15:
    #                 self.melee(target)
    #                 self.update_stats(target, damage, crit, "atk", 2)
    #                 self.strength -= 5
    #                 target.health -= damage

    #                 if self.game.sound:
    #                     pygame.mixer.Sound.play(self.default_attack_sfx)

    #                 print(
    #                     f"You steal underwear from {target.name}!, {target.name} fell ashame rather to died"
    #                 )

    #             else:
    #                 self.strength += 1
    #                 print("You dont have enought strength to steal underwear")
    #                 print(f"{self.strength}/15 ")

    #             return True
