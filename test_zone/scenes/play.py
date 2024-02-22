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
        pygame.mixer.music.set_volume(self.game.volume)
        pygame.mixer.music.play(-1)

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

        # self.ui_sprites.add(ui_functions.TextSprite("Type", 30, "freesansbold", "white", self.xc - 200, self.yc + 200, "typing"))
        # self.ui_sprites.add(ui_functions.TextSprite("[Last msg]", 20, "freesansbold", "white", self.xc - 300, self.yc + 300, "lastmsg"))

        cf.set_positions(self.player_positions, self.game.players)
        cf.set_positions(self.enemy_positions, self.game.enemies)

        # Make a list so we can dynamically adjust our pointer position
        self.player_list = []
        self.enemy_list = []
        self.alive_player_dict = {}
        self.alive_enemy_dict = {}

        for i, sprite in enumerate(self.game.players.sprites()):
            self.player_list.append(sprite)

        for i, sprite in enumerate(self.game.enemies.sprites()):
            self.enemy_list.append(sprite)

        # The reason why there is a dictionary and a list is because the list gets changed during game iteration
        # While the alive dictionary needs to be fixed with keys so it doesn't keep appending
        # Since it needs to be updated every loop

        self.selected_unit = self.player_list[0]

        # Add pointer sprite
        self.ui_sprites.add(ui_functions.TargetImage(self, images.player_target))

    # Currently unused; use only if we need to adjust the unit object's .selected attribute
    # def select_player(self, pointer):
    #     self.player_list[pointer].selected = True

    def update(self, actions):
        self.update_alive_dict()

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

        # self.current_text = ui_functions.store_text("lastmsg", self.ui_sprites, self.game)

        # # Print it if it is not empty
        # if self.current_text:
        #     print(self.current_text)

        # for sprite in self.ui_sprites:
        #     if sprite.name == "typing":
        #         sprite.text = self.game.text_buffer

        # Reset the selected state of all sprites at the start of each loop
        for sprite in self.game.all_units.sprites():
            sprite.selected = False

        for sprite in self.ui_sprites.sprites():
            sprite.selected = True

        # Remove dead sprites from list
        for i, sprite in enumerate(self.player_list):
            if not sprite.alive:
                self.player_list.pop(i)

        # Constrains the pointer to the length of the player list
        self.pointer = self.pointer % len(self.player_list)

        self.selected_unit = self.player_list[self.pointer]

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
