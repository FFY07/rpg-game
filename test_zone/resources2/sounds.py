from pathlib import Path

import pygame

pygame.init()

# Cannot load music streams here as pygame only holds one at a time (only the last-loaded music stream will play)

# BGM
battle = f"{Path('test_zone/resources2/audio/bgm/Fantasy RPG Music Pack Vol.3/Tracks/mp3/Action 2.mp3')}"
start = f"{Path('test_zone/resources2/audio/bgm/Fantasy RPG Music Pack Vol.3/Tracks//mp3/Ambient 3.mp3')}"
game_over = f"{Path('test_zone/resources2/audio/bgm/Fantasy RPG Music Pack Vol.3/Tracks/mp3/Fx 3.mp3')}"
copyright_pls = f"{Path('test_zone/resources2/audio/bgm/king.mp3')}"

# Sound effects
sword_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/unsheath_sword-6113.mp3')}")
magic_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/1168-za-warudo-sound-effect.mp3')}")
magic_sfx.set_volume(0.4)

# Stupid section
easter = f"{Path('test_zone/resources2/audio/bgm/driftveil-city-theme-pokémon-black-&-white-(toothless-dancing)-made-with-Voicemod.mp3')}"