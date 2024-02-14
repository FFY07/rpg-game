import pygame
from pathlib import Path

#menu background
menubackground_img = pygame.image.load(f"{Path('test_zone/resources2/images/backgrounds/menubackground.png')}")

options_background = pygame.image.load(f"{Path('test_zone/resources2/images/backgrounds/starrynight.png')}")
credits_background = pygame.image.load(f"{Path('test_zone/resources2/images/backgrounds/space.png')}")
char_create_background = pygame.image.load(f"{Path('test_zone/resources2/images/backgrounds/grunge.jpg')}")

#background image
background_img = pygame.image.load(f"{Path('test_zone/resources2/images/backgrounds/throne.png')}")

#panel image
panel_img = pygame.image.load(f"{Path('test_zone/resources2/images/backgrounds/parchment.png')}")

#load image
#load victory and defeat images
victory_img = pygame.image.load(f"{Path('test_zone/resources2/images/ui_elements/victory.png')}")
victory_img = pygame.transform.scale(victory_img, (600,500))

defeat_img = pygame.image.load(f"{Path('test_zone/resources2/images/ui_elements/defeat.png')}")
defeat_img = pygame.transform.scale(defeat_img, (600,500))