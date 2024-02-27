import pygame
from pathlib import Path

# This part is for my Black formatter extension don't worry about it
# fmt: off

#menu background
menubackground_img = pygame.image.load(f"{Path('resources2/images/backgrounds/menubackground.png')}")

options_background = pygame.image.load(f"{Path('resources2/images/backgrounds/option.jpg')}")
credits_background = pygame.image.load(f"{Path('resources2/images/backgrounds/artofjoniken_forge2.jpg')}")
story_background = pygame.image.load(f"{Path('resources2/images/backgrounds/story.jpg')}")
char_select_menu = pygame.image.load(f"{Path('resources2/images/backgrounds/artofjokinen_siege.jpg')}") 
char_select_background = pygame.image.load(f"{Path('resources2/images/backgrounds/artofjokinen_castle.jpg')}")

#background image
background_img = pygame.image.load(f"{Path('resources2/images/backgrounds/throne.png')}")

#load victory and defeat images
victory_img = pygame.image.load(f"{Path('resources2/images/ui_elements/victory.png')}")
victory_img = pygame.transform.scale(victory_img, (600,500))

defeat_img = pygame.image.load(f"{Path('resources2/images/ui_elements/defeat.png')}")
defeat_img = pygame.transform.scale(defeat_img, (600,500))


player_target = pygame.image.load(f"{Path('resources2/images/ui_elements/player_target.png')}")
player_target = pygame.transform.scale(player_target, (192, 192))

enemy_target = pygame.image.load(f"{Path('resources2/images/ui_elements/enemy_target.png')}")
enemy_target = pygame.transform.scale(enemy_target, (192, 192))

# Marketing images
warrior_marketing = pygame.image.load(f"{Path('resources2/images/units/Warrior/Kassadin_0.jpg')}")
reaper_marketing = pygame.image.load(f"{Path('resources2/images/units/Reaper/reaper_marketing.jpg')}")
bandit_marketing = pygame.image.load(f"{Path('resources2/images/units/Bandit/bandit_marketing.jpg')}")
tank_marketing = pygame.image.load(f"{Path('resources2/images/units/Tank/tank_marketing.jpg')}")
