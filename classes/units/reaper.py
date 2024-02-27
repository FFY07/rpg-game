import pygame, random

from classes.unit import Unit

import resources.audio as audio

# Range of values
STRENGTH = (25, 25)
INTELLIGENCE = (5, 5)
DEFENCE = (20, 20)
MAGIC_RESIST = (40, 40)


class Reaper(Unit):
    def __init__(self, name, team, id_no=0, game=None):
        super().__init__(name, team, id_no)
        self.game = game

        self.unit_class = "Reaper"

        self.name = name
        self.team = team
        self.id = id_no

        self.strength = random.randint(*STRENGTH)
        self.intelligence = random.randint(*INTELLIGENCE)
        self.defence = random.randint(*DEFENCE)
        self.magic_resist = random.randint(*MAGIC_RESIST)

        self.size_scale = 2

        if self.team == "enemy":
            self.direction = "left"

        self.load_animations()

        self.load_sounds()

        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.moves["Soul Attack (10)"] = self.soulattack
        # self.moves["Sacrifice (50)"] = self.sacrifice
        self.moves["Harvest (99)"] = self.harvest


    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 10
        self.defence += 5
        self.magic_resist += 2

    def soulattack(self, target, target_team):
        if self.is_target_hostile(target) :
            health_cost = 10
        
            if self.health >= health_cost:
                self.health -= health_cost

                self.strength = STRENGTH[0] * (1 -(self.health/self.max_health))
                damage, crit = self.calc_damage(target, "physical", 2)

            
                self.melee(target)
                self.update_stats(target, damage, crit, "hlood2", 1)
        
        return True


    # def sacrifice(self, target, target_team):
    #     mana_cost = 50
    #     if self.mana >= mana_cost:
    #         if self.is_target_hostile(target):
    #             if self.health <= (self.max_health * 0.3):
    #                 mana_cost = 50
    #                 if self.mana >= mana_cost:
    #                     self.mana -= mana_cost

    #                     damage, crit = self.calc_damage(target, "physical", 999)

    #                     self.melee(target)
    #                     self.update_stats(target, damage, crit, "reaper_sacrifice", 1)
    #                     self.health -= damage
    #                     self.change_state("hurt")

    #                 if self.game.sound:
    #                     pygame.mixer.find_channel().play(self.default_attack_sfx)

    #                 print(f"{self.name} sacrificed itself to kill {target.name}")

    #                 return True

    #         else:
    #             if target != self:
    #                 mana_cost = 50
    #                 if self.mana >= mana_cost:
    #                     self.mana -= mana_cost

    #                     self.max_health += self.max_health + target.health
    #                     self.health += self.health + target.health
    #                     self.strength += self.strength + target.strength
    #                     self.defence += self.defence + target.defence

    #                     damage = 999
    #                     crit = False
    #                     self.melee(target)
    #                     self.update_stats(target, damage, crit, "statsteal", 1)

    #                     print(
    #                         f"{self.name} sacrifice {target.name} to increase it owns stat ! "
    #                     )
    #                     print(
    #                         f"[DEBUG]: {self.max_health}, {self.health},  {self.strength}, {self.defence}"
    #                     )

    #                     if self.game.sound:
    #                         pygame.mixer.find_channel().play(self.default_attack_sfx)

    #                     return True

    def harvest(self, target: object, target_team: list):
        if self.is_target_hostile(target):
            mana_cost = 99

            if self.mana >= mana_cost:
                self.mana -= mana_cost

                target_list = target_team

                for t in target_list:
                    damage, crit = self.calc_damage(t, "physical", 999)
                    self.update_stats(t, damage, crit, "atk", 2)

                if self.game.sound:(
                        pygame.mixer.find_channel().play(self.default_attack_sfx)
                    )

                return True