import pygame
import resources.font as font
import resources as rsc
import gui.screen as sc
import gui.gamelog as gamelog
import classes.class_functions as cf
from gui import bars as bars
import random

# Lists of valid character coordinates for this scene
player_positions = [(300, 210), 
                   (230, 260), 
                   (160, 310)]

enemy_positions = [(720, 200),
                   (790, 250),
                   (860, 300)]

player_list = [("Southpaw", "Reaper"),
               ("Genesis", "Knight"),
               ("Akshan", "Knight"),]

class_list = ['Knight', 'Reaper']
enemy_list = []
for i in range(3):
    name  = 'AI ' + str(random.randint(10, 99))
    classes = random.choice(class_list)
    enemy =  (name, classes)
    enemy_list.append(enemy)


# enemy_list = [("Fury", "Reaper"),
#               ("Hawk", "Reaper"),
#               ("Nova", "Knight")]

cf.create_team(player_list, "player")
cf.create_team(enemy_list, "enemy")

cf.set_positions(player_positions, cf.players)
cf.set_positions(enemy_positions, cf.enemies)

def play():
    sc.draw_bg()
    sc.draw_panel()
    gamelog.draw_game_logs()

    
    cf.all_units.update()
    cf.all_units.draw(sc.screen)

    for count, i in enumerate(enemy_list):
                #show name and health
                sc.draw_text(f'{i}',font.hp_font, font.RED, 800, (12) + count  * 42)
                
    bars.allbars.update()
    bars.allbars.draw(sc.screen)
    
    # Rendering the text after the bar image makes it display on top of the bar image
    bars.textbars.update()
    bars.textbars.draw(sc.screen)

    # Initial setup

    