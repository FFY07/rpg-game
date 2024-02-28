import pygame, json

from scenes.scene import Scene
import resources.images
from gui import ui_functions
import resources.audio as audio

import classes.class_functions as cf

BUTTON_TEXT_SIZE = 30
BUTTON_FONT = "freesansbold"
BUTTON_FONT_COLOR = "white"
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 40
BUTTON_OFFSET = 50


class Options(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.background = resources.images.options_background
        self.sprites = pygame.sprite.Group()
        self.pointer = 0
        self.button_list = ["Music", "Sound", "Save", "Load", "Back", "New Game"]

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
                if self.game.music:
                    self.game.music = False

                else:
                    self.game.music = True

        # Sound toggle
        if self.pointer == 1:
            # Toggles game sound effects
            if actions["enter"]:
                if self.game.sound:
                    self.game.sound = False

                else:
                    self.game.sound = True

        # Save game
        if self.pointer == 2:
            if actions["enter"]:
                save_game(self.game)
                # save gamelog
                self.sprites.empty()
                self.exit_scene()

        # Load game
        if self.pointer == 3:
            if actions["enter"]:
                load_game(self.game)
                self.sprites.empty()
                self.exit_scene()

        # Back to previous scene
        if self.pointer == 4:
            if actions["enter"]:
                self.exit_scene()

        # Back to main menu
        if self.pointer == 5:
            if actions["enter"]:
                self.sprites.empty()
                pygame.mixer.music.load(self.game.intro_music_path)
                pygame.mixer.music.set_volume(self.game.volume)
                pygame.mixer.music.play(-1)

                while len(self.game.stack) > 1:
                    self.exit_scene()

        if actions["down"]:
            self.pointer += 1

        if actions["up"]:
            self.pointer -= 1

        if actions["escape"]:
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


def save_game(game=object, file_name="save.json"):
    """Saves all units to a json file"""
    save_dict = {}

    # If there are sprites at all
    if len(game.all_units.sprites()):

        for i, sprite in enumerate(game.all_units.sprites()):
            save_dict[i] = {}
            save_dict[i]["name"] = sprite.name
            save_dict[i]["mana"] = sprite.mana
            save_dict[i]["health"] = sprite.health

            save_dict[i]["crit_chance"] = sprite.crit_chance
            save_dict[i]["crit_mult"] = sprite.crit_mult

            save_dict[i]["level"] = sprite.level
            save_dict[i]["exp"] = sprite.exp
            save_dict[i]["coins"] = sprite.coins

            save_dict[i]["unit_class"] = sprite.unit_class
            save_dict[i]["team"] = sprite.team

            save_dict[i]["inventory"] = sprite.inventory

            save_dict[i]["burn_stacks"] = sprite.burn_stacks
            save_dict[i]["health_regen_stacks"] = sprite.health_regen_stacks
            save_dict[i]["mana_regen_stacks"] = sprite.mana_regen_stacks

            save_dict[i]["bonus_strength_stacks"] = sprite.bonus_strength_stacks
            save_dict[i]["bonus_intelligence_stacks"] = sprite.bonus_intelligence_stacks
            save_dict[i]["bonus_defence_stacks"] = sprite.bonus_defence_stacks
            save_dict[i]["bonus_magic_resist_stacks"] = sprite.bonus_magic_resist_stacks

            with open(file_name, "w") as save_file:
                json.dump(save_dict, save_file)
        game.event_log.append(f'Game successfully saved to "{file_name}"!')
        print(f'Game successfully saved to "{file_name}"!')
    else:
        game.event_log.append("Nothing to save!")
        print("Nothing to save!")


def load_game(game: object, file_name="save.json"):
    holding_player_pos_list = []
    holding_enemy_pos_list = []
    for sprite in game.all_units.sprites():
        if sprite.team == "player":
            holding_player_pos_list.append(sprite.position)

        elif sprite.team == "enemy":
            holding_enemy_pos_list.append(sprite.position)

    try:
        with open(file_name, "r") as save_file:
            loaded_units = json.load(save_file)

            # If save file exists, kill everyone
            for sprite in game.all_units.sprites():
                sprite.kill()

            for sprite in game.stat_guis.sprites():
                sprite.kill()

            for _, v in loaded_units.items():
                unit = cf.create_unit(v["name"], v["unit_class"], v["team"], game)
                unit.health = v["health"]
                unit.mana = v["mana"]
                unit.crit_chance = v["crit_chance"]
                unit.crit_mult = v["crit_mult"]
                unit.level = v["level"]
                unit.exp = v["exp"]
                unit.coins = v["coins"]
                unit.inventory = v["inventory"]

                unit.burn_stacks = v["burn_stacks"]
                unit.health_regen_stacks = v["health_regen_stacks"]
                unit.mana_regen_stacks = v["mana_regen_stacks"]

                unit.bonus_strength_stacks = v["bonus_strength_stacks"]
                unit.bonus_intelligence_stacks = v["bonus_intelligence_stacks"]
                unit.bonus_defence_stacks = v["bonus_defence_stacks"]
                unit.bonus_magic_resist_stacks = v["bonus_magic_resist_stacks"]

        # Set positions
        cf.set_positions(holding_player_pos_list, game.players)
        cf.set_positions(holding_enemy_pos_list, game.enemies)

        # Re create all the info GUIS
        ui_functions.create_info_guis(game)

        print(f'Successfully loaded save from "{file_name}".')
        game.event_log.append(f'Successfully loaded save from "{file_name}"!')

    except FileNotFoundError:
        print("No save detected!")
        game.event_log.append("No save detected!")
