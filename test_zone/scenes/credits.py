import pygame

import gui2.ui_functions as ui_functions
from scenes.scene import Scene
import gui2.screen as scr
import resources2.images as images
import resources2.audio as audio

title = [55, "hightowertext", "red2"]
desc = [50, "hightowertext", "orangered"]
name = [35, "Palatino Linotype", "grey95"]
note = [40, "hightowertext", "red"]


class Credits(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        self.background = images.credits_background
        self.sprites = pygame.sprite.Group()

        pygame.mixer.music.load(audio.credits_bgm)
        self.game.volume = 0.4
        pygame.mixer.music.play(-1, 48, 5000)

        # Can't go below integer so use fps to tune the speed (higher fps = faster)
        self.game.fps = 60
        self.falling_speed = (0, -1)

        # Starting position
        self.position = scr.SCREEN_HEIGHT - 100

        self.load_section(
            [" — PSB INTRODUCTION TO — ", "PROGRAMMING ASSIGNMENT"], title, 50
        )
        self.position += 150

        self.load_section(["GAME CREATED BY"], desc, 75)

        self.load_section(["Desmond Foo Fong Yoong"], name, 50)
        self.load_section([">9000 lines modified"], note, 100)
        self.load_section(["Haarith Bin Naguri Ibrahim"], name, 50)
        self.load_section([">90 lines modified"], note, 400)

        self.load_section(["GROUP A1 MEMBERS"], desc, 75)
        self.load_section(
            [
                "Desmond Foo Fong Yoong",
                "Haarith Bin Naguri Ibrahim",
                "Haohong Luo",
                "Yi Soon Pong",
                "Xu Xiang (Ye Xuxiang) Yap",
                "Qiao Er Kang",
            ],
            name,
            75,
        )
        self.position += 100
        self.load_section(["THANKS FOR PLAYING"], title, 100)

    def load_section(self, text_list, section_type, offset):
        for text in text_list:
            self.sprites.add(
                ui_functions.TextSprite(
                    text, *section_type, True, self.position, False, *self.falling_speed
                )
            )
            self.position += offset

    def update(self, actions):
        if actions["escape"] or actions["enter"]:
            self.game.fps = 60
            self.game.volume = 0.8

            for sprite in self.game.all_units:
                sprite.kill()

            pygame.mixer.music.load(self.game.music_path)
            pygame.mixer.music.set_volume(self.game.volume)
            pygame.mixer.music.play(-1)

            while len(self.game.stack) > 1:
                self.exit_scene()

        self.sprites.update()
        self.game.reset_keys()

        # Go back once credits are finished
        if len(self.sprites) == 0:
            self.game.fps = 60
            self.game.volume = 0.8

            for sprite in self.game.all_units:
                sprite.kill()

            pygame.mixer.music.load(self.game.music_path)
            pygame.mixer.music.set_volume(self.game.volume)
            pygame.mixer.music.play(-1)

            while len(self.game.stack) > 1:
                self.exit_scene()

    def render(self, screen):
        screen.blit(
            pygame.transform.scale(
                self.background, (self.game.screen_width, self.game.screen_height)
            ),
            (0, 0),
        )
        self.sprites.draw(screen)
