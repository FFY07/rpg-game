import pygame, random

from classes.unit import Unit

import resources2.audio as audio


#Range value
STRENGTH = (12, 12)
INTELLIGENCE = (25, 25)
DEFENCE = (30, 30)
MAGIC_RESIST = (35, 35)

class Princess(Unit):
    def __init__(self, name, team, id_no=0, game=None):
        super().__init__(name, team, id_no)
        self.game = game

        self.unit_class = "Princess"

        self.name = name
        self.team = team
        self.id = id_no

        self.strength = random.randint(*STRENGTH)
        self.intelligence = random.randint(*INTELLIGENCE)
        self.defence = random.randint(*DEFENCE)
        self.magic_resist = random.randint(*MAGIC_RESIST)

        self.size_scale = 3

        if self.team == "enemy":
            self.direction = "left"

        self.load_animations()

        self.load_sounds()

        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        # self.rect.center[1] = self.rect.center[1] - 20
        self.moves["Healing (10)"] = self.healing


    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 10
        self.defence += 5
        self.magic_resist += 2

    def healing(self, target, target_team):
        if not self.is_target_hostile(target):
            mana_cost = 10
            healing = 30
            if self.mana >= mana_cost:
                self.mana -= mana_cost

                heal = healing
                self.melee(target)
                self.update_healstats(target, heal, "healing", 1)
                self.change_state("defend")
                print(f"{self.name} heal {target.name} 30 hp ! ")
                print(f"[DEBUG]:{target.health}/{target.max_health} ")
                return True