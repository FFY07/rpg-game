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
        # self.load_sounds()

        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.move_desc["Passive"] = "Deal more DMG to Undead"

        self.moves["Heal (20%HP, (10))"] = self.healing
        self.move_desc["Heal (20% HP and 10 MANA)"] = "Heal allies, if allies HP less than 30%, Heal 25% more"

        self.moves["Gospel (30)"] = self.gospel
        self.move_desc["Gospe; (30 MANA)"] = "__"


    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 10
        self.defence += 5
        self.magic_resist += 2

    def healing(self, target, target_team):
        if not self.is_target_hostile(target) and target.health != target.max_health and target != self:
            healratio = self.max_health * 0.2
            mana_cost = 10
            heal = self.intelligence 
            if self.mana >= mana_cost and self.health > healratio:
                self.mana -= mana_cost
                self.health -= healratio

                if target.health <=  0.3:
                    heal = heal * 1.25

                target.health += heal
                self.game.sprites.add(
                        ui_functions.HitImage("unit/princess/holy",target , 25)
                    )

                self.melee(target)
                self.update_healstats(target, heal, "healing", 1)
                self.change_state("defend")
                
                self.game.event_log.append(
                f"{self.name} heal {target.name} for {int(heal)}"
            )

                return True
            
    def gospel (self, target, target_team):
        " increase team damge, and deal damage to enemy"
        if self.is_target_hostile(target):
            mana_cost = 30
            if self.mana >= mana_cost:
                self.mana -= mana_cost


                for t in target_team:
                    damage, crit = self.calc_damage(t, "physical", 0.9)
                    self.update_stats(t, damage, crit, "misc/physical/slash2", 50)

        
                self.play_sound(self.game.audio_handler.sword_sfx)
                self.game.event_log.append(
                        f"{self.name} buff allies and deal {int(damage)}"
                    )
                return True