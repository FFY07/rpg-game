import pygame

import gui2.screen as scr

from scenes.scene import Scene

import gui2.ui_functions as ui_functions
import resources2.images

from classes.units.knight import Knight
from classes.units.reaper import Reaper

from scenes.options import Options

class Play(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = resources2.images.background_img
        self.text_sprites = pygame.sprite.Group()
        
        text = ui_functions.TextSprite("PRESS WASD TO DANCE", 50, None, "white", True, 400)
        self.text_sprites.add(text)

        self.reaper_test = Reaper("John", "player")
        self.knight_test = Knight("Sam", "enemy")
        
        self.knight_test.position = ((scr.SCREEN_WIDTH // 2) + 100, scr.SCREEN_HEIGHT // 2)
        self.reaper_test.position = ((scr.SCREEN_WIDTH // 2) - 100, scr.SCREEN_HEIGHT // 2)
        
        self.game.all_units.add(self.knight_test)
        self.game.all_units.add(self.reaper_test)
    
    def update(self, dt, actions):
        if actions["escape"]:
            next_scene = Options(self.game)
            next_scene.start_scene()
            
        if actions["right"]:
            for sprite in self.game.all_units.sprites():
                sprite.attack_test()
                
        if actions["left"]:
            for sprite in self.game.all_units.sprites():
                sprite.defend_test()
        
        if actions["up"]:
            for sprite in self.game.all_units.sprites():
                sprite.hurt_test()
        
        if actions["down"]:
            for sprite in self.game.all_units.sprites():
                sprite.death_test()
        
        for sprite in self.game.all_units.sprites():
            print(sprite.name, sprite.state, sprite.current_frame)
            
        self.game.reset_keys()
        self.text_sprites.update()
        self.game.all_units.update()
        
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))
        self.text_sprites.draw(self.game.canvas)
        self.game.all_units.draw(self.game.canvas)