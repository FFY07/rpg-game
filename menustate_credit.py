import gui.screen as sc
import pygame
import resources.font as font

def draw_menu_credit():

    sc.screen.fill((0, 0, 0))
    sc.draw_centertext ('[ Credits ]', font.menu_font, font.YELLOW,- 220)
    sc.draw_centertext ('PSB INTRODUCTION TO PROGRAMMING ASSIGNMENT', font.menucontent_font, font.GREEN, - 180)
    sc.draw_centertext ('GAME CREATED BY (GROUP A1 ) ', font.menucontent_font, font.GREEN, - 150)

    sc.draw_centertext('[ Members ]', font.menu_font, font.YELLOW,- 110)
    sc.draw_centertext('Desmond Foo Fong Yoong (GL)', font.menucontent_font, font.WHITE,- 70)
    sc.draw_centertext('Haarith Bin Naguri Ibrahim', font.menucontent_font, font.WHITE,- 40)
    sc.draw_centertext('Haohong Luo', font.menucontent_font, font.WHITE,- 10)
    sc.draw_centertext('Qiao Er Kang', font.menucontent_font, font.WHITE, 20)
    sc.draw_centertext('Xu Xiang (Ye Xuxiang) Yap', font.menucontent_font, font.WHITE, 50)
    sc.draw_centertext('Yi Soon Pong', font.menucontent_font, font.WHITE, 80)

    sc.draw_centertext('[ Special Thanks ]', font.menu_font, font.YELLOW, 130)
    sc.draw_centertext('Rui Zheng Siah', font.menucontent_font, font.WHITE, 170)