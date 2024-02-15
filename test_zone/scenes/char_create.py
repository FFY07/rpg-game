import pygame
import sys

import gui2.ui_functions as ui_functions
import classes.class_functions as cf

from scenes.scene import Scene
from scenes.play import Play

import resources2.images

class CreateChar(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        self.background = resources2.images.char_create_background
        self.sprites = pygame.sprite.Group()
        
        self.player_list = [("Slashy", "Reaper"),
                            ("Tiger", "Knight"),
                            ("Joker", "Tank")]
        
        self.enemy_list = [("Quinn", "Bandit"),
                           ("Kuyz", "Knight"),
                           ("Ampersand", "Reaper")]
        
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