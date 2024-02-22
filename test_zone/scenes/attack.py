import pygame

from scenes.scene import Scene
from scenes.target import ChooseTarget

# NOT WRITTEN YET; SKIPPING STRAIGHT TO TARGET


class ChooseAttack(Scene):
    def __init__(self, game: object, selected_unit: pygame.sprite.Sprite):
        super().__init__(game)
        self.selected_unit = selected_unit

        self.x_offset = 50
        self.y_offset = 0
        self.button_x, self.button_y = self.selected_unit.rect.midright
        self.button_x += self.x_offset
        self.button_y += self.y_offset

        self.anchor = None

        self.movelist = list(self.selected_unit.moves.keys())
        self.generate_buttons(
            self.movelist,
            30,
            None,
            "white",
            150,
            50,
            "grey20",
            (self.button_x, self.button_y),
            (0, 50),
            255,
        )

        # Create a dictionary for the buttons before we add our pointer sprite image
        self.button_dict = self.create_dict(self.button_sprites)
        self.text_dict = self.create_dict(self.text_sprites)
        self.pointer = 0

        print(self.button_dict)
        print(self.movelist)

    def update(self, actions):
        self.pointer = self.pointer % len(self.movelist)

        for sprite in self.sprites.sprites():
            sprite.selected = False

            # Experimental method since some dumbass (me) designed the "Button" as a function that glues two separate sprite objects together
            if sprite.name == self.button_dict[self.pointer].name:
                sprite.selected = True

        self.selected_move = self.movelist[self.pointer]

        # Update both the button and the text
        self.button_dict[self.pointer].selected = True
        self.text_dict[self.pointer].selected = True

        print(self.pointer)
        print(self.selected_move)
        # Execute the selected action (it's the attack function)

        if actions["down"]:
            self.pointer += 1

        if actions["up"]:
            self.pointer -= 1

        if actions["enter"]:
            next_scene = ChooseTarget(
                self.game,
                self.selected_unit,
                self.selected_unit.moves[self.selected_move],
                self.anchor,
            )
            next_scene.start_scene()

        if actions["escape"]:
            self.sprites.empty()
            self.exit_scene()

        self.game.reset_keys()
        self.sprites.update()
        self.game.all_units.update()

    def render(self, screen):
        self.anchor.render(screen)
        self.sprites.draw(screen)
