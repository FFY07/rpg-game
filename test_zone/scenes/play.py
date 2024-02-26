import pygame

import gui2.screen as scr

from scenes.scene import Scene
from scenes.action import Action
from scenes.end import GameOver

from gui2 import ui_functions
import resources2.images as images
import resources2.audio as audio

from classes import class_functions as cf

from scenes.options import Options


class Play(Scene):
    def __init__(self, game):
        super().__init__(game)
        pygame.mixer.music.load(audio.battle_alt)
        pygame.mixer.music.play(-1, 0, 1000)

        self.stat_guis = pygame.sprite.Group()

        self.background = images.background_img
        self.ui_sprites = pygame.sprite.Group()
        self.pointer = 1

        # self.crazy_guy = cf.create_unit("William", "Reaper", "enemy", self.game)
        # self.crazy_guy.dx, self.crazy_guy.dy = 5, 5

        # testing coordinates
        self.player_positions = [
            (self.xc - 500, self.yc + 150),
            (self.xc - 375, self.yc),
            (self.xc - 250, self.yc - 150),
        ]

        self.enemy_positions = [
            (self.xc + 500, self.yc + 150),
            (self.xc + 375, self.yc),
            (self.xc + 250, self.yc - 150),
        ]
        cf.set_positions(self.player_positions, self.game.players)
        cf.set_positions(self.enemy_positions, self.game.enemies)

        # Move sprites off-screen
        for sprite in self.game.players:
            sprite.rect.center = sprite.rect.center[0] - 200, sprite.rect.center[1]
            sprite.dx = 5

        for sprite in self.game.enemies:
            sprite.rect.center = sprite.rect.center[0] + 200, sprite.rect.center[1]
            sprite.dx = -5

        # The reason why there is a dictionary and a list is because the list gets changed during game iteration
        # While the alive dictionary needs to be fixed with keys so it doesn't keep appending
        # Since it needs to be updated every loop

        self.selected_unit = self.game.players.sprites()[0]

        # Add pointer sprite
        self.ui_sprites.add(ui_functions.TargetImage(self, images.player_target))

        self.button_dict = self.create_dict(self.button_sprites)
        self.text_dict = self.create_dict(self.text_sprites)

        for sprite in self.game.all_units.sprites():
            stat_bar = ui_functions.Statbar(sprite)
            self.stat_guis.add(stat_bar)
            self.ui_sprites.add(stat_bar)

    # def create_health_gui(self, x, y, width = 120, height = 60):

    # gui = ui_functions.Healthbar(x, y , width, height, "green")

    # self.ui_sprites.add(gui)

    def update(self, actions):
        self.update_alive_dict()

        for sprite in self.game.all_units:
            rectx, recty = sprite.rect.center
            if rectx > scr.SCREEN_WIDTH:
                sprite.rect.center = 0, recty
            elif rectx < 0:
                sprite.rect.center = scr.SCREEN_WIDTH, recty

            if rectx == sprite.position[0]:
                sprite.dx = 0

        if not self.alive_player_dict:
            victor = "enemy"
            next_scene = GameOver(self.game, victor)
            next_scene.start_scene()
            return

        if not self.alive_enemy_dict:
            victor = "player"
            next_scene = GameOver(self.game, victor)
            next_scene.start_scene()
            return

        for sprite in self.game.all_units.sprites():
            sprite.selected = False

        for sprite in self.ui_sprites.sprites():
            sprite.selected = True

        self.pointer = self.pointer % len(self.alive_player_dict)

        self.selected_unit = list(self.alive_player_dict.values())[self.pointer]

        if actions["escape"]:
            next_scene = Options(self.game)
            next_scene.start_scene()

        if actions["up"]:
            self.pointer += 1

        if actions["down"]:
            self.pointer -= 1

        if actions["enter"]:

            # Create an anchor as well using self because we will be referencing this scene in the other menu scenes
            next_scene = Action(self.game, self.selected_unit, self)

            for sprite in self.ui_sprites:
                sprite.selected = False
            next_scene.start_scene()

        self.ui_sprites.update()
        self.game.all_units.update()

        self.game.reset_keys()

    def render(self, screen):
        screen.blit(
            pygame.transform.scale(
                self.background, (self.game.screen_width, self.game.screen_height)
            ),
            (0, 0),
        )

        # Rendering order (last to render = on top)
        self.game.all_units.draw(screen)
        self.ui_sprites.draw(screen)

        # for group in self.manual_groups:
        #     group.update()
        #     group.draw(screen)
