import pygame

from scenes.scene import Scene


import resources.images as images


class GameOver(Scene):
    def __init__(self, game: object, victor: str):
        super().__init__(game)
        self.sprites = pygame.sprite.Group()
        self.victor = victor

        if self.victor == "player":
            self.result = images.victory_img

        else:
            self.result = images.defeat_img

    def update(self, actions):

        # Prevents accidentally skipping by spamming enter
        if actions["space"]:

            # If this isn't set, the game will keep counting rounds
            self.sprites.empty()
            pygame.mixer.music.load(self.game.intro_music_path)
            pygame.mixer.music.set_volume(self.game.volume)
            pygame.mixer.music.play(-1)

            self.game.rounds = 1
            while len(self.game.stack) > 1:
                self.exit_scene()

        self.game.reset_keys()
        self.sprites.update()
        self.game.all_units.update()
        self.game.stat_guis.update()

    def render(self, screen):
        self.sprites.draw(screen)
        self.prev.render(screen)
        screen.blit(self.result, (self.xc, self.yc))
