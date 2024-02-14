import pygame, random, sys

from classes.units.knight import Knight
from .reaper import Reaper

pygame.init()

def create_unit(name, unit_class, team, game):
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
            game.players.add(unit)
        
        case "enemy":
            game.enemies.add(unit)
            
    # Add all of the units to a main sprite group as well
    game.all_units.add(unit)
    
    return unit

# player_list = [("Southpaw", "Reaper"),
#                ("Genesis", "Knight"),
#                ("Akshan", "Knight"),
#                ("Samal", "Reaper")]

# enemy_list = [("Fury", "Reaper"),
#               ("Hawk", "Reaper"),
#               ("Nova", "Knight")]

def create_team(unit_list: list, team: str, game):
    """Creates units based on an input list and team name
    
    unit_list = list of tuples (name, char_class)"""
    for unit in unit_list:
        create_unit(unit[0], unit[1], team, game)
        
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
