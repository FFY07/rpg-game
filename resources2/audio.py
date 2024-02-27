from pathlib import Path

import pygame

pygame.init()
# fmt: off

# Cannot load music streams here as pygame only holds one at a time (only the last-loaded music stream will play)


# BGM
battle_alt = f"{Path('resources2/audio/bgm/sts_mind_bloom.wav')}"

menu = f"{Path('resources2/audio/bgm/sts_main.wav')}"

credits_bgm = f"{Path('resources2/audio/bgm/Phantom.wav')}"

# Stupid section
easter = f"{Path('resources2/audio/bgm/driftveil-city-theme-pokémon-black-&-white-(toothless-dancing)-made-with-Voicemod.mp3')}"

# Create a class so it doesn't load every time the sound is played and crash the game
# Sound effects

class SoundEffects():
    def __init__(self):        
        self.click_sfx = pygame.mixer.Sound(f"{Path('resources2/audio/game_effects/click.wav')}")

        self.sword_sfx = pygame.mixer.Sound(f"{Path('resources2/audio/character_effects/unsheath_sword-6113.wav')}")

        self.reaper_basic = pygame.mixer.Sound(f"{Path('resources2/audio/character_effects/Reaper/double_unsheath2.wav')}")

        self.warrior_basic = pygame.mixer.Sound(f"{Path('resources2/audio/character_effects/Warrior/heavy_slash.wav')}")
        self.warrior_basic.set_volume(1)

        self.tank_basic = pygame.mixer.Sound(f"{Path('resources2/audio/character_effects/Tank/wot_37mm.wav')}")
        self.tank_machine_gun = pygame.mixer.Sound(f"{Path('resources2/audio/character_effects/Tank/wot_autocannon.wav')}")
        self.tank_load_shell = pygame.mixer.Sound(f"{Path('resources2/audio/character_effects/Tank/wot_load_shell.wav')}")
        self.tank_183mm = pygame.mixer.Sound(f"{Path('resources2/audio/character_effects/Tank/wot_183mm.wav')}")

        self.magic_sfx = pygame.mixer.Sound(f"{Path('resources2/audio/character_effects/1168-za-warudo-sound-effect.wav')}")
        self.magic_sfx.set_volume(0.4)

        self.potion_sfx = pygame.mixer.Sound(f"{Path('resources2/audio/character_effects/potion.wav')}")
        self.potion_sfx.set_volume(0.4)

        self.oom_sfx = pygame.mixer.Sound(f"{Path('resources2/audio/game_effects/error.wav')}")

        self.death_sfx = pygame.mixer.Sound(f"{Path('resources2/audio/character_effects/warzone_armour_crack.wav')}")
