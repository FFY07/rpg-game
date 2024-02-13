import pygame

from scenes.scene import Scene
import resources2.images
import classes.class_functions as cf
from scenes.options import Options

class Play(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = resources2.images.background_img
                
        player_positions = [(300, 210), 
                            (230, 260), 
                            (160, 310)]

        enemy_positions = [(720, 200),
                           (790, 250),
                           (860, 300)]

        player_list = [("Southpaw", "Reaper"),
                       ("Genesis", "Knight"),
                       ("Akshan", "Knight"),]
        
        cf.create_team(player_list, "player", self.game)
        cf.set_positions(player_positions, self.game.players)
    
        for sprite in self.game.all_units.sprites():
            for k, v in sprite.animations.items():
                print(k, len(v))
    
    def update(self, actions):
        if actions["escape"]:
            next_scene = Options(self.game)
            next_scene.start_scene()
        
        if actions["enter"]:
            for sprite in self.game.all_units.sprites():
                if sprite.name == "Southpaw":
                    sprite.action = "attack"
                    # print(sprite.frame, len(sprite.animations["attack"]))
        
        self.game.reset_keys()
        self.game.all_units.update()
        
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))
        self.game.all_units.draw(self.game.canvas)