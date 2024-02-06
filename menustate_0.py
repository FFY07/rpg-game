import gui.screen as sc
import pygame



def draw_menu0():
    sc.screen.fill((0, 0, 0))
    sc.draw_centertext ('[ INTRODUCTION TO PROGRAMMING ]', sc.font.menu_font, sc.font.GREY,- 220)
    sc.draw_centertext ('(DICT/DNDFC) ASSIGNMENT ', sc.font.menu_font, sc.font.GREY, - 180)
    sc.draw_centertext('TURN-BASED RPG', sc.font.menutitle_font, sc.font.TEXT_COL,- 130)



    sc.draw_centertext('Start Game', sc.font.menutitle_font, sc.font.TEXT_COL, 0 )
    sc.draw_centertext('Options', sc.font.menutitle_font, sc.font.TEXT_COL, 55)
    sc.draw_centertext('Credits', sc.font.menutitle_font, sc.font.TEXT_COL, 55 *2)
    sc.draw_centertext('Quit', sc.font.menutitle_font, sc.font.TEXT_COL, 55 * 3)
    sc.draw_centertext('>>> currently doing gui, pls use space to start <<<', sc.font.gui_font, sc.font.GREY , 220)  

