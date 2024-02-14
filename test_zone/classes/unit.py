from pathlib import Path

import pygame


class Unit(pygame.sprite.Sprite):
    def __init__(self, name, team):
        super().__init__()
        self.selected = False
        self.direction = "left"
        
        self.name = name
        self.unit_class = "Reaper"
        self.size_scale = 2
        

        self.current_frame = 0
        self.last_updated = 0
        self.speed = 0
        self.state = "idle"
        self.states = ["idle",
                       "attack",
                       "hurt",
                       "defend",
                       "death"
        ]
        self.animations = {}
        
        self.load_animations()
        
    def load_animations(self):
        for state in self.states:
            path = Path(f"test_zone/resources2/images/units/{self.unit_class}/{state}")
            image_list = (list(path.glob("*.*")))
            
            # Load images as pygame surfaces
            loaded_images = []
            for frame in image_list:
                image = pygame.image.load(frame)
                image = pygame.transform.scale(image, (image.get_width()*self.size_scale, image.get_height()*self.size_scale))
            
                if self.direction == "left":
                    image = pygame.transform.flip(image, True, False)
                    loaded_images.append(image)
                    
                elif self.direction == "right":
                    loaded_images.append(image)
        
            self.animations[state] = loaded_images
                
    def animate(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_updated > 100:
            self.last_updated = current_time
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.state])