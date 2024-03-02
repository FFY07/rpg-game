import random

import gui.screen as scr

from classes.units import reaper
from classes.units import warrior
from classes.units import bandit
from classes.units import tank
from classes.units import princess
from classes.units import necromancer
from classes.units import paladin

import resources.images as images

# IMPORTANT: UPDATE THIS WHEN ADDING A NEW CLASS
unit_dict = {
    "Warrior": "Generally balance character, able to buff teammate and deal damage",
    "Reaper": "Use HP cast skill insteal of Mana, ATK change based on current HP ",
    "Bandit": "High INT, Able to use Sword with different effect",
    "Tank": "Tank",
    "Princess": "Able to heal and regen Mana for teammate, but get more damage by other",
    "Necromancer": "Powerful mage with high intelligence and magic resistance",
    "Paladin": "Holy Knight that can heal and deal more damage to Undead"
}

unitrace_dict = {
    "Warrior": f"{warrior.race}",
    "Reaper": f"{reaper.race}",
    "Bandit": f"{bandit.race}",
    "Tank": f"{tank.race}",
    "Princess": f"{princess.race}",
    "Necromancer": f"{necromancer.race}",
    "Paladin" : f"{paladin.race}"
}

stat_dict = {
    "Warrior": f"STR: {warrior.STRENGTH[0]:<5} INT: {warrior.INTELLIGENCE[0]:<5} DEF: {warrior.DEFENCE[0]:<5} MR: {warrior.MAGIC_RESIST[0]:<5}",
    "Reaper": f"STR: {reaper.STRENGTH[0]:<5} INT: {reaper.INTELLIGENCE[0]:<5} DEF: {reaper.DEFENCE[0]:<5} MR: {reaper.MAGIC_RESIST[0]:<5}",
    "Bandit": f"STR: {bandit.STRENGTH[0]:<5} INT: {bandit.INTELLIGENCE[0]:<5} DEF: {bandit.DEFENCE[0]:<5} MR: {bandit.MAGIC_RESIST[0]:<5}",
    "Tank": f"STR: {tank.STRENGTH[0]:<5} INT: {tank.INTELLIGENCE[0]:<5} DEF: {tank.DEFENCE[0]:<5} MR: {tank.MAGIC_RESIST[0]:<5}",
    "Princess": f"STR: {princess.STRENGTH[0]:<5} INT: {princess.INTELLIGENCE[0]:<5} DEF: {princess.DEFENCE[0]:<5} MR: {princess.MAGIC_RESIST[0]:<5}",
    "Necromancer": f"STR: {necromancer.STRENGTH[0]:<5} INT: {necromancer.INTELLIGENCE[0]:<5} DEF: {necromancer.DEFENCE[0]:<5} MR: {necromancer.MAGIC_RESIST[0]:<5}",
    "Paladin": f"STR: {paladin.STRENGTH[0]:<5} INT: {paladin.INTELLIGENCE[0]:<5} DEF: {paladin.DEFENCE[0]:<5} MR: {paladin.MAGIC_RESIST[0]:<5}"
}


marketing_images = {
    "Warrior": images.warrior_marketing,
    "Reaper": images.reaper_marketing,
    "Bandit": images.bandit_marketing,
    "Tank": images.tank_marketing,
    "Princess": images.princess_marketing,
    "Necromancer": images.necromancer_marketing,
    "Paladin": images.paladin_marketing,
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
            unit = reaper.Reaper(name, team, game)

        case "Warrior":
            unit = warrior.Warrior(name, team, game)

        case "Bandit":
            unit = bandit.Bandit(name, team, game)

        case "Tank":
            unit = tank.Tank(name, team, game)

        case "Princess":
            unit = princess.Princess(name, team, game)

        case "Necromancer":
            unit = necromancer.Necromancer(name, team, game)
        
        case "Paladin":
            unit = paladin.Paladin(name, team, game)

        case _:
            raise Exception(
                f"An error has occured while creating Unit objects. (Class [{unit_class}] does not exist)"
            )

    # Increment the current game id by 1
    # game.current_id += 1

    # Add the unit to the correct sprite group

    if not standalone:
        match team:
            case "player":
                game.players.add(unit)

            case "enemy":
                game.enemies.add(unit)

        # Add all of the units to the main units sprite group as well
        game.all_units.add(unit)

    game.event_log.append(f"{unit.name} [{unit.unit_class}] was created!")

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

        # After setting our coordinates, remember the unit's starting position
        unit.prev_pos = unit.rect.center
