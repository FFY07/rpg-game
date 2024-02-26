from pathlib import Path
import random
import pygame

import gui2.screen as scr
import resources2.images as images
import resources2.audio as audio

import gui2.ui_functions as ui_functions

MAX_HEALTH = 100
MAX_MANA = 100

START_LEVEL = 1
BASE_EXP = 0
EXP_TO_NEXT_LEVEL = 100

COINS = 0

# Note: check knight.py for class-specific references


class Unit(pygame.sprite.Sprite):
    def __init__(self, name, team, id_no=0, game=None):
        super().__init__()
        self.game = game
        self.max_health = MAX_HEALTH
        self.health = self.max_health
        self.max_mana = MAX_MANA
        self.mana = self.max_mana

        # 20% default is quite high, want to change?
        self.crit_chance = 20
        self.crit_mult = 1.5

        self.level = START_LEVEL
        self.exp = BASE_EXP
        self.exp_to_next_level = EXP_TO_NEXT_LEVEL

        self.coins = COINS

        self.selected = False
        self.direction = "right"
        self.id = id_no

        self.name = name
        self.size_scale = 2
        self.unit_class = "Knight"
        self.alive = True

        # Starting position
        self.position = (scr.SCREEN_WIDTH // 2, scr.SCREEN_HEIGHT // 2)
        self.prev_pos = self.position

        self.current_frame = 0
        self.last_updated = 0
        self.dx = 0
        self.dy = 0
        self.state = "idle"
        self.states = ["idle", "attack", "hurt", "defend", "death"]
        self.animations = {}
        self.anim_speed = 100

        self.attack_audio = audio.sword_sfx
        self.death_audio = audio.death_sfx

        self.death_effect = ui_functions.HitImage("blood1", self, 100)

        self.inventory = {
            "Health Potion": 3,
            "Mana Potion": 3,
            "Strength Shard": 1,
            "Defence Shard": 1,
        }

        self.moves = {"Basic Attack": self.basic_attack}

    def load_animations(self):
        for state in self.states:
            path = Path(f"test_zone/resources2/images/units/{self.unit_class}/{state}")
            image_list = list(path.glob("*.*"))

            # Load images as pygame surfaces
            loaded_images = []
            for frame in image_list:
                image = pygame.image.load(frame)
                image = pygame.transform.scale(
                    image,
                    (
                        image.get_width() * self.size_scale,
                        image.get_height() * self.size_scale,
                    ),
                )
                # image = pygame.transform.scale(image, (160, 160))

                if self.direction == "right":
                    loaded_images.append(image)

                elif self.direction == "left":
                    image = pygame.transform.flip(image, True, False)
                    loaded_images.append(image)

            self.animations[state] = loaded_images

    def update(self):
        # self.game.canvas.blit(images.hit_effect, (0,0))
        current_time = pygame.time.get_ticks()
        if (
            current_time - self.last_updated > self.anim_speed
            and self.current_frame != -1
        ):
            self.last_updated = current_time
            self.current_frame += 1

        # Resets back to idle frame after completing an animation state
        if (
            self.current_frame >= len(self.animations[self.state])
            and self.state != "death"
        ):
            self.current_frame = 0
            self.state = "idle"

        # Leaves character dead body on the ground
        elif (
            self.current_frame >= len(self.animations[self.state])
            and self.state == "death"
        ):
            self.current_frame = -1

        self.image = self.animations[self.state][self.current_frame]
        self.rect.move_ip(self.dx, self.dy)

        # Checks unit state
        self.update_alive()
        self.update_level()

    def update_alive(self):
        if self.alive:
            if self.health <= 0:
                self.health = 0
                self.alive = False
                self.change_state("death")

    def update_level(self):
        if self.alive:
            # if self.level <= len(self.level_dict)
            # else print can't level anymore or something most RPGs and games like LoL also have max levels

            # Please change this to a dictionary system {1: 100, 2: 150, 3: 240, 4: 350, etc}
            # if self.exp > self.level_dict[self.level]:

            if self.exp > self.exp_to_next_level:
                self.exp -= self.exp_to_next_level
                self.level += 1

                # We can spawn particles or something here as well
                print(f"{self.name} has levelled up to {self.level}!")

    def change_state(self, target_state):
        """Resets the current frame to 0 so the animation doesn't start halfway"""
        self.current_frame = 0
        self.state = target_state

        if target_state == "death":
            self.game.sprites.add(self.death_effect)
            pygame.mixer.Sound.play(self.death_audio)

    def activate(self, active_pos):
        """Move character to the active position"""
        self.prev_pos = self.rect.center
        self.rect.center = active_pos

    def deactivate(self):
        self.rect.center = self.prev_pos

    def consume_item(self, item):
        """Probably shouldn't be coding all the item effects here :D I love deadlines"""
        if self.inventory[item] > 0:
            self.inventory[item] -= 1
            pygame.mixer.Sound.play(audio.potion_sfx)

            match item:
                case "Health Potion":
                    self.health -= 500  # test
                    if self.health > self.max_health:
                        self.health = self.max_health

                    print("Recovered health!")

                case "Mana Potion":
                    self.mana += 50

                    print("Recovered mana!")

                case "Strength Shard":
                    self.prev_strength = self.strength
                    self.strength = int(self.strength * 999)

                    print(
                        f"Increased strength from {self.prev_strength} to {self.strength}!"
                    )

                case "Defence Shard":
                    self.defence = int(self.defence * 1.1)

                    print("Increased defence!")
        else:
            print(f"No {item} left!")

    def is_target_hostile(self, target) -> bool:
        """Returns True if target is not on the same team as us"""
        if self.team != target.team:
            return True
        
        else:
            return False

    def melee(self, target: object, distance=0):
        """Warps in front of the target"""

        # Do not call this multiple times in a loop as the deactivate is currently not set to handle repeated activations
        if self.team == "player":
            destx, desty = target.rect.midleft
            destx -= distance
            self.activate((destx, desty))
        else:
            destx, desty = target.rect.midright
            destx += distance
            self.activate((destx, desty))

        self.change_state("attack")
        target.change_state("hurt")

    def update_stats(
        self, target: object, damage: int, damage_effect_name="atk", effect_speed=2
    ):
        """Update animations, damage text, exp, coins, etc."""
        # Game design-wise it would be better to not have float exp and coins
        self.exp += int(damage)
        self.coins += int(damage)

        self.change_state("attack")
        target.change_state("hurt")
        target.health -= damage

        self.game.sprites.add(
            ui_functions.HitImage(damage_effect_name, target, effect_speed)
        )
        self.game.sprites.add(ui_functions.DamageText(target, int(damage)))

    def update_healstats(
        self, target: object, heal: int, damage_effect_name="healing", effect_speed=2
    ):
        """Update animations, damage text, exp, coins, etc."""
        # Game design-wise it would be better to not have float exp and coins
  
        self.change_state("defend")
        target.change_state("defend")
        target.health += heal
        
        # THIS IS NOT AI WRITTEN,  it will always set the smallest number, this code ensure that it wont heal more than max_health)
        target.health = min(target.max_health, target.health) 

        self.game.sprites.add( 
            ui_functions.HitImage(damage_effect_name, target, effect_speed)
        )
        self.game.sprites.add(ui_functions.DamageText(target, int(heal)))

    def calc_damage(
        self, target: object, damage_type="Physical", multiplier=1.0
    ) -> float:
        """Checks for crit and enemy resistances"""

        if damage_type == "physical":
            base_damage = self.strength * multiplier
        elif damage_type == "magic":
            base_damage = self.intelligence * multiplier

        # Check for crit
        if self.crit_chance >= random.randint(0, 100):
            damage = base_damage * self.crit_mult
        else:
            damage = base_damage

        # Check target resistances
        if damage_type == "physical":
            final_damage = damage / (1 + (target.defence / 100))

        elif damage_type == "magic":
            final_damage = damage / (1 + (target.magic_resist / 100))

        if final_damage < 0:
            final_damage = 0

        return final_damage

    def basic_attack(self, target: object, target_team: list):
        """Basic physical attack that also restores a bit of mana"""
        if self.is_target_hostile(target):
            damage = self.calc_damage(target, "physical", 1)

            # Melee is optional and only for direct attacks
            self.melee(target)
            self.update_stats(target, damage, "atk", 2)

            # Add mana when attacking
            if self.mana < self.max_mana:
                self.mana += 5
                if self.mana > self.max_mana:
                    self.mana = self.max_mana

            if self.game.sound:
                pygame.mixer.Sound.play(self.attack_audio)

            # temporary
            print(f"[DEBUG] Target {target.name} HP: {target.health}/{target.max_health}")
            print(f"[DEBUG] {self.name} MANA: {self.mana}/{self.max_mana}")
            print(f"[DEBUG] {self.name} EXP: {self.exp} COINS: {self.coins}")

            # Note: the game will check if the attack returns True, else the attack will not proceed (e.g. prevent attacking with not enough mana)
            return True