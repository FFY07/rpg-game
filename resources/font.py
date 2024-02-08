'''

list for pygame.Color  :^)
https://www.pygame.org/docs/ref/color_list.html


( This file is use to store all the color variable and font variable )

(import this file if you need to use any color/font )


'''

import pygame
import gui.screen as screen

pygame.init()

#game log font size
game_log_font = pygame.font.SysFont("arial", 15)

#define colours
RED = pygame.Color('red')
GREEN = pygame.Color('green')
TEXT_COL = pygame.Color('white')
YELLOW = pygame.Color('yellow')
GREY = pygame.Color('dimgray')
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
ORANGERED = pygame.Color('orangered4')
DARKRED = pygame.Color('DARKRED')

#gui variable
gui_font = pygame.font.Font(None, 32)
menu_font = pygame.font.Font(None, 45)
menucontent_font = pygame.font.Font(None, 35)
menutitle_font = pygame.font.SysFont('Impact', 70)

#define font
font = pygame.font.SysFont("arialblack" , 40)
hp_font = pygame.font.SysFont("freesansbold", 26)
smaller_gui_font= pygame.font.SysFont("arial", 15)


#input variable (start menu)
base_font = pygame.font.Font(None, 32)
input_hp_font = pygame.font.Font(None, 26)

input_text1, input_text2 = '', ''


color_active = pygame.Color('white')
color_passive = pygame.Color('gray15')

def font_make(size = 20, name = "freesansbold"):
    """
    Generates a font object
    """
    created_font = pygame.font.SysFont(name, size)
    return created_font

class TextSprite(pygame.sprite.Sprite):
    # Creates a text sprite; replace me with a docstring once all the parameters are done
    def __init__(self, text: str, size: int, text_font = "freesansbold", color = "white", x = True, y = True, falling = False):
        """Generates a text sprite
        
        Args:
            text (str): The text to display
            size (int): The size of the text
            text_font (str, optional): The font name. Defaults to "freesansbold".
            color (str, optional): The font color. Defaults to "white".
            x (bool, optional): The x coordinate. True = Centered.
            y (bool, optional): The y coordinate. True = Centered.
            falling (bool, optional): Whether the text is falling
        """
        super().__init__()
        
        if x is True:
            self.x = screen.SCREEN_WIDTH // 2
        else:
            self.x = x
            
        if y is True:
            self.y = screen.SCREEN_HEIGHT // 2
        else:
            self.y = y
            
        self.falling = falling
        
        self.font = pygame.font.SysFont(text_font, size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    
    def update(self):
        if self.falling:
            self.rect.move_ip(0, 5)