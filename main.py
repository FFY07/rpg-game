import random
from pathlib import Path

import pygame

import classes
import resources.font as font
import resources as rsc
import gui.screen as sc
import gamelog
import gui.damagetext as dt

#menu
import menu_states.start as ms0
import menu_states.options as msoptions
import menu_states.game_options as msgameoptions
import menu_states.credits as mscredit
import menu_states.lazy as mssorry
pygame.init()

clock = pygame.time.Clock()
FPS = 60

#define game variables

game_paused = False
menu_state = -1  # 0 : main , 1:start, 2:option, 3:play
menu_brake = False

playerheart = 3  
current_fighter = 1
total_fighter = 4
action_cooldown = 0
action_wait_time = 90
attack = False
magic = False
clicked = False
game_over = 0 #  -1:lose 1:win



ask_text = 'Name your character :'
ask1_rect = pygame.Rect(80,200,140,32) # x, y, w, h
ask2_text = 'Hope you enjoy :^)) :'
ask2_rect = pygame.Rect(80,300,140,32)
colorAskinput1 = pygame.Color('BLACK')
colorAskinput2 = pygame.Color('BLACK')

start_text = 'Begin your adventure..'
start_rect = pygame.Rect(700,500,140,32)


option1 = False
option2 = False
option3 = False
option4 = False
option1color = font.GREY
option2color = font.GREY
option3color = font.GREY
option4color = font.GREY


input1 = True
input2 = False
startbutton = False

color_attack = font.GREY
color_def = font.GREY
color_power = font.GREY
color_bandit1, color_bandit2, color_bandit3 = font.GREY, font.GREY, font.GREY
attackTF = False
defenceTF = False
powerTF = False
bandit1gui = False
bandit2gui = False
bandit3gui = False

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
knight1 = classes.Fighter(300, 210, font.input_text1,'knightpic', 40, 20, 6)
knight2 = classes.Fighter(230, 260, '(test1)','knightpic', 40, 20, 6)
knight3 = classes.Fighter(160, 310, '(test2)','knightpic', 40, 20, 6)

ai1 = '(AI '  + str(random.randint(10,99)) + ')'
ai2 = '(AI '  + str(random.randint(10,99)) + ')' 
ai3 = '(AI '  + str(random.randint(10,99)) + ')'


bandit1 = classes.Fighter(720, 200 , ai1, 'reaperpic', 50 , 10, 6)   #x = base + 70 , = base  +50
bandit2 = classes.Fighter(790, 250 , ai2, 'banditpic', 20, 6 , 6)
bandit3 = classes.Fighter(860, 300 , ai3, 'banditpic', 20, 6 , 6)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)
bandit_list.append(bandit3)

knight_health_bar = healthbar(80, 30 , knight1.hp, knight1.max_hp)
knight2_health_bar = healthbar(80, 70 , knight2.hp, knight2.max_hp)
knight3_health_bar = healthbar(80, 110 , knight3.hp, knight3.max_hp)
bandit1_health_bar = healthbar(800,30 , bandit1.hp, bandit1.max_hp)
bandit2_health_bar = healthbar(800,70, bandit2.hp, bandit2.max_hp)
bandit3_health_bar = healthbar(800,110, bandit3.hp, bandit3.max_hp)

knight_health_bar.draw(knight1.hp)
knight2_health_bar.draw(knight2.hp)
knight3_health_bar.draw(knight3.hp)
bandit1_health_bar.draw(bandit1.hp)
bandit2_health_bar.draw(bandit2.hp)
bandit3_health_bar.draw(bandit3.hp)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////[ GAME START ]///////////////////////////////////////////[ GAME START ]//////////////////////////////////////////////////[ GAME START ]/////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#use to loop the game
run = True   
while run: 
    clock.tick(FPS)
    # menustate == -1 is use to fix no music during menustate == 0 (mainmenu)
    if menu_state == -1:       
        sc.screen.fill((0, 0, 0))
        music = pygame.mixer.music.load(rsc.sound.start)
        pygame.mixer_music.play(-1)
        menu_state = 0
        option1 = True

    #main
    if menu_state ==  0 : 
     # 0 : main , 1:start,2pause 3:option, 4:play, 5:gameover 6 attack
        ms0.draw_menu0()
       
        if option1 == True:
            option1color = font.WHITE
        else:
            option1color = font.GREY
        if option2 == True:
            option2color = font.WHITE
        else:
            option2color = font.GREY
        if option3 == True:
            option3color = font.WHITE
        else:
            option3color = font.GREY
        if option4 == True:
            option4color = font.WHITE
        else:
            option4color = font.GREY

        sc.draw_centertext('Start Game', font.menu_font, option1color, 0 )
        sc.draw_centertext('Options', font.menu_font, option2color, 55)
        sc.draw_centertext('Credits', font.menu_font, option3color, 55 *2)
        sc.draw_centertext('Quit', font.menu_font, option4color, 55 * 3)

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
                            menu_brake = True
                            music = pygame.mixer.music.load(rsc.sound.battle)
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
                    elif event.key == pygame.K_ESCAPE:
                            menu_state = 0
                    
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

                            knight1 = classes.Fighter(300, 210, '(' + font.input_text1 + ')','knightpic', 40, 10, 6)   
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
            if event.type ==  pygame.QUIT:
                run = False
                                    
    #pause menu
    if menu_state == 'GAMEOPTIONS': 
        msgameoptions.draw_menu_options()

        if option1 == True:
            option1color = font.BLACK
        else:
            option1color = font.GREY
        if option2 == True:
            option2color = font.BLACK
        else:
            option2color = font.GREY
        if option3 == True:
            option3color = font.BLACK
        else:
            option3color = font.GREY
        if option4 == True:
            option4color = font.BLACK
        else:
            option4color = font.GREY

        sc.draw_centertext('Resume', font.menu_font, option1color, - 10 )
        sc.draw_centertext('Save Game', font.menu_font, option2color, - 10 + 60)
        sc.draw_centertext('Game Infomation', font.menu_font, option3color,-10 + 60 *2)
        sc.draw_centertext('Back To Menu', font.menu_font, option4color, -10 + 60 * 3)

    #game menu
    if menu_state == 4:

        #draw background
        sc.draw_bg()

        #draw panel
        sc.draw_panel()
        sc.draw_text(f'{knight1.name} HP:{knight1.hp}',font.hp_font, font.RED, 80, 12)
        sc.draw_text(f'{knight2.name} HP:{knight2.hp}',font.hp_font, font.RED, 80, 12 + 1 * 42)
        sc.draw_text(f'{knight3.name} HP:{knight3.hp}',font.hp_font, font.RED, 80, 12 + 2 * 42 )

        # draw game log
        gamelog.draw_game_logs()

        #bandit stats
        for count, i in enumerate(bandit_list):
            #show name and health
            sc.draw_text(f'{i.name} HP: {i.hp}',font.hp_font, font.RED, 800, (12) + count  * 42)


        #draw health bar
        knight_health_bar.draw(knight1.hp)
        knight2_health_bar.draw(knight2.hp)
        knight3_health_bar.draw(knight3.hp)
        bandit1_health_bar.draw(bandit1.hp)
        bandit2_health_bar.draw(bandit2.hp)
        bandit3_health_bar.draw(bandit3.hp)

     
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

        #defence 
        sc.draw_text('Dragon :^) ', font.gui_font, color_def , 80 , 460 )
        #magic
        sc.draw_text('Surrender', font.gui_font, color_power , 80 , 490 )
     

        sc.draw_text(' [How to play the game]', font.hp_font, font.BLACK, 265, 434)
        sc.draw_text('Use arrow key [ up/down ] to change menu', font.smaller_gui_font, font.BLACK, 260, 457)
        sc.draw_text('Press ENTER to select menu, Q to go back', font.smaller_gui_font,font.BLACK , 260, 475)

        #draw fighter
        knight1.update()
        knight1.draw()
        knight2.update()
        knight2.draw()
        knight3.update()
        knight3.draw()
        for bandit in bandit_list:
            bandit.update()
            bandit.draw()



        #draw the damage text 
        dt.damage_text_group.update()
        dt.damage_text_group.draw(sc.screen)

    # if game_over == 0:
        #player action
        if knight1.alive == False:
            playerheart -= 1
        if knight2.alive == False:
            playerheart -= 1
        if knight3.alive == False:
            playerheart -= 1
    
        if playerheart > 0:
            if current_fighter == 1:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    #look for player action
                    #attack
                        if attack == True and attacker != None and target != None and magic == False:
                            attacker.attack(target)
                            rsc.sound.sword_sfx.play()
                            target = None
                            attacker = None
                            attack = False
                            current_fighter += 1
                            action_cooldown = 0
                        elif magic == True and attacker != None and target != None and attack == False :
                            rsc.sound.magic_sfx.play()
                            attacker.magic(target)
                            target = None
                            attacker = None
                            magic = False
                            current_fighter += 1
                            action_cooldown = 0
        if playerheart == 0:
            game_over = -1
        #enemy action
        for count, bandit in enumerate(bandit_list):
            if current_fighter == 2 + count:
                if bandit.alive == True:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        #attack
                        onetwothree = random.randint(1,3)
                        if onetwothree == 1 and knight1.alive == True:
                            aiattack = knight1
                        if onetwothree == 2 and knight2.alive == True:
                            aiattack = knight2
                        if onetwothree == 3 and knight3.alive == True:
                            aiattack = knight3
                        else:
                             onetwothree = random.randint(1,3)

                        bandit.attack(aiattack)
                        rsc.sound.sword_sfx.play()
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
            music = pygame.mixer.music.load(rsc.sound.game_over)
            pygame.mixer_music.play(-1)
            if game_over == 1:
                sc.screen.blit(rsc.image.victory_img,(160,50))
                    
                    
            if game_over == -1:
                sc.screen.blit(rsc.image.defeat_img,(160,50))   

        
    #function to restart the game (add by haarith)
            menu_state = 5
            
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
                    ai1 = '(AI '  + str(random.randint(10,99)) + ')'
                    ai2 = '(AI '  + str(random.randint(10,99)) + ')'
                    ai3 = '(AI '  + str(random.randint(10,99)) + ')'


                    bandit1 = classes.Fighter(720, 200 , ai1, 'banditpic', 20, 10 , 6)
                    bandit2 = classes.Fighter(790, 250 , ai2, 'banditpic', 20, 6 , 6)
                    bandit3 = classes.Fighter(860, 300 , ai3, 'banditpic', 20, 6 , 6)

                    bandit_list = []
                    bandit_list.append(bandit1)
                    bandit_list.append(bandit2)
                    bandit_list.append(bandit3)

                    knight_health_bar = healthbar(80, 30 , knight1.hp, knight1.max_hp)
                    bandit1_health_bar = healthbar(550,30 , bandit1.hp, bandit1.max_hp)
                    bandit2_health_bar = healthbar(550,70, bandit2.hp, bandit2.max_hp)
                    bandit3_health_bar = healthbar(800,110, bandit3.hp, bandit3.max_hp)

                elif event.key == pygame.K_q:
                    run = False

    if menu_state == 6:
        sc.screen.blit(sc.panel_img,(0,sc.SCREEN_HEIGHT - sc.BOTTOM_PANEL))
        sc.draw_bg()
        # knight1.update()
        knight1.draw()
        # knight2.update()
        knight2.draw()
        # knight3.update()
        knight3.draw()

        sc.draw_text(knight1.name, font.gui_font, color_bandit1 , 80 , 430 )
        sc.draw_text(knight2.name, font.gui_font, color_bandit2 , 80 , 460 )
        sc.draw_text(knight3.name, font.gui_font, color_bandit3 , 80 , 490 )

        attacker = None


        #i lazy so  i use the color variable for the attack AI 
        if bandit1gui == True:
            color_bandit1 = font.BLACK
            knight1.update()
        else:
            color_bandit1 = font.GREY
        if bandit2gui == True:
            color_bandit2 = font.BLACK
            knight2.update()
        else:
            color_bandit2 = font.GREY
        if bandit3gui == True:
            color_bandit3 = font.BLACK
            knight3.update()
        else:
            color_bandit3 = font.GREY

    if menu_state == 7:

        sc.screen.blit(sc.panel_img,(0,sc.SCREEN_HEIGHT - sc.BOTTOM_PANEL))
        sc.draw_bg()
        for bandit in bandit_list:
            # bandit.update()
            bandit.draw()

        if attacker == knight1:
            knight1.draw()
            knight1.update()
        if attacker == knight2:
            knight2.draw()
            knight2.update()

        if attacker == knight3:
            knight3.draw()
            knight3.update()



        if bandit1.alive == True:
            sc.draw_text(ai1, font.gui_font, color_bandit1 , 80 , 430 )
            sc.draw_text('HP: ' + str(bandit1.hp), font.hp_font, color_bandit1, 160, 435)
        if bandit2.alive == True:
            sc.draw_text(ai2, font.gui_font, color_bandit2 , 80 , 460 )
            sc.draw_text('HP: ' + str(bandit2.hp), font.hp_font, color_bandit2, 160, 465)
        if bandit3.alive == True:
            sc.draw_text(ai3, font.gui_font, color_bandit3 , 80 , 490 )
            sc.draw_text('HP: ' + str(bandit3.hp), font.hp_font, color_bandit3, 160, 495)

        
        if bandit1gui == True:
            color_bandit1 = font.BLACK
            bandit1.update()
        else:
            color_bandit1 = font.GREY
        if bandit2gui == True:
            color_bandit2 = font.BLACK
            bandit2.update()
        else:
            color_bandit2 = font.GREY
        if bandit3gui == True:
            color_bandit3 = font.BLACK
            bandit3.update()
         
        else:
            color_bandit3 = font.GREY

    if menu_state == 8:
        sc.screen.blit(sc.panel_img,(0,sc.SCREEN_HEIGHT - sc.BOTTOM_PANEL))
        sc.draw_bg()

        if attacker == knight1:
            knight1.draw()
            knight1.update()
        if attacker == knight2:
            knight2.draw()
            knight2.update()

        if attacker == knight3:
            knight3.draw()
            knight3.update() 

        if target == bandit1:
            bandit1.draw()
            bandit1.update()

        if target == bandit2:
            bandit2.draw()
            bandit2.update()

        if target == bandit3:
            bandit3.draw()
            bandit3.update()

        if bandit1gui == True:
            color_bandit1 = font.BLACK
        else:
            color_bandit1 = font.GREY
        if bandit2gui == True:
            color_bandit2 = font.BLACK
        else:
            color_bandit2 = font.GREY

        sc.draw_text('Slash Attack', font.gui_font, color_bandit1 , 80 , 430 )
        sc.draw_text('Magic Attack', font.gui_font, color_bandit2 , 80 , 460 )
        
    if menu_state == 'MENUOPTIONS':
        msoptions.draw_menu_options()

        if option1 == True:
            option1color = font.WHITE
        else:
            option1color = font.GREY
        if option2 == True:
            option2color = font.WHITE
        else:
            option2color = font.GREY
        if option3 == True:
            option3color = font.WHITE
        else:
            option3color = font.GREY
        if option4 == True:
            option4color = font.WHITE
        else:
            option4color = font.GREY

        sc.draw_centertext('Music Setting', font.menu_font, option1color, - 10 )
        sc.draw_centertext('Video Setting', font.menu_font, option2color, - 10 + 60)
        sc.draw_centertext('Game Infomation', font.menu_font, option3color,-10 + 60 *2)
        sc.draw_centertext('Back To Menu', font.menu_font, option4color, -10 + 60 * 3)

    if menu_state == 'CREDIT':
        mscredit.draw_menu_credit()
        mscredit.text_sprites.update()
        mscredit.text_sprites.draw(sc.screen)
        # print(mscredit.text_sprites) DEBUG

    if menu_state == 'ERROR':
        mssorry.draw_menu()

    # FIX THE FILE PATHS FOR THIS 
    if menu_state == 'easter':
        pygame.mixer.music.unload()
        music = pygame.mixer.music.load(rsc.sound.easter)
        music_run = True
        pygame.mixer_music.play(-1)
        for i in range(1,109):
            easteregg_img = pygame.image.load(f"{Path(f'resources/picture/toothless/toothlessdrag ({i}).png')}")
            sc.screen.blit(easteregg_img, (250,200))
            pygame.display.flip()
            clock.tick(50)
        for i in range(1,109):
            easteregg_img = pygame.image.load(f"{Path(f'resources/picture/toothless/toothlessdrag ({i}).png')}")
            sc.screen.blit(easteregg_img, (130,200))
            sc.screen.blit(easteregg_img, (380,200))
            pygame.display.flip()
            clock.tick(50)
        for i in range(1,109):
            easteregg_img = pygame.image.load(f"{Path(f'resources/picture/toothless/toothlessdrag ({i}).png')}")
            sc.screen.blit(easteregg_img, (130,300))
            sc.screen.blit(easteregg_img, (380,300))
            sc.screen.blit(easteregg_img, (130,80))
            sc.screen.blit(easteregg_img, (380,80))
            pygame.display.flip()
            clock.tick(51)



        # sc.screen.fill((0, 0, 0))
        menu_state = 4

    #quit the game
    for event in pygame.event.get(): 
        
        if event.type == pygame.KEYDOWN:
            if menu_state == 0:
                if event.key == pygame.K_RETURN:
                    if option1 == True:
                        menu_state = 1 
                        input1 = True
                    elif option2 == True:
                        menu_state = 'MENUOPTIONS'
                        option2 = False
                        menu_brake = True
                    elif option3 == True:
                        option3 = False
                        menu_state = 'CREDIT'
                    elif option4 == True:
                        pygame.quit()
                elif event.key == pygame.K_DOWN:
                    if menu_brake == True:
                        menu_brake = False
                        option4 = True
                    if option1 == True:
                        option1 = False
                        option2 = True
                    elif option2 == True:
                        option2 = False
                        option3 = True
                    elif option3 == True:
                        option3 = False
                        option4 = True
                    elif option4 == True:
                        option4 = False
                        option1 = True
                elif event.key == pygame.K_UP:
                    if menu_brake == True:
                        menu_brake = False
                        option2 = True
                    if option1 == True:
                        option1 = False
                        option4 = True
                    elif option4 == True:
                        option4 = False
                        option3 = True
                    elif option3 == True:
                        option3 = False
                        option2 = True
                    elif option2 == True:
                        option2 = False
                        option1 = True
            
            if menu_state == 'MENUOPTIONS':
                if event.key == pygame.K_RETURN:
                    if option1 == True:
                        option1 = False
                        menu_state = 'ERROR'
                        last_state = 'MENUOPTIONS'
                    elif option2 == True:
                        option2 = False
                        menu_state = 'ERROR'
                        last_state = 'MENUOPTIONS'
                    elif option3 == True:
                        option3 = False
                        menu_state = 'ERROR'
                        last_state = 'MENUOPTIONS'
                    elif option4 == True:
                        menu_state = 0
                elif event.key == pygame.K_ESCAPE:
                    menu_state = 0
                    option1 = False
                    option2 = True
                    option3 = False
                    option4 = False
                elif event.key == pygame.K_DOWN:
                    if menu_brake == True:
                        menu_brake = False
                        option4 = True
                    if option1 == True:
                        option1 = False
                        option2 = True
                    elif option2 == True:
                        option2 = False
                        option3 = True
                    elif option3 == True:
                        option3 = False
                        option4 = True
                    elif option4 == True:
                        option4 = False
                        option1 = True
                elif event.key == pygame.K_UP:
                    if menu_brake == True:
                        menu_brake = False
                        option2 = True
                    if option1 == True:
                        option1 = False
                        option4 = True
                    elif option4 == True:
                        option4 = False
                        option3 = True
                    elif option3 == True:
                        option3 = False
                        option2 = True
                    elif option2 == True:
                        option2 = False
                        option1 = True

            if menu_state == 'CREDIT':
                if event.key == pygame.K_ESCAPE:
                    menu_state = 0
                    option1 = False
                    option2 = False
                    option3 = True
                    option4 = False

            if menu_state == 'ERROR':
                if event.key == pygame.K_ESCAPE:
                    if last_state == 'MENUOPTIONS':
                        menu_state = 'MENUOPTIONS'
                        last_state = None
                        menu_brake = True
                    elif  last_state == 'GAMEOPTIONS':
                        menu_state = 'GAMEOPTIONS'
                        last_state = None
                        menu_brake = True

            if menu_state == 'GAMEOPTIONS':
                if event.key == pygame.K_RETURN:
                    if option1 == True:
                        menu_state = 4
                        menu_brake = True
                    elif option2 == True:
                        option2 = False
                        menu_state = 'ERROR'
                        last_state = 'GAMEOPTIONS'
                    elif option3 == True:
                        option3 = False
                        menu_state = 'ERROR'
                        last_state = 'GAMEOPTIONS'
                    elif option4 == True:
                        menu_state = 0
                        menu_brake = True

                elif event.key == pygame.K_ESCAPE:
                        menu_state = 4
                elif event.key == pygame.K_DOWN:
                    if menu_brake == True:
                        menu_brake = False
                        option1 = True
                    if option1 == True:
                        option1 = False
                        option2 = True
                    elif option2 == True:
                        option2 = False
                        option3 = True
                    elif option3 == True:
                        option3 = False
                        option4 = True
                    elif option4 == True:
                        option4 = False
                        option1 = True
                elif event.key == pygame.K_UP:
                    if menu_brake == True:
                        menu_brake = False
                        option4 = True
                    if option1 == True:
                        option1 = False
                        option4 = True
                    elif option4 == True:
                        option4 = False
                        option3 = True
                    elif option3 == True:
                        option3 = False
                        option2 = True
                    elif option2 == True:
                        option2 = False
                        option1 = True

            if menu_state == 4:
                if event.key == pygame.K_DOWN:
                    if menu_brake == True:
                        menu_brake = False
                        powerTF = True
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
                    if menu_brake == True:
                        menu_brake = False
                        defenceTF = True
                    if attackTF == True:
                        attackTF = False
                        powerTF =True
                    elif defenceTF == True:
                        defenceTF = False
                        attackTF = True
                    elif powerTF == True:
                        powerTF = False
                        defenceTF = True
                elif event.key == pygame.K_RETURN:
                    if attackTF == True and defenceTF == False and powerTF == False : 
                        menu_state = 6
                        menu_brake = True
                    elif powerTF == True and attackTF == False and defenceTF == False:
                        game_over = -1
                    elif defenceTF == True and attackTF == False and powerTF == False:
                        menu_state = 'easter'

                        #call game options menu
                elif event.key == pygame.K_ESCAPE:
                    menu_state = 'GAMEOPTIONS' 
                    attackTF = False
                    defenceTF = False
                    powerTF = False
            

            if menu_state == 6:
                if event.key == pygame.K_RETURN:
                    if bandit1gui == True and knight1.alive == True:
                        attacker = knight1
                        menu_state = 7
                        bandit1gui = False
                        menu_brake = True
                    elif bandit2gui == True and knight2.alive == True:
                        attacker = knight2
                        menu_state = 7
                        bandit2gui = False
                        menu_brake = True
                    elif bandit3gui == True and knight3.alive == True:
                        attacker = knight3
                        menu_state = 7
                        bandit3gui = False
                        menu_brake = True

                elif event.key == pygame.K_DOWN:
                    if menu_brake == True:
                        menu_brake = False
                        bandit1gui = True
                    if bandit1gui == True:
                        bandit1gui = False
                        bandit2gui = True
                    elif bandit2gui == True:
                        bandit2gui = False
                        bandit3gui = True
                    elif bandit3gui == True:
                        bandit3gui = False
                        bandit1gui = True
                elif event.key == pygame.K_UP:
                    if bandit1gui == True:
                        bandit1gui = False
                        bandit3gui = True
                    elif bandit2gui == True:
                        bandit2gui = False 
                        bandit1gui = True
                    elif bandit3gui == True:
                        bandit3gui = False
                        bandit2gui = True
            
                elif event.key == pygame.K_q:
                    menu_state = 4
                        
            if menu_state == 7:
                if event.key == pygame.K_RETURN:
                    if bandit1gui == True and bandit1.alive == True:
                        target = bandit1
                        menu_state = 8
                        bandit1gui = False
                        menu_brake = True
                    elif bandit2gui == True and bandit2.alive == True:
                        target = bandit2
                        menu_state = 8
                        bandit2gui = False
                        menu_brake = True
                    elif bandit3gui == True and bandit3.alive == True:
                        target = bandit3
                        menu_state = 8
                        bandit3gui = False
                        menu_brake = True
                elif event.key == pygame.K_DOWN:
                    if menu_brake == True:
                        menu_brake = False
                        bandit1gui = True
                    elif bandit1gui == True:
                        bandit1gui = False
                        bandit2gui = True
                    elif bandit2gui == True:
                        bandit2gui = False
                        bandit3gui = True
                    elif bandit3gui == True:
                        bandit3gui = False
                        bandit1gui = True
                elif event.key == pygame.K_UP:
                    if bandit1gui == True:
                        bandit1gui = False
                        bandit3gui = True
                    elif bandit2gui == True:
                        bandit2gui = False 
                        bandit1gui = True
                    elif bandit3gui == True:
                        bandit3gui = False
                        bandit2gui = True
            
                elif event.key == pygame.K_q:
                    menu_state = 6
                    
            if menu_state == 8:
                    if event.key == pygame.K_RETURN:
                        if bandit1gui == True:
                            attack = True
                            menu_state = 4
                        elif bandit2gui == True:
                            magic = True
                            menu_state = 4
                    elif event.key == pygame.K_DOWN:
                        if menu_brake == True:
                            menu_brake = False
                            bandit1gui = True
                        elif bandit1gui == True:
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
                        menu_state = 7
        
        if event.type ==  pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False
            
    # print(f"Current menu state: {menu_state}") DEBUG
    pygame.display.update()

pygame.quit()