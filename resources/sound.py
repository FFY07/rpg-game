from pathlib import Path

import pygame

pygame.init()

# Cannot load music streams here as pygame only holds one at a time (only the last-loaded music stream will play)

# BGM
battle = f"{Path('resources/sound/Fantasy RPG Music Pack Vol.3/Tracks/mp3/Action 3.mp3')}"
start = f"{Path('resources/sound/Fantasy RPG Music Pack Vol.3/Tracks//mp3/Ambient 2.mp3')}"
game_over = f"{Path('resources/sound/Fantasy RPG Music Pack Vol.3/Tracks/mp3/Fx 3.mp3')}"

# Sound effects
sword_sfx = pygame.mixer.Sound(f"{Path('resources/sound/unsheath_sword-6113.mp3')}")

# Stupid section
easter = f"{Path('resources/sound/jocofullinterview41.mp3')}"