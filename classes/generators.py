import pygame, random

import main_unit
from knight import Knight
from reaper import Reaper

all_units = pygame.sprite.Group()
enemies = pygame.sprite.Group()
players = pygame.sprite.Group()

def create_unit(name, class_type, team = "enemy"):
    """Creates a new unit object and adds it to the sprite group(s)?

    Args:
        name (str): Name of the unit
        class_type (str): Class of the unit
        team (str, optional): Which team this unit is on. Defaults to "enemy".

    Returns:
        obj: returns the newly-created unit object
    """
    match class_type:
        case "Reaper":
            unit = Reaper(name, team)
        
        case "Knight":
            unit = Knight(name, team)
        
        case _:
            print("Error, invalid class. Defaulting to Knight")
            unit = Knight(name, team)
            
    match team:
        case "player":
            players.add(unit)
        
        case "enemy":
            enemies.add(unit)
            
    all_units.add(unit)
    return unit



player1 = create_unit("Magnus", "Reaper", "player")
enemy1 = create_unit("Kremlin", "Knight", "enemy")

print(enemies)
print(players)
print(all_units)


# player1 = Reaper("Magnus", "player")
# enemy1 = Knight("Kremlin", "enemy")

    
for k, v in player1.animations.items():
    print(k)
    for n, i in enumerate(v):
        print(f"{n+1}: {i}")
    
for k,v in enemy1.animations.items():
    print(k, v)

# character_list = []
# for i in range(3):
#     character = main_unit.Fighter()
#     character_list.append(character)
    
# # print(character_list)

# player_pos_list = [(300, 210), 
#                    (230, 260), 
#                    (160, 310)
#                    ]

# for position, character in zip(player_pos_list, character_list):
#     character.x, character.y = position
#     print(position, character)

# for character in character_list:
#     print(f"x: {character.x} y: {character.y}")
    
# Something like that lets us set all our positions in a list


# player1.basic_attack(enemy1)
# player1.fireball(enemy1)

# enemy1.basic_attack(player1)
# enemy1.fireball(player1)

# enemy1.fireball(enemy1)

# player1.show_stats()
# enemy1.show_stats()
