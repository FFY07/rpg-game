import pygame

from pathlib import Path

import resources.images as images

class Toothless(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

        self.animations = []
        self.current_sprite = 0

        path = Path(f"resources/images/toothless")
        image_list = list(path.glob("*.*"))

        # Load images as pygame surfaces

        for frame in image_list:
            image = pygame.image.load(frame).convert_alpha()

            # # Size of image
            # image = pygame.transform.scale(
            #     image,
            #     (
            #         self.width,
            #         self.height,
            #     ),
            # )

            self.animations.append(image)
        self.image = self.animations[self.current_sprite] 

        self.rect = self.image.get_rect()
        self.rect.midbottom = [self.x, self.y]


    def update(self,speed):
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.animations):
                self.current_sprite = 0
                self.attack_animation = False

            self.image = self.animations[int(self.current_sprite)]