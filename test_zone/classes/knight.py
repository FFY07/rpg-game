from classes import Unit

class Knight(Unit):
    '''Knight class from Unit'''
    def __init__(self, name = "DefaultKnight", team = "enemy"):
        super().__init__()
        self.name = name
        self.team = team
        self.unit_name = "Knight"
        self.strength += 5
        self.intelligence -= 5
        self.defence += 5
        self.magic_resist -= 5

        self.size_scale = 3
        
        # Load image according to team
        if team == "player":
            self.load_animations()
        else:
            self.load_animations(True)