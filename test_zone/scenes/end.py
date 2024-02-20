import pygame

from scenes.scene import Scene

import resources2.images as images

class GameOver(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        self.sprites = pygame.sprite.Group()
        
    def update(self, actions):       
        if self.game.victor == "player":
            self.result = images.victory_img
        
        else:
            self.result = images.defeat_img
            
        if actions["escape"] or actions["enter"]:
            self.sprites.empty()
            while len(self.game.stack) > 1:
                self.exit_scene()
            
        self.game.reset_keys()
        self.sprites.update()
        self.game.all_units.update()
        
    def render(self, screen):
        screen.blit(self.result)
        self.sprites.draw(screen)