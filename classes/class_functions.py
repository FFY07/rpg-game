import random

import gui.screen as scr

from classes.units.reaper import Reaper
from classes.units.warrior import Warrior
from classes.units.bandit import Bandit
from classes.units.tank import Tank
from classes.units.princess import Princess
import resources.images as images

# IMPORTANT: UPDATE THIS WHEN ADDING A NEW CLASS
unit_dict = {"Warrior": "Generally balance character, able to buff teammate and deal damage", 
             "Reaper": "Use HP insteal of Mana, Play risk to get high reward", 
             "Bandit": "just a NPC", 
             "Tank": "Using INT point to Deal Damage and able to attack Multiple enemy ", 
             "Princess": "Able to heal and regen Mana for teammate, It have very low DEF and Magic DEF"}

stat_dict = {"Warrior": "STRENGTH : 12       INTELLIGIENCE : 10           DEFENCE : 45         MAGIC RESIST : 40",
             "Reaper": "STRENGTH : 25       INTELLIGIENCE : 5           DEFENCE : 20         MAGIC RESIST : 40" ,
             "Bandit": "STRENGTH : 8       INTELLIGIENCE : 20           DEFENCE : 40         MAGIC RESIST : 50" ,
             "Tank": "STRENGTH : 10       INTELLIGIENCE : 15           DEFENCE : 80         MAGIC RESIST : 30" , 
             "Princess": "STRENGTH : 11       INTELLIGIENCE : 25           DEFENCE : 10         MAGIC RESIST : 5" }


marketing_images = {
    "Warrior": images.warrior_marketing,
    "Reaper": images.reaper_marketing,
    "Bandit": images.bandit_marketing,
    "Tank": images.tank_marketing,
    "Princess": images.background_img,
}


def create_unit(name, unit_class, team, game, standalone=False):
    """Creates a new unit object and adds it to the sprite groups

    Args:
        name (str): Name of the unit
        unit_class (str): Class of the unit
        team (str, optional): Which team this unit is on. Defaults to "enemy".

    Returns:
        obj: returns the newly-created unit object
    """

    # If the given unit class is invalid, select a random one
    if unit_class not in unit_dict.keys():
        print(f"[{unit_class}] is not a valid class")
        unit_class = random.choice(list(unit_dict.keys()))
        print(f"[{unit_class}] has been selected instead")

    # Create the unit object
    match unit_class:

        case "Reaper":
            unit = Reaper(name, team, game.current_id, game)

        case "Warrior":
            unit = Warrior(name, team, game.current_id, game)

        case "Bandit":
            unit = Bandit(name, team, game.current_id, game)

        case "Tank":
            unit = Tank(name, team, game.current_id, game)

        case "Princess":
            unit = Princess(name, team, game.current_id, game)

        case _:
            raise Exception(
                f"An error has occured while creating Unit objects. (Class [{unit_class}] does not exist)"
            )

    # Increment the current game id by 1
    game.current_id += 1

    # Add the unit to the correct sprite group

    if not standalone:
        match team:
            case "player":
                game.players.add(unit)

            case "enemy":
                game.enemies.add(unit)

        # Add all of the units to the main units sprite group as well
        game.all_units.add(unit)

    # If unit is a standalone unit, we'll want to store it somewhere
    return unit


def create_team(unit_list: list, team: str, game):
    """Creates units based on an input list and team name

    unit_dict = list of tuples (name, char_class)"""
    for name, unit in unit_list:
        create_unit(name, unit, team, game)


def set_positions(position_list, sprite_group, anchor="center"):
    for unit in sprite_group:

        # Assigns a coordinate position to the unit
        try:
            coordinates = position_list.pop(0)

            # assign the coordinates to the unit
            match anchor:
                case "center":
                    unit.rect.center = coordinates

                case "midbottom":
                    unit.rect.midbottom = coordinates

                case "midtop":
                    unit.rect.midtop == coordinates

                case "midleft":
                    unit.rect.midleft == coordinates

                case "midright":
                    unit.rect.midright == coordinates

                case _:
                    print("Invalid anchor, check the code again!")
                    unit.rect.center == coordinates

            unit.position = coordinates

        # If there are no available positions left, we leave the unit's coordinates at default
        except IndexError:
            unit.rect.center = random.randint(0, scr.SCREEN_WIDTH), random.randint(
                0, scr.SCREEN_HEIGHT
            )
            print(f"No available positions left! Randomising to {unit.rect.center}!")

        unit.prev_pos = unit.rect.center
