import pygame

from scenes.scene import Scene

import resources2.audio as audio


class Inventory(Scene):
    def __init__(
        self, game: object, selected_unit: pygame.sprite.Sprite, anchor: object
    ):
        super().__init__(game)
        self.sprites = pygame.sprite.Group()
        self.anchor = anchor
        self.selected_unit = selected_unit
        self.inventory_list = []

        self.x_offset = 50
        self.y_offset = 0
        self.button_x, self.button_y = self.selected_unit.rect.midright
        self.button_x += self.x_offset
        self.button_y += self.y_offset

        self.anchor = None

        for item, _ in self.selected_unit.inventory.items():
            self.inventory_list.append(item)

        self.generate_buttons(
            self.inventory_list,
            30,
            "segoeuiemoji",
            "white",
            150,
            50,
            "grey20",
            (self.button_x, self.button_y),
            (0, 50),
            255,
        )

        self.inventory_items = self.create_dict(self.sprites)
        # Create a dictionary for the buttons before we add our pointer sprite image
        self.pointer = 0

    def select_item(self, item_name, actions):
        for _, button in self.inventory_items.items():
            if button.name == item_name:
                button.selected = True

        if actions["enter"]:
            self.selected_unit.consume_item(item_name)
            self.selected_unit.change_state("defend")  # TEMPORARY

            while self.game.stack[-1] != self.anchor:
                self.exit_scene()

    def update(self, actions):
        self.pointer = self.pointer % len(self.inventory_list)

        for sprite in self.sprites.sprites():
            sprite.selected = False

        if actions["down"]:
            self.pointer += 1

        if actions["up"]:
            self.pointer -= 1

        if self.pointer == 0:
            self.select_item("Health Potion", actions)

        if self.pointer == 1:
            self.select_item("Strength Potion", actions)

        if self.pointer == 2:
            self.select_item("Defence Potion", actions)

        if actions["escape"]:
            self.sprites.empty()
            self.exit_scene()

        self.game.reset_keys()
        self.sprites.update()
        self.game.all_units.update()

        # for item in self.selected_unit.inventory.items():
        #     print(item)

    def render(self, screen):
        self.anchor.render(screen)
        self.sprites.draw(screen)
