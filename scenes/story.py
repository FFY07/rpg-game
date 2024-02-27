import pygame

import gui.ui_functions as ui_functions
from scenes.scene import Scene
import gui.screen as scr
import resources.images as images
import resources.audio as audio

from scenes.play import Play

header = [55, None, "yellow"]
body = [45, None, "white"]


class Story(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        self.background = images.story_background
        self.sprites = pygame.sprite.Group()

        # pygame.mixer.music.load(audio.credits_bgm)
        # pygame.mixer.music.set_volume(self.game.volume)
        # pygame.mixer.music.play(-1, 48, 5000)

        # Can't go below integer so use fps to tune the speed (higher fps = faster)
        self.game.fps = 60
        self.falling_speed = (0, -1)

        # Starting position
        self.position = scr.SCREEN_HEIGHT - 100

        self.load_section(["Aventure to PSB Academy", "Stupid story sorry"], header, 50)
        self.position += 100
        self.load_section(
            [
                "Inside PSB Academy, something wasn't right.",
                "The students were acting strangely",
                "They doing bad things like being a freerider",
                "Not doing their assignment",
                "Using Chatgpt to do all the quiz",
                "You noticed it and decided to stop it with friend",
                # "as all of you went through the keep seeing all the bad stuff",
                # "happening because of the students being idiot.",
                # "PLease kill them",
            ],
            body,
            75,
        )
        self.position += 100
        self.load_section(["Press Enter to Continue"], header, 50)

    def load_section(self, text_list, section_type, offset):
        for text in text_list:
            self.sprites.add(
                ui_functions.TextSprite(
                    text, *section_type, True, self.position, False, *self.falling_speed
                )
            )
            self.position += offset

    def update(self, actions):
        if actions["escape"]:
            self.game.fps = 60
            self.exit_scene()

        if actions["enter"] or actions["space"]:
            self.game.fps = 60
            next_scene = Play(self.game)
            next_scene.start_scene()

        self.sprites.update()
        self.game.reset_keys()

        #  Automatically proceed once story is finished
        if len(self.sprites) == 0:
            self.game.fps = 60
            next_scene = Play(self.game)
            next_scene.start_scene()

    def render(self, screen):
        screen.blit(
            pygame.transform.scale(
                self.background, (self.game.screen_width, self.game.screen_height)
            ),
            (0, 0),
        )
        self.sprites.draw(screen)
