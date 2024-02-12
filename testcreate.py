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

pygame.mixer.music.load('resources/sound/driftveil-city-theme-pokémon-black-&-white-(toothless-dancing)-made-with-Voicemod.mp3')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.1)

color_active = pygame.Color('white')
color_passive = pygame.Color('gray15')
BLACK = pygame.Color('black')
input1_rect = pygame.Rect(80, 280, 170, 32)
input2_rect = pygame.Rect(415, 280, 170, 32)
input3_rect = pygame.Rect(730, 280, 170, 32)
test1_rect = pygame.Rect(50, 80, 250, 380)
test2_rect = pygame.Rect(375, 80, 250, 380)
test3_rect = pygame.Rect(700, 80, 250, 380) # x, y, w, h

class1_rect = pygame.Rect(80, 370, 170, 32)
class2_rect = pygame.Rect(415, 370, 170, 32)
class3_rect = pygame.Rect(730, 370, 170, 32)
option1 = True
option2 = False
option3 = False
bigsquare1 = color_passive
bigsquare2 = color_passive
bigsquare3 = color_passive


input1 = False
input2 = False
input3 = False
input1color = color_passive
input2color = color_passive
input3color = color_passive

class1 = False
class2 = False
class3 = False
class1color = color_passive
class2color = color_passive
class3color = color_passive

title_text = '[ Create Your Character ]'

# input_text1, input_text2, input_text3 = '', '', ''


text1 = 'Player 1'
text2 = 'Player 2'
text3 = 'Player 3' 

class_text1 = 'Knight'
class_text2 = 'Knight'
class_text3 = 'Knight'

start_text = 'Begin your adventure..'
start_rect = pygame.Rect(700,500,140,32)
run  = True

knightimg = pygame.image.load(f"{Path('resources/picture/Knight/idle/1.png')}")
knightimg = pygame.transform.scale(knightimg, (90,90))
reaperimg = pygame.image.load(f"{Path('resources/picture/Reaper/idle/1.png')}")
reaperimg = pygame.transform.scale(reaperimg, (90,90))
tankimg = pygame.image.load(f"{Path('resources/picture/banditpic/idle/1.png')}")
tankimg = pygame.transform.scale(tankimg, (90,90))
while run:
    menustate = 'create'

    pygame.display.update()
    clock.tick(FPS)
    if menustate == 'create':
        sc.screen.fill((0, 0, 0))
        sc.draw_centertext(title_text, font.menu_font, font.WHITE, -230)

        if option1 == True:
            bigsquare1 = color_active
        else:
            bigsquare1 = color_passive
        if option2 == True:
            bigsquare2 = color_active
        else:
            bigsquare2 = color_passive
        if option3 == True:
            bigsquare3 = color_active
        else:
            bigsquare3 = color_passive

        if input1 == True:
            input1color = color_active
        else:
            input1color = color_passive
        if input2 == True:
            input2color = color_active
        else:
            input2color = color_passive
        if input3 == True:
            input3color = color_active
        else:
            input3color = color_passive

        if class1 == True:
            class1color = color_active
        else:
            class1color = color_passive
        if class2 == True:
            class2color = color_active
        else:
            class2color = color_passive
        if class3 == True:
            class3color = color_active
        else:
            class3color = color_passive

        if class_text1 == 'Knight':
            sc.screen.blit(knightimg, (120,140))
        elif class_text1 == 'Reaper':
            sc.screen.blit(reaperimg, (120,140))
        elif class_text1 == 'Tank':
            sc.screen.blit(tankimg, (120,140))
        if class_text2 == 'Knight':
            sc.screen.blit(knightimg, ((375+70),140))
        elif class_text2 == 'Reaper':
            sc.screen.blit(reaperimg, ((375+70),140))
        elif class_text2 == 'Tank':
            sc.screen.blit(tankimg, ((375+70),140))
        if class_text3 == 'Knight':
            sc.screen.blit(knightimg, (770,140))
        elif class_text3 == 'Reaper':
            sc.screen.blit(reaperimg, (770,140))
        elif class_text3 == 'Tank':
            sc.screen.blit(tankimg, (770,140))
        # 3 main square
        pygame.draw.rect(sc.screen, bigsquare1, test1_rect, 3)
        pygame.draw.rect(sc.screen, bigsquare2, test2_rect, 3)
        pygame.draw.rect(sc.screen, bigsquare3, test3_rect, 3)
        
        #Upper line 
        pygame.draw.line(sc.screen, bigsquare1, (50, 130), (300, 130), 1)
        pygame.draw.line(sc.screen, bigsquare2, (375, 130), (625, 130), 1)
        pygame.draw.line(sc.screen, bigsquare3, (700, 130), (950, 130), 1)  

        #draw player 1,2,3
        sc.draw_text(text1, font.base_font, bigsquare1, 130, 100)
        sc.draw_text(text2, font.base_font, bigsquare2, 460, 100)
        sc.draw_text(text3, font.base_font, bigsquare3, 780, 100)

        #draw knight
        # # sc.screen.blit(knightimg, (120,140))   #120 - base 50 = gap 70
        # sc.screen.blit(knightimg, ((375+70),140))         
        # sc.screen.blit(knightimg, (770,140))

        #Lower line
        pygame.draw.line(sc.screen, bigsquare1, (50, 240), (300, 240), 1)
        pygame.draw.line(sc.screen, bigsquare2, (375, 240), (625, 240), 1)
        pygame.draw.line(sc.screen, bigsquare3, (700, 240), (950, 240), 1) 

        #draw name
        sc.draw_text('Name:', font.base_font, bigsquare1, 130, 250)
        sc.draw_text('Name:', font.base_font, bigsquare2, 460, 250)
        sc.draw_text('Name:', font.base_font, bigsquare3, 780, 250)

        #input 1
        pygame.draw.rect(sc.screen, input1color, input1_rect, 1)
        text_surface = font.base_font.render(font.input_text1, True, input1color)
        sc.screen.blit(text_surface, (input1_rect.x + 5, input1_rect.y + 5 ))
        sc.input_rect.w = max(100,text_surface.get_width() + 10)

        #input 2
        pygame.draw.rect(sc.screen, input2color, input2_rect, 1)
        text_surface = font.base_font.render(font.input_text2, True, input2color)
        sc.screen.blit(text_surface, (input2_rect.x + 5, input2_rect.y + 5 ))
        sc.input_rect.w = max(100,text_surface.get_width() + 10)
        #input 3
        pygame.draw.rect(sc.screen, input3color, input3_rect, 1)
        text_surface = font.base_font.render(font.input_text3, True, input3color)
        sc.screen.blit(text_surface, (input3_rect.x + 5, input3_rect.y + 5 ))
        sc.input_rect.w = max(100,text_surface.get_width() + 10)
        


        #draw select class
        sc.draw_text('[ Class ]', font.base_font, class1color, 120, 330)
        sc.draw_text('[ Class ]', font.base_font, class2color, 450, 330)
        sc.draw_text('[ Class ]', font.base_font, class3color, 770, 330)

        pygame.draw.rect(sc.screen, class1color, class1_rect, 1)
        text_surface = font.base_font.render(class_text1, True, class1color)
        sc.screen.blit(text_surface, (class1_rect.x + 50, class1_rect.y + 5 ))
        sc.input_rect.w = max(100,text_surface.get_width() + 10)

        pygame.draw.rect(sc.screen, class2color, class2_rect, 1)
        text_surface = font.base_font.render(class_text2, True, class2color)
        sc.screen.blit(text_surface, (class2_rect.x + 50, class2_rect.y + 5 ))
        sc.input_rect.w = max(100,text_surface.get_width() + 10)

        pygame.draw.rect(sc.screen, class3color, class3_rect, 1)
        text_surface = font.base_font.render(class_text3, True, class3color)
        sc.screen.blit(text_surface, (class3_rect.x + 50, class3_rect.y + 5 ))
        sc.input_rect.w = max(100,text_surface.get_width() + 10)




        #  start adventure
        pygame.draw.rect(sc.screen, color_active, start_rect, 2)
        text_surface = font.base_font.render(start_text, True, (255, 255, 255))
        sc.screen.blit(text_surface, (start_rect.x + 5, start_rect.y + 5 ))
        start_rect.w = max(100,text_surface.get_width() + 10)


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if menustate == 'create':
                if event.key == pygame.K_RETURN:
                    if option1 == True:
                        input1 = True
                    elif option2 == True:
                        input2 = True
                    elif option3 == True:
                        input3 = True
                    if class1 == True:
                        class1 = False
                        option1 = True
                    if class2 == True:
                        class2 = False
                        option2 = True
                    if class3 == True:
                        class3 = False
                        option3 = True
                elif event.key == pygame.K_RIGHT:
                    if option1 == True:
                        option1 = False
                        option2 = True
                        input1 = False
                        class1 = False
                    elif option2 == True:
                        option2 = False
                        option3 = True
                        input2 = False
                        class2 = False
                    elif option3 == True:
                        option3 = False
                        option1 = True
                        input3 = False
                        class3 = False

                    if class1 == True:
                        if class_text1 == 'Knight':
                            class_text1 = 'Reaper'
                        elif class_text1 == 'Reaper':
                            class_text1 = 'Tank'
                        elif class_text1 == 'Tank':
                            class_text1 = 'Knight'
                    if class2 == True:
                        if class_text2 == 'Knight':
                            class_text2 = 'Reaper'
                        elif class_text2 == 'Reaper':
                            class_text2 = 'Tank'
                        elif class_text2 == 'Tank':
                            class_text2 = 'Knight'
                    if class3 == True:
                        if class_text3 == 'Knight':
                            class_text3 = 'Reaper'
                        elif class_text3 == 'Reaper':
                            class_text3 = 'Tank'
                        elif class_text3 == 'Tank':
                            class_text3 = 'Knight'
                elif event.key == pygame.K_LEFT:
                    if option1 == True:
                        option1 = False
                        option3 = True
                        input1 = False
                        class1 = False
                    elif option2 == True:
                        option2 = False
                        option1 = True
                        input2 = False
                        class2 = False
                    elif option3 == True:
                        option3 = False
                        option2 = True
                        input3 = False
                        class3 = False

                    if class1 == True:
                        if class_text1 == 'Knight':
                            class_text1 = 'Tank'
                        elif class_text1 == 'Reaper':
                            class_text1 = 'Knight'
                        elif class_text1 == 'Tank':
                            class_text1 = 'Reaper'
                    if class2 == True:
                        if class_text2 == 'Knight':
                            class_text2 = 'Tank'
                        elif class_text2 == 'Reaper':
                            class_text2 = 'Knight'
                        elif class_text2 == 'Tank':
                            class_text2 = 'Reaper'
                    if class3 == True:
                        if class_text3 == 'Knight':
                            class_text3 = 'Tank'
                        elif class_text3 == 'Reaper':
                            class_text3 = 'Knight'
                        elif class_text3 == 'Tank':
                            class_text3 = 'Reaper'
                elif event.key == pygame.K_DOWN:
                    if option1 == True:
                        if input1 == True:
                            input1 = False
                            option1 = False
                            class1 = True
                        elif class1 == True:
                            class1 = False
                            input1 = True
                    if option2 == True:
                        if input2 == True:
                            input2 = False
                            option2 = False
                            class2 = True
                        elif class2 == True:
                            class2 = False
                            input2 = True
                    if option3 == True:
                        if input3 == True:
                            input3 = False
                            option3 = False
                            class3 = True
                        elif class3 == True:
                            class3 = False
                            input3 = True
                if input1 == True:
                    if event.key == pygame.K_BACKSPACE:
                        font.input_text1 = font.input_text1[0:-1]
                    else:
                        press1 = pygame.key.get_pressed()       
                        for i in range( pygame.K_a, pygame.K_z + 1 ): 
                            if press1[i] == True:
                                font.input_text1 += pygame.key.name(i) 
                        for i in range( pygame.K_0, pygame.K_9 + 1 ): 
                            if press1[i] == True:
                                font.input_text1 += pygame.key.name(i)
                if input2 == True:
                    if event.key == pygame.K_BACKSPACE:
                        font.input_text2 = font.input_text2[0:-1]
                    else:
                        press1 = pygame.key.get_pressed()       
                        for i in range( pygame.K_a, pygame.K_z + 1 ): 
                            if press1[i] == True:
                                font.input_text2 += pygame.key.name(i) 
                        for i in range( pygame.K_0, pygame.K_9 + 1 ): 
                            if press1[i] == True:
                                font.input_text2 += pygame.key.name(i)
                if input3 == True:
                    if event.key == pygame.K_BACKSPACE:
                        font.input_text3 = font.input_text3[0:-1]
                    else:
                        press1 = pygame.key.get_pressed()       
                        for i in range( pygame.K_a, pygame.K_z + 1 ): 
                            if press1[i] == True:
                                font.input_text3 += pygame.key.name(i) 
                        for i in range( pygame.K_0, pygame.K_9 + 1 ): 
                            if press1[i] == True:
                                font.input_text3 += pygame.key.name(i)
        if event.type ==  pygame.QUIT:
            run = False

pygame.quit()