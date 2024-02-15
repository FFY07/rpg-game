import random

from classes.unit import Unit

# Range of values
STRENGTH = (5, 20)
INTELLIGENCE = (3, 15)
DEFENCE = (1, 10)
MAGIC_RESIST = (1, 5)

class Knight(Unit):
    def __init__(self, name, team, id_no = 0):
        super().__init__(name, team, id_no)
        self.unit_class = "Knight"
        
        self.name = name
        self.team = team
        self.id = id_no
        
        self.strength = random.randint(*STRENGTH)
        self.intelligence = random.randint(*INTELLIGENCE)
        self.defence = random.randint(*DEFENCE)
        self.magic_resist = random.randint(*MAGIC_RESIST)
        
        self.size_scale = 3
        
        if self.team == "enemy":
            self.direction = "left"
            
        self.load_animations()
        
        # Loads the first idle frame so the proper rect size can be generated
        # Make sure all images are the same size
        self.image = self.animations["idle"][0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position