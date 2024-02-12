import pygame
from pathlib import Path

#menu background
menubackground_img = pygame.image.load(f"{Path('resources/picture/menubackground.png')}")
#background image
background_img = pygame.image.load(f"{Path('resources/picture/background3.png')}")


#panel image
panel_img = pygame.image.load(f"{Path('resources/picture/UI board Large parchment.png')}")

#load image
#load victory and defeat images
victory_img = pygame.image.load(f"{Path('resources/picture/victory.png')}")
victory_img = pygame.transform.scale(victory_img, (600,500))

defeat_img = pygame.image.load(f"{Path('resources/picture/defeat.png')}")
defeat_img = pygame.transform.scale(defeat_img, (600,500))