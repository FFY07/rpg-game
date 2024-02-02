'''

(Used for show the text after character hit someone)
(note: I import damagetext as dt )

'''

import pygame
from resources.font import font

pygame.init()

damage_text_group = pygame.sprite.Group()

class DamageText(pygame.sprite.Sprite):
	def __init__(self, x, y, damage, colour):
		pygame.sprite.Sprite.__init__(self)
		self.image = font.render(damage, True, colour).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.max_lifetime = 180
		self.lifetime = self.max_lifetime

	def update(self):
		self.fade_start = 90
		self.fly_speed = 1
  
		#move damage text up
		self.rect.y -= self.fly_speed
		#delete the text after n frames
		self.lifetime -= 1

		if self.lifetime > self.fade_start:
			normaliser = (self.lifetime - self.fade_start) / (self.max_lifetime - self.fade_start)
			self.image.set_alpha(int(f"{int((255 * normaliser))}"))
			print(f"Formula: {self.lifetime} (counter) - {self.fade_start} (Fade Start) / {self.max_lifetime} (Kill) - {self.fade_start} (Fade Start) = {normaliser}")
			print(f"Alpha: 255 * {normaliser} = {int((255 * normaliser))}")
		if self.lifetime <= 0:
			self.kill()