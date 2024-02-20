import pygame

from scenes.scene import Scene

import resources2.images as images

class GameOver(Scene):
    def __init__(self, game: object, victor: str):
        super().__init__(game)
        self.sprites = pygame.sprite.Group()
        self.victor = victor

        if self.victor == "player":
            self.result = images.victory_img
        
        else:
            self.result = images.defeat_img
        
    def update(self, actions):       
        if actions["escape"] or actions["enter"]:
            for sprite in self.game.all_units:
                sprite.kill()
            pygame.mixer.music.load(self.game.music_path)
            pygame.mixer.music.set_volume(self.game.volume)
            pygame.mixer.music.play(-1)
                
            while len(self.game.stack) > 1:
                self.exit_scene()

        self.game.reset_keys()
        self.sprites.update()
        self.game.all_units.update()
        
    def render(self, screen):
        self.sprites.draw(screen)
        self.prev.render(screen)
        screen.blit(self.result, (self.xc, self.yc))