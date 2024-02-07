# CURRENT STATUS: TESTING MODE (RUN THIS FILE DIRECTLY)

import pygame, random

from knight import Knight
from reaper import Reaper

all_units = pygame.sprite.Group()
enemies = pygame.sprite.Group()
players = pygame.sprite.Group()

def create_unit(name, class_type, team = "enemy"):
    """Creates a new unit object and adds it to the sprite groups

    Args:
        name (str): Name of the unit
        class_type (str): Class of the unit
        team (str, optional): Which team this unit is on. Defaults to "enemy".

    Returns:
        obj: returns the newly-created unit object
    """
    
    # Create the unit object
    match class_type:
        
        case "Reaper":
            unit = Reaper(name, team)
        
        case "Knight":
            unit = Knight(name, team)
        
        case _:
            print("Error, invalid class. Defaulting to Knight")
            unit = Knight(name, team)
    
    # Add the unit to the correct sprite group
    match team:
        case "player":
            players.add(unit)
        
        case "enemy":
            enemies.add(unit)
            
    # Add all of the units to a main sprite group as well
    all_units.add(unit)
    
    return unit

# Testing zone
player1 = create_unit("Magnus", "Reaper", "player")
player2 = create_unit("Ampersand", "Knight", "player")
enemy1 = create_unit("Kremlin", "Knight", "enemy")

# Checking the number of sprites in each sprite group
print(enemies)
print(players)
print(all_units)

# Checking if the images are loaded    
for k, v in player1.animations.items():
    print(f"player1 {k}")
    for n, i in enumerate(v):
        print(f"{n+1}: {i}")
    
for k, v in enemy1.animations.items():
    print(f"enemy1 {k}")
    for n, i in enumerate(v):
        print(f"{n+1}: {i}")


# Create a list of predefined positions

player_pos_list = [(300, 210), 
                   (230, 260), 
                   (160, 310)
                   ]

# I haven't test indexerror yet ah TBD
# This sets the character self.x and self.y according to the position list
for position, character in zip(player_pos_list, players):
    character.x, character.y = position
    print(position, character)

# As you can see each character has a x and y based on the list
for character in players:
    print(f"x: {character.x} y: {character.y}")

# Note to RZ: can the list be a dictionary instead?

# player1.basic_attack(enemy1)
# player1.fireball(enemy1)

# enemy1.basic_attack(player1)
# enemy1.fireball(player1)

# enemy1.fireball(enemy1)

# player1.show_stats()
# enemy1.show_stats()
