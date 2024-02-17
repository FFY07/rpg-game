import pygame

import gui2.screen as scr

from scenes.scene import Scene
from scenes.attack import Attack

import gui2.ui_functions as ui_functions
from gui2.play_gui import PlayGUI
import resources2.images

from classes import class_functions as cf

from scenes.options import Options

class Play(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = resources2.images.background_img
        self.ui_sprites = pygame.sprite.Group()
        self.pointer = 0

        # self.crazy_guy = cf.create_unit("William", "Reaper", "enemy", self.game)
        # self.crazy_guy.dx, self.crazy_guy.dy = 5, 5
                
        # unit stands here when they want to attack
        # self.player_active_position = (self.xc - 100, self.yc)
        # self.enemy_active_position = (self.xc + 100, self.yc)
        
        # testing coordinates
        self.player_positions = [(self.xc - 500, self.yc + 150),
                                (self.xc - 375, self.yc),
                                (self.xc - 250, self.yc - 150)
        ]
        
        self.enemy_positions = [(self.xc + 500, self.yc + 150),
                                (self.xc + 375, self.yc),
                                (self.xc + 250, self.yc - 150)
        ]
        
        # self.ui_sprites.add(ui_functions.TextSprite("Type", 30, "freesansbold", "white", self.xc - 200, self.yc + 200, "typing"))
        # self.ui_sprites.add(ui_functions.TextSprite("[Last msg]", 20, "freesansbold", "white", self.xc - 300, self.yc + 300, "lastmsg"))
        
        cf.set_positions(self.player_positions, self.game.players)
        cf.set_positions(self.enemy_positions, self.game.enemies)
        
        # Dictionaries make life easier (give up on sprite groups mode)
        self.all_players = {}
        self.all_enemies = {}
        
        for i, sprite in enumerate(self.game.players.sprites()):
            self.all_players[i] = sprite     
        self.alive_players = self.all_players
        
        for i, sprite in enumerate(self.game.enemies.sprites()):
            self.all_enemies[i] = sprite        
        self.alive_enemies = self.all_enemies
    
    # Currently unused
    def select_player(self, pointer):
        self.all_players[pointer].selected = True
            
    def select_enemy(self, pointer):
        self.all_enemies[pointer].selected = True

    
    def update(self, actions):
        # self.current_text = ui_functions.store_text("lastmsg", self.ui_sprites, self.game)
        
        # # Print it if it is not empty
        # if self.current_text:
        #     print(self.current_text)
        
        # if self.crazy_guy.rect.left > scr.SCREEN_WIDTH - 64:
        #     self.crazy_guy.dx = - 5
        # elif self.crazy_guy.rect.right < 64:
        #     self.crazy_guy.dx = 5

        # if self.crazy_guy.rect.top > scr.SCREEN_HEIGHT - 64:
        #     self.crazy_guy.dy = - 5
        # elif self.crazy_guy.rect.bottom < 64:
        #     self.crazy_guy.dy = 5
            
        # for sprite in self.ui_sprites:
        #     if sprite.name == "typing":
        #         sprite.text = self.game.text_buffer
        
        # Reset the selected state of all sprites at the start of each loop
        for sprite in self.game.all_units.sprites() or sprite in self.ui_sprites.sprites():
            sprite.selected = False
        
        # Constrains the pointer to the length of the player list
        # This will break if the teams are uneven!!!
        self.pointer = self.pointer % len(self.all_players)
        
        # Select player based on pointer position
        self.selected_player = self.all_players[self.pointer]
        

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
            self.pointer += 1
        
        if actions["down"]:
            self.pointer -= 1
            
        if actions["enter"]:
            # self.game.typing = True
            next_scene = Attack(self.game, self.selected_player)
            next_scene.start_scene()
        
        print(self.pointer, self.selected_player)
        
        self.ui_sprites.update()
        self.game.all_units.update()
        
        self.game.reset_keys()
        
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))
        
        # Rendering order (last to render = on top)
        self.ui_sprites.draw(screen)
        self.game.all_units.draw(screen)