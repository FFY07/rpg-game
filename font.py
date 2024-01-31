import pygame

pygame.init()

#game log font size
game_log_font = pygame.font.SysFont("arial", 15)

#define colours
RED = (255,0,0) 
GREEN = (0,255,0)
#define colours
TEXT_COL = (255,255,255)
YELLOW = (255,255,51)
grey = (96,96,96)
black = (0,0,0)

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