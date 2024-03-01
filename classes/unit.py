from pathlib import Path
import random
import pygame

import gui.screen as scr

import gui.ui_functions as ui_functions

MAX_HEALTH = 100
MAX_MANA = 100

EXP_TO_NEXT_LEVEL = 100

COINS = 0


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

        self.level = 1

        # Exp to next level
        self.level_exp_dict = {
            1: 100,
            2: 150,
            3: 220,
            4: 340,
            5: 450,
            6: 560,
            7: 680,
            8: 840,
            9: 1200,
            10: 1400,
            11: 1700,
            12: 2000,
            13: 2400,
            14: 2900,
            15: 4000,
            16: 5500,
            17: 7200,
        }

        self.exp = 0

        self.coins = COINS

        self.selected = False
        self.direction = "right"

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

        self.stat_bar_center_offset_x = 0
        self.stat_bar_center_offset_y = -100

        self.death_effect = ui_functions.HitImage("effect/misc/blood/blood1", self, 100)

        self.inventory = {
            "Health Potion": 2,
            "Mana Potion": 2,
            "Strength Shard": 1,
            "Defence Shard": 1,
        }

        # Turn-based effects

        # Example usage: burn for 5 rounds, 10 damage each = self.burn_stacks.append[5, 10]
        # Increase bonus_defence by 5 for 3 rounds = self.bonus_defence_stacks = [3, 5]
        self.burn_stacks = []
        self.health_regen_stacks = []

        # Give every character default mana regen (-1 = infinite)
        self.mana_regen_stacks = [[-1, 5]]

        self.bonus_strength = 0
        self.bonus_strength_stacks = []

        self.bonus_intelligence = 0
        self.bonus_intelligence_stacks = []

        self.bonus_defence = 0
        self.bonus_defence_stacks = []

        self.bonus_magic_resist = 0
        self.bonus_magic_resist_stacks = []

        # Counter-based effects
        # self.curse_stacks = int
        # self.parry_stacks = []

        # def parry(self, number):
        #     for i in range(3):
        #         self.parry_stacks.append(self.strength * 2)

        # if target.parry_stacks:
        #     damage = target.parry_stacks.pop(0)
        #     self.health -= damage
        self.moves = {"Basic Attack": self.basic_attack}
        self.move_desc = {
            "Basic Attack": "Basic attack for attacking attacked with attacker attack"
        }

    # UPDATE: YES THIS WILL CRASH THE GAME RANDOMLY
    # def load_sounds(self):
    #     """Loads the sounds into variables... wonder if this causes crashing"""
    #     match self.unit_class:
    #         case "Tank":
    #             self.default_attack_sfx = self.game.audio_handler.tank_basic

    #         case "Warrior":
    #             self.default_attack_sfx = self.game.audio_handler.warrior_basic

    #         case "Reaper":
    #             self.default_attack_sfx = self.game.audio_handler.reaper_basic

    #         case _:
    #             self.default_attack_sfx = self.game.audio_handler.sword_sfx

    def load_animations(self):
        for state in self.states:
            path = Path(f"resources/images/units/{self.unit_class}/{state}")
            image_list = list(path.glob("*.*"))

            # Load images as pygame surfaces
            loaded_images = []
            for frame in image_list:
                image = pygame.image.load(frame).convert_alpha()
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

    def update_alive(self):
        if self.alive:
            if self.health <= 0:
                self.health = 0
                self.alive = False
                self.change_state("death")
                self.game.event_log.append(f"\n{self.name} HAS DIED! \n")

            if self.health > self.max_health:
                self.health = self.max_health

            if self.mana > self.max_mana:
                self.mana = self.max_mana

    def update_level(self):
        """Updates the level of the unit based on their exp"""

        # Only updates if the unit is alive
        if self.alive:

            # Max level cannot exceed the level dict
            if self.level < len(self.level_exp_dict):

                if self.exp > self.level_exp_dict[self.level]:
                    self.exp -= self.level_exp_dict[self.level]
                    self.level += 1
                    self.level_stats()

                    # We can spawn particles or something here as well
                    self.game.event_log.append(
                        f"{self.name} has levelled up to {self.level}!"
                    )

    def tick_effects(self):

        # NOTE ON POTENTIAL BUG: Have not tested with negative bonus values on stats resulting in overall negative stat

        damage = 0
        if self.alive:

            # Forget it, let's just hardcode
            if self.burn_stacks:
                self.game.sprites.add(
                    ui_functions.HitImage("misc/magic/magma", self, 1, 128, 128)
                )
                # Example burn: [5, 10] = tick 5 turns, 10 damage each time
                for i, burn in enumerate(self.burn_stacks):
                    if not burn[0] < 0:
                        burn[0] -= 1
                    damage += burn[1]
                    self.game.event_log.append(
                        f"{self.name} has lost {damage} health due to burn!"
                    )

                    # If there are no more ticks left on the burn, remove it from the list
                    if not burn[0]:
                        self.burn_stacks.pop(i)
                        self.game.event_log.append(
                            f"{self.name} has recovered from a burn!"
                        )

            # negative negative = positive
            if self.health_regen_stacks:
                for i, regen in enumerate(self.health_regen_stacks):
                    if not regen[0] < 0:
                        regen[0] -= 1
                    damage -= regen[1]
                    self.game.event_log.append(
                        f"{self.name} has regenerated {abs(damage)} health!"  # abs else negative
                    )
                    if not regen[0]:
                        self.health_regen_stacks.pop(i)
                        self.game.event_log.append(
                            f"A health regeneration stack has worn off for {self.name}"
                        )

            if self.mana_regen_stacks:
                for i, regen in enumerate(self.mana_regen_stacks):
                    if not regen[0] < 0:
                        regen[0] -= 1
                    self.mana += regen[1]
                    self.game.event_log.append(
                        f"{self.name} has regenerated {regen[1]} mana!"
                    )
                    if not regen[0]:
                        self.mana_regen_stacks.pop(i)
                        self.game.event_log.append(
                            f"A mana regeneration stack has worn off for {self.name}"
                        )

            # reset bonus_strength before calculating how much we get
            self.bonus_strength = 0
            if self.bonus_strength_stacks:
                for i, effect in enumerate(self.bonus_strength_stacks):
                    if not effect[0] < 0:
                        effect[0] -= 1
                    self.bonus_strength += effect[1]
                    self.game.event_log.append(
                        f"{self.name} has {self.bonus_strength} bonus strength!"
                    )
                    if not effect[0]:
                        self.bonus_strength_stacks.pop(i)
                        self.game.event_log.append(
                            f"{self.name}'s damage is back to normal..."
                        )

            self.bonus_intelligence = 0
            if self.bonus_intelligence_stacks:
                for i, effect in enumerate(self.bonus_intelligence_stacks):
                    if not effect[0] < 0:
                        effect[0] -= 1
                    self.bonus_intelligence += effect[1]
                    self.game.event_log.append(
                        f"{self.name} has {self.bonus_intelligence} bonus intelligence!"
                    )
                    if not effect[0]:
                        self.bonus_intelligence_stacks.pop(i)
                        self.game.event_log.append(
                            f"{self.name}'s intelligence is back to normal..."
                        )

            self.bonus_defence = 0
            if self.bonus_defence_stacks:
                for i, effect in enumerate(self.bonus_defence_stacks):
                    if not effect[0] < 0:
                        effect[0] -= 1
                    self.bonus_defence += effect[1]
                    self.game.event_log.append(
                        f"{self.name} has {self.bonus_defence} bonus defence!"
                    )
                    if not effect[0]:
                        self.bonus_defence_stacks.pop(i)
                        self.game.event_log.append(
                            f"{self.name}'s defence is back to normal..."
                        )

            self.bonus_magic_resist = 0
            if self.bonus_magic_resist_stacks:
                for i, effect in enumerate(self.bonus_magic_resist_stacks):
                    if not effect[0] < 0:
                        effect[0] -= 1
                    self.bonus_magic_resist += effect[1]
                    self.game.event_log.append(
                        f"{self.name} has {self.bonus_magic_resist} bonus magic resist!"
                    )

                    if not effect[0]:
                        self.bonus_magic_resist_stacks.pop(i)
                        self.game.event_log.append(
                            f"{self.name}'s magic resistance is back to normal..."
                        )

            if damage > 0:
                self.health -= damage
                self.game.sprites.add(ui_functions.DamageText(self, int(damage)))

            if damage < 0:
                self.health -= damage

                self.game.sprites.add(
                    ui_functions.DamageText(self, abs(int(damage)), False, "green")
                )

    def change_state(self, target_state):
        """Resets the current frame to 0 so the animation doesn't start halfway"""
        self.current_frame = 0
        self.state = target_state

        if target_state == "death":
            self.game.sprites.add(self.death_effect)
            self.play_sound(self.game.audio_handler.death_sfx)

    def activate(self, active_pos):
        """Move character to the active position"""
        self.prev_pos = self.rect.center
        self.rect.center = active_pos

    def deactivate(self):
        self.rect.center = self.prev_pos

    def play_sound(self, sound_object: pygame.mixer.Sound):
        """Plays sound if sound is enabled; separates player and enemy sounds into separate channels"""
        if self.game.sound:
            if self.team == "player":
                self.game.main_channel.play(sound_object)
            elif self.team == "enemy":
                self.game.main_channel.play(sound_object)

                # It should never reach this point, and this may cause crashes
            else:
                pygame.mixer.Sound.play(sound_object)

    def consume_item(self, item):
        """Probably shouldn't be coding all the item effects here :D I love deadlines"""
        if self.inventory[item] > 0:
            self.inventory[item] -= 1
            self.play_sound(self.game.audio_handler.potion_sfx)

            match item:
                case "Health Potion":
                    if self.unit_class == "Necromancer":
                        self.health -= self.max_health * 0.1
                    else:
                        self.health += self.max_health * 0.5  # test

                    if self.health > self.max_health:
                        self.health = self.max_health

                    self.game.event_log.append(
                        f"{self.name} consumed a health potion! {self.inventory[item]} left."
                    )
                    print("Recovered health!")

                case "Mana Potion":
                    if self.unit_class == "reaper":
                        self.health += self.max_health * 0.1
                    else:
                        self.mana += 50

                    self.game.event_log.append(
                        f"{self.name} consumed a mana potion! {self.inventory[item]} left."
                    )
                    print("Recovered mana!")

                case "Strength Shard":
                    self.prev_strength = self.strength
                    self.strength = int(self.strength * 0.1)

                    self.game.event_log.append(
                        f"{self.name} used a strength shard! {self.inventory[item]} left."
                    )
                    print(
                        f"Increased strength from {self.prev_strength} to {self.strength}!"
                    )

                case "Defence Shard":
                    self.defence = int(self.defence * 1.1)

                    self.game.event_log.append(
                        f"{self.name} used a defence shard! {self.inventory[item]} left."
                    )
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
        self,
        target: object,
        damage: int,
        crit=False,
        damage_effect_name="atk",
        effect_speed=2,
    ):
        """Update animations, damage text, exp, coins, etc."""

        # Game design-wise it would be better to not have float exp and coins so we int them
        self.exp += int(damage)
        self.coins += int(damage)

        self.change_state("attack")
        target.change_state("hurt")
        target.health -= damage

        self.game.sprites.add(
            ui_functions.HitImage(damage_effect_name, target, effect_speed)
        )
        self.game.sprites.add(ui_functions.DamageText(target, int(damage), crit))

    def update_healstats(
        self, target: object, heal: int, damage_effect_name="healing", effect_speed=2
    ):
        """Update heal stats or something"""

        self.change_state("defend")
        target.change_state("defend")
        target.health += heal

        # THIS IS NOT AI WRITTEN,  it will always set the smallest number, this code ensure that it wont heal more than max_health)
        target.health = min(target.max_health, target.health)

        self.game.sprites.add(
            ui_functions.HitImage(damage_effect_name, target, effect_speed)
        )
        self.game.sprites.add(ui_functions.DamageText(target, int(heal)))

    # obvious what this do if u know healthstats
    def update_manastats(
        self, target: object, regen: int, damage_effect_name="healing", effect_speed=2
    ):

        self.change_state("defend")
        target.change_state("defend")
        target.mana += regen
        target.mana = min(target.max_mana, target.mana)

        self.game.sprites.add(
            ui_functions.HitImage(damage_effect_name, target, effect_speed)
        )
        self.game.sprites.add(ui_functions.DamageText(target, int(regen)))

    def calc_damage(
        self, target: object, damage_type="physical", multiplier=1.0
    ) -> float:
        """Checks for crit and enemy resistances"""

        if damage_type == "physical":
            base_damage = (self.strength + self.bonus_strength) * multiplier
        elif damage_type == "magic":
            base_damage = (self.intelligence + self.bonus_intelligence) * multiplier

        # Check for crit
        if self.crit_chance >= random.randint(0, 100):
            damage = base_damage * self.crit_mult
            crit = True
        else:
            damage = base_damage
            crit = False

        # Check target resistances
        if damage_type == "physical":
            final_damage = damage / (
                1 + ((target.defence + target.bonus_defence) / 100)
            )

        elif damage_type == "magic":
            final_damage = damage / (
                1 + ((target.magic_resist + target.bonus_magic_resist) / 100)
            )

        if final_damage < 0:
            final_damage = 0

        return final_damage, crit

    def basic_attack(self, target: object, target_team: list):
        """Basic physical attack that also restores a bit of mana"""
        if self.is_target_hostile(target):
            damage, crit = self.calc_damage(target, "physical", 1)

            # Melee is optional and only for direct attacks
            self.melee(target)
            self.update_stats(target, damage, crit, "misc/physical/spark", 2)

            # Add mana when attacking
            if self.mana < self.max_mana:
                self.mana += 10
                if self.mana > self.max_mana:
                    self.mana = self.max_mana

            # This part needs to be hardcoded else the game will crash. Pygame mixer does not like passing sound objects
            # through variables, so I can't use the load sounds method above to assign default sound objects in variables
            match self.unit_class:
                case "Warrior":
                    self.play_sound(self.game.audio_handler.warrior_basic)

                case "Tank":
                    self.play_sound(self.game.audio_handler.tank_basic)

                case "Reaper":
                    self.play_sound(self.game.audio_handler.reaper_basic)

                # case "Necromancer":
                #     self.play_sound(self.game.audio_handler.necromancer_basic)

                case _:
                    self.play_sound(self.game.audio_handler.sword_sfx)

            self.play_sound(self.game.audio_handler.sword_sfx)
            self.game.event_log.append(
                f"{self.name} basic attacks {target.name} for {int(damage)} physical damage!"
            )

            if crit:
                self.game.event_log.append("It was a crit!")

            # Note: the game will check if the attack returns True, else the attack will not proceed (e.g. prevent attacking with not enough mana)
            return True

    def check_ratio(self, stat: str) -> float:
        match stat:
            case "health":
                return self.health / self.max_health
            case "mana":
                return self.mana / self.max_mana
            case "exp":
                return self.exp / self.level_exp_dict[self.level]

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
