import pygame

from scenes.scene import Scene
import resources2.images
from gui2 import ui_functions
import resources2.audio as audio

BUTTON_TEXT_SIZE = 30
BUTTON_FONT = "freesansbold"
BUTTON_FONT_COLOR = "white"
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 40
BUTTON_OFFSET = 50


class Options(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = resources2.images.options_background
        self.sprites = pygame.sprite.Group()
        self.pointer = 0
        self.button_list = ["Music", "Sound", "Back", "New Game"]

        self.generate_buttons(
            self.button_list,
            30,
            "freesansbold",
            "white",
            120,
            40,
            "lightgrey",
            (True, 350),
            (0, 50),
        )

        self.button_dict = self.create_dict(self.button_sprites)
        self.text_dict = self.create_dict(self.text_sprites)

    def update(self, actions):
        # Reset all selected
        for sprite in self.sprites.sprites():
            sprite.selected = False

        self.pointer = self.pointer % len(self.button_list)

        for sprite in self.sprites.sprites():
            if sprite.name == "Music":
                if self.game.music:
                    self.game.music = False
                    sprite.toggled = False
                else:
                    self.game.music = True
                    sprite.toggled = True

            elif sprite.name == "Sound":
                if self.game.sound:
                    self.game.sound = False
                    sprite.toggled = False
                else:
                    self.game.sound = True
                    sprite.toggled = True

        # Show button and text (button temporarily disabled)

        # self.button_dict[self.pointer].selected = True
        self.text_dict[self.pointer].selected = True

        # Music toggle
        if self.pointer == 0:
            if actions["enter"]:
                pygame.mixer.Sound.play(audio.click_sfx)
                if self.game.music:
                    self.game.music = False

                else:
                    pygame.mixer.Sound.play(audio.click_sfx)
                    self.game.music = True

        # Sound toggle
        if self.pointer == 1:
            # Toggles game sound effects
            if actions["enter"]:
                pygame.mixer.Sound.play(audio.click_sfx)
                if self.game.sound:
                    self.game.sound = False

                else:
                    pygame.mixer.Sound.play(audio.click_sfx)
                    self.game.sound = True

        # Back to previous scene
        if self.pointer == 2:
            if actions["enter"]:
                pygame.mixer.Sound.play(audio.click_sfx)
                self.exit_scene()

        # Back to main menu
        if self.pointer == 3:
            if actions["enter"]:
                pygame.mixer.Sound.play(audio.click_sfx)
                self.sprites.empty()
                pygame.mixer.music.load(self.game.music_path)
                pygame.mixer.music.set_volume(self.game.volume)
                pygame.mixer.music.play(-1)

                while len(self.game.stack) > 1:
                    self.game.stack.pop()

        if actions["down"]:
            pygame.mixer.Sound.play(audio.click_sfx)
            self.pointer += 1

        if actions["up"]:
            pygame.mixer.Sound.play(audio.click_sfx)
            self.pointer -= 1

        if actions["escape"]:
            pygame.mixer.Sound.play(audio.click_sfx)
            # Clear sprites to save resources
            self.sprites.empty()
            self.exit_scene()

        self.game.reset_keys()
        self.sprites.update()

    def render(self, screen):
        screen.blit(
            pygame.transform.scale(
                self.background, (self.game.screen_width, self.game.screen_height)
            ),
            (0, 0),
        )

        self.sprites.draw(screen)
