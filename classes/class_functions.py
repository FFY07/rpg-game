import random

import gui.screen as scr

from classes.units import *

import resources.images as images

# IMPORTANT: UPDATE THIS WHEN ADDING A NEW CLASS
unit_dict = {
    "Warrior": "Generally balance character, able to buff teammate and deal damage",
    "Reaper": "Use HP cast skill insteal of Mana, ATK change based on current HP ",
    "Bandit": "High INT, Able to use Sword with different effect",
    "Tank": "Tank",
    "Princess": "Able to heal and regen Mana for teammate, but get more damage by other",
    "Necromancer": "Powerful mage with high intelligence and magic resistance",
    "Paladin": "Holy Knight that can heal and deal more damage to Undead",
    "Marchosias": "A demon who specializes in the use of fire.",
}

unit_race_dict = {
    "Warrior": f"{warrior.race}",
    "Reaper": f"{reaper.race}",
    "Bandit": f"{bandit.race}",
    "Tank": f"{tank.race}",
    "Princess": f"{princess.race}",
    "Necromancer": f"{necromancer.race}",
    "Paladin": f"{paladin.race}",
    "Marchosias": f"{marchosias.race}",
}

stat_str_dict = {
    "Warrior": f"STR: {warrior.STRENGTH[0]:<5}",
    "Reaper": f"STR: {reaper.STRENGTH[0]:<5}",
    "Bandit": f"STR: {bandit.STRENGTH[0]:<5}",
    "Tank": f"STR: {tank.STRENGTH[0]:<5}",
    "Princess": f"STR: {princess.STRENGTH[0]:<5}",
    "Necromancer": f"STR: {necromancer.STRENGTH[0]:<5}",
    "Paladin": f"STR: {paladin.STRENGTH[0]:<5}",
    "Marchosias": f"STR: {marchosias.STRENGTH[0]:<5}",
}

stat_int_dict = {
    "Warrior": f"INT: {warrior.INTELLIGENCE[0]:<5}",
    "Reaper": f"INT: {reaper.INTELLIGENCE[0]:<5}",
    "Bandit": f"INT: {bandit.INTELLIGENCE[0]:<5}",
    "Tank": f"INT: {tank.INTELLIGENCE[0]:<5}",
    "Princess": f"INT: {princess.INTELLIGENCE[0]:<5}",
    "Necromancer": f"INT: {necromancer.INTELLIGENCE[0]:<5}",
    "Paladin": f"INT: {paladin.INTELLIGENCE[0]:<5}",
    "Marchosias": f"INT: {marchosias.INTELLIGENCE[0]:<5}",
}
stat_def_dict = {
    "Warrior": f"DEF: {warrior.DEFENCE[0]:<5}",
    "Reaper": f"DEF: {reaper.DEFENCE[0]:<5}",
    "Bandit": f" DEF: {bandit.DEFENCE[0]:<5}",
    "Tank": f"DEF: {tank.DEFENCE[0]:<5}",
    "Princess": f"DEF: {princess.DEFENCE[0]:<5}",
    "Necromancer": f"DEF: {necromancer.DEFENCE[0]:<5}",
    "Paladin": f"DEF: {paladin.DEFENCE[0]:<5}",
    "Marchosias": f"DEF: {marchosias.DEFENCE[0]:<5}",
}
stat_mr_dict = {
    "Warrior": f"MR: {warrior.MAGIC_RESIST[0]:<5}",
    "Reaper": f"MR: {reaper.MAGIC_RESIST[0]:<5}",
    "Bandit": f"MR: {bandit.MAGIC_RESIST[0]:<5}",
    "Tank": f"MR: {tank.MAGIC_RESIST[0]:<5}",
    "Princess": f"MR: {princess.MAGIC_RESIST[0]:<5}",
    "Necromancer": f"MR: {necromancer.MAGIC_RESIST[0]:<5}",
    "Paladin": f"MR: {paladin.MAGIC_RESIST[0]:<5}",
    "Marchosias": f"MR: {marchosias.MAGIC_RESIST[0]:<5}",
}

marketing_images = {
    "Warrior": images.warrior_marketing,
    "Reaper": images.reaper_marketing,
    "Bandit": images.bandit_marketing,
    "Tank": images.tank_marketing,
    "Princess": images.princess_marketing,
    "Necromancer": images.necromancer_marketing,
    "Paladin": images.paladin_marketing,
    "Marchosias": images.marchosias_marketing,
}

passive_images = {
    "Warrior": images.warrior_passive,
    "Reaper": images.reaper_passive,
    "Bandit": images.bandit_passive,
    "Tank": images.tank_passive,
    "Princess": images.princess_passive,
    "Necromancer": images.necromancer_passive,
    "Paladin": images.paladin_passive,
    "Marchosias": images.marchosias_passive,
}

skill1_images = {
    "Warrior": images.warrior_skill1,
    "Reaper": images.reaper_skill1,
    "Bandit": images.bandit_skill1,
    "Tank": images.tank_skill1,
    "Princess": images.princess_skill1,
    "Necromancer": images.necromancer_skill1,
    "Paladin": images.paladin_skill1,
    "Marchosias": images.marchosias_skill1,
}
skill2_images = {
    "Warrior": images.warrior_skill2,
    "Reaper": images.reaper_skill2,
    "Bandit": images.bandit_skill2,
    "Tank": images.tank_skill2,
    "Princess": images.princess_skill2,
    "Necromancer": images.necromancer_skill2,
    "Paladin": images.paladin_skill2,
    "Marchosias": images.marchosias_skill2,
}
skill3_images = {
    "Warrior": images.warrior_skill3,
    "Reaper": images.reaper_skill3,
    "Bandit": images.bandit_skill3,
    "Tank": images.tank_skill3,
    "Princess": images.princess_skill3,
    "Necromancer": images.necromancer_skill3,
    "Paladin": images.paladin_skill3,
    "Marchosias": images.marchosias_skill3,
}

skill1_dict = {
    "Warrior": "Hasagi",
    "Reaper": "Decay",
    "Bandit": "Water Sword",
    "Tank": "Cannon",
    "Princess": "Heal",
    "Necromancer": "Siphon",
    "Paladin": "Sacrifice",
    "Marchosias": "Hell fire",
}

skill2_dict = {
    "Warrior": "Inspire",
    "Reaper": "Dead Scythe",
    "Bandit": "Fire Sword",
    "Tank": "Machine Gun",
    "Princess": "Cleanse",
    "Necromancer": "Infect",
    "Paladin": "Gospel",
    "Marchosias": "Infernal Rebirth",
}

skill3_dict = {
    "Warrior": "Execute",
    "Reaper": "Hell descent",
    "Bandit": "",
    "Tank": "Flamethrower",
    "Princess": "Wish",
    "Necromancer": "Doom",
    "Paladin": "Smite",
    "Marchosias": "Infernal Cataclysm",
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

    # Easter egg
    if name.casefold() == "toothless":
        unit = nightfury.NightFury(name, team, game)

    else:
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

            case "Marchosias":
                unit = marchosias.Marchosias(name, team, game)
            case _:
                raise Exception(
                    f"An error has occured while creating Unit objects. (Class [{unit_class}] does not exist)"
                )

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
