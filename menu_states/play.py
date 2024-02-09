import pygame
import resources.font as font
import gui.screen as sc
import gui.gamelog as gamelog
import classes.class_functions as cf
import random

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

cf.set_positions(sc.player_positions, cf.players)
cf.set_positions(sc.enemy_positions, cf.enemies)


def play():
    sc.draw_bg()
    sc.draw_panel()
    gamelog.draw_game_logs()
    
    cf.all_units.update()
    cf.all_units.draw(sc.screen)

    for count, i in enumerate(enemy_list):
                #show name and health
                sc.draw_text(f'{i}',font.hp_font, font.RED, 800, (12) + count  * 42)

    # Initial setup

    