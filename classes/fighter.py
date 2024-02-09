'''

(This file is use for character class like warrior )
(character image also load here)


'''


from pathlib import Path

import pygame
import random

import gui.screen as sc
import gui.damagetext as dt
import resources.font as font
import gui.gamelog as gamelog

import resources as rsc


pygame.init()
clock = pygame.time.Clock()
# TURN THIS INTO pygame.sprite.Sprite!!!!!!!!!


class Unit():
    def __init__(self,x,y,name,namepic,max_hp,strength,defence, level=1):
        # ((self,x,y,name,namepic,max_hp,strength,defence, mana):)
        self.name = name 
        self.namepic = namepic
        self.level = level
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.defence = defence
        self.alive = True
        self.animationlist= []
        self.frame_index = 0
        self.action = 0 #0:idle, 1:attack , 2:hurt , 3:dead , 4Ldefence
        self.update_time = pygame.time.get_ticks()
        
        # Temporary, will rewrite this whole loading part and replace animationlist with a dictionary in a new Unit class
        if self.namepic == "reaperpic":
            self.scale = 2
        
        elif self.namepic == "knightpic":
            self.scale = 3
        
        else:
            self.scale = 3
            
        #load image
        temp_list = []
        if self.namepic == "reaperpic":
            for i in range(1,9):
                img = pygame.image.load(f"{Path(f'resources/picture/{self.namepic}/idle/{i}.png')}")
                self.image = pygame.transform.scale(img, (img.get_width()*self.scale ,img.get_height()*self.scale))
                temp_list.append(self.image)
            
        else:
            for i in range(1,5):
                img = pygame.image.load(f"{Path(f'resources/picture/{self.namepic}/idle/{i}.png')}")
                self.image = pygame.transform.scale(img, (img.get_width()*self.scale ,img.get_height()*self.scale))
                temp_list.append(self.image)
        self.animationlist.append(temp_list) #list of list


        #load attack
        temp_list = []
        if self.namepic == "reaperpic":
            for i in range(1,14):
                img = pygame.image.load(f"{Path(f'resources/picture/{self.namepic}/attack/{i}.png')}")
                self.image = pygame.transform.scale(img, (img.get_width()*self.scale ,img.get_height()*self.scale))
                temp_list.append(self.image)
        elif self.namepic == "knightpic" :
            for i in range(1,10):
                img = pygame.image.load(f"{Path(f'resources/picture/{self.namepic}/attack/{i}.png')}")
                self.image = pygame.transform.scale(img, (img.get_width()*self.scale ,img.get_height()*self.scale))
                temp_list.append(self.image)
        # Move this to Tank or a different class
        else:
            for i in range(1,10):
                img = pygame.image.load(f"{Path(f'resources/picture/{self.namepic}/attack/{i}.png')}")
                self.image = pygame.transform.scale(img, (img.get_width()*self.scale ,img.get_height()*self.scale))
                temp_list.append(self.image)
        self.animationlist.append(temp_list)

        #load hurt image
        temp_list = []
        
        if self.namepic == "reaperpic":            
            for i in range(1,3):
                img = pygame.image.load(f"{Path(f'resources/picture/{self.namepic}/hurt/{i}.png')}")
                self.image = pygame.transform.scale(img, (img.get_width()*self.scale ,img.get_height()*self.scale))
                temp_list.append(self.image)
        else:
            for i in range(1,3):
                img = pygame.image.load(f"{Path(f'resources/picture/{self.namepic}/hurt/{i}.png')}")
                self.image = pygame.transform.scale(img, (img.get_width()*self.scale ,img.get_height()*self.scale))
                temp_list.append(self.image)

        self.animationlist.append(temp_list)

        #load dead image
        temp_list = []
        if self.namepic == "reaperpic":
            for i in range(1,19):
                img = pygame.image.load(f"{Path(f'resources/picture/{self.namepic}/death/{i}.png')}")
                self.image = pygame.transform.scale(img, (img.get_width()*self.scale ,img.get_height()*self.scale))
                temp_list.append(self.image)
        else:        
            for i in range(1,9):
                img = pygame.image.load(f"{Path(f'resources/picture/{self.namepic}/death/{i}.png')}")
                self.image = pygame.transform.scale(img, (img.get_width()*self.scale ,img.get_height()*self.scale))
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
        damage = (self.strength + rand) - (self.defence)
        if damage < 0 :
            damage = 0
        target.hp -= damage 
        #run enemy animation
        target.hurt() 
        # effect
        for i in range(1,5):
            atkeffect = pygame.image.load(f"{Path(f'resources/picture/effect/atk/atk ({i}).png')}")
            sc.screen.blit(atkeffect, (target.rect.centerx - 110, target.rect.y - 50))
            pygame.display.flip()
            clock.tick(60)
        # check is target died 
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death() 
            
        damage_text = dt.DamageText(target.rect.centerx, target.rect.y, str(damage), font.RED)
        dt.damage_text_group.add(damage_text)
        #the names for game log (-haarith, needs work not showing name of the user)
        gamelog.game_logs.append(f'{self.name} attacked {target.name} for {damage} damage')
        gamelog.game_logs.append(f'{target.name} blocked {(target.defence)} damage from {self.name}')
        
        #set variable to attack
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def magic(self, target):
        #deal magic damage to the enemy
        # currently i use for delete enemy with 999 dmg
        # za wa ru do !!!
        damage = 999
        if damage < 0 :
            damage = 0
        target.hp -= damage 
        #run enemy animation
        target.hurt() 
        # effect
        for i in range(1,21):
            atkeffect = pygame.image.load(f"{Path(f'resources/picture/effect/magic/magic ({i}).png')}")
            sc.screen.blit(atkeffect, (600, 50))
            pygame.display.update()
            clock.tick(10)


        #set variable to attack
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


        #check is target died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death() 
        damage_text = dt.DamageText(target.rect.centerx, target.rect.y, str(damage), font.RED)
        dt.damage_text_group.add(damage_text)
        #the names for game log (-haarith, needs work not showing name of the user)
        gamelog.game_logs.append(f'{self.name} attacked {target.name} for {damage} damage')
        gamelog.game_logs.append(f'{target.name} get burst by {self.name}, IS MAGIC')
        gamelog.game_logs.append(f'{self.name} use ZAWARU DO !!!')
        
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
        # Draw the unit image
        sc.screen.blit(self.image, self.rect)
        # Draw the units name
        sc.draw_text(self.name, font.hp_font, font.RED, self.rect.centerx - 30, self.rect.y - 20)


