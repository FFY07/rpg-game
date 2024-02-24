import random, pygame

from classes.unit import Unit

import resources2.audio as audio
import gui2.ui_functions as ui_functions

# Range of values
STRENGTH = (1, 20)
INTELLIGENCE = (10, 20)
DEFENCE = (5, 15)
MAGIC_RESIST = (5, 15)


class Tank(Unit):
    def __init__(self, name, team, id_no=0, game=None):
        super().__init__(name, team, id_no)
        self.game = game

        self.unit_class = "Tank"
        self.attack_audio = audio.tank_basic

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

        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.cannon_shells = 0

        # Add moves to moves dictionary
        self.moves["Cannon"] = self.cannon
        self.moves["Machine Gun"] = self.machine_gun

    def cannon(self, target: object, target_team: list):
        mana_cost = 40

        if self.mana >= mana_cost:
            if not self.cannon_shells:
                self.cannon_shells += 1
                if self.game.sound:
                    pygame.mixer.Sound.play(audio.tank_load_shell)
                    self.game.sprites.add(ui_functions.HitImage("tank_charge", self, 2))

            # If we have cannon shells, proceed to fire
            else:
                self.cannon_shells = 0
                self.mana -= mana_cost
                if self.game.sound:
                    pygame.mixer.Sound.play(audio.tank_183mm)
                damage = (self.intelligence - target.magic_resist) * 3

                if damage < 0:
                    damage = 0

                self.game.sprites.add(ui_functions.HitImage("tank_cannon", target, 2))

                self.melee(target)
                self.change_state("attack")
                target.change_state("hurt")
                target.health -= damage
                print(f"[DEBUG] {target.name} HP: {target.health}")

            return True
        else:
            # Attack fail
            return False

    def machine_gun(self, target: object, target_team: list):
        mana_cost = 30

        if self.mana >= mana_cost:
            self.mana -= mana_cost
            print(f"[DEBUG] Mana: {self.mana + mana_cost} - {mana_cost} = {self.mana}")
            try:
                # Selects 2 targets from the target team
                target_list = random.sample(target_team, 2)
            except:
                # in case there's only 1 target left
                target_list = target_team

            for t in target_list:
                damage = self.intelligence - t.magic_resist
                if damage < 0:
                    damage = 0

                self.change_state("attack")
                t.change_state("hurt")
                t.health -= damage

                # Create effect
                self.game.sprites.add(ui_functions.HitImage("tank_mg", t, 2))
                print(f"[DEBUG] {t.name} HP: {t.health}")

            if self.game.sound:
                pygame.mixer.Sound.play(audio.tank_machine_gun)

            return True

        else:
            # Attack fail
            return False
