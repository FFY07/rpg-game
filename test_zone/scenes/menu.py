# Main menu scene
# This is our default scene when starting the game
import pygame

from scenes.scene import Scene
import resources2.images
from gui2 import ui_functions

from scenes.char_create import CreateChar

BUTTON_TEXT_SIZE = 30
BUTTON_FONT = "freesansbold"
BUTTON_FONT_COLOR = "white"
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 40
BUTTON_OFFSET = 50

class MainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = resources2.images.menubackground_img
        self.sprites = pygame.sprite.Group()
        self.pointer = 0
        self.button_list = ["Play", "Options", "Credits", "Quit"]
        
        self.generate_buttons(self.button_list, 30, "freesansbold", "white", 200, 40, "lightgrey", (True, 350), (0, 50))
    
    def navigation_button(self, pointer: int, name: str, actions, dest_scene):
        if pointer == self.pointer:
            for sprite in self.sprites.sprites():
                if sprite.name == name:
                    sprite.selected = True
            
            if actions["enter"]:
                # Plop the next scene onto the stack
                dest_scene.start_scene()
    
    def update(self, actions):
        # Reset all selected
        for sprite in self.sprites.sprites():
            sprite.selected = False
        
        if self.pointer > len(self.button_list) - 1 or self.pointer < 0:
            self.pointer = 0
                    
        self.navigation_button(0, "Play", actions, CreateChar(self.game))
        self.navigation_button(1, "Options", actions, CreateChar(self.game))
        self.navigation_button(2, "Credits", actions, CreateChar(self.game))

        if self.pointer == 3:
            for sprite in self.sprites.sprites():
                if sprite.name == "Quit":
                    sprite.selected = True
            
            if actions["enter"]:
                # Plop the next scene onto the stack
                self.game.running, self.game.playing = False, False
            
        if actions["down"]:
            self.pointer += 1
        
        if actions["up"]:
            if self.pointer == 0:
                self.pointer = len(self.button_list) - 1
                
            else:
                self.pointer -= 1
            
        if actions["escape"]:
            self.game.running, self.game.playing = False, False
            
        self.game.reset_keys()
        self.sprites.update()
        
        # print(len(self.game.stack))
    
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))

        self.sprites.draw(self.game.canvas)