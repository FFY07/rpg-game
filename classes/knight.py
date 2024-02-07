import main_unit as unit

class Knight(unit.Unit):
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
        self.load_animations()