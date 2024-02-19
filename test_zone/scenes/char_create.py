import pygame
import random 

import gui2.ui_functions as ui_functions
import classes.class_functions as cf

from scenes.scene import Scene
from scenes.play import Play
from scenes.char_create_select import CreateCharSelect

import resources2.images
# input1_rect = pygame.Rect(80, 280, 170, 32)


class CreateChar(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        self.background = pygame.Surface((1, 1))
        self.sprites = pygame.sprite.Group()
        self.gui_dict = {}
        self.pointer = 0
        self.selected_name_dict = {}
        self.selected_class_dict = {}

        self.player_list = [("Slashy", "Reaper"),
                            ("Tiger", "Knight"),
                            ("Joker", "Tank")]
        
        #random name and random classes 

        self.class_list = ['Knight', 'Reaper', 'Tank', 'Bandit']
        self.enemy_list = []
        
        self.create_enemies()
        
        cf.create_team(self.player_list, "player", self.game)
        cf.create_team(self.enemy_list, "enemy", self.game)
        
        self.sprites.add(ui_functions.TextSprite("CREATE YOUR CHARACTER", 50, 'Impact', "white", True, 50, name = "SELECTED"))

        # This only selects the rectangle and not the text
        self.gui_dict["start"] = self.create_button("START GAME", 30, None, "white", 300, 40, 'white', 'start' , 1060, 680)[0]
        
        # guirect = ui_functions.RectGUI()
        #draw rect
        self.create_guis(3, 213)
    
    def create_guis(self, amount, offset):
        """Create some amount of GUIs"""
        # color_list = ["grey27", "grey27", "grey27"]
        # for i, color in zip(range(amount), color_list):
        for i in range(amount):
            gui = ui_functions.RectGUI(57, 100 + i * offset, 700, 143, "white", 1 * i, "grey27")

            self.create_button("hi", 30, None, "white", 300, 40, 'white', f'hi {i}' , gui.rect.center[0] - 150, gui.rect.center[1] - 45)
            self.sprites.add(gui)
            self.gui_dict[i] = gui
            
    def create_enemies(self):
        for i in range(self.game.max_enemies):
            name  = 'AI ' + str(random.randint(10, 99))
            classes = random.choice(self.class_list)
            enemy =  (name, classes)
            self.enemy_list.append(enemy)
        
    def update(self, actions):
        for sprite in self.sprites.sprites():
            if not sprite.name == "SELECTED":
                sprite.selected = False

        self.pointer = self.pointer % (len(self.gui_dict))

        if self.pointer == 0:
            for sprite in self.sprites.sprites():
                if sprite.name == self.pointer:
                    sprite.selected = True
        
            if actions["enter"]:
                next_scene = CreateCharSelect(self.game, self.pointer)
                next_scene.start_scene()

        if self.pointer == 1:
            for sprite in self.sprites.sprites():
                if sprite.name == self.pointer:
                    sprite.selected = True
        
            if actions["enter"]:
                next_scene = CreateCharSelect(self.game, self.pointer)
                next_scene.start_scene()
                    
        if self.pointer == 2:
            for sprite in self.sprites.sprites():
                if sprite.name == self.pointer:
                    sprite.selected = True
        
            if actions["enter"]:
                next_scene = CreateCharSelect(self.game, self.pointer)
                next_scene.start_scene()
                    
        if self.pointer == 3:
            for sprite in self.sprites.sprites():
                if sprite.name == "start":
                    sprite.selected = True
        
            if actions["enter"]:
                next_scene = Play(self.game)
                next_scene.start_scene()
        
        self.selected_name_dict[self.pointer] = self.game.text_buffer
        self.text_buffer = ""

                

        if actions["escape"]:
            self.exit_scene()
        
        if actions['space']:
            next_scene = Play(self.game)
            next_scene.start_scene()

        # if actions["enter"]:            
        #     next_scene = Play(self.game)
        #     next_scene.start_scene()
        
        if actions['up']:
            self.pointer -= 1 

        if actions['down']:
            self.pointer += 1


        self.game.reset_keys()
        self.sprites.update()
        
        # print(f"Current pointer: {self.pointer}")
    
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))
        self.sprites.draw(screen)

        for sprite in self.sprites.sprites():
            sprite.draw(screen)