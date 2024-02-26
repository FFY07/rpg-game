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

# Stupid section
easter = f"{Path('test_zone/resources2/audio/bgm/driftveil-city-theme-pokémon-black-&-white-(toothless-dancing)-made-with-Voicemod.mp3')}"

# Create a class so it doesn't load every time the sound is played and crash the game
# Sound effects

class SoundEffects():
    def __init__(self):        
        self.click_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/game_effects/click.mp3')}")

        self.sword_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/unsheath_sword-6113.mp3')}")

        self.reaper_basic = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/double_unsheath2.mp3')}")

        self.warrior_basic = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/heavy_slash.mp3')}")
        self.warrior_basic.set_volume(1)

        self.tank_basic = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/Tank/wot_37mm.mp3')}")
        self.tank_machine_gun = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/Tank/wot_autocannon.mp3')}")
        self.tank_load_shell = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/Tank/wot_load_shell.mp3')}")
        self.tank_183mm = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/Tank/wot_183mm.mp3')}")

        self.magic_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/1168-za-warudo-sound-effect.mp3')}")
        self.magic_sfx.set_volume(0.4)

        self.potion_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/potion.wav')}")
        self.potion_sfx.set_volume(0.4)

        self.oom_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/game_effects/error.wav')}")

        self.death_sfx = pygame.mixer.Sound(f"{Path('test_zone/resources2/audio/character_effects/warzone_armour_crack.wav')}")
