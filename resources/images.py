import pygame
from pathlib import Path

# This part is for my Black formatter extension don't worry about it
# fmt: off


# convert_aplha for transparent background
#menu background
menubackground_img = pygame.image.load(f"{Path('resources/images/backgrounds/menubackground.png')}").convert()

options_background = pygame.image.load(f"{Path('resources/images/backgrounds/option.jpg')}").convert()
credits_background = pygame.image.load(f"{Path('resources/images/backgrounds/credit.jpg')}").convert()
story_background = pygame.image.load(f"{Path('resources/images/backgrounds/story.jpg')}").convert()
char_select_menu = pygame.image.load(f"{Path('resources/images/backgrounds/charselect.jpg')}").convert()
char_select_background = pygame.image.load(f"{Path('resources/images/backgrounds/charselect.jpg')}").convert()
gamelog_background = pygame.image.load(f"{Path('resources/images/backgrounds/parchment.png')}").convert_alpha()

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
paladin_marketing = pygame.image.load(f"{Path('resources/images/units/Paladin/paladinborder.jpg')}").convert()
marchosias_marketing = pygame.image.load(f"{Path('resources/images/units/Marchosias/marchosiasborder.jpg')}").convert()

# passive images
warrior_passive = pygame.image.load(f"{Path('resources/images/skill/warriorpassive.png')}").convert()
reaper_passive = pygame.image.load(f"{Path('resources/images/skill/reaperpassive.png')}").convert()
bandit_passive = pygame.image.load(f"{Path('resources/images/skill/anyhow.png')}").convert()
tank_passive = pygame.image.load(f"{Path('resources/images/skill/anyhow.png')}").convert()
princess_passive = pygame.image.load(f"{Path('resources/images/skill/anyhow.png')}").convert()
necromancer_passive = pygame.image.load(f"{Path('resources/images/skill/anyhow.png')}").convert()
paladin_passive = pygame.image.load(f"{Path('resources/images/skill/paladinpassive.png')}").convert()
marchosias_passive = pygame.image.load(f"{Path('resources/images/skill/marchosiaspassive.png')}").convert()


#skill 1 images
warrior_skill1 = pygame.image.load(f"{Path('resources/images/skill/hasaki.png')}").convert()
reaper_skill1 = pygame.image.load(f"{Path('resources/images/skill/Decay.png')}").convert()
bandit_skill1 = pygame.image.load(f"{Path('resources/images/skill/anyhow.png')}").convert()
tank_skill1 = pygame.image.load(f"{Path('resources/images/skill/cannon.jpg')}").convert()
princess_skill1 = pygame.image.load(f"{Path('resources/images/skill/heal.jpg')}").convert()
necromancer_skill1 = pygame.image.load(f"{Path('resources/images/skill/siphon.png')}").convert()
paladin_skill1 = pygame.image.load(f"{Path('resources/images/skill/Sacrifice.png')}").convert()
marchosias_skill1 = pygame.image.load(f"{Path('resources/images/skill/hell_fire.png')}").convert()


#skill 2 images
warrior_skill2 = pygame.image.load(f"{Path('resources/images/skill/inspire.png')}").convert()
reaper_skill2 = pygame.image.load(f"{Path('resources/images/skill/Dead_Scythe.png')}").convert()
bandit_skill2 = pygame.image.load(f"{Path('resources/images/skill/anyhow.png')}").convert()
tank_skill2 = pygame.image.load(f"{Path('resources/images/skill/Machine_Gun.png')}").convert()
princess_skill2 = pygame.image.load(f"{Path('resources/images/skill/regen.png')}").convert()
necromancer_skill2 = pygame.image.load(f"{Path('resources/images/skill/infect.png')}").convert()
paladin_skill2 = pygame.image.load(f"{Path('resources/images/skill/gospel.png')}").convert()
marchosias_skill2 = pygame.image.load(f"{Path('resources/images/skill/Infernal_Rebirth.png')}").convert()

# skill 3 images
warrior_skill3 = pygame.image.load(f"{Path('resources/images/skill/execute.png')}").convert()
reaper_skill3 = pygame.image.load(f"{Path('resources/images/skill/Hell_descent.png')}").convert()
bandit_skill3 = pygame.image.load(f"{Path('resources/images/skill/empty.png')}").convert()
tank_skill3 = pygame.image.load(f"{Path('resources/images/skill/Flamethrower.png')}").convert()
princess_skill3 = pygame.image.load(f"{Path('resources/images/skill/wish.png')}").convert()
necromancer_skill3 = pygame.image.load(f"{Path('resources/images/skill/doom.png')}").convert()
paladin_skill3 = pygame.image.load(f"{Path('resources/images/skill/smite.jpg')}").convert()
marchosias_skill3 = pygame.image.load(f"{Path('resources/images/skill/Infernal_Cataclysm.png')}").convert()
