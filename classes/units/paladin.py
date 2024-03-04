import pygame, random, math

from classes.unit import Unit
import gui.ui_functions as ui_functions

# Range of values
STRENGTH = (15, 15)
INTELLIGENCE = (18, 18)
DEFENCE = (80, 80)
MAGIC_RESIST = (90, 90)

race = "Human"


class Paladin(Unit):
    def __init__(self, name, team, game=None):
        super().__init__(name, team)
        self.game = game

        self.unit_class = "Paladin"
        self.race = race

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
        self.load_sounds()

        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.move_desc["Passive "] = (
            "Deal more DMG , Skill (Effect/ Duration) will change when target is Undead "
        )

        self.moves["Sacrifice (20%HP, (10))"] = self.sacrifice
        self.move_desc["Sacrifice (20% HP and 10 MANA)"] = (
            "Heal allies, if allies are undead, Heal less 25% "
        )

        self.moves["Gospel (30)"] = self.gospel
        self.move_desc["Gospel (30 MANA)"] = (
            "Increase team damge 15% and regen 10 HP for 3 turn"
        )

        self.moves["Smite (40)"] = self.smite
        self.move_desc["Smite (40 MANA)"] = (
            "Summon a lighting to deal damage and burn target"
        )

    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 10
        self.defence += 5
        self.magic_resist += 2

    def basic_attack(self, target: object, target_team: list):

        if self.is_target_hostile(target):
            if target.race == "Undead":
                damage, crit = self.calc_damage(target, "physical", 1.5)
            else:
                damage, crit = self.calc_damage(target, "physical", 1)

            # Melee is optional and only for direct attacks
            self.melee(target)
            self.update_stats(target, damage, crit, "misc/physical/slash1", 50)

            # Add mana when attacking
            if self.mana < self.max_mana:
                self.mana += 10
                if self.mana > self.max_mana:
                    self.mana = self.max_mana

            self.play_sound(self.default_attack_sfx)

            return True

    def sacrifice(self, target, target_team):
        if (
            not self.is_target_hostile(target)
            and target.health != target.max_health
            and target != self
        ):
            healratio = self.max_health * 0.2
            mana_cost = 10
            heal = self.intelligence
            if self.mana >= mana_cost and self.health > healratio:
                self.mana -= mana_cost
                self.health -= healratio

                self.play_sound(self.game.audio_handler.heal_sfx)

                if target.race == "Undead":
                    heal = heal * 0.75

                target.health += heal
                self.game.sprites.add(
                    ui_functions.HitImage("unit/princess/holy", target, 25)
                )

                self.melee(target)
                self.update_healstats(target, heal, "healing", 1)
                self.change_state("defend")

                self.game.event_log.append(
                    f"{self.name} heal {target.name} for {int(heal)}"
                )

                return True

    def gospel(self, target, target_team):
        "increase team damge 15% and regen 10 HP for 3 turn"
        mana_cost = 30
        if not self.is_target_hostile(target):
            if self.mana >= mana_cost:
                self.mana -= mana_cost

                self.change_state("defend")

                for t in target_team:
                    t.bonus_strength_stacks.append(
                        [3, target.strength * 0.15]
                    )  # 20% increase
                    t.bonus_intelligence_stacks.append([3, target.intelligence * 0.15])
                    t.health_regen_stacks.append(
                        [4, self.intelligence / 1.8]
                    )  # heal 10
                    self.game.sprites.add(
                        ui_functions.HitImage("unit/princess/holy", t, 40)
                    )

                # steal your warrior sound XD
                self.play_sound(self.game.audio_handler.warrior_inspire)

                self.game.event_log.append(
                    f"{self.name} use gospel, Everyone increase 15% damage and regen {int(self.intelligence / 1.8)} "
                )

                return True

    def smite(self, target, target_team):
        "summon a lighting to deal damage and burn target"
        if self.is_target_hostile(target):
            mana_cost = 40
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                if target.race == "Undead":
                    damage, crit = self.calc_damage(target, "physical", 2.5)
                else:
                    damage, crit = self.calc_damage(target, "physical", 1.4)

                if target.race == "Undead":
                    target.burn_stacks.append([3, self.intelligence * 1])
                    target.health_regen_stacks.clear()

                else:
                    target.burn_stacks.append([3, self.intelligence * 0.5])

                self.change_state("defend")
                self.update_stats(target, damage, crit, "mnit/princess/holy", 50)

                self.game.sprites.add(
                    ui_functions.HitImage("unit/paladin/smite", target, 40)
                )

                self.play_sound(self.game.audio_handler.paladin_smite)

                return True
