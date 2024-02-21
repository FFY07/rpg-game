import random

from classes.unit import Unit

import resources2.audio as audio

# Range of values
STRENGTH = (5, 20)
INTELLIGENCE = (3, 15)
DEFENCE = (1, 10)
MAGIC_RESIST = (1, 5)


class Knight(Unit):
    def __init__(self, name, team, id_no=0, game=None):
        super().__init__(name, team, id_no)
        self.game = game

        self.unit_class = "Warrior"
        self.attack_audio = audio.warrior_basic
        self.anim_speed = 50

        self.name = name
        self.team = team
        self.id = id_no

        # self.strength = random.randint(*STRENGTH)
        self.strength = 999
        self.intelligence = random.randint(*INTELLIGENCE)
        self.defence = random.randint(*DEFENCE)
        self.magic_resist = random.randint(*MAGIC_RESIST)

        self.size_scale = 3.5

        if self.team == "enemy":
            self.direction = "left"

        self.load_animations()

        # Loads the first idle frame so the proper rect size can be generated
        # Make sure all images are the same size
        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position
