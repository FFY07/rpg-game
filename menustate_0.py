import gui.screen as sc
import pygame
import resources.font as font

menustate = 0
def draw_menu0():
    # option1color = font.GREY
    # option2color = font.GREY
    # option3color = font.GREY
    # option4color = font.GREY    

    sc.screen.fill((0, 0, 0))
    sc.draw_centertext ('[ INTRODUCTION TO PROGRAMMING ]', font.menu_font, font.GREY,- 220)
    sc.draw_centertext ('(DICT/DNDFC) ASSIGNMENT ', font.menu_font, font.GREY, - 180)
    sc.draw_centertext('TURN-BASED RPG', font.menutitle_font, font.YELLOW,- 110)



    # sc.draw_centertext('Start Game', font.menutitle_font, option1color, 0 )
    # sc.draw_centertext('Options', font.menutitle_font, option2color, 55)
    # sc.draw_centertext('Credits', font.menutitle_font, option3color, 55 *2)
    # sc.draw_centertext('Quit', font.menutitle_font, option4color, 55 * 3)
    # sc.draw_centertext('>>> currently doing gui, pls use space to start <<<', font.gui_font, font.GREY , 220)  


