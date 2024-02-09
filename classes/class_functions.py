# CURRENT STATUS: TESTING MODE (RUN THIS FILE DIRECTLY)

import pygame, random, sys

from .knight import Knight
from .reaper import Reaper

all_units = pygame.sprite.Group()
enemies = pygame.sprite.Group()
players = pygame.sprite.Group()

pygame.init()

# FPS = 60

# test_window = pygame.display.set_mode((1280, 720))
# pygame.display.set_caption("test window")
# clock = pygame.time.Clock()

def create_unit(name, unit_class, team = "enemy"):
    """Creates a new unit object and adds it to the sprite groups

    Args:
        name (str): Name of the unit
        unit_class (str): Class of the unit
        team (str, optional): Which team this unit is on. Defaults to "enemy".

    Returns:
        obj: returns the newly-created unit object
    """
    
    # Create the unit object
    match unit_class:
        
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

# player_list = [("Southpaw", "Reaper"),
#                ("Genesis", "Knight"),
#                ("Akshan", "Knight"),
#                ("Samal", "Reaper")]

# enemy_list = [("Fury", "Reaper"),
#               ("Hawk", "Reaper"),
#               ("Nova", "Knight")]

def create_team(unit_list: list, team: str):
    """Creates units based on an input list and team name
    
    unit_list = list of tuples (name, char_class)"""
    for unit in unit_list:
        create_unit(unit[0], unit[1], team)
        
def set_positions(position_list, sprite_group):
    for character in sprite_group:
        
        # Assigns a coordinate position to the unit
        try:
            coordinates = position_list.pop(0)
            
            # assign the coordinates to the character
            character.x, character.y = coordinates
        
        # If there are no available positions left, we leave the unit's coordinates at default
        except IndexError:
            pass

# create_team(player_list, "player")
# create_team(enemy_list, "enemy")


# TEMPORARY, the real list is at gui.screen
player_positions = [(300, 210), 
                   (230, 260), 
                   (160, 310)]

enemy_positions = [(720, 200),
                   (790, 250),
                   (860, 300)]

# Set the character self.x and self.y according to the position list
for position, character in enumerate(players):
        
    # remove the position from the list if it exists, else just ignore and let it default
    try:
        coordinates = player_positions.pop(0)
        # assign the coordinates to the character
        character.x, character.y = coordinates
    except IndexError:
        pass

for position, character in enumerate(enemies):
    try:
        coordinates = enemy_positions.pop(0)
        character.x, character.y = coordinates
    except IndexError:
        pass

# As you can see each character has a x and y based on the list
for character in players:
    print(f"{character.name} x: {character.x} y: {character.y}")
    # Delete this part after you understand DEBUG ONLY

# JUST A TEST WINDOW
# while True:
    
#     test_window.fill((50, 50, 50))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
    
#     # enemies.update()
#     # enemies.draw(test_window)
    
#     # Player team follows the player position list, enemy doesn't because I didn't create a position list for them
#     # TODO: Flip enemy sprite accordingly with pygame.transform.flip()
#     all_units.update()
#     all_units.draw(test_window)
    
#     clock.tick(FPS)
#     pygame.display.update()