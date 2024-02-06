import pygame, random

import references

# from fighter import Unit as Fighter

# def create_char(name = "Unnamed", class_name = "Fighter", team = "enemy"):
#     if team == "enemy":
#         match class_name:
#             case "Fighter":
#                 character = Fighter(name, )
                
# not done yet, need to completely redo, especially draw function

character_list = []
for i in range(3):
    character = references.Fighter()
    character_list.append(character)
# print(character_list)

player_pos_list = [(300, 210), 
                   (230, 260), 
                   (160, 310)
                   ]

for position, character in zip(player_pos_list, character_list):
    character.x, character.y = position
    print(position, character)

for character in character_list:
    print(f"x: {character.x} y: {character.y}")
    
# Something like that lets us set all our positions in a list