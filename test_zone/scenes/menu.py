# Main menu scene
# This is our default scene when starting the game
import pygame

from scenes.scene import Scene
from gui2 import ui_functions

class MainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)
    
        self.sprites = pygame.sprite.Group()    
    
    def update(self, actions):
        self.game.reset_keys()
        self.sprites.update()
    
    def render(self, screen):
        screen.fill("darkgrey")
        text = ui_functions.TextSprite("Main Menu", 40)
        self.sprites.add(text)
        self.sprites.draw(self.game.canvas)