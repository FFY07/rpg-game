import pygame

from scenes.scene import Scene
import resources2.images
from gui2 import ui_functions

BUTTON_TEXT_SIZE = 30
BUTTON_FONT = "freesansbold"
BUTTON_FONT_COLOR = "white"
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 40
BUTTON_OFFSET = 50

class Options(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = resources2.images.options_background
        self.sprites = pygame.sprite.Group()
        self.pointer = 0
        self.button_list = ["Music", "Sound", "Back", "Menu"]
        
        self.generate_buttons(self.button_list, 30, "freesansbold", "white", 120, 40, "lightgrey", (True, 350), (0, 50))
    
    def update(self, dt, actions):
        # Reset all selected
        for sprite in self.sprites.sprites():
            sprite.selected = False
        
        self.pointer = self.pointer % len(self.button_list)
            
        for sprite in self.sprites.sprites():
            if sprite.name == "Music":
                if self.game.music:
                    self.game.music = False
                    sprite.toggled = True
                else:
                    self.game.music = True
                    sprite.toggled = False
                    
            elif sprite.name == "Sound":
                if self.game.sound:
                    self.game.sound = False
                    sprite.toggled = True
                else:
                    self.game.sound = True
                    sprite.toggled = False
            
        # Music toggle
        if self.pointer == 0:
            for sprite in self.sprites.sprites():
                if sprite.name == "Music":
                    sprite.selected = True
                    
            if actions["enter"]:
                if self.game.music:
                    self.game.music = False
                    pygame.mixer.music.pause()
                    
                else:
                    self.game.music = True
                    pygame.mixer.music.unpause()
        
        # Sound toggle
        if self.pointer == 1:
            for sprite in self.sprites.sprites():
                if sprite.name == "Sound":
                    sprite.selected = True
            
            # Toggles game volume
            if actions["enter"]:
                if self.game.sound:
                    self.game.sound = False
                    self.game.volume = 1
                    
                else:
                    self.game.sound = True
                    self.game_volume = 0
                    
        # Back to previous scene
        if self.pointer == 2:
            for sprite in self.sprites.sprites():
                if sprite.name == "Back":
                    sprite.selected = True
            
            if actions["enter"]:
                self.exit_scene()
                
        if self.pointer == 3:
            for sprite in self.sprites.sprites():
                if sprite.name == "Menu":
                    sprite.selected = True
            
            if actions["enter"]:
                while len(self.game.stack) > 1:
                    self.game.stack.pop()
                
        if actions["down"]:
            self.pointer += 1
        
        if actions["up"]:
            self.pointer -= 1
            
        if actions["escape"]:
            self.exit_scene()
            
        self.game.reset_keys()
        self.sprites.update()
    
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))

        self.sprites.draw(self.game.canvas)