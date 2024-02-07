import gui.screen as sc
import pygame
import resources.font as font

def draw_menu():
    sc.screen.fill((0, 0, 0))
    sc.draw_centertext (' ERROR 403 :( ', font.menutitle_font, font.YELLOW,- 200)
    sc.draw_centertext (' sorry, Desmond is lazy to do this feature', font.menu_font, font.WHITE, 0)
    sc.draw_centertext('and he most likely not going to do this :^) ', font.menu_font, font.WHITE, 40)
