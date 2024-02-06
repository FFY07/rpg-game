'''

list for pygame.Color  :^)
https://www.pygame.org/docs/ref/color_list.html


( This file is use to store all the color variable and font variable )

(import this file if you need to use any color/font )


'''

import pygame

pygame.init()

#game log font size
game_log_font = pygame.font.SysFont("arial", 15)

#define colours
RED = pygame.Color('red')
GREEN = pygame.Color('green')
TEXT_COL = pygame.Color('white')
YELLOW = pygame.Color('yellow')
GREY = pygame.Color('dimgray')
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')

#gui variable
gui_font = pygame.font.Font(None, 32)
menu_font = pygame.font.Font(None, 45)
menucontent_font = pygame.font.Font(None, 35)
menutitle_font = pygame.font.Font(None, 70)
#define font
font = pygame.font.SysFont("arialblack" , 40)
hp_font = pygame.font.SysFont("freesansbold", 26)
smaller_gui_font= pygame.font.SysFont("arial", 15)


#input variable (start menu)
base_font = pygame.font.Font(None, 32)
input_hp_font = pygame.font.Font(None, 26)

input_text1, input_text2 = '', ''


color_active = pygame.Color('white')
color_passive = pygame.Color('gray15')
