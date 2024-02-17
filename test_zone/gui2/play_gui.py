import pygame

import resources2.images

class PlayGUI(pygame.sprite.Sprite):
    def __init__(self, sprite_group: pygame.sprite.Group, scene: object, game: object):
        super().__init__()
        self.units = {}
        self.enemy_units = {}
        self.scene = scene
        self.game = game
        self.pointer = 0
        self.target_pointer = 0
        
        # Selecting the unit
        self.selecting = False
        self.targeting = False
        
        self.gui_buttons = {}
        
        # Create a numbered dictionary from the sprite group so it's easier to navigate
        self.load_sprites(sprite_group)
            
        self.image = pygame.Surface((100, 200))
        self.image.fill("grey")
        self.rect = self.image.get_rect() # get rekt
        
        # Sets initial position of the gui
        self.rect.midleft = self.units[0].rect.midright
        
        self.attack_button = GUIText("Attack")
        self.gui_buttons[0] = self.attack_button
        # UNHARDCODE THIS LATER PUT INTO A FOR LOOP FUNCTION THAT ACCEPTS A LIST
        self.shop_button = GUIText("Shop")
        self.gui_buttons[1] = self.shop_button
        
        self.target_icon = TargetCircle()
        
        self.scene.ui_front.add([self.attack_button, self.shop_button, self.target_icon])
        
    def load_sprites(self, sprite_group):
        index = 0
        for sprite in sprite_group.sprites():
            if sprite.team == "player":
                self.units[index] = sprite
                index += 1
                
        index = 0
        for sprite in sprite_group.sprites():
            if sprite.team == "enemy":
                self.enemy_units[index] = sprite
                index += 1
                
        # Can't use enumerate because the enemy list will start after player list
                
    def position_buttons(self, offset):
        start_x, start_y = self.rect.midtop
        
        for _, button in self.gui_buttons.items():
            button.rect.center = (start_x, start_y)
            start_y += offset
            
    def deselect_buttons(self):
        for _, button in self.gui_buttons.items():
            button.selected = False
            
    def position_targeting_icon(self):
        self.target_icon.rect.midbottom = self.enemy_units[self.target_pointer].rect.midtop
    
    def update(self):      
        self.scene.pointer = self.scene.pointer % len(self.units)
        self.pointer = self.pointer % len(self.gui_buttons)
        self.target_pointer = self.target_pointer % len(self.enemy_units)
        
        self.deselect_buttons()
        self.position_buttons(40)
        self.position_targeting_icon()
        
        self.rect.midleft = self.units[self.scene.pointer].rect.midright
        
        self.gui_buttons[self.pointer].selected = True
        self.scene.target = self.enemy_units[self.target_pointer]
                    
        if self.selecting:
            if self.game.actions["down"]:
                self.pointer -= 1
            
            if self.game.actions["up"]:
                self.pointer += 1
                
            if self.game.actions["escape"]:
                self.selecting = False
                self.game.reset_keys()
        
        if self.targeting:
            self.game.reset_keys()
            self.selecting = False
            
            if self.game.actions["down"]:
                self.target_pointer -= 1
            
            if self.game.actions["up"]:
                self.target_pointer += 1
                
            if self.game.actions["enter"]:
                self.target_selected = True
            
            if self.game.actions["escape"]:
                self.targeting = False
                self.selecting = True
                self.game.reset_keys()
                
            self.target_selected = False
        
        print(self.selecting, self.pointer, self.targeting, self.target_pointer, self.scene.target)
        
class GUIText(pygame.sprite.Sprite):
    def __init__(self, text = "Enter Text Here", size = 30, font = None, color = "white"):
        super().__init__()
        self.text = text
        self.size = size
        self.color = color
        self.selected = False
        
        self.font = pygame.font.SysFont(font, self.size)
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()

    def update(self):
        if self.selected:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(100)
        
class TargetCircle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = resources2.images.target_img
        self.scale = 5
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * self.scale, self.image.get_height() * self.scale))
        self.rect = self.image.get_rect()
        
    