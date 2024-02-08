# CURRENT STATUS: TESTING MODE (RUN THIS FILE DIRECTLY)

import pygame, random, sys

from knight import Knight
from reaper import Reaper

all_units = pygame.sprite.Group()
enemies = pygame.sprite.Group()
players = pygame.sprite.Group()

pygame.init()

FPS = 60

test_window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("test window")
clock = pygame.time.Clock()

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
player3 = create_unit("Millenium", "Knight", "player")
player4 = create_unit("Hakko", "Knight", "player")
enemy1 = create_unit("Kremlin", "Knight", "enemy")
enemy2 = create_unit("Moscow", "Reaper", "enemy")
enemy3 = create_unit("Berlin", "Reaper", "enemy")

# Checking the number of sprites in each sprite group
print(enemies)
print(players)
print(all_units)

# Checking if the images are loaded    
# for k, v in player1.animations.items():
#     print(f"player1 {k}")
#     for n, i in enumerate(v):
#         print(f"{n+1}: {i}")
    
# for k, v in enemy1.animations.items():
#     print(f"enemy1 {k}")
#     for n, i in enumerate(v):
#         print(f"{n+1}: {i}")


# Lists of valid coordinates for placing characters

player_positions = [(300, 210), 
                   (230, 260), 
                   (160, 310)
                   ]

enemy_positions = [(720, 200),
                   (790, 250),
                   (860, 300)
                   ]

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
        # assign the coordinates to the character
        character.x, character.y = coordinates
    except IndexError:
        pass

# As you can see each character has a x and y based on the list
for character in players:
    print(f"x: {character.x} y: {character.y}")
    # Delete this part after you understand

while True:
    
    test_window.fill((50, 50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # enemies.update()
    # enemies.draw(test_window)
    
    # Player team follows the player position list, enemy doesn't because I didn't create a position list for them
    # TODO: Flip enemy sprite accordingly with pygame.transform.flip()
    all_units.update()
    all_units.draw(test_window)
    
    clock.tick(FPS)
    pygame.display.update()