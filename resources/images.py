import pygame
from pathlib import Path

# This part is for my Black formatter extension don't worry about it
# fmt: off

#menu background
menubackground_img = pygame.image.load(f"{Path('resources/images/backgrounds/menubackground.png')}").convert()

options_background = pygame.image.load(f"{Path('resources/images/backgrounds/option.jpg')}").convert()
credits_background = pygame.image.load(f"{Path('resources/images/backgrounds/artofjoniken_forge2.jpg')}").convert()
story_background = pygame.image.load(f"{Path('resources/images/backgrounds/story.jpg')}").convert()
char_select_menu = pygame.image.load(f"{Path('resources/images/backgrounds/charselect.jpg')}").convert()
char_select_background = pygame.image.load(f"{Path('resources/images/backgrounds/charselect.jpg')}").convert()

#background image
background_img = pygame.image.load(f"{Path('resources/images/backgrounds/throne.png')}").convert()

#load victory and defeat images
victory_img = pygame.image.load(f"{Path('resources/images/ui_elements/victory.png')}").convert_alpha()
victory_img = pygame.transform.scale(victory_img, (600,500))

defeat_img = pygame.image.load(f"{Path('resources/images/ui_elements/defeat.png')}").convert_alpha()
defeat_img = pygame.transform.scale(defeat_img, (600,500))


player_target = pygame.image.load(f"{Path('resources/images/ui_elements/player_target.png')}").convert_alpha()
player_target = pygame.transform.scale(player_target, (192, 192))

enemy_target = pygame.image.load(f"{Path('resources/images/ui_elements/enemy_target.png')}").convert_alpha()
enemy_target = pygame.transform.scale(enemy_target, (192, 192))

# Marketing images
warrior_marketing = pygame.image.load(f"{Path('resources/images/units/Warrior/warriorborder.jpg')}").convert()
reaper_marketing = pygame.image.load(f"{Path('resources/images/units/Reaper/reaperborder.jpg')}").convert()
bandit_marketing = pygame.image.load(f"{Path('resources/images/units/Bandit/banditborder.jpg')}").convert()
tank_marketing = pygame.image.load(f"{Path('resources/images/units/Tank/tank_marketing.jpg')}").convert()
princess_marketing = pygame.image.load(f"{Path('resources/images/units/Princess/prinsborder.jpeg')}").convert()
necromancer_marketing = pygame.image.load(f"{Path('resources/images/units/Necromancer/necromancer_marketing.jpg')}").convert()
