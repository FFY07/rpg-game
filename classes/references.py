import random
from pathlib import Path

import pygame

# Character default stats
MAX_HEALTH = 100
STRENGTH = 10
INTELLIGENCE = 10
DEFENCE = 5
MAGIC_RESIST = 5

START_LEVEL = 1
BASE_EXP = 0
EXP_TO_LEVEL = 100

COINS = 0
MANA = 0

'''
This code not finished but ya just reference only, can use or delete up to you
Can move your classes as children under this Unit class (e.g. Fighter(Unit)) so it's easier to manage all the attributes
Don't forget to update the __init__.py 
'''

class Unit(pygame.sprite.Sprite):
    '''Base Class for all characters'''
    def __init__(self):
        super().__init__()
        self.name = "DefaultName"
        self.team = "No team"
        self.health = MAX_HEALTH
        self.strengh = STRENGTH
        self.intellignce = INTELLIGENCE
        self.defence = DEFENCE
        self.magic_resist = MAGIC_RESIST
        self.level = START_LEVEL
        self.exp = BASE_EXP
        self.exp_to_level = EXP_TO_LEVEL
        self.coins = COINS
        self.mana = MANA
        self.animation_list = []
        self.x = 0
        self.y = 0
    
    def basic_attack(self, enemy):
        # There's no code that prevents you from attacking yourself
        damage = self.attack - enemy.defence
        
        if damage <0:
            damage = 0
        
        enemy.health -= damage
        
        print(f"{self.name} dealt {self.attack} - {enemy.defence} = {damage} damage to {enemy.name}") # DEBUG
    
    def fireball(self, enemy):
        damage = self.intelligence - enemy.magic_resist
        
        if damage <0:
            damage = 0
        
        enemy.health -= damage
        
        print(f"{self.name} dealt {self.intelligence} - {enemy.magic_resist} = {damage} magic damage to {enemy.name}") # DEBUG
        
    def show_stats(self):
        print(f"Name: {self.name}, Health: {self.health}, Level: {self.level}, Exp: {self.exp}")
    
    def load_animation(self, folder):
        '''Loads a spritesheet from a folder'''
        path = Path(folder)
        img_list = (list(path.glob("*.*")))
        for i in img_list:
            image = pygame.image.load(i)
            image = pygame.transform.scale(image, (image.get_width()*2 ,image.get_height()*2))
            self.animation_list.append(image)
            # print(image)
            # print(type(image))
        
          

class Mage(Unit):
    '''Mage class from Unit'''
    def __init__(self, name = "DefaultMage", team = "enemy"):
        super().__init__()
        self.name = name
        self.team = team
        self.attack = 5
        self.intelligence = 20
        self.magic_resist = 10
        
class Fighter(Unit):
    '''Fighter class from Unit'''
    def __init__(self, name = "DefaultFighter", team = "enemy"):
        super().__init__()
        self.name = name
        self.team = team
        self.attack = 15
        self.intelligence = 5
        self.defence = 15

        self.load_animation(f"{Path('resources/picture/knightpic/death')}")
        

# Test zone (pls delete in future)

player1 = Mage("Magnus", "player")
enemy1 = Fighter("Kremlin", "enemy")

active_units = []
enemy_list = []
for character in active_units:
    if character.team == "enemy":
        enemy_list.append(character)
    else:
        pass

# player1.load_animation(f"{Path('resources/picture/knightpic/death')}")
    
# for i in player1.animation_list:
#     print(i)

# player1.basic_attack(enemy1)
# player1.fireball(enemy1)

# enemy1.basic_attack(player1)
# enemy1.fireball(player1)

# enemy1.fireball(enemy1)

# player1.show_stats()
# enemy1.show_stats()
