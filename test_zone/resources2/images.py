import pygame
from pathlib import Path

#menu background
menubackground_img = pygame.image.load(f"{Path('test_zone/resources2/images/backgrounds/menubackground.png')}")

options_background = pygame.image.load(f"{Path('test_zone/resources2/images/backgrounds/seaview.png')}")
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

target_img = pygame.image.load(f"{Path('test_zone/resources2/images/ui_elements/target.png')}")
red_arrow_down = pygame.image.load(f"{Path('test_zone/resources2/images/ui_elements/red_arrow_down.png')}")
red_arrow_down = pygame.transform.scale(red_arrow_down, (red_arrow_down.get_width() * 2, red_arrow_down.get_height() * 2))