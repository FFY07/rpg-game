import pygame, random

from classes.unit import Unit

from gui import ui_functions

# Range of values
STRENGTH = (16, 16)
INTELLIGENCE = (8, 8)
DEFENCE = (90, 90)
MAGIC_RESIST = (75, 75)
race = "Demon"


class Warrior(Unit):
    def __init__(self, name, team, game=None):
        super().__init__(name, team)
        self.game = game

        self.unit_class = "Warrior"
        self.race = race
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
        self.move_desc["Passive"] = "ITS NOT YASUO"

        self.moves["Hasagi (15)"] = self.hasagi
        self.move_desc["Hasagi (15 Mana)"] = "Randomly slashes 1-2 enemies"

        self.moves["Inspire (35)"] = self.inspire
        self.move_desc["Inspire (35 Mana)"] = (
            "Temporarily boosts ally strength and intelligence"
        )

        self.moves["Execute (45)"] = self.execute
        self.move_desc["Execute (45 Mana)"] = (
            "Deals increased damage to low-health enemies"
        )

    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 10
        self.intelligence += 4
        self.defence += 8
        self.magic_resist += 8

    def hasagi(self, target: object, target_team: list):
        """Randomly slashes 1-2 enemies"""
        if self.is_target_hostile(target):
            mana_cost = 15

            if self.mana >= mana_cost:
                self.mana -= mana_cost
                enemies = random.randint(1, 2)
                try:
                    # Selects 2 targets from the target team
                    target_list = random.sample(target_team, enemies)
                except:
                    # in case there's only 1 target left
                    target_list = target_team

                for t in target_list:
                    damage, crit = self.calc_damage(t, "physical", 1.4)
                    self.update_stats(t, damage, crit, "misc/physical/slash2", 2)
                    self.game.event_log.append(
                        f"{self.name} slashes {t.name} for {int(damage)} damage!"
                    )
                    if crit:
                        self.game.event_log.append("It was a crit!")

                self.play_sound(self.game.audio_handler.warrior_basic)

                return True

    def inspire(self, target: object, target_team: list):
        """Temporarily boosts ally strength and intelligence"""
        mana_cost = 35
        if not self.is_target_hostile(target):
            if self.mana >= mana_cost:
                self.mana -= mana_cost

                self.change_state("defend")
                
                self.play_sound(self.game.audio_handler.warrior_inspire)

                for t in target_team:
                    t.bonus_strength_stacks.append(
                        [5, target.strength * 0.2]
                    )  # 20% increase
                    t.bonus_intelligence_stacks.append([5, target.intelligence * 0.2])
                    self.game.sprites.add(
                        ui_functions.HitImage("unit/warrior/inspire", t, 40)
                    )

                self.game.event_log.append(
                    f"{self.name} rallies all teammates, increasing their strength!"
                )

                return True

    def execute(self, target: object, target_team: list):
        """Deals increased damage to low-health enemies"""
        if self.is_target_hostile(target):
            mana_cost = 45
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                damage, crit = self.calc_damage(
                    target, "physical", (1 * (target.max_health / target.health) / 1.2)
                )  # Lower health enemies take more damage

                self.melee(target)
                self.update_stats(target, damage, crit, "misc/physical/slash3", 50)

                self.play_sound(self.game.audio_handler.warrior_basic)

                self.game.event_log.append(
                    f"{self.name} uses execute on {target.name} for {int(damage)} damage!"
                )
                if crit:
                    self.game.event_log.append("It was a crit!")

                return True
