import random

import pygame

import button
import classes
import font
import screen as sc
import gamelog

pygame.init()

clock = pygame.time.Clock()
FPS = 60
 

#music
music = pygame.mixer.music.load('music/Fantasy RPG Music Pack Vol.3/Tracks/mp3/Fx 1.mp3')
pygame.mixer_music.play(-1)

#define game variables

game_paused = False
menu_state = 0  # 0 : main , 1:start, 2:option, 3:play

current_fighter = 1
total_fighter = 3
action_cooldown = 0
action_wait_time = 90
attack = False
clicked = False
game_over = 0 #  -1:lose 1:win



ask_text = 'Name your character :'
ask1_rect = pygame.Rect(80,200,140,32) # x, y, w, h
ask2_text = 'Hope you enjoy :^)) :'
ask2_rect = pygame.Rect(80,300,140,32)
colorAskinput1 = pygame.Color('BLACK')
colorAskinput2 = pygame.Color('BLACK')

start_text = 'Begin your adventure..'
start_rect = pygame.Rect(500,500,140,32)



input1 = True
input2 = False
startbutton = False

color_attack = font.GREY
color_def = font.GREY
color_power = font.GREY
color_bandit1, color_bandit2 = font.GREY, font.GREY
attackTF = False
defenceTF = False
powerTF = False
bandit1gui = True
bandit2gui = False

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////[ IMAGE AND SOUND LOAD AREA ]////////////////////////////[ IMAGE AND SOUND LOAD AREA }//////////////////////////////////////[ IMAGE AND SOUND LOAD AREA ]/////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#load buttom images
resume_img = pygame.image.load('picture/button/resumebut.png')
resume_img = pygame.transform.scale(resume_img, (resume_img.get_width()*3 ,resume_img.get_height()*3))
option_img = pygame.image.load('picture/button/optionbut.png')
option_img = pygame.transform.scale(option_img, (option_img.get_width()*3 ,option_img.get_height()*3))
quit_img = pygame.image.load('picture/button/quitbut.png')
quit_img = pygame.transform.scale(quit_img, (quit_img.get_width()*3 ,quit_img.get_height()*3))
video_img = pygame.image.load('picture/button/videobut.png')
video_img = pygame.transform.scale(video_img, (video_img.get_width()*3 ,video_img.get_height()*3))
audio_img = pygame.image.load('picture/button/audiobut.png')
audio_img = pygame.transform.scale(audio_img, (audio_img.get_width()*3 ,audio_img.get_height()*3))
back_img = pygame.image.load('picture/button/backbut.png')
back_img = pygame.transform.scale(back_img, (back_img.get_width()*3 ,back_img.get_height()*3))

#create button instances
resume_button = button.Button(5, 180, resume_img, 1)
option_button = button.Button(270, 180, option_img, 1)
backoption_button = button.Button(250, 350, option_img, 1)
# quit_button = button.Button(530, 180, quit_img, 1)
video_button = button.Button(150, 40, video_img, 1)
audio_button = button.Button(350, 40, audio_img, 1)
back_button = button.Button(530, 180, back_img, 1)

#??



#load image
#load victory and defeat images
victory_img = pygame.image.load('picture/victory.png')
victory_img = pygame.transform.scale(victory_img, (600,500))
defeat_img = pygame.image.load('picture/defeat.png')
defeat_img = pygame.transform.scale(defeat_img, (600,500))

#sword pointer image
sword_img = pygame.image.load('picture/icon(trans)/PineTools.com_files/row-6-column-5.png').convert_alpha()

#sword sound
attack_sfx = pygame.mixer.Sound('music/unsheath_sword-6113.mp3')


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////[ DEF FUNCTION ]///////////////////////////////////////////[ DEF FUNCTION ]////////////////////////////////////////////[ DEF FUNCTION ]/////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



                            

   #draw the bandit names on the sc.screen (still needs work -haarith)
def draw_bandit_names():
    for count, bandit in enumerate(bandit_list):
        sc.draw_text(bandit.name, font.hp_font, pygame.Color("aliceblue"), 550, (12) + count * 42)

class healthbar():
    def __init__(self,x,y,hp,max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self,hp):
        #update with new health
        self.hp = hp
        #calculate health ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(sc.screen,font.RED,( self.x, self.y, 150, 20))
        pygame.draw.rect(sc.screen,font.GREEN,( self.x, self.y, 150 * ratio , 20))

    

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////[ GAME STAT ]///////////////////////////////////////////[ GAME STAT ]/////////////////////////////////////////////////////[ GAME STAT ]/////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
knight = classes.fighter(200, 260, font.input_text1,'knightpic', 40, 10, 6)
randomAI = str(random.randint(10,99))
randomAI2 = str(random.randint(10,99)) 

bandit1 = classes.fighter(550, 200 , '(AI ' + randomAI + ')', 'banditpic', 20, 10 , 6)
bandit2 = classes.fighter(650, 250 ,'(AI ' + randomAI2 + ')', 'banditpic', 20, 6 , 6)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

knight_health_bar = healthbar(80, 30 , knight.hp, knight.max_hp)
bandit1_health_bar = healthbar(550,30 , bandit1.hp, bandit1.max_hp)
bandit2_health_bar = healthbar(550,70, bandit2.hp, bandit2.max_hp)


knight_health_bar.draw(knight.hp)
bandit1_health_bar.draw(bandit1.hp)
bandit2_health_bar.draw(bandit2.hp)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////[ GAME START ]///////////////////////////////////////////[ GAME START ]//////////////////////////////////////////////////[ GAME START ]/////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



#use to loop the game
run = True   
while run: 


    clock.tick(FPS)
    #main
    if menu_state ==  0 :            # 0 : main , 1:start,2pause 3:option, 4:play, 5:gameover 6 attack
        sc.draw_main()
    #start menu
    if menu_state == 1 :
        sc.screen.fill((0, 0, 0))

        if input1 == True:
            colorinput1 = font.color_active
        else:
            colorinput1 = font.color_passive
        if input2 == True:
            colorinput2 = font.color_active
        else:
            colorinput2 = font.color_passive
        if startbutton == True:
            colorstartbutton = font.color_active
        else:
            colorstartbutton = font.color_passive
        #input 1
        pygame.draw.rect(sc.screen, colorinput1, sc.input_rect, 2)
        text_surface = font.base_font.render(font.input_text1, True, (255, 255, 255))
        sc.screen.blit(text_surface, (sc.input_rect.x + 5, sc.input_rect.y + 5 ))
        sc.input_rect.w = max(100,text_surface.get_width() + 10)
        #ask 1
        pygame.draw.rect(sc.screen, colorAskinput1, ask1_rect, 0)
        text_surface = font.base_font.render(ask_text, True, (255, 255, 255))
        sc.screen.blit(text_surface, (ask1_rect.x + 5, ask1_rect.y + 5 ))
        ask1_rect.w = max(100,text_surface.get_width() + 10)
        #input 2
        pygame.draw.rect(sc.screen, colorinput2, sc.input2_rect, 2)
        text_surface = font.base_font.render(font.input_text2, True, (255, 255, 255))
        sc.screen.blit(text_surface, (sc.input2_rect.x + 5, sc.input2_rect.y + 5 ))
        sc.input2_rect.w = max(100,text_surface.get_width() + 10)
        #ask 2
        pygame.draw.rect(sc.screen, colorAskinput2, ask2_rect, 0)
        text_surface = font.base_font.render(ask2_text, True, (255, 255, 255))
        sc.screen.blit(text_surface, (ask2_rect.x + 5, ask2_rect.y + 5 ))
        ask2_rect.w = max(100,text_surface.get_width() + 10)
        #start 
        pygame.draw.rect(sc.screen, colorstartbutton, start_rect, 2)
        text_surface = font.base_font.render(start_text, True, (255, 255, 255))
        sc.screen.blit(text_surface, (start_rect.x + 5, start_rect.y + 5 ))
        start_rect.w = max(100,text_surface.get_width() + 10)
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if menu_state == 1:
                
                    if event.key == pygame.K_RETURN:
                        if input1 == True:
                            input1 = False
                            input2 =True
                        elif input2 == True:
                            input2 = False
                            startbutton = True
                        elif startbutton == True:
                            menu_state = 4
                            attackTF = True
                            music = pygame.mixer.music.load('music/Fantasy RPG Music Pack Vol.3/Tracks/mp3/Action 3.mp3')
                            pygame.mixer_music.play(-1)
                            
                    elif event.key == pygame.K_DOWN:
                        if input1 == True:
                            input1 = False
                            input2 =True
                        elif input2 == True:
                            input2 = False
                            startbutton = True
                        elif startbutton == True:
                            startbutton = False
                            input1 = True
                    elif event.key == pygame.K_UP:
                        if input1 == True:
                            input1 = False
                            startbutton =True
                        elif input2 == True:
                            input2 = False
                            input1 = True
                        elif startbutton == True:
                            startbutton = False
                            input2 = True
                            
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

                            knight = classes.fighter(200, 260, '(' + font.input_text1 + ')','knightpic', 40, 10, 6)   
                    if input2 == True:
                        if event.key == pygame.K_BACKSPACE:
                            font.input_text2 = font.input_text2[0:-1]

                        else:
                            press = pygame.key.get_pressed()
                            for i in range( pygame.K_a, pygame.K_z + 1 ): 
                                if press[i] == True:
                                    font.input_text2 += pygame.key.name(i)
                            for i in range( pygame.K_0, pygame.K_9 + 1 ): 
                                if press[i] == True:
                                    font.input_text2 += pygame.key.name(i)
    #pause menu
    if menu_state == 2 :
        sc.screen.fill((0, 0, 0))

        pygame.mouse.set_visible(True)
        #draw pause sc.screen button
        if resume_button.draw(sc.screen):
             menu_state = 4
        if option_button.draw(sc.screen):
             menu_state = 3
        if back_button.draw(sc.screen):
            menu_state = menu_state - 2
        # check if the option menu is open
    #option menu        
    if menu_state == 3 :
        sc.screen.fill((0, 0, 0))

        pygame.mouse.set_visible(True)
        if video_button.draw(sc.screen):
            print('i didnt make a code for Video Settings :3')
        if audio_button.draw(sc.screen):
            print('i didnt make a code for music Settings :3')
        if backoption_button.draw(sc.screen):
            menu_state = menu_state - 1
    #game menu
    if menu_state == 4:

        #draw background
        sc.draw_bg()

        #draw panel
        sc.draw_panel()
        sc.draw_text(f'{knight.name} HP:{knight.hp}',font.hp_font, font.RED, 80, 12)

        #bandit stats
        for count, i in enumerate(bandit_list):
            #show name and health
            sc.draw_text(f'{i.name} HP: {i.hp}',font.hp_font, font.RED, 550, (12) + count  * 42)


        #draw health bar
        knight_health_bar.draw(knight.hp)
        bandit1_health_bar.draw(bandit1.hp)
        bandit2_health_bar.draw(bandit2.hp)

        #GUI panel
        if attackTF == True:
            color_attack = font.BLACK
        else:
            color_attack = font.GREY

        if defenceTF == True:
            color_def = font.BLACK
        else:
            color_def = font.GREY

        if powerTF == True:
            color_power = font.BLACK
        else:
            color_power = font.GREY
        
        #attack 
        sc.draw_text('Attack', font.gui_font, color_attack , 80 , 430 )
        sc.draw_text('(press E to select, Q to go back)', font.smaller_gui_font, color_attack, 156, 434)

        #defence 
        sc.draw_text('Magic', font.gui_font, color_def , 80 , 460 )
        sc.draw_text('(press E to select)', font.smaller_gui_font,color_def , 156, 464)

        #magic
        sc.draw_text('Surrender', font.gui_font, color_power , 80 , 490 )
        sc.draw_text('(press E to select)', font.smaller_gui_font, color_power, 200, 494)

         #draw fighter
        knight.update()
        knight.draw()
        for bandit in bandit_list:
            bandit.update()
            bandit.draw()

         #draw the damage text 
        classes.damage_text_group.update()
        classes.damage_text_group.draw(sc.screen)


        # #control player action
        # #reset action variables
        # attack = False
        # target = None 
        # #make sure mouse is visible
        # pygame.mouse.set_visible(True)
        # pos = pygame.mouse.get_pos()
        # for count, bandit in enumerate(bandit_list):
        #     if bandit. rect.collidepoint(pos):
        #         #hide mouse
        #         pygame.mouse.set_visible(False)
        #         #show sword in place of mouse cursor 
        #         sc.screen.blit(sword_img, pos)
        #         if clicked == True and bandit.alive == True:
        #             attack = True 
        #             target = bandit_list[count]
            
    # if game_over == 0:
        #player action
        if knight.alive == True:
            if current_fighter == 1:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    #look for player action
                    #attack
                    if attack == True and target != None:
                        knight.attack(target)
                        attack_sfx.play()
                        target = None
                        current_fighter += 1
                        action_cooldown = 0
                
        else:
            game_over = -1
        #enemy action
        for count, bandit in enumerate(bandit_list):
            if current_fighter == 2 + count:
                if bandit.alive == True:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        #attack
                        bandit.attack(knight)
                        attack_sfx.play()
                        current_fighter += 1
                        action_cooldown = 0
                else:
                    current_fighter += 1

        #if all fighter have had a turn than reset
        if current_fighter > total_fighter:
            current_fighter = 1

        #check if all bandits are dead
        alive_bandits = 0
        for bandit in bandit_list:
            if bandit.alive == True:
                alive_bandits += 1
        if alive_bandits == 0:
            game_over = 1
                
         #check if game is over
        if game_over != 0:
            music = pygame.mixer.music.load('music/Fantasy RPG Music Pack Vol.3/Tracks/mp3/Fx 3.mp3')
            pygame.mixer_music.play(-1)
            if game_over == 1:
                sc.screen.blit(victory_img,(160,50))
                    
                    
            if game_over == -1:
                sc.screen.blit(defeat_img,(160,50))   

        
    #function to restart the game (add by haarith)
            menu_state = 5
            

    if menu_state == 4:  # state where game is active
        gamelog.draw_game_logs()

    if menu_state == 5:
        #display game over message
        small_font = pygame.font.Font(None, 40) 
        if game_over == 1:
            sc.draw_text('You win. Press R to replay or Q to quit', small_font, font.TEXT_COL, 100, sc.SCREEN_HEIGHT // 2)
        if game_over == -1:
            sc.draw_text('Game over. Press R to replay or Q to quit', small_font, font.TEXT_COL, 100, sc.SCREEN_HEIGHT // 2)
        #check for user input
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    #reset game
                    menu_state = 0
                    #reset game Variable
                    game_over = 0
                    pygame.mouse.set_visible(True)  #cursor

                    # Reset game variables
                    knight = classes.fighter(200, 260, font.input_text1,'knightpic', 40, 10, 6)
                    bandit1 = classes.fighter(550, 200 , 'AI ' + randomAI, 'banditpic', 20, 10 , 6)
                    bandit2 = classes.fighter(650, 250 ,'AI ' + randomAI2, 'banditpic', 20, 6 , 6)

                    bandit_list = []
                    bandit_list.append(bandit1)
                    bandit_list.append(bandit2)

                    knight_health_bar = healthbar(80, 30 , knight.hp, knight.max_hp)
                    bandit1_health_bar = healthbar(550,30 , bandit1.hp, bandit1.max_hp)
                    bandit2_health_bar = healthbar(550,70, bandit2.hp, bandit2.max_hp)
                    
                elif event.key == pygame.K_q:
                    run = False

    #quit the game
    for event in pygame.event.get(): 
        
        if event.type == pygame.KEYDOWN:
            if menu_state == 0:
                if event.key == pygame.K_SPACE:
                    menu_state = 1
                    input1 = True

            if menu_state == 4:
                if event.key == pygame.K_DOWN:
                    if attackTF == True:
                        attackTF = False 
                        defenceTF = True
                    elif defenceTF == True:
                        defenceTF = False
                        powerTF = True
                    elif powerTF == True:
                       powerTF = False
                       attackTF = True 
                elif event.key == pygame.K_UP:
                    if attackTF == True:
                        attackTF = False
                        powerTF =True
                    elif defenceTF == True:
                        defenceTF = False
                        attackTF = True
                    elif powerTF == True:
                        powerTF = False
                        defenceTF = True
                elif event.key == pygame.K_e:
                    if attackTF == True and defenceTF == False and powerTF == False : 
                        menu_state = 6
                    elif powerTF == True and attackTF == False and defenceTF == False:
                        game_over = -1
                    elif defenceTF == True and attackTF == False and powerTF == False:
                        menu_state = 'easter'
                        
            if menu_state == 6:
                sc.screen.blit(sc.panel_img,(0,sc.SCREEN_HEIGHT - sc.BOTTOM_PANEL))
                sc.draw_bg()
                for bandit in bandit_list:
                    bandit.update()
                    bandit.draw()
                sc.draw_text('(AI ' + randomAI + ')', font.gui_font, color_bandit1 , 80 , 430 )
                sc.draw_text('(AI ' + randomAI2 + ')', font.gui_font, color_bandit2 , 80 , 460 )

                
                if bandit1gui == True:
                    color_bandit1 = font.BLACK
                else:
                    color_bandit1 = font.GREY
                if bandit2gui == True:
                    color_bandit2 = font.BLACK
                else:
                    color_bandit2 = font.GREY
                
                if event.key == pygame.K_RETURN:
                    if bandit1gui == True and bandit.alive == True:
                        target = bandit1
                        attack = True
                        menu_state = 4
                    elif bandit2gui == True and bandit.alive == True:
                        target = bandit2
                        attack = True
                        menu_state = 4
                elif event.key == pygame.K_DOWN:
                    if bandit1gui == True:
                        bandit1gui = False
                        bandit2gui = True
                    elif bandit2gui == True:
                        bandit2gui = False
                        bandit1gui = True
                elif event.key == pygame.K_UP:
                    if bandit1gui == True:
                        bandit1gui = False
                        bandit2gui = True
                    elif bandit2gui == True:
                        bandit2gui = False
                        bandit1gui = True
                elif event.key == pygame.K_q:
                    menu_state =4

            if menu_state == 'easter':
                music = pygame.mixer.music.load('music/Dancin-(Krono-Remix)(PaglaSongs).mp3')
                music_run = True
                pygame.mixer_music.play(-1)
                for i in range(1,71):
                    easteregg_img = pygame.image.load(f'picture/milo/milo ({i}).jpg')
                    sc.screen.blit(easteregg_img, (100,100))
                    pygame.display.flip()
                    clock.tick(24)
                for i in range(1,71):
                    easteregg_img = pygame.image.load(f'picture/milo/milo ({i}).jpg')
                    sc.screen.blit(easteregg_img, (100,100))
                    pygame.display.flip()
                    clock.tick(24)
                for i in range(1,71):
                    easteregg_img = pygame.image.load(f'picture/milo/milo ({i}).jpg')
                    sc.screen.blit(easteregg_img, (100,100))
                    pygame.display.flip()
                    clock.tick(24)
                
                # sc.screen.fill((0, 0, 0))
                menu_state = 4
                

            if menu_state != (0 and 1) :
                if event.key == pygame.K_ESCAPE:
                    if menu_state == 2:    #if pause than game
                     menu_state = 4
                    else:
                        menu_state = 2
            if menu_state == 1:
                    if event.key == pygame.K_KP_ENTER:
                        menu_state = 4
        if event.type ==  pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

    pygame.display.update()



pygame.quit()