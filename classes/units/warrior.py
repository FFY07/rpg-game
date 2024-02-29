import pygame, random

from classes.unit import Unit

from gui import ui_functions

# Range of values
STRENGTH = (12, 12)
INTELLIGENCE = (10, 10)
DEFENCE = (45, 45)
MAGIC_RESIST = (40, 40)


class Warrior(Unit):
    def __init__(self, name, team, game=None):
        super().__init__(name, team)
        self.game = game

        self.unit_class = "Warrior"
        self.anim_speed = 50

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
        self.load_sounds()
        # Loads the first idle frame so the proper rect size can be generated
        # Make sure all images are the same size
        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        # Add moves to moves dictionary
        # self.moves["Life Steal (15)"] = self.lifesteal
        self.moves["Rally (25)"] = self.rally
        self.moves["Execute (30)"] = self.execute

    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 10
        self.defence += 5
        self.magic_resist += 2

    def rally(self, target: object, target_team: list):
        mana_cost = 25
        if not self.is_target_hostile(target):
            if self.mana > mana_cost:
                self.mana -= mana_cost

                self.play_sound(self.game.audio_handler.warrior_rally)

                for t in target_team:
                    t.bonus_strength_stacks.append([5, self.strength / 2])
                    self.game.sprites.add(ui_functions.HitImage("stat_buff", t, 2))

                self.game.event_log.append(
                    f"{self.name} rallies all teammates, increasing their strength!"
                )

                return True

    def execute(self, target: object, target_team: list):
        if self.is_target_hostile(target):
            mana_cost = 30
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                damage, crit = self.calc_damage(target, "physical", 3)

                self.melee(target)
                self.update_stats(target, damage, crit, "blood3", 2)

                self.play_sound(self.default_attack_sfx)

                print(f"Executed {target.name}")
                self.game.event_log.append(f"{self.name} execute")

                return True
