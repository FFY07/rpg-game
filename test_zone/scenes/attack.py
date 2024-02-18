import pygame

from scenes.scene import Scene

class Attack(Scene):
    def __init__(self, game: object, selected_unit: pygame.sprite.Sprite):
        super().__init__(game)
        self.sprites = pygame.sprite.Group()
        self.selected_unit = selected_unit
        
        self.x_offset = 50
        self.y_offset = 0
        self.button_x, self.button_y = self.selected_unit.rect.midright
        self.button_x += self.x_offset
        self.button_y += self.y_offset
        
        
        self.anchor = None
        
        self.button_list = ["Attack ⚔", "Items 👛", "Shop 🛒"]
        self.generate_buttons(self.button_list, 30, "segoeuiemoji", "white", 150, 50, "grey20", (self.button_x, self.button_y), (0, 50), 255)
        
        # Create a dictionary for the buttons before we add our pointer sprite image
        self.button_dict = self.create_dict(self.sprites)
        self.pointer = 0
        
    def update(self, actions):       
        self.pointer = self.pointer % len(self.button_list)
        
        for sprite in self.sprites.sprites():
            sprite.selected = False

        if actions["down"]:
            self.pointer += 1
        
        if actions["up"]:
            self.pointer -= 1
            
        if self.pointer == 0:
            for _, sprite in self.button_dict.items():
                if sprite.name == "Attack ⚔":
                    sprite.selected = True
            
            if actions["enter"]:
                self.selected_unit.state_change("attack")
                print("Opening targeting scene! (haven't code yet :P)")
        
        if self.pointer == 1:
            for _, sprite in self.button_dict.items():
                if sprite.name == "Items 👛":
                    sprite.selected = True
                    
            if actions["enter"]:
                print("Opening inventory (haven't code yet :/)")
        
        if self.pointer == 2:
            for _, sprite in self.button_dict.items():
                if sprite.name == "Shop 🛒":
                    sprite.selected = True
                    
            if actions["enter"]:
                print("Opening shop (haven't code yet D:)")
        
        if actions["escape"] or actions["enter"]:
            self.sprites.empty()
            self.exit_scene()
            
        self.game.reset_keys()
        self.sprites.update()
        self.game.all_units.update()
        
    def render(self, screen):
        self.anchor.render(screen)
        self.sprites.draw(screen)