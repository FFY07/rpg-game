import gui.screen as sc
import pygame
import resources.font as font

def draw_menu_options():
    sc.draw_menubg()
    sc.draw_centertext ('[ OPTIONS ]', font.menu_font, font.YELLOW,- 220)
