# Main menu scene
# This is our default scene when starting the game
import pygame

from scenes.scene import Scene
import resources2.images
from gui2 import ui_functions

from scenes.char_create import CreateChar

class MainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = resources2.images.menubackground_img
    
        self.sprites = pygame.sprite.Group()
    
    def update(self, actions):
        if actions["enter"]:
            # Initialise the next scene
            next_scene = CreateChar(self.game)
            
            # Then plop it onto the stack
            next_scene.start_scene()

            
        self.game.reset_keys()
        self.sprites.update()
        
        print(actions)
    
    def render(self, screen):
        screen.blit(self.background, (0, 0))
        text = ui_functions.TextSprite("Main Menu", 40)
        
        self.sprites.add(text)
        self.sprites.draw(self.game.canvas)