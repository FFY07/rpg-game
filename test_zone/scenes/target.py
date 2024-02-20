import pygame

from scenes.scene import Scene

from gui2 import ui_functions

import resources2.images as images

# NOT WRITTEN YET

class ChooseTarget(Scene):
    def __init__(self, game: object, selected_unit: pygame.sprite.Sprite):
        super().__init__(game)
        self.sprites = pygame.sprite.Group()
        self.attacking_unit = selected_unit
        
        self.all_enemies = []
        
        # Add all enemy sprites to a list
        for unit in self.game.enemies.sprites():
            self.all_enemies.append(unit)
        
 
        self.selected_unit = self.all_enemies[0]

    
        # Create pointer image sprite
        self.pointer_image = images.red_arrow_down
        self.pointer_sprite = ui_functions.TargetImage(self, self.pointer_image)
        self.sprites.add(self.pointer_sprite)
        self.pointer = 1
        
    def update(self, actions):
        # Remove dead sprites from list
        for i, sprite in enumerate(self.all_enemies):
            if not sprite.alive:
                self.all_enemies.pop(i)
        
        # Deselect all sprites and kill dead sprites
        for sprite in self.sprites.sprites():
            sprite.selected = False
            # if not sprite.alive:
            #     sprite.kill()
            # We cannot kill the sprite or they won't stay dead on the floor
               
        self.pointer = self.pointer % len(self.all_enemies)
        
        self.selected_unit = self.all_enemies[self.pointer]
            
        if actions["up"]:
            self.pointer += 1
        
        if actions["down"]:
            self.pointer -= 1

        if actions["enter"]:
            self.attacking_unit.basic_attack(self.selected_unit)
        
        if actions["escape"] or actions["enter"]:
            self.sprites.empty()
            while self.game.stack[-1] != self.anchor:
                self.exit_scene()
            
        self.game.reset_keys()
        self.sprites.update()
        self.game.all_units.update()
        
    def render(self, screen):
        self.anchor.render(screen)
        self.sprites.draw(screen)