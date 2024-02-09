from unit import Unit

class Reaper(Unit):
    '''Reaper class from Unit'''
    def __init__(self, name = "DefaultReaper", team = "enemy"):
        super().__init__()
        self.name = name
        self.team = team
        self.unit_name = "Reaper"
        self.strength -= 5
        self.intelligence += 5
        self.defence -= 5
        self.magic_resist += 5
        
        self.size_scale = 2
        self.load_animations()
        
        # Make reaper animation speed faster when attacking