import random

from classes.unit import Unit

# Range of values
STRENGTH = (8, 15)
INTELLIGENCE = (1, 5)
DEFENCE = (1, 8)
MAGIC_RESIST = (1, 8)

class Bandit(Unit):
    def __init__(self, name, team, id_no = 0, game = None):
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