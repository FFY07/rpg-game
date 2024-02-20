import random

from classes.unit import Unit

import resources2.audio as audio

# Range of values
STRENGTH = (1, 10)
INTELLIGENCE = (5, 15)
DEFENCE = (5, 15)
MAGIC_RESIST = (5, 15)

class Tank(Unit):
    def __init__(self, name, team, id_no = 0, game = None):
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