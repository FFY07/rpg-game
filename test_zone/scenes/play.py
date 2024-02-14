import pygame

from scenes.scene import Scene
import resources2.images
import classes.unit
from classes.units.knight import Knight
from scenes.options import Options

class Play(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = resources2.images.background_img

        self.player_test = Knight("John", "player")
        self.test_list = pygame.sprite.Group()
        
        self.game.all_units.add(self.player_test)
        self.test_list.add(self.player_test)
    
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
                sprite.idle_test()
        
        if actions["down"]:
            for sprite in self.game.all_units.sprites():
                sprite.death_test()
        
        for sprite in self.game.all_units.sprites():
            print(sprite.name, sprite.state, sprite.current_frame)
            
        self.game.reset_keys()
        self.game.all_units.update()
        
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))
        self.game.all_units.draw(self.game.canvas)