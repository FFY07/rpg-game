import pygame

import resources.font as font
from classes.knight import Knight
import gui.screen as sc
import classes.class_functions as cf

BAR_WIDTH = 100
BAR_HEIGHT = 15
BAR_OFFSET_Y = -75
BAR_OFFSET_X = 0

DEFAULT_QTY = BAR_WIDTH // 2

healthbars = pygame.sprite.Group()
manabars = pygame.sprite.Group()
allbars = pygame.sprite.Group()

class DisplayBar(pygame.sprite.Sprite):
    """Parent class for health and mana bars"""
    def __init__(self, unit: object):
        super().__init__()
        self.unit = unit
        
        # Sets the bar coordinates relative to the unit's coordinates
        self.x = self.unit.x + BAR_OFFSET_X
        self.y = self.unit.y + BAR_OFFSET_Y
        
        # Default amount of fill (overwrite this part)
        self.current_quantity = DEFAULT_QTY
        self.max_quantity = BAR_WIDTH
        
        # Initialises the coordinates and default fill
        self.image = pygame.Surface((BAR_WIDTH, BAR_HEIGHT))
        self.image.fill("grey")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
        # Create text
        self.text = f"{str(self.current_quantity)} / {str(self.max_quantity)}"
        self.text_size = 16
        self.text_font = None
        self.text_color = "white"
        self.text_sprite = font.TextSprite(self.text, self.text_size, self.text_font, self.text_color, True, True)
        
class HealthBar(DisplayBar):
    def __init__(self, unit):
        super().__init__(unit)    
        self.background = DisplayBar(unit)
        self.foreground = DisplayBar(unit)
        
        allbars.add(self.background)

            
test_knight = cf.create_unit("testknight", "Knight")
test_bar = DisplayBar(test_knight)


print(test_bar.current_quantity)

test_health = HealthBar(test_knight)

print(test_health.current_quantity, test_health.max_quantity)

print(test_health.background, test_health.foreground)