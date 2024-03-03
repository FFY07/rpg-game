import pygame
import random

import gui.ui_functions as ui_functions
import classes.class_functions as cf

from scenes.scene import Scene

from scenes.story import Story
from scenes.char_create_select import CreateCharSelect

import resources.images as images
from resources import fonts

# input1_rect = pygame.Rect(80, 280, 170, 32)


class CreateChar(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        # self.background = pygame.Surface(0, 0)
        self.background = images.char_select_menu
        self.sprites = pygame.sprite.Group()

        self.ready = False
        self.menu_dict = {}
        self.pointer = 0

        self.player_dict = {
            0: ("Player1", "Reaper"),
            1: ("Player2", "Tank"),
            2: ("Player3", "Warrior"),
        }

        self.player_dict = {}
        self.generate_player_dict()

        self.enemy_list = []
        self.create_enemies()

        # Create our menu guis (amount, offset)
        self.create_guis(3, 213)
        self.create_enemyguis(3, 213)

        self.sprites.add(
            ui_functions.TextSprite(
                "CHOOSE YOUR CHARACTER",
                40,
                "Impact",
                "white",
                True,
                40,
                name="SELECTED",
            )
        )

        self.sprites.add(
            ui_functions.TextSprite(
                "VS",
                160,
                fonts.squealer_embossed,
                "white",
                self.xc - 15,
                420,
                name="SELECTED",
            )
        )

        # Create the start game button 1060, 680
        self.start_button = self.create_button(
            "START GAME",
            50,
            fonts.squealer,
            "white",
            300,
            60,
            "white",
            "start",
            self.xc - 15,
            self.yc + 200,
        )

        self.text_dict = self.create_dict(self.text_sprites)
        self.button_dict = self.create_dict(self.button_sprites)

        # Get rid of the key we automatically generated
        # self.text_dict.pop(0)
        # self.button_dict.pop(0)

        # # Set the button background and text index to be right after the last item in our list of menu guis (this is the start game button)
        # self.button_dict[len(self.menu_dict)] = self.start_button[0]
        # self.text_dict[len(self.menu_dict)] = self.start_button[1]

    def create_guis(self, amount, offset):
        """Create some amount of GUIs"""
        # color_list = ["grey27", "grey27", "grey27"]
        # for i, color in zip(range(amount), color_list):
        for i in range(amount):
            gui = ui_functions.RectGUI(
                self.xc - 520,
                100 + i * offset,
                192,
                192,
                "black",
                i,
                "grey27",
                self.game,
            )

            self.sprites.add(gui)
            gui.selected_name.text = self.player_dict[i][0]
            gui.selected_class.text = self.player_dict[i][1]

            gui.image = cf.marketing_images[self.player_dict[i][1]]
            self.menu_dict[i] = gui

    def generate_player_dict(self, amount=3):
        for i in range(amount):
            name = f"Player {i+1}"
            char_class = random.choice(list(cf.unit_dict.items()))
            self.player_dict[i] = (name, char_class[0])

    def create_enemies(self):
        for _ in range(self.game.max_enemies):
            name = f"AI {random.randint(10, 99)}"
            char_class = random.choice(list(cf.unit_dict.items()))
            enemy = (name, char_class[0])
            self.enemy_list.append(enemy)

    def create_enemyguis(self, amount, offset):
        """Create some amount of GUIs"""
        # color_list = ["grey27", "grey27", "grey27"]
        # for i, color in zip(range(amount), color_list):
        for i in range(amount):
            gui = ui_functions.EnemyRect(
                self.xc + 300,
                100 + i * offset,
                192,
                192,
                "black",
                i,
                "grey27",
                self.game,
            )

            self.sprites.add(gui)
            gui.enemy_name.text = self.enemy_list[i][0]
            gui.enemy_class.text = self.enemy_list[i][1]

            gui.image = cf.marketing_images[self.enemy_list[i][1]]
            gui.image = pygame.transform.flip(gui.image, True, False)

    def update(self, actions):
        for sprite in self.sprites.sprites():
            if not sprite.name == "SELECTED":
                sprite.selected = False

        self.pointer = self.pointer % (len(self.menu_dict))

        # fmt: off
        # This selects the selected_name.text from our rectgui using our self.pointer as the index
        # Then slots it into the 0 index of our player dict which is the name (name, class) tuple
        self.menu_dict[self.pointer].selected_name.text = self.player_dict[self.pointer][0]
        self.menu_dict[self.pointer].selected_class.text = self.player_dict[self.pointer][1]
        self.menu_dict[self.pointer].image = cf.marketing_images[self.player_dict[self.pointer][1]]
        # fmt: on
        if not self.ready:
            self.menu_dict[self.pointer].selected = True

            if self.pointer == 0:
                if actions["enter"]:
                    next_scene = CreateCharSelect(self.game, self.pointer)
                    next_scene.start_scene()

            if self.pointer == 1:
                if actions["enter"]:
                    next_scene = CreateCharSelect(self.game, self.pointer)
                    next_scene.start_scene()

            if self.pointer == 2:
                if actions["enter"]:
                    next_scene = CreateCharSelect(self.game, self.pointer)
                    next_scene.start_scene()

            if actions["up"]:
                self.pointer -= 1

            if actions["down"]:
                self.pointer += 1

        if self.ready:
            self.button_dict[0].selected = True
            self.text_dict[0].selected = True

            if actions["enter"] or actions["space"]:

                # Create the characters
                cf.create_team(list(self.player_dict.values()), "player", self.game)
                cf.create_team(self.enemy_list, "enemy", self.game)

                # Start the game
                next_scene = Story(self.game)
                next_scene.start_scene()

                self.game.event_log.append("\nSTARTING GAME\n")

        # self.selected_name_dict[self.pointer] = self.game.text_buffer
        self.text_buffer = ""

        if actions["escape"]:
            self.exit_scene()

        if actions["right"]:
            self.ready = True

        if actions["left"]:
            self.ready = False

        self.game.reset_keys()
        self.sprites.update()

        # print(f"Current pointer: {self.pointer}")

    def render(self, screen):
        screen.blit(
            pygame.transform.scale(
                self.background, (self.game.screen_width, self.game.screen_height)
            ),
            (0, 0),
        )
        self.sprites.draw(screen)

        for sprite in self.sprites.sprites():
            sprite.draw(screen)
