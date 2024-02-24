from pathlib import Path

import pygame

pygame.init()
# fmt: off

# Cannot load music streams here as pygame only holds one at a time (only the last-loaded music stream will play)

# BGM
battle = f"{Path('test_zone/resources2/audio/bgm/Fantasy RPG Music Pack Vol.3/Tracks/mp3/Action 2.mp3')}"
battle_alt = f"{Path('test_zone/resources2/audio/bgm/sts_mind_bloom.mp3')}"

start = f"{Path('test_zone/resources2/audio/bgm/Fantasy RPG Music Pack Vol.3/Tracks//mp3/Ambient 3.mp3')}"
game_over = f"{Path('test_zone/resources2/audio/bgm/Fantasy RPG Music Pack Vol.3/Tracks/mp3/Fx 3.mp3')}"
menu = f"{Path('test_zone/resources2/audio/bgm/sts_main.mp3')}"

credits_bgm = f"{Path('test_zone/resources2/audio/bgm/Phantom.mp3')}"

# Sound effects
click_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/game_effects/click.mp3')}")

sword_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/unsheath_sword-6113.mp3')}")

reaper_basic = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/double_unsheath2.mp3')}")

warrior_basic = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/heavy_slash.mp3')}")
warrior_basic.set_volume(1)

tank_basic = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/wot_122mm.mp3')}")
tank_basic.set_volume(1)

magic_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/1168-za-warudo-sound-effect.mp3')}")
magic_sfx.set_volume(0.4)

potion_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/potion.wav')}")
potion_sfx.set_volume(0.4)

death_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/warzone_armour_crack.wav')}")

# Stupid section
easter = f"{Path('test_zone/resources2/audio/bgm/driftveil-city-theme-pokémon-black-&-white-(toothless-dancing)-made-with-Voicemod.mp3')}"
