from pathlib import Path

from pygame import mixer

# mixer.init()

# In case other people are using black formatter
# fmt: off

# Create a class so it doesn't load every time the sound is played and crash the game
# Sound effects

# STAHP FREEZING
class SoundEffects():
    def __init__(self):
        
        # BGM music paths to stream instead of load into sound object
        self.battle_bgm_path = f"{Path('resources/audio/bgm/sts_mind_bloom.wav')}"
        self.menu_bgm_path = f"{Path('resources/audio/bgm/sts_main.wav')}"
        self.credits_bgm_path = f"{Path('resources/audio/bgm/sts_credits.wav')}"
        self.easter_bgm_path = f"{Path('resources/audio/bgm/driftveil-city-theme-pokémon-black-&-white-(toothless-dancing)-made-with-Voicemod.mp3')}"
        
        
        # Sound effects
        self.click_sfx = mixer.Sound(f"{Path('resources/audio/game_effects/click.wav')}")

        self.sword_sfx = mixer.Sound(f"{Path('resources/audio/character_effects/unsheath_sword-6113.wav')}")

        self.reaper_basic = mixer.Sound(f"{Path('resources/audio/character_effects/Reaper/double_unsheath2.wav')}")
        self.reaper_blood = mixer.Sound(f"{Path('resources/audio/character_effects/Reaper/breeze-of-blood-122253.mp3')}")

        self.warrior_basic = mixer.Sound(f"{Path('resources/audio/character_effects/Warrior/heavy_slash.wav')}")
        self.warrior_basic.set_volume(1)
        
        self.warrior_inspire = mixer.Sound(f"{Path('resources/audio/character_effects/Warrior/inspire.wav')}")

        self.tank_basic = mixer.Sound(f"{Path('resources/audio/character_effects/Tank/wot_37mm.wav')}")
        self.tank_machine_gun = mixer.Sound(f"{Path('resources/audio/character_effects/Tank/wot_autocannon.wav')}")
        self.tank_load_shell = mixer.Sound(f"{Path('resources/audio/character_effects/Tank/wot_load_shell.wav')}")
        self.tank_183mm = mixer.Sound(f"{Path('resources/audio/character_effects/Tank/wot_183mm.wav')}")
        
        self.necromancer_basic = mixer.Sound(f"{Path('resources/audio/character_effects/Necromancer/staff.wav')}")
        self.necromancer_weaken = mixer.Sound(f"{Path('resources/audio/character_effects/Necromancer/weaken.wav')}")
        self.necromancer_infect = mixer.Sound(f"{Path('resources/audio/character_effects/Necromancer/infect.wav')}")     
        self.necromancer_doom = mixer.Sound(f"{Path('resources/audio/character_effects/Necromancer/doom.wav')}")

        self.paladin_smite = mixer.Sound(f"{Path('resources/audio/character_effects/Paladin/magic-charge-mana-2-186628.mp3')}")

        self.marchosias_fire = mixer.Sound(f"{Path('resources/audio/character_effects/Marchosias/dragon-breathes-fire-1-191085.mp3')}")
        self.marchosias_fireshort = mixer.Sound(f"{Path('resources/audio/character_effects/Marchosias/fireball-whoosh-2-179126.mp3')}")
        self.heal_sfx = mixer.Sound(f"{Path('resources/audio/character_effects/02_Heal_02.wav')}")
        self.heal_sfx.set_volume(0.4)
        self.magic_sfx = mixer.Sound(f"{Path('resources/audio/character_effects/1168-za-warudo-sound-effect.wav')}")
        self.magic_sfx.set_volume(0.4)

        self.potion_sfx = mixer.Sound(f"{Path('resources/audio/character_effects/potion.wav')}")
        self.potion_sfx.set_volume(0.4)

        self.oom_sfx = mixer.Sound(f"{Path('resources/audio/game_effects/error.wav')}")
        self.oom_sfx.set_volume(0.5)

        self.death_sfx = mixer.Sound(f"{Path('resources/audio/character_effects/oof.wav')}")
        self.death_sfx.set_volume(0.5)

        self.firemagic_sfx = mixer.Sound(f"{Path('resources/audio/character_effects/fire-magic-6947.mp3')}")