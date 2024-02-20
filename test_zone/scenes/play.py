import pygame

import gui2.screen as scr

from scenes.scene import Scene
from scenes.action import Action

from gui2 import ui_functions
import resources2.images as images
import resources2.audio as audio

from classes import class_functions as cf

from scenes.options import Options

class Play(Scene):
    def __init__(self, game):
        super().__init__(game)
        pygame.mixer.music.load(audio.battle_alt)
        pygame.mixer.music.set_volume(self.game.volume)
        pygame.mixer.music.play(-1)
        
        print("hi")
        
        self.background = images.background_img
        self.ui_sprites = pygame.sprite.Group()
        self.pointer = 1

        # self.crazy_guy = cf.create_unit("William", "Reaper", "enemy", self.game)
        # self.crazy_guy.dx, self.crazy_guy.dy = 5, 5
                
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
        
        # Make a list so we can dynamically adjust our pointer position
        self.player_list = []
        self.enemy_list = []
        self.alive_player_dict = []
        self.alive_enemy_dict = []
        
        for i, sprite in enumerate(self.game.players.sprites()):
            self.player_list.append(sprite)
            if sprite.alive:
                self.alive_player_list[i] = sprite
                
        for i, sprite in enumerate(self.game.enemies.sprites()):
            self.enemy_list.append(sprite)
            if sprite.alive:
                self.alive_enemy_list[i] = sprite
        
        self.selected_unit = self.player_list[0]
    
        self.pointer_image = images.red_arrow_down
        self.pointer_sprite = ui_functions.TargetImage(self, self.pointer_image)
        self.ui_sprites.add(self.pointer_sprite)

    # Currently unused; use only if we need to adjust the unit object's .selected attribute
    # def select_player(self, pointer):
    #     self.player_list[pointer].selected = True
    
    def check_alive(self):
        pass


    
    def update(self, actions):
        
        # self.current_text = ui_functions.store_text("lastmsg", self.ui_sprites, self.game)
        
        # # Print it if it is not empty
        # if self.current_text:
        #     print(self.current_text)
            
        # for sprite in self.ui_sprites:
        #     if sprite.name == "typing":
        #         sprite.text = self.game.text_buffer
        
        # Reset the selected state of all sprites at the start of each loop
        for sprite in self.game.all_units.sprites() or sprite in self.ui_sprites.sprites():
            sprite.selected = False
            
            # # get rid of dead sprites
            # if not sprite.alive:
            #     sprite.kill()
            # We cannot kill the sprite or they won't stay dead on the floor
                
        # Remove dead sprites from list
        for i, sprite in enumerate(self.player_list):
            if not sprite.alive:
                self.player_list.pop(i)
        
        # Constrains the pointer to the length of the player list
        # This will break if the teams are uneven!!!
        self.pointer = self.pointer % len(self.player_list)
        
        # Select player based on pointer position
        try:
            self.selected_unit = self.player_list[self.pointer]
        except:
            # GAME OVER ENEMY WINS SCREEN
            print("Enemy wins!")
        
        if actions["escape"]:
            next_scene = Options(self.game)
            next_scene.start_scene()
        
        if actions["up"]:
            self.pointer += 1
        
        if actions["down"]:
            self.pointer -= 1
            
        if actions["enter"]:
            # self.game.typing = True
            next_scene = Action(self.game, self.selected_unit)
            
            # Create an anchor because we will be returning to this screen
            next_scene.anchor = self
            next_scene.start_scene()
        
        # print(self.pointer, self.selected_unit, self.pointer_sprite.rect)
        
        self.ui_sprites.update()
        self.game.all_units.update()
        
        self.game.reset_keys()
        
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))
        
        # Rendering order (last to render = on top)
        self.ui_sprites.draw(screen)
        self.game.all_units.draw(screen)