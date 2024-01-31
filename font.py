import pygame

pygame.init()

#game log font size
game_log_font = pygame.font.SysFont("arial", 15)

#define colours
RED = pygame.Color('red')
GREEN = pygame.Color('green')
TEXT_COL = pygame.Color('white')
YELLOW = pygame.Color('yellow')
grey = pygame.Color('dimgray')
black = pygame.Color('black')


#gui variable
gui_font = pygame.font.Font(None, 32)
menu_font = pygame.font.Font(None, 55)

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
colorinput1, colorinput2, colorstartbutton = color_passive, color_passive, color_passive