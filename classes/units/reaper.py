import pygame, random

from classes.unit import Unit

from gui import ui_functions

# Range of values
STRENGTH = (50, 50)
INTELLIGENCE = (11, 11)
DEFENCE = (120, 120)
MAGIC_RESIST = (120, 120)


class Reaper(Unit):
    def __init__(self, name, team, game=None):
        super().__init__(name, team)
        self.game = game

        self.unit_class = "Reaper"

        self.name = name
        self.team = team

        self.mana = 0
        self.max_mana = 0.1
        self.strength = random.randint(*STRENGTH)
        self.intelligence = random.randint(*INTELLIGENCE)
        self.defence = random.randint(*DEFENCE)
        self.magic_resist = random.randint(*MAGIC_RESIST)

        self.size_scale = 2

        if self.team == "enemy":
            self.direction = "left"

        self.load_animations()

        # self.load_sounds()

        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.moves["Decay (-10HP)"] = self.decay
        self.moves["Dead Scythe (-25HP)"] = self.tidesofsoul
        self.moves["Blood Ritual (-50% Current HP)"] = self.blood_ritual

    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 10
        self.defence += 5
        self.magic_resist += 2

    def basic_attack(self, target: object, target_team: list):

        self.strength = max(
            5, STRENGTH[0] * (1 - (self.health / self.max_health))
        )  # atleast deal 5 dmg

        if self.is_target_hostile(target):
            damage, crit = self.calc_damage(target, "physical", 0.6)

            # Melee is optional and only for direct attacks
            self.melee(target)
            self.update_stats(target, damage, crit, "misc/physical/slash1", 50)

            # Add mana when attacking
            if self.health < self.max_health:
                self.health += 5
                if self.health > self.max_health:
                    self.health = self.max_health

            self.play_sound(self.game.audio_handler.reaper_basic)

            return True

    def decay(self, target, target_team):
        if self.is_target_hostile(target):
            health_check = 10

            if self.health > health_check:
                self.health -= health_check
                self.strength = max(
                    10, STRENGTH[0] * (1 - (self.health / self.max_health))
                )

                damage, crit = self.calc_damage(target, "physical", 0.9)
                self.health += min(35,(max(10,damage)))  #atleast heal 10 and max 35

                self.melee(target)
                self.update_stats(target, damage, crit, "unit/reaper/soul", 3)

                self.play_sound(self.game.audio_handler.sword_sfx)

            return True


    def tidesofsoul(self, target: object, target_team: list):
        if self.is_target_hostile(target):
            health_cost = 25
            self.strength = max(10, STRENGTH[0] * (1 - (self.health / self.max_health)))

            if self.health > health_cost:
                self.health -= health_cost

                target_list = target_team

                for t in target_list:
                    damage, crit = self.calc_damage(t, "physical", 0.9)
                    self.update_stats(t, damage, crit, "misc/physical/slash2", 50)

                self.play_sound(self.game.audio_handler.sword_sfx)

                return True

    def blood_ritual(self, target: object, target_team: list):
        """Sacrifices half of current health to boost strength for 3 turns"""
        if not self.is_target_hostile(target):
            self.health = self.health / 2

            # Effectively 2 times strength for 3 turns
            target.bonus_strength_stacks.append([3, self.strength * 0.7])

            self.game.sprites.add(ui_functions.HitImage("misc/blood/blood2", self, 2))
            self.game.event_log.append(
                f"{self.name} exchanges half its health for a strength buff!"
            )

            return True
