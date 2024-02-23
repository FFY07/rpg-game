from pathlib import Path

import pygame

pygame.init()
# fmt: off

# Cannot load music streams here as pygame only holds one at a time (only the last-loaded music stream will play)

# BGM
battle = f"{Path('test_zone/resources2/audio/bgm/Fantasy RPG Music Pack Vol.3/Tracks/mp3/Action 2.mp3')}"
battle_alt = f"{Path('test_zone/resources2/audio/bgm/glorious_morning.mp3')}"

start = f"{Path('test_zone/resources2/audio/bgm/Fantasy RPG Music Pack Vol.3/Tracks//mp3/Ambient 3.mp3')}"
game_over = f"{Path('test_zone/resources2/audio/bgm/Fantasy RPG Music Pack Vol.3/Tracks/mp3/Fx 3.mp3')}"
menu_alt = f"{Path('test_zone/resources2/audio/bgm/amaranth_inst.mp3')}"



# Sound effects
click_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/game_effects/click.mp3')}")

sword_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/unsheath_sword-6113.mp3')}")

reaper_basic = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/double_unsheath2.mp3')}")

warrior_basic = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/charge_slash.mp3')}")
warrior_basic.set_volume(0.4)

tank_basic = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/cannon-fire.mp3')}")
tank_basic.set_volume(0.5)

magic_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/1168-za-warudo-sound-effect.mp3')}")
magic_sfx.set_volume(0.4)

potion_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/potion.wav')}")
potion_sfx.set_volume(0.4)

# Stupid section
easter = f"{Path('test_zone/resources2/audio/bgm/driftveil-city-theme-pokémon-black-&-white-(toothless-dancing)-made-with-Voicemod.mp3')}"
