'''

(This file is use for screen , draw function )
(note: I import screen as sc )

'''


import pygame
import font

pygame.init()

#game window
BOTTOM_PANEL = 150
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400 + BOTTOM_PANEL

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("RPG GAME")


#load image
#background image
background_img = pygame.image.load('picture/background3.png')
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH,(SCREEN_HEIGHT-BOTTOM_PANEL)))


#panel image
panel_img = pygame.image.load('picture/UI board Large  parchment.png')
panel_img = pygame.transform.scale(panel_img, (SCREEN_WIDTH,BOTTOM_PANEL))

input_rect = pygame.Rect(350,200,140,32)
inputgame_rect = pygame.Rect(150,7,140,32)
input2_rect = pygame.Rect(350,300,140,32)

music = pygame.mixer.music.load('music/Fantasy RPG Music Pack Vol.3/Tracks/mp3/Ambient 2.mp3')

#function for drawing text
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

#function for draw background
def draw_bg():
    screen.blit(background_img,(0,0))
def draw_main():
    screen.fill((0, 0, 0))
    pygame.mixer_music.play(-1, 2)
    draw_text ('PSB PROGRAMMING ASSIGNMENT', font.menu_font, font.TEXT_COL,80 , SCREEN_HEIGHT / 2 - 120)
    draw_text('TURN BASED RPG', font.menu_font, font.TEXT_COL, 220, SCREEN_HEIGHT / 2 - 80)
    draw_text('>>> PRESS SPACEBAR TO START THE GAME <<<', font.gui_font, font.YELLOW , 120 , SCREEN_HEIGHT/ 2 + 150)

#function for draw panel
def draw_panel():
    '''draw rectangular panel'''
    screen.blit(panel_img,(0,SCREEN_HEIGHT - BOTTOM_PANEL))
  