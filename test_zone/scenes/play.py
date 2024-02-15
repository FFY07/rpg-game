import pygame

import gui2.screen as scr

from scenes.scene import Scene

import gui2.ui_functions as ui_functions
import resources2.images

from classes import class_functions as cf

from scenes.options import Options

class Play(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = resources2.images.background_img
        self.text_sprites = pygame.sprite.Group()
        
        # unit stands here when they want to attack
        
        self.crazy_guy = cf.create_unit("William", "Knight", "player", self.game)
        self.crazy_guy.dx = 500
        
        self.player_active_position = (300, 400)
        self.enemy_active_position = (500, 400)
        
        # temporary list just for testing
        self.player_positions = [(400, 300),
                                 (370, 400),
                                 (340, 500)
        ]
        
        self.enemy_positions = [(600, 300),
                                (570, 400),
                                (540, 500)
        ]
        
        text = ui_functions.TextSprite("PRESS WASD TO DANCE", 50, None, "white", True, 400)
        self.text_sprites.add(text)
        
        cf.set_positions(self.player_positions, self.game.players)
        cf.set_positions(self.enemy_positions, self.game.enemies)

        # self.knight_test.position = ((scr.SCREEN_WIDTH // 2) + 100, scr.SCREEN_HEIGHT // 2)
        # self.reaper_test.position = ((scr.SCREEN_WIDTH // 2) - 100, scr.SCREEN_HEIGHT // 2)
    
    def update(self, actions):
        # print(self.crazy_guy.rect, self.crazy_guy.dx)
        if self.crazy_guy.rect[0] > scr.SCREEN_WIDTH:
            self.crazy_guy.rect[0] = 0
            print("whee")
        
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
        
        # for sprite in self.game.all_units.sprites():
        #     print(sprite.name, sprite.state, sprite.id, sprite.strength, sprite.defence)
            
        self.game.reset_keys()
        self.text_sprites.update()
        self.game.all_units.update()
        
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))
        self.text_sprites.draw(self.game.canvas)
        self.game.all_units.draw(self.game.canvas)