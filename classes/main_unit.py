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
        self.strength = STRENGTH
        self.intelligence = INTELLIGENCE
        self.defence = DEFENCE
        self.magic_resist = MAGIC_RESIST
        self.level = START_LEVEL
        self.exp = BASE_EXP
        self.exp_to_level = EXP_TO_LEVEL
        self.coins = COINS
        self.mana = MANA
        


        self.size_scale = 1
        self.x = 0
        self.y = 0
        
        self.actions = ["idle",
                "attack",
                "hurt",
                "death"]
        
        self.animations = {}
        
        # Temporary for debug only
    def show_stats(self):
        print(f"Name: {self.name}, Health: {self.health}, Level: {self.level}, Exp: {self.exp}")
    
    def load_animations(self):
        '''loads all animations into the self.animations dictionary'''
        for action in self.actions:
            path = Path(f"resources/picture/{self.unit_name}/{action}")
            img_list = (list(path.glob("*.*")))
            
            # Create a temporary list
            loaded_img_list = []
            for i in img_list:
                image = pygame.image.load(i)
                image = pygame.transform.scale(image, (image.get_width()*self.size_scale, image.get_height()*self.size_scale))
                loaded_img_list.append(image)
            
            # Create a key value pair using action and loaded_img_list in the animations dictionary
            self.animations[action] = loaded_img_list
    
   
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