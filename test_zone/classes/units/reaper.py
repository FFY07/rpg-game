import random

from classes.unit import Unit

# Range of values
STRENGTH = (10, 25)
INTELLIGENCE = (1, 10)
DEFENCE = (1, 5)
MAGIC_RESIST = (1, 5)

class Reaper(Unit):
    def __init__(self, name, team, id_no = 0):
        super().__init__(name, team, id_no)
        self.unit_class = "Reaper"
        
        self.name = name
        self.team = team
        self.id = id_no
        
        self.strength = random.randint(*STRENGTH)
        self.intelligence = random.randint(*INTELLIGENCE)
        self.defence = random.randint(*DEFENCE)
        self.magic_resist = random.randint(*MAGIC_RESIST)
        
        self.size_scale = 2
        
        if self.team == "enemy":
            self.direction = "left"
            
        self.load_animations()