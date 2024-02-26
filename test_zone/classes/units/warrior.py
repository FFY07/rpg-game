import pygame, random

from classes.unit import Unit

import resources2.audio as audio

# Range of values
STRENGTH = (15, 15)
INTELLIGENCE = (3, 3)
DEFENCE = (55, 55)
MAGIC_RESIST = (55, 55)


class Warrior(Unit):
    def __init__(self, name, team, id_no=0, game=None):
        super().__init__(name, team, id_no)
        self.game = game

        self.unit_class = "Warrior"
        self.anim_speed = 50

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
        # Loads the first idle frame so the proper rect size can be generated
        # Make sure all images are the same size
        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        # Add moves to moves dictionary
        self.moves["Life Steal (15)"] = self.lifesteal
        self.moves["Execute (30)"] = self.execute

    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 10
        self.defence += 5
        self.magic_resist += 2

    def lifesteal(self, target: object, target_team: list):
        if self.is_target_hostile(target):
            mana_cost = 15
            if self.mana > mana_cost:
                self.mana -= mana_cost
                damage = self.calc_damage(target, "physical", 2)

                self.melee(target)
                self.update_stats(target, damage, "blood2", 2)
                self.lifesteal = 0.7
                self.health += damage * self.lifesteal
                if self.game.sound:
                    pygame.mixer.Sound.play(self.default_attack_sfx)

                print(
                    f"You attack {target.name} for {damage} and steal {damage * self.lifesteal} health!"
                )

                return True

    def execute(self, target: object, target_team: list):
        if self.is_target_hostile(target):
            mana_cost = 30
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                damage = self.calc_damage(target, "physical", 3)

                self.melee(target)
                self.update_stats(target, damage, "blood3", 2)

                if self.game.sound:
                    pygame.mixer.Sound.play(self.default_attack_sfx)

                print(f"Executed {target.name}")

                return True
