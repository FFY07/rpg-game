import pygame, random

from classes.unit import Unit

# Range value
STRENGTH = (11, 11)
INTELLIGENCE = (25, 25)
DEFENCE = (32, 32)
MAGIC_RESIST = (30, 30)


class Princess(Unit):
    def __init__(self, name, team, game=None):
        super().__init__(name, team)
        self.game = game

        self.unit_class = "Princess"

        self.name = name
        self.team = team

        self.strength = random.randint(*STRENGTH)
        self.intelligence = random.randint(*INTELLIGENCE)
        self.defence = random.randint(*DEFENCE)
        self.magic_resist = random.randint(*MAGIC_RESIST)

        self.size_scale = 3

        if self.team == "enemy":
            self.direction = "left"

        self.load_animations()

        # self.load_sounds()

        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        # self.rect.center[1] = self.rect.center[1] - 20
        self.moves["Healing (10)"] = self.healing

        self.moves["Mana Regen (20)"] = self.regenmana

        self.moves["Regen (15)"] = self.regen

    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 10
        self.defence += 5
        self.magic_resist += 1.3

    def healing(self, target, target_team):
        if not self.is_target_hostile(target) and target.health != target.max_health:
            mana_cost = 10
            healing = 100
            if self.mana >= mana_cost:
                self.mana -= mana_cost

                heal = healing
                self.melee(target)
                self.update_healstats(target, heal, "healing", 1)
                self.change_state("defend")
                print(f"{self.name} heal {target.name} 30 hp ! ")
                print(f"[DEBUG]:{target.health}/{target.max_health} ")
                return True

    def regenmana(self, target, target_team):
        if (
            not self.is_target_hostile(target)
            and target.mana != target.max_mana
            and target.max_mana != 0.1
        ):
            mana_cost = 20
            regen = 40
            if self.mana >= mana_cost:
                self.mana -= mana_cost

                self.melee(target)
                self.update_manastats(target, regen, "healing", 1)
                self.change_state("defend")

                return True

    def regen(self, target: object, target_team: list):
        if not self.is_target_hostile(target):
            mana_cost = 15
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                target.health_regen_stacks.append([3, self.intelligence])

                damage, crit = self.calc_damage(target, "magic", 0.1)
                self.melee(target)
                self.update_stats(target, damage, crit, "healing", 2)

                return True
