'''

(Used for show the text after character hit someone)
(note: I import damagetext as dt )

'''






import pygame
from resources.font import font

pygame.init()

class DamageText(pygame.sprite.Sprite):
	def __init__(self, x, y, damage, colour):
		pygame.sprite.Sprite.__init__(self)
		self.image = font.render(damage, True, colour).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.counter = 0


        
	def update(self):
		self.fade_start = 10
		self.fly_speed = 1
		self.end = 60
  
		#move damage text up
		self.rect.y -= self.fly_speed
		#delete the text after a few seconds
		self.counter += 1
		
		if self.counter > self.fade_start:
			normaliser = (self.counter - self.fade_start) / (self.end - self.fade_start)
			self.image.set_alpha(255 * normaliser)
			print(f"normaliser: {normaliser}")
  
		if self.counter > self.end:
			self.kill()
	
