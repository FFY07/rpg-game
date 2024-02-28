import pygame
import random

import gui.ui_functions as ui_functions
import classes.class_functions as cf

from scenes.scene import Scene
from scenes.play import Play
from scenes.story import Story
from scenes.char_create_select import CreateCharSelect

import resources.images as images

# input1_rect = pygame.Rect(80, 280, 170, 32)


class CreateChar(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        # self.background = pygame.Surface(0, 0)
        self.background = images.char_select_menu
        self.sprites = pygame.sprite.Group()

        self.menu_dict = {}
        self.pointer = 0

        self.player_dict = {
            0: ("Player1", "Reaper"),
            1: ("Player2", "Tank"),
            2: ("Player3", "Warrior"),
        }

        # CreateCharSelect(self.game, self.pointer)

        self.enemy_list = []

        self.create_enemies()

        # Create our menu guis (amount, offset)
        self.create_guis(3, 213)

        self.sprites.add(
            ui_functions.TextSprite(
                "CREATE YOUR CHARACTER",
                50,
                "Impact",
                "white",
                True,
                50,
                name="SELECTED",
            )
        )

        # Create the start game button 1060, 680
        self.start_button = self.create_button(
            "START GAME",
            50,
            None,
            "white",
            300,
            60,
            "white",
            "start",
            1060,
            self.yc + 280,
        )

        self.text_dict = self.create_dict(self.text_sprites)
        self.button_dict = self.create_dict(self.button_sprites)

        # Get rid of the key we automatically generated
        self.text_dict.pop(0)
        self.button_dict.pop(0)

        # Set the button background and text index to be right after the last item in our list of menu guis (this is the start game button)
        self.button_dict[len(self.menu_dict)] = self.start_button[0]
        self.text_dict[len(self.menu_dict)] = self.start_button[1]

    def create_guis(self, amount, offset):
        """Create some amount of GUIs"""
        # color_list = ["grey27", "grey27", "grey27"]
        # for i, color in zip(range(amount), color_list):
        for i in range(amount):
            gui = ui_functions.RectGUI(
                300, 100 + i * offset, 192, 192, "black", i, "grey27", self.game
            )

            self.sprites.add(gui)
            gui.selected_name.text = self.player_dict[i][0]
            gui.image = cf.marketing_images[self.player_dict[i][1]]
            self.menu_dict[i] = gui

    def create_enemies(self):
        for i in range(self.game.max_enemies):
            name = "AI " + str(random.randint(10, 99))
            classes = random.choice(list(cf.unit_dict.items()))
            enemy = (name, classes[0])
            self.enemy_list.append(enemy)

    def update(self, actions):
        for sprite in self.sprites.sprites():
            if not sprite.name == "SELECTED":
                sprite.selected = False

        # haha hardcode + 1
        self.pointer = self.pointer % (len(self.menu_dict) + 1)

        # Since they're separate dictionaries this will switch after len(self.menu_dict)
        try:
            # fmt: off
            # This selects the selected_name.text from our rectgui using our self.pointer as the index
            # Then slots it into the 0 index of our player dict which is the name (name, class) tuple
            self.menu_dict[self.pointer].selected_name.text = self.player_dict[self.pointer][0]
            self.menu_dict[self.pointer].image = cf.marketing_images[self.player_dict[self.pointer][1]]
            # fmt: on
            self.menu_dict[self.pointer].selected = True
        except:
            pass

        try:
            self.button_dict[self.pointer].selected = True
            self.text_dict[self.pointer].selected = True
        except:
            pass

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

        if self.pointer == 3:
            if actions["enter"]:

                # Create the characters
                cf.create_team(list(self.player_dict.values()), "player", self.game)
                cf.create_team(self.enemy_list, "enemy", self.game)

                # Start the game
                next_scene = Story(self.game)
                next_scene.start_scene()

        # self.selected_name_dict[self.pointer] = self.game.text_buffer
        self.text_buffer = ""

        if actions["escape"]:
            self.exit_scene()

        if actions["space"]:
            next_scene = Story(self.game)
            next_scene.start_scene()

        # if actions["enter"]:
        #     next_scene = Play(self.game)
        #     next_scene.start_scene()

        if actions["up"]:
            self.pointer -= 1

        if actions["down"]:
            self.pointer += 1

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
