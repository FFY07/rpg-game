import random, pygame

from classes.unit import Unit

import resources2.audio as audio
import gui2.ui_functions as ui_functions

# Range of values
STRENGTH = (1, 20)
INTELLIGENCE = (5, 15)
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

        # Add moves to moves dictionary
        self.moves["Machine Gun"] = self.machine_gun

    def machine_gun(self, target: object, target_team: list):
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
            t.health -= damage

            # Create effect
            self.game.sprites.add(ui_functions.HitImage("tank_mg", t, 2))
            print(f"[DEBUG] {t.name} HP: {t.health}")

        if self.game.sound:
            pygame.mixer.Sound.play(audio.tank_machine_gun)
