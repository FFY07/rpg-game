import gui.screen as sc
import pygame
import resources.font as font

def draw_menu0():
    sc.screen.fill((0, 0, 0))
    sc.draw_centertext ('[ INTRODUCTION TO PROGRAMMING ]', font.menu_font, font.GREY,- 220)
    sc.draw_centertext ('(DICT/DNDFC) ASSIGNMENT ', font.menu_font, font.GREY, - 180)
    sc.draw_centertext('TURN-BASED RPG', font.menutitle_font, font.YELLOW,- 110)



