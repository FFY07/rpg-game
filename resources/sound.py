from pathlib import Path

import pygame

parent = Path(__file__).parents[0]

# BGM
start = f"{parent}\\sound\\Fantasy RPG Music Pack Vol.3\\Tracks\\mp3\\Action 3.mp3"
battle = f"{parent}\\sound\\Fantasy RPG Music Pack Vol.3\\Tracks/\\mp3\\Ambient 2.mp3"
game_over = f"{parent}\\sound\\Fantasy RPG Music Pack Vol.3\\Tracks\\mp3\\Fx 3.mp3"

# sword sound
sword_sfx = pygame.mixer.Sound(f"{parent}\\sound\\unsheath_sword-6113.mp3")

# Stupid section
easter = f"{parent}\\sound\\Dancin-(Krono-Remix)(PaglaSongs).mp3"