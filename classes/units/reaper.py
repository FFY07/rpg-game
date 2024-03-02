import pygame, random

from classes.unit import Unit

from gui import ui_functions

# Range of values
STRENGTH = (50, 50)
INTELLIGENCE = (10, 10)
DEFENCE = (80, 80)
MAGIC_RESIST = (80, 80)


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

        self.move_desc["Passive"] = "The lower the HP, the higher the ATK, Use HP instead of MANA"

        self.moves["Decay (-10HP)"] = self.decay
        self.move_desc["Decay (10 HP)"] = "Decay Enemy and drain their soul to recover HP"

        self.moves["Dead Scythe (-25HP)"] = self.deadscythe
        self.move_desc["Dead Scythe (25 HP)"] = "Slash all enemies with scythe"

        self.moves["Hell descent (-40HP)"] = self.helldescent
        self.move_desc["Hell descent (40HP)"] = "Sacrifices HP to Hell and get Regenation for 3 turns and ATK boost for 1 turns"

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
            health_cost = self.max_health * 0.1

            if self.health > health_cost:
                self.health -= health_cost
                self.strength = max(
                    target.health * 0.1 , STRENGTH[0] * (1 - (self.health / self.max_health))
                )

                damage, crit = self.calc_damage(target, "physical", 0.9)
                regen = min(self.max_health * 0.35 ,(max(self.max_health * 0.1 ,damage)))
                self.health += regen  #atleast heal 10 and max 35

                self.melee(target)
                self.update_stats(target, damage, crit, "unit/reaper/soul", 3)

                self.play_sound(self.game.audio_handler.sword_sfx)
                self.game.event_log.append(
                f"{self.name} decay {target.name} for {int(damage)} and recover {regen}"
            )

                return True

    def deadscythe(self, target: object, target_team: list):
        if self.is_target_hostile(target):
            health_cost = self.max_health * 0.25
            self.strength = max(target.health * 0.1, STRENGTH[0] * (1 - (self.health / self.max_health)))

            if self.health > health_cost:
                self.health -= health_cost

                target_list = target_team

                for t in target_list:
                    damage, crit = self.calc_damage(t, "physical", 0.9)
                    self.update_stats(t, damage, crit, "misc/physical/slash2", 50)

                self.play_sound(self.game.audio_handler.sword_sfx)
                self.game.event_log.append(
                    f"{self.name} slash every AI in enemy team for {int(damage)}"
                )
                return True

    def helldescent(self, target: object, target_team: list):
        """Sacrifices half of current health to boost strength for 3 turns"""

        health_cost = self.max_health * 0.4
        if self.health > health_cost:
            self.health -= health_cost

            
            #clear all buff
            self.burn_stacks.clear()
            self.bonus_strength_stacks.clear()

            # Effectively 2 times strength for 3 turns
            self.bonus_strength_stacks.append([1, self.strength * 0.7])
            self.health_regen_stacks.append([4, self.max_health * 0.12])

            self.game.sprites.add(ui_functions.HitImage("misc/blood/blood2", self, 2))
            self.game.event_log.append(f"{self.name} sacrifice 40hp to Hell")
            self.game.event_log.append(
                f"Hell cleanse {self.name} and gave extra attack and hp recovery"
            )
            return True
