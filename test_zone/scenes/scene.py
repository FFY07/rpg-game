# Parent class for the different scenes
from gui2 import ui_functions
import gui2.screen as scr

class Scene():
    def __init__(self, game: object):
        self.game = game
        self.prev = None
        self.xc = scr.SCREEN_WIDTH // 2
        self.yc = scr.SCREEN_HEIGHT // 2
    
    def update(self, actions):
        pass
    
    def render(self, screen):
        pass
        
    def start_scene(self):
        # If this is not the only (bottom) item in the stack
        if len(self.game.stack) > 1:
            
            # Previous state allows us to render the previous scene so we can overlay menus on top
            self.prev = self.game.stack[-1]
        
        # Add ourselves to the end of the state stack
        self.game.stack.append(self)
        
    def exit_scene(self):
        # Removes ourselves from the list as we go back down the stack
        self.game.stack.pop()
    
    def create_button(self,
                    text,
                    size,
                    font,
                    text_color,
                    rect_width,
                    rect_height,
                    rect_fill,
                    name,
                    x = True,
                    y = True,
                    button_alpha = 100,
                    text_alpha = 255):
        button_sprite = ui_functions.Button(rect_width, rect_height, rect_fill, x, y, name, button_alpha)
        text_sprite = ui_functions.TextSprite(text, size, font, text_color, x, y, name, 0, 0, text_alpha)

        
        self.sprites.add(button_sprite)
        self.sprites.add(text_sprite)

        
    def generate_buttons(self, 
                         button_list, 
                         text_size, 
                         font, 
                         font_color,
                         width,
                         height,
                         fill,
                         xy: tuple,
                         offset: tuple,
                         button_alpha = 100,
                         text_alpha = 255):
        """Generates multiple buttons using a list"""
        start_x, start_y = xy
        offset_x, offset_y = offset
        
        if start_x is True:
            start_x = scr.SCREEN_WIDTH // 2
        if start_y is True:
            start_y = scr.SCREEN_HEIGHT // 2
        
        for button in button_list:
            self.create_button(button,
                                text_size,
                                font,
                                font_color,
                                width,
                                height,
                                fill,
                                button,
                                start_x,
                                start_y,
                                button_alpha,
                                text_alpha
                                )
            start_x += offset_x
            start_y += offset_y
            
    def create_dict(self, sprite_group):
        """Create enumerated dictionary from sprite group"""
        sprite_dict = {}

        for i, sprite in enumerate(sprite_group.sprites()):
            sprite_dict[i] = sprite
        
        return sprite_dict