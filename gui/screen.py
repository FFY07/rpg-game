'''

(This file is use for screen , draw function )
(note: I import screen as sc )

'''

import pygame

import resources.font as font
import resources.sound as sound
import resources.image as image

pygame.init()

#game window
BOTTOM_PANEL = 150
SCREEN_WIDTH = 800                       
SCREEN_HEIGHT = 400 + BOTTOM_PANEL 

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("RPG GAME")

#load image

background_img = image.background_img
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH,(SCREEN_HEIGHT-BOTTOM_PANEL)))

panel_img = image.panel_img
panel_img = pygame.transform.scale(panel_img, (SCREEN_WIDTH,BOTTOM_PANEL))

input_rect = pygame.Rect(350,200,140,32)
inputgame_rect = pygame.Rect(150,7,140,32)
input2_rect = pygame.Rect(350,300,140,32)

#function for drawing text
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

#function for draw background
def draw_bg():
    screen.blit(background_img,(0,0))

#function for draw panel
def draw_panel():
    '''draw rectangular panel'''
    screen.blit(panel_img,(0,SCREEN_HEIGHT - BOTTOM_PANEL))
  