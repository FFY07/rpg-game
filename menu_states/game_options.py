import gui.screen as sc
import pygame
import resources.font as font

def draw_menu_options():
    sc.draw_optionbg()
    sc.draw_centertext ('[ OPTIONS ]', font.menu_font, font.BLACK,- 180)

