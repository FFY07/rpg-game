import pygame
import random
import button

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

#define font
font = pygame.font.SysFont("arialblack" , 40)
hp_font = pygame.font.SysFont("Times New Romon", 26)

#input variable
base_font = pygame.font.Font(None, 32)

input_text1 = ''
input_text2 = ''
input_rect = pygame.Rect(200,200,140,32)
input2_rect = pygame.Rect(200,300,140,32)
color_active = pygame.Color('white')
color_passive = pygame.Color('gray15')
colorinput1 = color_passive
colorinput2 = color_passive

ask_text = 'Test ask:'
ask1_rect = pygame.Rect(80,200,140,32) # x, y, w, h

colorAskinput1 = pygame.Color('black')

input1 = False
input2 = False

#define colours
red = (255,0,0)
green = (0,255,0)
#define colours
TEXT_COL = (255,255,255)

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



#load image
#background image
background_img = pygame.image.load('picture/background3.png')
background_img = pygame.transform.scale(background_img, (screen_width,(screen_height-bottem_panel)))

menu_img = pygame.image.load('picture/menuimg.png')
menu_img = pygame.transform.scale(menu_img, (screen_width,(screen_height)))
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
    screen.blit(menu_img,(0,0))

#function for draw panel
def draw_panel():
    #draw panel rectangle
    screen.blit(panel_img,(0,screen_height - bottem_panel))
    #show knight stats
    draw_text(f'{knight.name} HP:{knight.hp}',hp_font, red, 100, screen_height - bottem_panel + 20)
    #bandit stats
    for count, i in enumerate(bandit_list):
        #show name and health
        draw_text(f'{i.name} HP:{i.hp}',hp_font, red, 500, (screen_height - bottem_panel + 20) + count  * 45)


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
        damage = self.strength + rand
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


damage_text_group = pygame.sprite.Group()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////[ GAME STAT ]///////////////////////////////////////////[ GAME STAT ]/////////////////////////////////////////////////////[ GAME STAT ]/////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

knight = fighter(200, 260, 'Knight','knightpic', 40, 10, 6)
bandit1 = fighter(550, 200 ,'Bandit', 'banditpic', 20, 6 , 6)
bandit2 = fighter(650, 250 ,'Bandit', 'banditpic', 20, 6 , 6)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

knight_health_bar = healthbar(100,screen_height - bottem_panel + 40, knight.hp, knight.max_hp)
bandit1_health_bar = healthbar(550,screen_height - bottem_panel + 40, bandit1.hp, bandit1.max_hp)
bandit2_health_bar = healthbar(550,screen_height - bottem_panel + 85, bandit2.hp, bandit2.max_hp)



#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////[ GAME START ]///////////////////////////////////////////[ GAME START ]//////////////////////////////////////////////////[ GAME START ]/////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



#use to loop the game
run = True   
while run: 


    clock.tick(fps)
    if menu_state ==  0 :            # 0 : main , 1:start,2pause 3:option, 4:play
        draw_main()

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

        pygame.draw.rect(screen, colorinput1, input_rect, 2)
        text_surface = base_font.render(input_text1, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5 ))
        input_rect.w = max(100,text_surface.get_width() + 10)

        pygame.draw.rect(screen, colorAskinput1, ask1_rect, 0)
        text_surface = base_font.render(ask_text, True, (255, 255, 255))
        screen.blit(text_surface, (ask1_rect.x + 5, ask1_rect.y + 5 ))
        ask1_rect.w = max(100,text_surface.get_width() + 10)

        pygame.draw.rect(screen, colorinput2, input2_rect, 2)
        text_surface = base_font.render(input_text2, True, (255, 255, 255))
        screen.blit(text_surface, (input2_rect.x + 5, input2_rect.y + 5 ))
        input2_rect.w = max(100,text_surface.get_width() + 10)
      
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
            
    if menu_state == 3 :
        screen.fill((0, 0, 0))

        pygame.mouse.set_visible(True)
        if video_button.draw(screen):
            print('i didnt make a code for Video Settings :3')
        if audio_button.draw(screen):
            if music_run == True:
                    music_run = False
                    pygame.mixer.music.pause()
            if music_run == False:
                    music_run = True
                    pygame.mixer.music.unpause()
        if backoption_button.draw(screen):
            menu_state = menu_state - 1

    if menu_state == 4:
        #draw background
        draw_bg()

        #draw panel
        draw_panel()
        knight_health_bar.draw(knight.hp)
        bandit1_health_bar.draw(bandit1.hp)
        bandit2_health_bar.draw(bandit2.hp)

         #draw fighter
        knight.update()
        knight.draw()
        for bandit in bandit_list:
            bandit.update()
            bandit.draw()

         #draw the damage text 
        damage_text_group.update()
        damage_text_group.draw(screen)


        #control player action
        #reset action variables
        attack = False
        target = None 
        #make sure mouse is visible
        pygame.mouse.set_visible(True)
        pos = pygame.mouse.get_pos()
        for count, bandit in enumerate(bandit_list):
            if bandit. rect.collidepoint(pos):
                #hide mouse
                pygame.mouse.set_visible(False)
                #show sword in place of mouse cursor 
                screen.blit(sword_img, pos)
                if clicked == True and bandit.alive == True:
                    attack = True 
                    target = bandit_list[count]
            
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
        play_sound = 1
        if game_over != 0:
            if game_over == 1:
                screen.blit(victory_img,(160,50))
                    
                    
            if game_over == -1:
                screen.blit(defeat_img,(160,50))       
             

    #quit the game
    for event in pygame.event.get(): 
        
        if event.type == pygame.KEYDOWN:
            if menu_state == 0:
                if event.key == pygame.K_SPACE:
                    menu_state = 1
                    input1 = True

            if menu_state == 1:
                if input1 == True:
                    if event.key == pygame.K_RETURN:
                        input1 = False
                        input2 =True
                    if event.key == pygame.K_DOWN:
                        input1 = False
                        input2 =True
                        
                    if event.key == pygame.K_BACKSPACE:
                        input_text1 = input_text1[0:-1]
                    else:
                        press = pygame.key.get_pressed()
                        for i in range( pygame.K_a, pygame.K_z + 1 ): 
                            if press[i] == True:
                                input_text1 += pygame.key.name(i) 
                        for i in range( pygame.K_0, pygame.K_9 + 1 ): 
                            if press[i] == True:
                                input_text1 += pygame.key.name(i)

                if input2 == True:
                    if event.key == pygame.K_RETURN:
                        pass
                    if event.key == pygame.K_UP:
                        input1 = True
                        input2 = False
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
