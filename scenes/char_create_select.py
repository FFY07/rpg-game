import pygame

import gui.ui_functions as ui_functions
import classes.class_functions as cf

from scenes.scene import Scene
import resources.images as images
import resources.fonts as fonts


class CreateCharSelect(Scene):
    def __init__(self, game: object, menu_id: int):
        super().__init__(game)
        self.sprites = pygame.sprite.Group()

        self.display_units = pygame.sprite.Group()
        self.display_units_list = []

        self.background = images.char_select_background

        # Indiates which menu we're modifying
        self.menu_id = menu_id

        # Default setup, note that cf.unit_list holds the list of classes
        self.chosen_name = "John Wick"
        self.chosen_class = "Knight"
        self.pointer = 0
        self.character_pointer = 0
        self.scroll_speed = 50

        self.position_list = []
        for i, unit in enumerate(cf.unit_list):
            x_offset = 150
            self.position_list.append((self.xc + (x_offset * i), self.yc))

        self.class_name = ui_functions.TextSprite(
            cf.unit_list[self.character_pointer],
            40,
            None,
            "white",
            True,
            100,
            "SELECTED",
        )

        self.class_des = ui_functions.TextSprite(
            cf.unit_des_list[self.character_pointer],
            40,
            None,
            "white",
            True,
            170,
            "SELECTED",
        )


        self.sprites.add(self.class_name)
        self.sprites.add(self.class_des)
        # Add our display units
        for unit in cf.unit_list:
            self.display_units.add(
                cf.create_unit(self.chosen_name, unit, "player", self.game, True)
            )

        for unit in self.display_units.sprites():
            self.display_units_list.append(unit)

        # Set character name
        self.name_field = self.create_button(
            "Enter Name",
            50,
            None,
            "white",
            400,
            60,
            "deepskyblue1",
            "name",
            True,
            self.yc + 200,
            100,
            
        )

        # Confirm character
        self.exit_button = self.create_button(
            "Create",
            50,
            None,
            "white",
            200,
            60,
            "deepskyblue1",
            "exit",
            True,
            self.yc + 300,
        )

        cf.set_positions(self.position_list, self.display_units, "center")

        self.center_position = (self.xc, self.yc)

    def update(self, actions):
        for sprite in self.sprites:
            if sprite.name != "SELECTED":
                sprite.selected = False

            if self.game.typing and sprite.name == "name":
                sprite.text = self.game.text_buffer

        if self.game.text_ready:
            self.chosen_name = self.game.text_buffer
            self.game.text_ready = False

        self.pointer = self.pointer % len(self.button_sprites)
        list(self.button_sprites.sprites())[self.pointer].selected = True

        self.class_name.text = cf.unit_list[self.character_pointer]
        self.class_des.text = cf.unit_des_list[self.character_pointer]

        self.chosen_character = (
            self.chosen_name,
            cf.unit_list[self.character_pointer],
        )

        # If the selected character reaches the center x position, stop all units in place
        if (
            self.display_units_list[self.character_pointer].rect.center[0]
            == self.center_position[0]
        ):
            for unit in self.display_units_list:
                unit.dx, unit.dy = 0, 0

        # We're doing the character_pointer range check manually instead of modulo
        # Because I want to stop it from moving past the original range
        # This is not as impressive as continuous scroll but adding it will require too much work to be rewritten
        if actions["right"]:
            if self.character_pointer + 1 < len(self.display_units):
                self.character_pointer += 1
                for unit in self.display_units.sprites():
                    unit.dx = -self.scroll_speed

        if actions["left"]:
            if self.character_pointer > 0:
                self.character_pointer -= 1
                for unit in self.display_units.sprites():
                    unit.dx = self.scroll_speed

        if actions["down"]:
            self.pointer += 1

        if actions["up"]:
            self.pointer -= 1

        if self.pointer == 0:
            if actions["enter"]:
                for sprite in self.button_sprites.sprites():
                    if sprite.name == "name":
                        sprite.text = self.game.text_buffer
                self.game.typing = True

        if self.pointer == 1:
            if actions["enter"]:
                self.prev.player_dict[self.menu_id] = self.chosen_character
                self.game.text_buffer = ""
                self.exit_scene()

        if actions["escape"]:
            self.exit_scene()

        self.display_units.update()
        self.sprites.update()
        self.game.reset_keys()

        # print(self.chosen_character)
        # print(self.position_list)

    def render(self, screen):
        screen.blit(
            pygame.transform.scale(
                self.background, (self.game.screen_width, self.game.screen_height)
            ),
            (0, 0),
        )
        self.display_units.draw(screen)
        self.sprites.draw(screen)
