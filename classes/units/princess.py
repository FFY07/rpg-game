import pygame, random

from classes.unit import Unit


from gui import ui_functions


# Range value
STRENGTH = (11, 11)
INTELLIGENCE = (25, 25)
DEFENCE = (32, 32)
MAGIC_RESIST = (30, 30)
race = "Human"

class Princess(Unit):
    def __init__(self, name, team, game=None):
        super().__init__(name, team)
        self.game = game

        self.unit_class = "Princess"
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
        # self.rect.center[1] = self.rect.center[1] - 20

        self.move_desc["Passive"] = "Heal more HP if allies HP low"

        self.moves["Heal (20%HP, (10))"] = self.healing
        self.move_desc["Heal (20% HP and 10 MANA)"] = "Heal allies, if allies HP less than 30%, Heal 25% more"

        self.moves["Cleanse (25)"] = self.cleanse
        self.move_desc["Cleanse (25 MANA)"] = "Remove allies debuff, Regen allies MANA"

        self.moves["Wish (70)"] = self.wish
        self.move_desc["Wish (70 MANA)"] = "Buff all allies (include self) with regeneration buff for 4 turns"

    def level_stats(self):
        self.health += self.max_health / 10
        self.strength += 2
        self.intelligence += 10
        self.defence += 5
        self.magic_resist += 1.3

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

    def cleanse(self, target, target_team):
        if (
            not self.is_target_hostile(target)
            and (target.mana != target.max_mana
            or 
            (target.health != target.max_health and target.max_mana == 0.1) #check if target use HP attack and HP full or not)
            )
        ):
            mana_cost = self.max_mana * 0.25
            regen = self.intelligence * 1.4

            if self.mana >= mana_cost:
                self.mana -= mana_cost

                target.burn_stacks.clear()

                if target.max_mana == 0.1:  # for reaper , add health instead
                    target.health += regen
                if target == self:
                    self.mana += regen * 1.7  # for self, add more mana
                else:
                    target.mana += regen

                self.game.sprites.add(
                        ui_functions.HitImage("unit/princess/healing", target , 15)
                    )

                self.melee(target)
                if target.max_mana == 0.1:
                    self.update_healstats(target, regen, "healing", 1)
                else:
                    self.update_manastats(target, regen, "healing", 1)
                self.change_state("defend")

                if target.max_mana == 0.1:
                    self.game.event_log.append(
                    f"{self.name} cleanse and heal {target.name} for {int(regen)}"
                )
                else:
                    self.game.event_log.append(
                f"{self.name} cleanse and regen {int(regen)} mana for{target.name}"
                )   
                return True

    def wish(self, target: object, target_team: list):
        if not self.is_target_hostile(target):
            mana_cost = 70
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                heal = 0
                for t in target_team:
                    t.health_regen_stacks.append([5 , self.intelligence / 1.667 ]) # heal 15
                    t.update_healstats(target, heal, "healing", 1)
                    self.game.sprites.add(
                        ui_functions.HitImage("unit/princess/holy", t, 25)
                    )

                t.change_state('defend')


                return True
