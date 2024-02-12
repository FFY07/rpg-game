'''
This is for me to hardcore all the drawing thing in the menu

'''

from pathlib import Path
import pygame
import gui.screen as sc
import resources.font as font

# sc.screen = pygame.display.set_mode ((1000, 550))
pygame.display.set_caption("Testing menu for character creation")
clock = pygame.time.Clock()
FPS = 60

color_active = pygame.Color('white')
color_passive = pygame.Color('gray15')
BLACK = pygame.Color('black')
input_rect = pygame.Rect(350,200,140,32)
test1_rect = pygame.Rect(50,80,250,400)
test2_rect = pygame.Rect(375,80,250,400)
test3_rect = pygame.Rect(700,80,250,400) # x, y, w, h

option1 = True
option2 = False
option3 = False
bigsquare1 = color_passive
bigsquare2 = color_passive
bigsquare3 = color_passive
title_text = '[ Create Your Character ]'

text1 = 'Player 1'
text2 = 'Player 2'
text3 = 'Player 3' 

start_text = 'Begin your adventure..'
start_rect = pygame.Rect(700,500,140,32)
run  = True

knightimg = pygame.image.load(f"{Path('resources/picture/Knight/idle/1.png')}")
knightimg = pygame.transform.scale(knightimg, (90,90))
while run:
    pygame.display.update()
    clock.tick(FPS)
    sc.screen.fill((0, 0, 0))
    sc.draw_centertext(title_text, font.menu_font, font.WHITE, -230)

    # 3 main square
    pygame.draw.rect(sc.screen, bigsquare1, test1_rect, 1)
    pygame.draw.rect(sc.screen, bigsquare2, test2_rect, 1)
    pygame.draw.rect(sc.screen, bigsquare3, test3_rect, 1)
    
    #line 
    pygame.draw.line(sc.screen, color_active, (50, 130), (300, 130), 1)
    pygame.draw.line(sc.screen, color_active, (375, 130), (625, 130), 1)
    pygame.draw.line(sc.screen, color_active, (700, 130), (950, 130), 1)  
    # draw player 1,2,3
    sc.draw_text(text1, font.base_font, font.WHITE, 130, 100)
    sc.draw_text(text2, font.base_font, font.WHITE, 460, 100)
    sc.draw_text(text3, font.base_font, font.WHITE, 780, 100)

    #draw knight
    sc.screen.blit(knightimg, (120,140))   #120 - base 50 = gap 70
    sc.screen.blit(knightimg, ((375+70),140))         
    sc.screen.blit(knightimg, (770,140))


    #  start adventure
    pygame.draw.rect(sc.screen, color_active, start_rect, 2)
    text_surface = font.base_font.render(start_text, True, (255, 255, 255))
    sc.screen.blit(text_surface, (start_rect.x + 5, start_rect.y + 5 ))
    start_rect.w = max(100,text_surface.get_width() + 10)

    if option1 == True:
        bigsquare1 = color_active
    else:
        bigsquare2 = color_passive
    if option2 == True:
        bigsquare2 = color_active
    else:
        bigsquare2 = color_passive
    if option3 == True:
        bigsquare3 = color_active
    else:
        bigsquare3 = color_passive





    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_DOWN:
                if option1 == True:
                    option1 = False
                    option2 = True
                if option2 == True:
                    option2 = False
                    option3 = True
                if option3 == True:
                    option3 = False
                    option1 = True

        if event.type ==  pygame.QUIT:
            run = False

pygame.quit()