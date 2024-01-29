import pygame
import random
import button
import time

game_logs = []

pygame.init()

clock = pygame.time.Clock()
fps = 60
 


#game window
bottem_panel = 150
screen_width = 800
screen_height = 400 + bottem_panel

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("RPG GAME")

#music
music = pygame.mixer.music.load('music/Fantasy RPG Music Pack Vol.3/Tracks/mp3/Action 4.mp3')
music_run = True
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

#define colours
red = (255,0,0) 
green = (0,255,0)
#define colours
TEXT_COL = (255,255,255)
yellow = (255,255,51)
grey = (96,96,96)
black = (0,0,0)

#define font
font = pygame.font.SysFont("arialblack" , 40)
hp_font = pygame.font.SysFont("Times New Romon", 26)

#game log font size
game_log_font = pygame.font.SysFont("arial", 15)



#input variable (start menu)
base_font = pygame.font.Font(None, 32)
input_hp_font = pygame.font.Font(None, 26)

input_text1, input_text2 = '', ''
input_rect = pygame.Rect(350,200,140,32)
inputgame_rect = pygame.Rect(150,7,140,32)

input2_rect = pygame.Rect(350,300,140,32)
color_active = pygame.Color('white')
color_passive = pygame.Color('gray15')
colorinput1, colorinput2, colorstartbutton = color_passive, color_passive, color_passive



ask_text = 'Name your charactor :'
ask1_rect = pygame.Rect(80,200,140,32) # x, y, w, h
ask2_text = 'Anything :'
ask2_rect = pygame.Rect(80,300,140,32)
colorAskinput1 = pygame.Color('black')
colorAskinput2 = pygame.Color('black')

start_text = 'Begin your adventure..'
start_rect = pygame.Rect(500,500,140,32)



input1 = True
input2 = False
startbutton = False

#gui variable
gui_font = pygame.font.Font(None, 32)
menu_font = pygame.font.Font(None, 55)

color_attack = grey
color_def = grey
color_power = grey
color_bandit1, color_bandit2 = grey, grey
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
#background image
background_img = pygame.image.load('picture/background3.png')
background_img = pygame.transform.scale(background_img, (screen_width,(screen_height-bottem_panel)))


#panel image
panel_img = pygame.image.load('picture/UI board Large  parchment.png')
panel_img = pygame.transform.scale(panel_img, (screen_width,bottem_panel))

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



                                 
#function for drawing text
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))



#function for draw background
def draw_bg():
    screen.blit(background_img,(0,0))
def draw_main():
    screen.fill((0, 0, 0))
    draw_text ('PSB PROGRAMMING ASSIGNMENT', menu_font, TEXT_COL,80 , screen_height / 2 - 120)
    draw_text('TURN BASED RPG', menu_font, TEXT_COL, 220, screen_height / 2 - 80)
    draw_text('>>> PRESS SPACEBAR TO START THE GAME <<<', gui_font, yellow , 120 , screen_height/ 2 + 150)

#function for draw panel
def draw_panel():
    #draw panel rectangle
    screen.blit(panel_img,(0,screen_height - bottem_panel))
    #show knight stats
    draw_text(f'{knight.name} HP:{knight.hp}',hp_font, red, 80, 12)
    #bandit stats
    for count, i in enumerate(bandit_list):
        #show name and health
        draw_text(f'{i.name} HP: {i.hp}',hp_font, red, 550, (12) + count  * 42)


#class
class fighter():
    def __init__(self,x,y,name,namepic,max_hp,strength,defence):
        self.name = name 
        self.namepic = namepic
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.defence = defence
        self.alive = True
        self.animationlist= []
        self.frame_index = 0
        self.action = 0 #0:idle, 1:attack , 2:hurt , 3:dead , 4Ldefence
        self.update_time = pygame.time.get_ticks()
        #load image
        temp_list = []
        for i in range(1,5):
            img = pygame.image.load(f'picture/{self.namepic}/idle/{i}.png')
            self.image = pygame.transform.scale(img, (img.get_width()*3 ,img.get_height()*3))
            temp_list.append(self.image)
        self.animationlist.append(temp_list) #list of list

        #load attack
        temp_list = []
        for i in range(1,10):
            if {self.namepic} == "knightpic" :
                img = pygame.image.load(f'picture/{self.namepic}/attack/{i}.png')
                self.image = pygame.transform.scale(img, (img.get_width()*6 ,img.get_height()*6))
        
            else:
                img = pygame.image.load(f'picture/{self.namepic}/attack/{i}.png')
                self.image = pygame.transform.scale(img, (img.get_width()*3 ,img.get_height()*3))
            temp_list.append(self.image)
        self.animationlist.append(temp_list)

        #load hurt image
        temp_list = []
        for i in range(1,3):
            img = pygame.image.load(f'picture/{self.namepic}/hurt/{i}.png')
            self.image = pygame.transform.scale(img, (img.get_width()*3 ,img.get_height()*3))
            temp_list.append(self.image)
        self.animationlist.append(temp_list)

        #load dead image
        temp_list = []
        for i in range(1,9):
            img = pygame.image.load(f'picture/{self.namepic}/death/{i}.png')
            self.image = pygame.transform.scale(img, (img.get_width()*3 ,img.get_height()*3))
            temp_list.append(self.image)
        self.animationlist.append(temp_list)

        self.image = self.animationlist[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


    def update(self):
        animation_cooldown = 100
        #handle animation
        #update image
        self.image = self.animationlist[self.action][self.frame_index]
        #check if enought time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1 
        #if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animationlist[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animationlist[self.action]) - 1
            else:
                self.idle()

    def idle(self):
        #set variable to idle
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def attack(self, target):
        #deal damage to the enemy
        rand = random.randint(-5, 5)
        damage = (self.strength + rand) - (self.defence + rand)
        target.hp -= damage 
        attack_sfx.play()
        #run enemy animation
        target.hurt()
        #check is target died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red)
        damage_text_group.add(damage_text)
        #the names for game log (-haarith, needs work not showing name of the user)
        game_logs.append(f'{self.name} damaged {target.name} for {damage} damage')
        game_logs.append(f'{target.name} block {(self.defence + rand)} damage from {self.name}')

        

        #set variable to attack
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        #set variable to hurt
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        #set variable to dead
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, self.rect)
        draw_text(self.name, hp_font, red, self.rect.centerx - 30, self.rect.y - 20)
    
    #draw the bandit names on the screen (still needs work -haarith)
    def draw_bandit_names():
        for count, bandit in enumerate(bandit_list):
            draw_text(bandit.name, hp_font, red, 550, (12) + count * 42)

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
        pygame.draw.rect(screen,red,( self.x, self.y, 150, 20))
        pygame.draw.rect(screen,green,( self.x, self.y, 150 * ratio , 20))


class DamageText(pygame.sprite.Sprite):
	def __init__(self, x, y, damage, colour):
		pygame.sprite.Sprite.__init__(self)
		self.image = font.render(damage, True, colour)
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.counter = 0

        
	def update(self):
		#move damage text up
		self.rect.y -= 1
		#delete the text after a few seconds
		self.counter += 1
		if self.counter > 30:
			self.kill()

def draw_game_logs():
    y = 435 # initial y value
    for log in game_logs[-4:]:  # display only the last 4 logs
        text_surface = game_log_font.render(log, True, (255, 0, 0))
        screen.blit(text_surface, (550, y))
        y += 23  # increment y value for next log
    


damage_text_group = pygame.sprite.Group()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////[ GAME STAT ]///////////////////////////////////////////[ GAME STAT ]/////////////////////////////////////////////////////[ GAME STAT ]/////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# knightname = input_text1
knight = fighter(200, 260, '','knightpic', 40, 10, 6)
randomAI = str(random.randint(10,99))
randomAI2 = str(random.randint(10,99)) 

bandit1 = fighter(550, 200 , 'AI ' + randomAI, 'banditpic', 20, 10 , 6)
bandit2 = fighter(650, 250 ,'AI ' + randomAI2, 'banditpic', 20, 6 , 6)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

knight_health_bar = healthbar(80, 30 , knight.hp, knight.max_hp)
bandit1_health_bar = healthbar(550,30 , bandit1.hp, bandit1.max_hp)
bandit2_health_bar = healthbar(550,70, bandit2.hp, bandit2.max_hp)



#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////[ GAME START ]///////////////////////////////////////////[ GAME START ]//////////////////////////////////////////////////[ GAME START ]/////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



#use to loop the game
run = True   
while run: 


    clock.tick(fps)
    #main
    if menu_state ==  0 :            # 0 : main , 1:start,2pause 3:option, 4:play, 5:gameover 6 attack
        draw_main()
    #start menu
    if menu_state == 1 :
        screen.fill((0, 0, 0))

        if input1 == True:
            colorinput1 = color_active
        else:
            colorinput1 = color_passive
        if input2 == True:
            colorinput2 = color_active
        else:
            colorinput2 = color_passive
        if startbutton == True:
            colorstartbutton = color_active
        else:
            colorstartbutton = color_passive
        #input 1
        pygame.draw.rect(screen, colorinput1, input_rect, 2)
        text_surface = base_font.render(input_text1, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5 ))
        input_rect.w = max(100,text_surface.get_width() + 10)
        #ask 1
        pygame.draw.rect(screen, colorAskinput1, ask1_rect, 0)
        text_surface = base_font.render(ask_text, True, (255, 255, 255))
        screen.blit(text_surface, (ask1_rect.x + 5, ask1_rect.y + 5 ))
        ask1_rect.w = max(100,text_surface.get_width() + 10)
        #input 2
        pygame.draw.rect(screen, colorinput2, input2_rect, 2)
        text_surface = base_font.render(input_text2, True, (255, 255, 255))
        screen.blit(text_surface, (input2_rect.x + 5, input2_rect.y + 5 ))
        input2_rect.w = max(100,text_surface.get_width() + 10)
        #ask 2
        pygame.draw.rect(screen, colorAskinput2, ask2_rect, 0)
        text_surface = base_font.render(ask2_text, True, (255, 255, 255))
        screen.blit(text_surface, (ask2_rect.x + 5, ask2_rect.y + 5 ))
        ask2_rect.w = max(100,text_surface.get_width() + 10)
        #start 
        pygame.draw.rect(screen, colorstartbutton, start_rect, 2)
        text_surface = base_font.render(start_text, True, (255, 255, 255))
        screen.blit(text_surface, (start_rect.x + 5, start_rect.y + 5 ))
        start_rect.w = max(100,text_surface.get_width() + 10)
    #pause menu
    if menu_state == 2 :
        screen.fill((0, 0, 0))

        pygame.mouse.set_visible(True)
        #draw pause screen button
        if resume_button.draw(screen):
             menu_state = 4
        if option_button.draw(screen):
             menu_state = 3
        if back_button.draw(screen):
            menu_state = menu_state - 2
        # check if the option menu is open
    #option menu        
    if menu_state == 3 :
        screen.fill((0, 0, 0))

        pygame.mouse.set_visible(True)
        if video_button.draw(screen):
            print('i didnt make a code for Video Settings :3')
        if audio_button.draw(screen):
            print('i didnt make a code for music Settings :3')
        if backoption_button.draw(screen):
            menu_state = menu_state - 1
    #game menu
    if menu_state == 4:
        #draw background
        draw_bg()

        #draw panel
        draw_panel()
        knight_health_bar.draw(knight.hp)
        bandit1_health_bar.draw(bandit1.hp)
        bandit2_health_bar.draw(bandit2.hp)

        #GUI panel
        if attackTF == True:
            color_attack = black
        else:
            color_attack = grey

        if defenceTF == True:
            color_def = black
        else:
            color_def = grey

        if powerTF == True:
            color_power = black
        else:
            color_power = grey
        
        

        #attack 
        draw_text('Attack (press E to select menu, Q to quit)', gui_font, color_attack , 80 , 430 )

        #defence 
        draw_text('>>> PLEASE DONT PRESS THIS <<<', gui_font, color_def , 80 , 460 )

        #magic
        draw_text('Surrender', gui_font, color_power , 80 , 490 )

        #for knight name
        pygame.draw.rect(screen, colorAskinput1, inputgame_rect, -1)
        text_surface = input_hp_font.render(input_text1, True, (0, 0, 0))
        screen.blit(text_surface, (inputgame_rect.x + 5, inputgame_rect.y + 5 ))
        inputgame_rect.w = max(100,text_surface.get_width() + 10)

         #draw fighter
        knight.update()
        knight.draw()
        for bandit in bandit_list:
            bandit.update()
            bandit.draw()

         #draw the damage text 
        damage_text_group.update()
        damage_text_group.draw(screen)


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
        #         screen.blit(sword_img, pos)
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
            if game_over == 1:
                screen.blit(victory_img,(160,50))
                    
                    
            if game_over == -1:
                screen.blit(defeat_img,(160,50))   

        
    #function to restart the game (add by haarith)
            menu_state = 5
            

    if menu_state == 4:  # state where game is active
        draw_game_logs()

    if menu_state == 5:
        #display game over message
        small_font = pygame.font.Font(None, 40) 
        if game_over == 1:
            draw_text('You win. Press R to replay or Q to quit', small_font, TEXT_COL, 100, screen_height // 2)
        if game_over == -1:
            draw_text('Game over. Press R to replay or Q to quit', small_font, TEXT_COL, 100, screen_height // 2)
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
                    knight = fighter(200, 260, '','knightpic', 40, 10, 6)
                    bandit1 = fighter(550, 200 ,'Bandit', 'banditpic', 2, 6 , 6)
                    bandit2 = fighter(650, 250 ,'Bandit', 'banditpic', 20, 6 , 6)

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
                        input_text1 = input_text1[0:-1]
                    else:
                        press1 = pygame.key.get_pressed()
                        for i in range( pygame.K_a, pygame.K_z + 1 ): 
                            if press1[i] == True:
                                input_text1 += pygame.key.name(i) 
                        for i in range( pygame.K_0, pygame.K_9 + 1 ): 
                            if press1[i] == True:
                                input_text1 += pygame.key.name(i)
                if input2 == True:
                    if event.key == pygame.K_BACKSPACE:
                        input_text2 = input_text2[0:-1]

                    else:
                        press = pygame.key.get_pressed()
                        for i in range( pygame.K_a, pygame.K_z + 1 ): 
                            if press[i] == True:
                                input_text2 += pygame.key.name(i)
                        for i in range( pygame.K_0, pygame.K_9 + 1 ): 
                            if press[i] == True:
                                input_text2 += pygame.key.name(i)
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
                screen.blit(panel_img,(0,screen_height - bottem_panel))
                draw_bg()
                for bandit in bandit_list:
                    bandit.update()
                    bandit.draw()
                draw_text('bandit1', gui_font, color_bandit1 , 80 , 430 )
                draw_text('bandit2', gui_font, color_bandit2 , 80 , 460 )

                
                if bandit1gui == True:
                    color_bandit1 = black
                else:
                    color_bandit1 = grey
                if bandit2gui == True:
                    color_bandit2 = black
                else:
                    color_bandit2 = grey
                
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
                    screen.blit(easteregg_img, (100,100))
                    pygame.display.flip()
                    clock.tick(24)
                for i in range(1,71):
                    easteregg_img = pygame.image.load(f'picture/milo/milo ({i}).jpg')
                    screen.blit(easteregg_img, (100,100))
                    pygame.display.flip()
                    clock.tick(24)
                for i in range(1,71):
                    easteregg_img = pygame.image.load(f'picture/milo/milo ({i}).jpg')
                    screen.blit(easteregg_img, (100,100))
                    pygame.display.flip()
                    clock.tick(24)
                
                # screen.fill((0, 0, 0))
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
