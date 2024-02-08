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
SCREEN_WIDTH = 1000                      
SCREEN_HEIGHT = 400 + BOTTOM_PANEL

# Lists of valid character coordinates
player_positions = [(300, 210), 
                   (230, 260), 
                   (160, 310)]

enemy_positions = [(720, 200),
                   (790, 250),
                   (860, 300)]

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("RPG GAME")

#load image
menubackground_img = image.menubackground_img
menubackground_img = pygame.transform.scale(menubackground_img, (SCREEN_WIDTH,SCREEN_HEIGHT))

background_img = image.background_img
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH,(SCREEN_HEIGHT-BOTTOM_PANEL)))

panel_img = image.panel_img
panel_img = pygame.transform.scale(panel_img, (SCREEN_WIDTH,BOTTOM_PANEL))
bigpanel_img = pygame.transform.scale(panel_img, (SCREEN_WIDTH,SCREEN_HEIGHT))

input_rect = pygame.Rect(350,200,140,32)
inputgame_rect = pygame.Rect(150,7,140,32)
input2_rect = pygame.Rect(350,300,140,32)

#function for drawing text

# REPLACE THIS WITH NEW CLASS
def draw_text(text, font, color, x, y):
    # True = Antialiasing (smooth edges)
    img = font.render(text, True, color)
    screen.blit(img,(x, y))

#function for drawing text also but centre
def draw_centertext(text, font, color, y):
    text = font.render(text, True, color)
    text_rect = text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y))
    screen.blit(text, text_rect)

def draw_menubg():
    screen.blit(menubackground_img,(0,0))

#function for draw background
def draw_bg():
    screen.blit(background_img,(0,0))

def draw_optionbg():
    screen.blit(bigpanel_img,(0,0))

#function for draw panel
def draw_panel():
    '''draw rectangular panel'''
    screen.blit(panel_img,(0,SCREEN_HEIGHT - BOTTOM_PANEL))
  