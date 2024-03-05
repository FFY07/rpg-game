import pygame, random

import gui.ui_functions as ui_functions
import classes.class_functions as cf

from scenes.scene import Scene
from scenes.char_desc import CharDesc

import resources.images as images
import resources.fonts as fonts
import resources.audio as audio

class CreateCharSelect(Scene):
    def __init__(self, game: object, menu_id: int):
        super().__init__(game)
        self.sprites = pygame.sprite.Group()

        self.display_units = pygame.sprite.Group()
        self.display_units_list = []
        
        self.background = images.options_background

        # Indiates which menu we're modifying
        self.menu_id = menu_id

        # Default setup, note that cf.unit_dict holds the list of classes
        self.chosen_name =  f"Player {random.randint(10, 99)}"
        self.chosen_class = "Knight"
        self.pointer = 0
        self.character_pointer = 0
        self.scroll_speed = 50

        self.position_list = []
        for i, unit in enumerate(list(cf.unit_dict.keys())):
            x_offset = 150
            self.position_list.append((self.xc + (x_offset * i), self.yc + 280))

        self.draw_marketing()
        self.draw_text()
        self.draw_passive()
        self.draw_skill()

        # Add our display units
        for unit in cf.unit_dict.keys():
            self.display_units.add(
                cf.create_unit(self.chosen_name, unit, "player", self.game, True)
            )

        for unit in self.display_units.sprites():
            self.display_units_list.append(unit)

        # Set character name
        self.name_field = self.create_button(
            "Enter Name",
            50,
            fonts.spartan_mb_semibold,
            "white",
            400,
            70,
            "deepskyblue1",
            "name",
            True,
            self.yc + 120,
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
            self.yc + 210,
        )

        cf.set_positions(self.position_list, self.display_units, "center")

        self.center_position = (self.xc, self.yc)


    def draw_marketing(self):
        # draw marketing image 
        self.gui = ui_functions.Draw_Picture(
                self.xc  - 100,
                self.yc - 200,
                192,
                192,
                "black",
                1,
                "grey27",
                self.game,
            )
        self.sprites.add(self.gui)

        self.gui.image = cf.marketing_images[(list(cf.unit_dict.keys())[self.character_pointer])]


    def draw_passive(self):
        # passsive icon
        self.passive_gui = ui_functions.Draw_Picture(
        self.xc  - 450,
        150 ,
        64,
        64,
        "black",
        0,
        "grey27",
        self.game,
    )
       
        # passive text
        self.passive = ui_functions.TextSprite(
        # f"Race: {list(cf.unit_race_dict.values())[self.character_pointer]}",
        "Passive" ,
        30,
        "Impact",
        "white",
        self.xc - 420,
        120,
        "SELECTED",
    )
        

        self.sprites.add(self.passive_gui)
        self.sprites.add(self.passive)
        self.passive_gui.image = cf.passive_images[(list(cf.passive_images.keys())[self.character_pointer])]


        
        
    def draw_skill(self):

        # i need a list, i know fuck i cannot think i hardcode firsst
       
        
        self.icon_gui = ui_functions.Draw_Picture(
        self.xc  + 250,
        150,
        64,
        64,
        "black",
        0,
        "grey27",
        self.game,
    )
        self.icon_gui2 = ui_functions.Draw_Picture(
        self.xc  + 250,
        150 + 75,
        64,
        64,
        "black",
        1,
        "grey27",
        self.game,
    )
        self.icon_gui3 = ui_functions.Draw_Picture(
        self.xc  + 250,
        150 + 75* 2,
        64,
        64,
        "black",
        2,
        "grey27",
        self.game,
    )
       

        self.skill = ui_functions.TextSprite(
            # f"Race: {list(cf.unit_race_dict.values())[self.character_pointer]}",
            "Character Skill" ,
            30,
            "Impact",
            "white",
            self.xc + 390,
            120,
            "SELECTED",
        )

        self.skill1_name = ui_functions.TextSprite(
            f"{list(cf.skill1_dict.values())[self.character_pointer]}",
            25,
            fonts.spartan_mb_semibold,
            "white",
            self.xc + 400,
            180,
            "SELECTED",
        )
        self.skill2_name = ui_functions.TextSprite(
            f"{list(cf.skill2_dict.values())[self.character_pointer]}",
            25,
            fonts.spartan_mb_semibold,
            "white",
            self.xc + 400,
            180 + 75,
            "SELECTED",
        )
        self.skill3_name = ui_functions.TextSprite(
            f"{list(cf.skill3_dict.values())[self.character_pointer]}",
            25,
            fonts.spartan_mb_semibold,
            "white",
            self.xc + 400,
            180 + 75 * 2,
            "SELECTED",
        )
    
        self.sprites.add(self.icon_gui)
        self.sprites.add(self.icon_gui2) 
        self.sprites.add(self.icon_gui3)
        
        self.sprites.add(self.skill)
        self.sprites.add(self.skill1_name)
        self.sprites.add(self.skill2_name)
        self.sprites.add(self.skill3_name)

        self.icon_gui.image = cf.skill1_images[(list(cf.unit_dict.keys())[self.character_pointer])]
        self.icon_gui2.image = cf.skill2_images[(list(cf.unit_dict.keys())[self.character_pointer])]
        self.icon_gui3.image = cf.skill3_images[(list(cf.unit_dict.keys())[self.character_pointer])]



    def draw_text(self):
        #still hardcore but use function :D
        self.class_name = ui_functions.TextSprite(
            list(cf.unit_dict.keys())[self.character_pointer],
            45,
            "Impact",
            "white",
            self.xc,
            75,
            "SELECTED",
        )
       
        self.race_name = ui_functions.TextSprite(
            # f"Race: {list(cf.unit_race_dict.values())[self.character_pointer]}",
            f"Race: {list(cf.unit_race_dict.values())[self.character_pointer]}",
            20,
            fonts.spartan_mb_semibold,
            "yellow",
            True,
            140,
            "SELECTED",
        )

        self.race_name = ui_functions.TextSprite(
            # f"Race: {list(cf.unit_race_dict.values())[self.character_pointer]}",
            f"Race: {list(cf.unit_race_dict.values())[self.character_pointer]}",
            20,
            fonts.spartan_mb_semibold,
            "yellow",
            True,
            140,
            "SELECTED",
        )


        self.class_des = ui_functions.TextSprite(
            list(cf.unit_dict.values())[self.character_pointer],
            25,
            fonts.spartan_mb_semibold,
            "white",
            self.xc,
            self.yc + 50,
            "SELECTED",
        )

        self.spacedes = ui_functions.TextSprite(
            "Press Space to view skill detail",
            20,
            fonts.spartan_mb_semibold,
            "azure4",
            self.xc + 400,
            self.yc + 25 ,  
            "SELECTED",
        )
    
        self.stat_str_des = ui_functions.TextSprite(
            list(cf.stat_str_dict.values())[self.character_pointer],
            30,
            fonts.spartan_mb_semibold,
            "brown1",
            self.xc - 170,
            self.yc - 180,
            "SELECTED",
        )

        self.stat_int_des = ui_functions.TextSprite(
            list(cf.stat_int_dict.values())[self.character_pointer],
            30,
            fonts.spartan_mb_semibold,
            "aqua",
            self.xc - 170,
            self.yc - 130,
            "SELECTED",
        )
        self.stat_def_des = ui_functions.TextSprite(
            list(cf.stat_def_dict.values())[self.character_pointer],
            30,
            fonts.spartan_mb_semibold,
            "chartreuse4",
            self.xc - 170,
            self.yc - 80,
            "SELECTED",
        )
        self.stat_mr_des = ui_functions.TextSprite(
            list(cf.stat_mr_dict.values())[self.character_pointer],
            30,
            fonts.spartan_mb_semibold,
            "darkorchid2",
            self.xc - 170,
            self.yc - 30,
            "SELECTED",
        )

        self.sprites.add(self.class_name)
        self.sprites.add(self.race_name)
        # self.sprites.add(self.class_des)
        self.sprites.add(self.spacedes)

        self.sprites.add(self.stat_str_des)
        self.sprites.add(self.stat_int_des)
        self.sprites.add(self.stat_def_des)
        self.sprites.add(self.stat_mr_des)

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
        list(self.text_sprites.sprites())[self.pointer].selected = True

        self.class_name.text = list(cf.unit_dict.keys())[self.character_pointer]
        self.race_name.text = (
            f"Race: {list(cf.unit_race_dict.values())[self.character_pointer]}"
        )
        self.class_des.text = list(cf.unit_dict.values())[self.character_pointer]

        self.stat_str_des.text = list(cf.stat_str_dict.values())[self.character_pointer]
        self.stat_int_des.text = list(cf.stat_int_dict.values())[self.character_pointer]
        self.stat_def_des.text = list(cf.stat_def_dict.values())[self.character_pointer]
        self.stat_mr_des.text = list(cf.stat_mr_dict.values())[self.character_pointer]

        self.skill1_name.text = list(cf.skill1_dict.values())[self.character_pointer]
        self.skill2_name.text = list(cf.skill2_dict.values())[self.character_pointer]
        self.skill3_name.text = list(cf.skill3_dict.values())[self.character_pointer]

        self.icon_gui.image = cf.skill1_images[(list(cf.unit_dict.keys())[self.character_pointer])]
        self.icon_gui2.image = cf.skill2_images[(list(cf.unit_dict.keys())[self.character_pointer])]
        self.icon_gui3.image = cf.skill3_images[(list(cf.unit_dict.keys())[self.character_pointer])]

        self.passive_gui.image = cf.passive_images[(list(cf.passive_images.keys())[self.character_pointer])]

        self.gui.image = cf.marketing_images[(list(cf.unit_dict.keys())[self.character_pointer])]
        self.chosen_character = (
            self.chosen_name,
            list(cf.unit_dict.keys())[self.character_pointer],
        )
        # self.chosen_character = (
        #     self.chosen_name,
        #     list(cf.stat_dict.keys())[self.character_pointer],
        # )

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

        if actions["space"]:
            
            next_scene = CharDesc(
                self.game, self.display_units_list[self.character_pointer]
            )

            next_scene.start_scene()

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
