# Parent class for the different scenes
import pygame

from gui2 import ui_functions
import gui2.screen as scr


class Scene:
    def __init__(self, game: object):
        self.game = game
        self.prev = None
        self.xc = scr.SCREEN_WIDTH // 2
        self.yc = scr.SCREEN_HEIGHT // 2

        self.sprites = pygame.sprite.Group()
        self.button_sprites = pygame.sprite.Group()
        self.text_sprites = pygame.sprite.Group()

    def update(self, actions):
        pass

    def render(self, screen):
        pass

    def start_scene(self):
        # If this is not the only (bottom) item in the stack
        if len(self.game.stack) > 1:

            # Previous state allows us to render the previous scene so we can overlay menus on top
            self.prev = self.game.stack[-1]

        # Add ourselves to the end of the state stack
        self.game.stack.append(self)

    def exit_scene(self):
        # Removes ourselves from the list as we go back down the stack
        self.game.stack.pop()

    def create_button(
        self,
        text,
        size,
        font,
        text_color,
        rect_width,
        rect_height,
        rect_fill,
        name,
        x=True,
        y=True,
        button_alpha=100,
        text_alpha=255,
    ):
        """Appends a TextSprite and Button object to the scene's self.sprites group"""
        button_sprite = ui_functions.Button(
            rect_width, rect_height, rect_fill, x, y, name, button_alpha
        )
        text_sprite = ui_functions.TextSprite(
            text, size, font, text_color, x, y, name, 0, 0, text_alpha
        )

        # Put the button and sprite into their own groups so they can be indexed the same way
        # THIS SYSTEM WILL BREAK IF EITHER GROUP GETS MODIFIED (index will change)
        self.button_sprites.add(button_sprite)
        self.text_sprites.add(text_sprite)

        self.sprites.add([button_sprite, text_sprite])

        return button_sprite, text_sprite

    def generate_buttons(
        self,
        button_list,
        text_size,
        font,
        font_color,
        width,
        height,
        fill,
        xy: tuple,
        offset: tuple,
        button_alpha=100,
        text_alpha=255,
    ):
        """Generates multiple buttons using an input list of strings and outputs them into the scene's self.sprites group"""
        start_x, start_y = xy
        offset_x, offset_y = offset

        if start_x is True:
            start_x = scr.SCREEN_WIDTH // 2
        if start_y is True:
            start_y = scr.SCREEN_HEIGHT // 2

        for button in button_list:
            self.create_button(
                button,
                text_size,
                font,
                font_color,
                width,
                height,
                fill,
                button,
                start_x,
                start_y,
                button_alpha,
                text_alpha,
            )
            start_x += offset_x
            start_y += offset_y

    def create_dict(self, sprite_group):
        """Create enumerated dictionary from sprite group"""
        sprite_dict = {}

        for i, sprite in enumerate(sprite_group.sprites()):
            sprite_dict[i] = sprite

        return sprite_dict

    def update_alive_dict(self):
        """Using a dictionary allows us to update our characters based on their key rather than appending an infinite list of characters per cycle"""
        self.alive_enemy_dict = {}
        self.alive_player_dict = {}

        for i, sprite in enumerate(self.game.players.sprites()):
            if sprite.alive:
                self.alive_player_dict[i] = sprite

        for i, sprite in enumerate(self.game.enemies.sprites()):
            if sprite.alive:
                self.alive_enemy_dict[i] = sprite
