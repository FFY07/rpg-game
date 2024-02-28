import random, pygame

from classes.unit import Unit

import gui.ui_functions as ui_functions

# Range of values
STRENGTH = (5, 5)
INTELLIGENCE = (20, 20)
DEFENCE = (40, 40)
MAGIC_RESIST = (80, 80)


class Necromancer(Unit):
    def __init__(self, name, team, id_no=0, game=None):
        super().__init__(name, team, id_no)
        self.game = game

        self.unit_class = "Necromancer"

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
        self.moves["Doom (80)"] = self.doom

    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 8
        self.defence += 3
        self.magic_resist += 8

    def doom(self, target: object, target_team: list):
        """Summons powerful dark energy on all enemies and reduces their damage resistances for 5 turns"""
        if self.is_target_hostile(target):
            mana_cost = 80
            if self.mana > mana_cost:
                self.mana -= mana_cost
                for t in target_team:
                    damage, crit = self.calc_damage(t, "magic", 2.5)
                    self.update_stats(t, damage, crit, "necro_doom", 2)
                    t.bonus_defence_stacks.append(
                        [5, -(self.intelligence + self.bonus_intelligence)]
                    )
                    t.bonus_magic_resist_stacks.append(
                        [5, -(self.intelligence + self.bonus_intelligence)]
                    )
                return True
