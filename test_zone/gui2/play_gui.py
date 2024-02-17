import pygame

class PlayGUI(pygame.sprite.Sprite):
    def __init__(self, sprite_group: pygame.sprite.Group, scene: object, game: object):
        super().__init__()
        self.units = {}
        self.scene = scene
        self.game = game
        self.pointer = 0
        self.selecting = False
        
        self.gui_buttons = []
        
        # Create a numbered dictionary from the sprite group so it's easier to navigate
        for i, sprite in enumerate(sprite_group.sprites()):
            self.units[i] = sprite
            
        self.image = pygame.Surface((100, 200))
        self.image.fill("grey")
        self.rect = self.image.get_rect() # get rekt
        
        # Sets initial position of the gui
        self.rect.midleft = self.units[i].rect.midright
        
        self.attack_button = GUIText("Attack")
        self.gui_buttons.append(self.attack_button)
        
        self.shop_button = GUIText("Shop")
        self.gui_buttons.append(self.shop_button)
        
        self.scene.ui_front.add([self.attack_button, self.shop_button])
        
    def position_buttons(self, offset):
        start_x, start_y = self.rect.midtop
        
        for button in self.gui_buttons:
            button.rect.center = (start_x, start_y)
            start_y += offset
            
    def deselect_buttons(self):
        for button in self.gui_buttons:
            button.selected = False
        
    def update(self):
        self.deselect_buttons()
        self.position_buttons(40)
        
        self.scene.pointer = self.scene.pointer % len(self.units)
        self.pointer = self.pointer % len(self.gui_buttons)
        
        self.rect.midleft = self.units[self.scene.pointer].rect.midright
        
        if self.selecting:
            if self.game.actions["down"]:
                self.pointer -= 1
            
            if self.game.actions["up"]:
                self.pointer += 1
            
            if self.game.actions["escape"]:
                self.selecting = False
                
        if self.pointer == 0:
            self.attack_button.selected = True
        
        if self.pointer == 1:
            self.shop_button.selected = True
            
        print(self.selecting, self.pointer, self.game.actions["down"])
        
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
        