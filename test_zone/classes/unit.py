from pathlib import Path

import pygame
import gui2.screen as scr

MAX_HEALTH = 100
MANA = 50

START_LEVEL = 1
BASE_EXP = 0
EXP_TO_NEXT_LEVEL = 100

COINS = 0

# IMPORTANT: UPDATE THIS WHEN ADDING A NEW CLASS
unit_list = ["Knight",
             "Reaper",
             "Bandit",
             "Tank"]

# Note: check knight.py for class-specific references

class Unit(pygame.sprite.Sprite):
    def __init__(self, name, team, id_no = 0):
        super().__init__()
        self.max_health = MAX_HEALTH
        self.health = self.max_health
        self.mana = MANA
        
        self.level = START_LEVEL
        self.exp = BASE_EXP
        self.exp_to_next_level = EXP_TO_NEXT_LEVEL
        
        self.coins = COINS
        
        self.selected = False
        self.direction = "right"
        self.id = id_no
        
        self.name = name
        self.size_scale = 2
        self.unit_class = "Knight"
        
        # Starting position
        self.position = (scr.SCREEN_WIDTH // 2, scr.SCREEN_HEIGHT // 2)

        self.current_frame = 0
        self.last_updated = 0
        self.dx = 0
        self.dy = 0 
        self.state = "idle"
        self.states = ["idle",
                       "attack",
                       "hurt",
                       "defend",
                       "death"
        ]
        self.animations = {}
        
    def load_animations(self):
        for state in self.states:
            path = Path(f"test_zone/resources2/images/units/{self.unit_class}/{state}")
            image_list = (list(path.glob("*.*")))
            
            # Load images as pygame surfaces
            loaded_images = []
            for frame in image_list:
                image = pygame.image.load(frame)
                image = pygame.transform.scale(image, (image.get_width()*self.size_scale, image.get_height()*self.size_scale))
            
                if self.direction == "right":
                    loaded_images.append(image)
                    
                elif self.direction == "left":
                    image = pygame.transform.flip(image, True, False)
                    loaded_images.append(image)
        
            self.animations[state] = loaded_images
                
    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_updated > 100 and self.current_frame != -1:
            self.last_updated = current_time
            self.current_frame += 1
        
        # Resets back to idle frame after completing an animation state
        if self.current_frame >= len(self.animations[self.state]) and self.state != "death":
            self.current_frame = 0
            self.state = "idle"
            
        # Leaves character dead body on the ground
        elif self.current_frame >= len(self.animations[self.state]) and self.state == "death":
            self.current_frame = -1

        self.image = self.animations[self.state][self.current_frame]
        self.rect.move_ip(self.dx, self.dy)
                
    def state_change(self, target_state):
        """Resets the current frame to 0 so the animation doesn't start halfway"""
        self.current_frame = 0
        self.state = target_state
        
    def attack_test(self):
        self.state_change("attack")
    
    def defend_test(self):
        self.state_change("defend")
    
    def death_test(self):
        self.state_change("death")
        
    def hurt_test(self):
        self.state_change("hurt")