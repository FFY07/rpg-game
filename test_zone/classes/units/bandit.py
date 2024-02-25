import pygame,random,math

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


        self.moves["Mana Theft (10)"] = self.manatheft
        self.moves["Stat Theft (20)"] = self.statstealing
    def manatheft(self, target: object, target_team: list):
        mana_cost = 10
        if self.mana > mana_cost:
            self.mana -= mana_cost
            damage = 5
            damagemana = 20

            # PUT THIS WHOLE SECTION INTO ONE METHOD LATER?
            if self.team == "player":
                self.activate(target.rect.midleft)
            else:
                self.activate(target.rect.midright)

            self.change_state("attack")
            target.change_state("hurt")
            target.health -= damage
            target.mana -= damagemana
            self.mana += damagemana
            if self.mana > 100:
                self.mana = 100

            if self.game.sound:
                pygame.mixer.Sound.play(self.attack_audio)
            # THIS WHOLE SECTION ABOVE INTO ONE METHOD?

            print(f"You steal 20 mana from {target.name}!")
            print(f"[DEBUG] Target MANA: {target.mana}/{target.max_mana}")
            print(f"[DEBUG] Your Mana: {self.mana}/{self.max_mana}")
            return True
        

    def statstealing(self, target: object, target_team: list):
        mana_cost = 20
        if self.mana > mana_cost:
            self.mana -= mana_cost
            damage = 1
            stealratio = 0.1
            # PUT THIS WHOLE SECTION INTO ONE METHOD LATER?
            if self.team == "player":
                self.activate(target.rect.midleft)
            else:
                self.activate(target.rect.midright)

            self.change_state("attack")
            target.change_state("hurt")
            target.health -= damage
            target.strength += math.floor(target.strength * stealratio)
            self.strength += math.floor(target.strength * stealratio)

            if self.game.sound:
                pygame.mixer.Sound.play(self.attack_audio)
            # THIS WHOLE SECTION ABOVE INTO ONE METHOD?

            print(f"You steal {math.floor(target.strength * stealratio)} damage from {target.name}!")
            print(f"[DEBUG] DAMAGE: {self.strength}")
            return True