import pygame

import resources.font as font
from knight import Knight

BAR_WIDTH = 150
BAR_HEIGHT = 20
BAR_OFFSET_Y = -25
BAR_OFFSET_X = 0

DEFAULT_QTY = BAR_WIDTH // 2

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
    """Bar based on health
    
    This is not done; still need the green bar overlapping the red bar
    It may be possible to add the green bar as a child of the red bar"""
    def __init__(self, unit: object):
        super().__init__(unit)
        
        self.current_quantity = unit.health
        self.max_quantity = unit.max_health
        
        self.image.fill("green")
        
    def update(self):
        self.current_quantity = self.unit.health
        self.max_quantity = self.unit.max_health
        
        self.text = f"{str(self.current_quantity)} / {str(self.max_quantity)}"
        self.text_sprite.font = pygame.font.SysFont(self.text, self.text_size)
            
test_knight = Knight()
test_bar = DisplayBar(test_knight)

print(test_bar.quantity)

test_health = HealthBar(test_knight)

print(test_health.quantity, test_health.max_quantity)
        
# TODO USE TWO INSTANCES OF HEALTH BARS AS EACH HEALTH BAR CAN ONLY HAVE ONE self.image and self.rect
        
# class healthbar():
#     def __init__(self,x,y,hp,max_hp):
#         self.x = x
#         self.y = y
#         self.hp = hp
#         self.max_hp = max_hp

#     def draw(self,hp):
#         #update with new health
#         self.hp = hp
#         #calculate health ratio
#         ratio = self.hp / self.max_hp
#         pygame.draw.rect(sc.screen,font.RED,( self.x, self.y, 150, 20))
#         pygame.draw.rect(sc.screen,font.GREEN,( self.x, self.y, 150 * ratio , 20))