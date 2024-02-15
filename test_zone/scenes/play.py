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
        
        # unit stands here when they want to attack\
        self.crazy_guy = cf.create_unit("William", "Tank", "enemy", self.game)
        self.crazy_guy.dx = 5
        
        self.player_active_position = (self.xc - 100, self.yc)
        self.enemy_active_position = (self.xc + 100, self.yc)
        
        # testing coordinates
        self.player_positions = [(self.xc - 500, self.yc + 150),
                                (self.xc - 375, self.yc),
                                (self.xc - 250, self.yc - 150)
        ]
        
        self.enemy_positions = [(self.xc + 500, self.yc + 150),
                                (self.xc + 375, self.yc),
                                (self.xc + 250, self.yc - 150)
        ]
        
        text = ui_functions.TextSprite("PRESS WASD TO PARTY", 50, None, "white", True, self.yc)
        self.text_sprites.add(text)
        text = ui_functions.TextSprite("Press Space to activate character with self.id == 0", 30, None, "white", True, self.yc + 100)
        self.text_sprites.add(text)
        
        cf.set_positions(self.player_positions, self.game.players)
        cf.set_positions(self.enemy_positions, self.game.enemies)
    
    def update(self, actions):
        if self.crazy_guy.rect.left > scr.SCREEN_WIDTH - 64:
            self.crazy_guy.dx = - 5
        elif self.crazy_guy.rect.right < 64:
            self.crazy_guy.dx = 5
            
        if actions["space"]:
            for sprite in self.game.all_units.sprites():
                if sprite.id == 0:
                    if not sprite.selected:
                        sprite.activate(self.player_active_position)
                    else:
                        sprite.deactivate()
        
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
        #     print(sprite.name, sprite.state, sprite.id, sprite.rect)
            
        self.game.reset_keys()
        self.text_sprites.update()
        self.game.all_units.update()
        
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))
        
        # Rendering order (last to render = on top)
        self.text_sprites.draw(self.game.canvas)
        self.game.all_units.draw(self.game.canvas)