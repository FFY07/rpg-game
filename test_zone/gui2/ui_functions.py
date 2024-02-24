from pathlib import Path

import pygame
import gui2.screen as scr


def store_text(name: str, text_group, game: object):
    if game.text_ready:
        for sprite in text_group.sprites():
            if sprite.name == name:
                sprite.text = game.text_buffer

        # Also return the text if necessary
        buffered_text = game.text_buffer

        game.text_buffer = ""
        game.text_ready = False

        return buffered_text


class TextSprite(pygame.sprite.Sprite):
    # Creates a text sprite; replace me with a docstring once all the parameters are done
    def __init__(
        self,
        text: str,
        size: int,
        text_font="freesansbold",
        color="white",
        x_centered=True,
        y_centered=True,
        name=False,
        dx=0,
        dy=0,
        alpha=255,
    ):
        """Generates a text sprite

        Args:
            text (str): The text to display
            size (int): The size of the text
            text_font (str, optional): The font name. Defaults to "freesansbold".
            color (str, optional): The font color. Defaults to "white".
            x (bool, optional): The x coordinate. True = Centered.
            y (bool, optional): The y coordinate. True = Centered.
            dx (bool, optional): Movement along x coordinate. Defaults to 0
            flying (bool, optional): Movement along y coordinate. Default to 0
        """
        super().__init__()
        self.selected = True
        self.toggled = False
        self.name = name
        self.text = text
        self.color = color
        self.alpha = alpha

        if x_centered is True:
            self.x = scr.SCREEN_WIDTH // 2
        else:
            self.x = x_centered

        if y_centered is True:
            self.y = scr.SCREEN_HEIGHT // 2
        else:
            self.y = y_centered

        self.dx = dx
        self.dy = dy

        self.font = pygame.font.SysFont(text_font, size)
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        pass

    def update(self):
        self.image = self.font.render(self.text, True, self.color)

        self.rect.move_ip(self.dx, self.dy)

        # Check if we're going upwards
        if self.dy < 0:
            if self.rect.bottom < 0:
                self.kill()
        else:
            if self.rect.top > scr.SCREEN_HEIGHT:
                self.kill()

        # EVERYTHING HERE IS NOT TESTED BECAUSE IDK WHICH SIDE IS WHICH
        if self.dx < 0:
            if self.rect.left < 0:
                self.kill()
        else:
            if self.rect.right > scr.SCREEN_WIDTH:
                self.kill()

        if self.selected:
            self.image.set_alpha(self.alpha)
        else:
            self.image.set_alpha(100)


class Button(pygame.sprite.Sprite):
    def __init__(self, width, height, color, x=True, y=True, name=False, alpha=100):
        super().__init__()
        self.width = width
        self.height = height
        self.name = name

        if x is True:
            self.x = scr.SCREEN_WIDTH // 2
        else:
            self.x = x

        if y is True:
            self.y = scr.SCREEN_HEIGHT // 2
        else:
            self.y = y

        self.color = color
        self.alpha = alpha

        self.selected = False
        self.toggled = False

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.image.set_alpha(self.alpha)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        pass

    def update(self):
        if self.toggled:
            self.image.fill("red")
            self.image.set_alpha(self.alpha)

        elif self.selected:
            self.image.fill(self.color)
            self.image.set_alpha(self.alpha)

        else:
            self.image.fill(self.color)
            self.image.set_alpha(0)


class TargetImage(pygame.sprite.Sprite):
    def __init__(self, scene, image, x_offset=0, y_offset=0):
        """Updates position based on the scene's self.selected_unit"""

        super().__init__()
        self.scene = scene
        self.target_sprite = scene.selected_unit
        self.target_x, self.target_y = self.target_sprite.rect.center
        self.selected = True

        self.x_offset = x_offset
        self.y_offset = y_offset

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (
            self.target_x + self.x_offset,
            self.target_y + self.y_offset,
        )

    def update(self):
        self.target_sprite = self.scene.selected_unit
        self.target_x, self.target_y = self.target_sprite.rect.center

        self.rect.center = (
            self.target_x + self.x_offset,
            self.target_y + self.y_offset,
        )

        if self.selected:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(0)


class HitImage(pygame.sprite.Sprite):
    def __init__(self, attack_name, target: object, speed=50, width=256, height=256):
        super().__init__()
        self.target = target
        self.attack_name = attack_name

        self.width = width
        self.height = height

        self.current_frame = 0
        self.last_updated = 0
        self.current_time = 0

        self.animations = []

        self.load_attack_sprites()

        self.anim_speed = speed  # ticks

    def update(self):
        self.current_time = pygame.time.get_ticks()

        if self.current_time - self.last_updated > self.anim_speed:
            self.last_updated = self.current_time
            self.current_frame += 1

            # print(self.target.name, self.current_frame)

        if self.current_frame < len(self.animations):
            self.image = self.animations[self.current_frame]
            self.rect = self.image.get_rect()
            self.rect.center = self.target.rect.center

        else:
            # print(self.current_frame, self.animations)
            self.kill()

    def load_attack_sprites(self):
        """Load attack sprite images"""

        path = Path(f"test_zone/resources2/images/effect/{self.attack_name}")
        image_list = list(path.glob("*.*"))

        # Load images as pygame surfaces

        for frame in image_list:
            image = pygame.image.load(frame)

            # Size of image
            image = pygame.transform.scale(
                image,
                (
                    self.width,
                    self.height,
                ),
            )

            self.animations.append(image)


class RectGUI(pygame.sprite.Sprite):
    def __init__(
        self,
        x=57,
        y=100,
        width=700,
        height=143,
        color="white",
        name=0,
        border_color="grey",
        game=None,
    ):
        super().__init__()
        self.sprites = pygame.sprite.Group()
        self.game = game

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.selected = False

        self.name = name
        self.color = color
        self.border_color = border_color
        self.default_border_color = self.border_color
        self.default_color = self.color
        self.selected_button = 0
        # #(57, 100, 853, 143, 213)
        # self.rect = pygame.Rect(x , y, width, height)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.image.set_alpha(255)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.player_text = TextSprite(
            f"Player {name + 1} ",
            25,
            "Impact",
            "white",
            self.rect.center[0] - 290,
            self.rect.center[1] - 50,
        )

        self.name_text = TextSprite(
            "Name: ",
            25,
            None,
            "white",
            self.rect.center[0] - 190,
            self.rect.center[1] - 45,
        )

        # self.name_button = "button object"
        self.selected_name = TextSprite(
            "Type here",
            30,
            None,
            "grey27",
            self.rect.center[0] - 50,
            self.rect.center[1] - 45,
            f"T{self.name}",
        )

        self.class_text = TextSprite(
            "Class: ",
            25,
            None,
            "white",
            self.rect.center[0] - 190,
            self.rect.center[1] + 5,
        )

        self.class_button = "another button here"

        # Don't forget to put the buttons into the sprites below
        self.sprites.add(
            [self.player_text, self.name_text, self.class_text, self.selected_name]
        )

    def update(self):
        # self.image.scale()
        if self.selected:
            self.border_color = "white"
            self.color = "white"
            # self.selected_name.text = self.game.text_buffer

        else:
            self.border_color = self.default_border_color
            self.color = self.default_color

        # store_text(f"T{self.name}", self.sprites, self.game)
        self.sprites.update()

    def draw(self, screen):
        pygame.draw.rect(screen, self.border_color, self.rect, 5)
        self.sprites.draw(screen)
