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

textbars = pygame.sprite.Group()
healthbars = pygame.sprite.Group()
manabars = pygame.sprite.Group()
allbars = pygame.sprite.Group()

class StaticBar(pygame.sprite.Sprite):
    """Parent class for static display based on fixed position"""
    def __init__(self, unit: object, x = 20, y = 50, color = "grey75", width = BAR_WIDTH, height = BAR_HEIGHT):
        super().__init__()
        self.unit = unit
        
        # Initialises the size and position values
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
        
        # Creates the image surface and rectangle to draw the surface on
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        
        self.max_width = BAR_WIDTH
        
        allbars.add(self)
        self.alt = True
    
    # This section is contains nonsense; I'm just testing using a toggle
    # We need two sprites: one for background and one for foreground (One red bar behind and one green bar in front)
    def update(self):                
        if self.alt:
            self.unit.health = 50
            self.alt = False
            self.color = "red"
        else:
            self.unit.health = 100
            self.alt = True
            self.color = "green"          
        
        self.fill_amount = BAR_WIDTH // (self.unit.max_health // self.unit.health)
        self.image = pygame.Surface((self.fill_amount, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

class BarText(pygame.sprite.Sprite):
    """Text for displaying values in bar sprites"""
    def __init__(self, unit, size, text_font, color):
        super().__init__()
        self.unit = unit
        self.x = self.unit.x + BAR_OFFSET_X
        self.y = self.unit.y + BAR_OFFSET_Y
        
        self.text = f"{str(self.unit.health)} / {str(self.unit.max_health)}"
        self.size = size
        self.font = pygame.font.SysFont(text_font, self.size)
        self.color = color
        
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
        textbars.add(self)
    
    def update(self):
        self.text = f"{str(self.unit.health):^5}/{str(self.unit.max_health):^5}"
        self.image = self.font.render(self.text, True, self.color)
        
    
class DynamicBar(pygame.sprite.Sprite):
    """Parent class for text that's based on unit's position"""
    def __init__(self, unit: object):
        super().__init__()
        self.unit = unit
        
        # Sets the bar coordinates relative to the unit's coordinates
        self.x = self.unit.x + BAR_OFFSET_X
        self.y = self.unit.y + BAR_OFFSET_Y
        self.width = BAR_WIDTH
        self.height = BAR_HEIGHT
        
        # Default amount of fill (overwrite this part)
        self.fill_amount = DEFAULT_QTY
        self.max_fill = BAR_WIDTH
        
        # Initialises the coordinates and default fill
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("grey")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
        self.alt = True
        
    def update(self):                
        if self.alt:
            self.unit.health = 50
            self.alt = False
            self.color = "red"
        else:
            self.unit.health = 100
            self.alt = True
            self.color = "green"          
        
        self.fill_amount = BAR_WIDTH // (self.unit.max_health // self.unit.health)
        self.image = pygame.Surface((self.fill_amount, self.height))
        self.image.fill(self.color)

        
class HealthBar(DynamicBar):
    def __init__(self, unit):
        super().__init__(unit)    
        self.background = DynamicBar(unit)
        self.foreground = DynamicBar(unit)
        # incomplete
        
        allbars.add(self.background)


# TESTING ZONE
test_knight = cf.create_unit("testknight", "Knight")

test_bar_text = BarText(test_knight, 30, None, "yellow") # This is the text for the dynamic HealthBar
test_health = HealthBar(test_knight) # This is the bar on top of the middle character

test_static_bar = StaticBar(test_knight) # This is the flickering one on the left based on fixed coordinates

# Slow down the FPS to see better ^

print(test_health.fill_amount, test_health.max_fill)

print(test_health.background, test_health.foreground)