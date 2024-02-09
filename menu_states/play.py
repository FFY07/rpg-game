import pygame

import gui.screen as sc
import gui.gamelog as gamelog
import classes.class_functions as cf

player_list = [("Southpaw", "Reaper"),
               ("Genesis", "Knight"),
               ("Akshan", "Knight"),
               ("Samal", "Reaper")]

enemy_list = [("Fury", "Reaper"),
              ("Hawk", "Reaper"),
              ("Nova", "Knight")]

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