import pygame
import random 

import gui2.ui_functions as ui_functions
import classes.class_functions as cf

from scenes.scene import Scene
from scenes.play import Play

import resources2.images
# input1_rect = pygame.Rect(80, 280, 170, 32)


class CreateChar(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        self.background = pygame.Surface((1, 1))
        self.sprites = pygame.sprite.Group()
        
        # temp = ui_functions.Button(80, 200, 'white', 170, 32)

        self.player_list = [("Slashy", "Reaper"),
                            ("Tiger", "Knight"),
                            ("Joker", "Tank")]
        
        #random name and random classes 

        class_list = ['Knight', 'Reaper', 'Tank', 'Bandit']
        self.enemy_list = []
        for i in range(self.game.max_enemies):
            name  = 'AI ' + str(random.randint(10, 99))
            classes = random.choice(class_list)
            enemy =  (name, classes)
            self.enemy_list.append(enemy)
        

        cf.create_team(self.player_list, "player", self.game)
        cf.create_team(self.enemy_list, "enemy", self.game)
        
        temporary_text = ui_functions.TextSprite("INCOMPLETE CHARACTER CREATION SCREEN", 50)
        temporary_text.add(self.sprites)
        
        temporary_text2 = ui_functions.TextSprite("PRESS ENTER TO CONTINUE", 30, None, "white", True, 550)
        temporary_text2.add(self.sprites)
        
    def update(self, actions):
        if actions["escape"]:
            self.exit_scene()
            
        if actions["enter"]:            
            next_scene = Play(self.game)
            next_scene.start_scene()
            
        self.game.reset_keys()
        self.sprites.update()
    
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))
        self.sprites.draw(self.game.canvas)