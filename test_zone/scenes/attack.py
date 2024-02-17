import pygame

import gui2.ui_functions as ui_functions
from scenes.scene import Scene
import gui2.screen as scr
import resources2.images

credit_section = [55, None, "yellow"]
credit_title = [45, None, "white"]
credit_desc = [45, None, "green"]
credit_name = [35, "segoeuiemoji", "white"]

class Attack(Scene):
    def __init__(self, game: object, selected_player: pygame.sprite.Sprite):
        super().__init__(game)
        self.selected_player = selected_player
        
        # Anchor the previous scene so we can keep updating and rendering the units there
        self.anchor = self.prev
                
        print(self.selected_player)

    def update(self, actions):
        if actions["escape"] or actions["enter"]:
            self.exit_scene()
            
        self.game.reset_keys()
        self.game.all_units.update()
        
    def render(self, screen):
        
        # So it doesn't crash before we load the prev scene into self.anchor
        try:
            self.prev.render(screen)
        except:
            pass
        