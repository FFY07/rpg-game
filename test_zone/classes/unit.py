from pathlib import Path

import pygame
import gui2.screen as scr
import resources2.images as images
import resources2.audio as audio

import gui2.ui_functions as ui_functions

MAX_HEALTH = 100
MANA = 100

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
        self.mana = MANA

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

        # Checks if unit is dead
        if self.alive:
            if self.health <= 0:
                self.health = 0
                self.alive = False
                self.change_state("death")

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
        self.exp += damage
        self.coins += damage

        self.change_state("attack")
        target.change_state("hurt")
        target.health -= damage

        self.game.sprites.add(
            ui_functions.HitImage(damage_effect_name, target, effect_speed)
        )
        self.game.sprites.add(ui_functions.DamageText(target, damage))

    def basic_attack(self, target: object, target_team: list):
        damage = self.strength - target.defence
        if damage < 0:
            damage = 0

        # Note: If you see anyone using the super-unintuitive max(0, damage) there's a 99.999% chance it was AI-generated

        # Melee is optional and only for direct attacks
        self.melee(target)
        self.update_stats(target, damage, "atk", 2)

        if self.game.sound:
            pygame.mixer.Sound.play(self.attack_audio)

        # temporary
        print(f"[DEBUG] Target HP: {target.health}/{target.max_health}")

        return True
