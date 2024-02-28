# Main menu scene
# This is our default scene when starting the game
import pygame

from scenes.scene import Scene
import resources.images
from gui import ui_functions
import resources.fonts as fonts
from scenes.char_create import CreateChar
from scenes.options import Options
from scenes.credits import Credits

BUTTON_TEXT_SIZE = 30
BUTTON_FONT = "freesansbold"
BUTTON_FONT_COLOR = "white"
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 40
BUTTON_OFFSET = 50


class MainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = resources.images.menubackground_img
        self.sprites = pygame.sprite.Group()
        self.pointer = 0
        self.button_list = ["Play", "Options", "Credits", "Quit"]

        self.generate_buttons(
            self.button_list,
            30,
            "freesansbold",
            "white",
            140,
            40,
            "lightgrey",
            (True, 350),
            (0, 50),
        )
        self.title_text = ui_functions.TextSprite(
            "RPG ADVENTURE", 140, fonts.squealer_embossed, "red", True, self.yc - 200
        )

        self.sprites.add(self.title_text)

    def update(self, actions):
        # There should not be any stat guis or sprites here
        for sprite in self.game.all_units.sprites():
            sprite.kill()

        for sprite in self.game.stat_guis.sprites():
            sprite.kill()

        # Reset all selected
        for sprite in self.sprites.sprites():
            sprite.selected = False

        # if self.pointer > len(self.button_list) - 1 or self.pointer < 0:
        # OR we just use maths instead
        self.pointer = self.pointer % len(self.button_list)

        if self.pointer == 0:
            for sprite in self.sprites.sprites():
                if sprite.name == "Play":
                    sprite.selected = True

            if actions["enter"]:
                # Removes any existing units before our character create screen
                for sprite in self.game.all_units.sprites():
                    sprite.kill()

                # Reset the current sprite id
                self.game.current_id = 0

                # Plop the next scene onto the stack

                next_scene = CreateChar(self.game)
                next_scene.start_scene()

        if self.pointer == 1:
            for sprite in self.sprites.sprites():
                if sprite.name == "Options":
                    sprite.selected = True

            if actions["enter"]:

                # Plop the next scene onto the stack
                next_scene = Options(self.game)
                next_scene.start_scene()

        if self.pointer == 2:
            for sprite in self.sprites.sprites():
                if sprite.name == "Credits":
                    sprite.selected = True

            if actions["enter"]:

                # Plop the next scene onto the stack
                next_scene = Credits(self.game)
                next_scene.start_scene()

        if self.pointer == 3:
            for sprite in self.sprites.sprites():
                if sprite.name == "Quit":
                    sprite.selected = True

            if actions["enter"]:

                # Plop the next scene onto the stack
                self.game.running, self.game.playing = False, False

        if actions["down"]:
            self.pointer += 1

        if actions["up"]:
            self.pointer -= 1

        if actions["escape"]:
            self.game.running, self.game.playing = False, False

        self.game.reset_keys()
        self.sprites.update()

    def render(self, screen):
        screen.blit(
            pygame.transform.scale(
                self.background, (self.game.screen_width, self.game.screen_height)
            ),
            (0, 0),
        )

        self.sprites.draw(self.game.canvas)
