import pygame, random, math

from classes.unit import Unit
import gui2.ui_functions as ui_functions

# Range of values
STRENGTH = (10, 10)
INTELLIGENCE = (3, 3)
DEFENCE = (60, 60)
MAGIC_RESIST = (40, 40)


class Bandit(Unit):
    def __init__(self, name, team, id_no=0, game=None):
        super().__init__(name, team, id_no)
        self.game = game

        self.unit_class = "Bandit"

        self.name = name
        self.team = team
        self.id = id_no

        self.strength = random.randint(*STRENGTH)
        self.intelligence = random.randint(*INTELLIGENCE)
        self.defence = random.randint(*DEFENCE)
        self.magic_resist = random.randint(*MAGIC_RESIST)

        self.size_scale = 2.5

        if self.team == "enemy":
            self.direction = "left"

        self.load_animations()

        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.moves["Mana Theft (10)"] = self.manatheft
        self.moves["Stat Theft (20)"] = self.statstealing
        self.moves["Underwear Theft (10)"] = self.stealunderwear

    def manatheft(self, target: object, target_team: list):
        mana_cost = 10
        if self.mana > mana_cost:
            self.mana -= mana_cost
            damage = self.calc_damage(target, "physical", 0.1)
            damagemana = 20

            self.melee(target)
            self.update_stats(target, damage, "manasteal", 2)

            target.health -= damage
            target.mana -= damagemana
            self.mana += damagemana
            if self.mana > self.max_mana:
                self.mana = self.max_mana

            if self.game.sound:
                pygame.mixer.Sound.play(self.attack_audio)
                self.game.sprites.add(ui_functions.HitImage("tank_charge", self, 2))

            print(f"You steal 20 mana from {target.name}!")
            # print(f"[DEBUG] Target MANA: {target.mana}/{target.max_mana}")
            # print(f"[DEBUG] Your Mana: {self.mana}/{self.max_mana}")
            return True

    def statstealing(self, target: object, target_team: list):
        mana_cost = 20
        if self.mana > mana_cost:
            self.mana -= mana_cost
            damage = self.calc_damage(target, "physical", 0.05)
            stealratio = 0.1

            self.melee(target)
            self.update_stats(target, damage, "statsteal", 2)

            target.health -= damage
            self.strength += max(10,math.floor(target.strength * stealratio))
            target.strength -= max(5,math.floor(target.strength * stealratio))


            if self.game.sound:
                pygame.mixer.Sound.play(self.attack_audio)

            print(
                f"You steal {math.floor(target.strength * stealratio)} damage from {target.name}!"
            )
            print(f"[DEBUG] DAMAGE: {self.strength}")
            return True

    def stealunderwear(self, target: object, target_team: list):
        mana_cost = 10
        if self.mana > mana_cost:
            self.mana -= mana_cost
            damage = self.calc_damage(target, "physical", 999)

            if self.strength >= 15:
                self.melee(target)
                self.update_stats(target, damage, "atk", 2)
                self.strength -= 5
                target.health -= damage

                if self.game.sound:
                    pygame.mixer.Sound.play(self.attack_audio)

                print(
                    f"You steal underwear from {target.name}!, {target.name} fell ashame rather to died"
                )

            else:
                self.strength += 1
                print("You dont have enought strength to steal underwear")
                print(f"{self.strength}/15 ")

            return True
