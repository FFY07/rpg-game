import pygame

class health_bar(pygame.sprite.Sprite):
    """Feed Unit objects into me"""
    def __init__(self, unit):
        self.unit = unit
        self.x = self.unit.x
        self.y = self.unit.y
        self.health = self.unit.health
        self.max_health = self.unit.max_health
        
        self.image = pygame.Surface((150, 20))
        self.image.fill("green")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
    def update(self):
        # Update with new health
        self.health = self.unit.health
        self.health_ratio = self.health / self.max_health
        
        
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