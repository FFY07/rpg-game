from pathlib import Path

import pygame
import gui.screen as scr

import resources.fonts as fonts


class TextSprite(pygame.sprite.Sprite):
    # Creates a text sprite; replace me with a docstring once all the parameters are done
    def __init__(
        self,
        text: str,
        size: int,
        text_font=None,
        color="white",
        x_centered=True,
        y_centered=True,
        name=False,
        dx=0,
        dy=0,
        alpha=255,
    ):
        """Generates a text sprite

        Args:
            text (str): The text to display
            size (int): The size of the text
            text_font (str, optional): The font name. Defaults to "freesansbold".
            color (str, optional): The font color. Defaults to "white".
            x (bool, optional): The x coordinate. True = Centered.
            y (bool, optional): The y coordinate. True = Centered.
            dx (bool, optional): Movement along x coordinate. Defaults to 0
            flying (bool, optional): Movement along y coordinate. Default to 0
        """
        super().__init__()
        self.selected = True
        self.toggled = False
        self.name = name
        self.text = text
        self.color = color
        self.alpha = alpha

        if x_centered is True:
            self.x = scr.SCREEN_WIDTH // 2
        else:
            self.x = x_centered

        if y_centered is True:
            self.y = scr.SCREEN_HEIGHT // 2
        else:
            self.y = y_centered

        self.dx = dx
        self.dy = dy

        try:
            self.font = pygame.font.Font(text_font, size)
        except:
            self.font = pygame.font.SysFont(text_font, size)

        self.image = self.font.render(self.text, True, self.color).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        pass

    def update(self):
        self.image = self.font.render(self.text, True, self.color)

        self.rect.move_ip(self.dx, self.dy)

        # Check if we're going upwards
        if self.dy < 0:
            if self.rect.bottom < 0:
                self.kill()
        else:
            if self.rect.top > scr.SCREEN_HEIGHT:
                self.kill()

        # EVERYTHING HERE IS NOT TESTED BECAUSE IDK WHICH SIDE IS WHICH
        if self.dx < 0:
            if self.rect.left < 0:
                self.kill()
        else:
            if self.rect.right > scr.SCREEN_WIDTH:
                self.kill()

        if self.selected:
            self.image.set_alpha(self.alpha)
        else:
            self.image.set_alpha(100)


class Button(pygame.sprite.Sprite):
    def __init__(self, width, height, color, x=True, y=True, name=False, alpha=100):
        super().__init__()
        self.width = width
        self.height = height
        self.name = name

        if x is True:
            self.x = scr.SCREEN_WIDTH // 2
        else:
            self.x = x

        if y is True:
            self.y = scr.SCREEN_HEIGHT // 2
        else:
            self.y = y

        self.color = color
        self.alpha = alpha

        self.selected = False
        self.toggled = False

        self.image = pygame.Surface((self.width, self.height)).convert_alpha()
        self.image.fill(self.color)
        self.image.set_alpha(self.alpha)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        pass

    def update(self):
        if self.toggled:
            self.image.fill("red")
            self.image.set_alpha(self.alpha)

        elif self.selected:
            self.image.fill(self.color)
            self.image.set_alpha(self.alpha)

        else:
            self.image.fill(self.color)
            self.image.set_alpha(0)


class TargetImage(pygame.sprite.Sprite):
    def __init__(self, scene, image, x_offset=0, y_offset=0):
        """Updates position based on the scene's self.selected_unit"""

        super().__init__()
        self.scene = scene
        self.target_sprite = scene.selected_unit
        self.target_x, self.target_y = self.target_sprite.rect.center
        self.selected = True

        self.x_offset = x_offset
        self.y_offset = y_offset

        self.image = image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (
            self.target_x + self.x_offset,
            self.target_y + self.y_offset,
        )

    def update(self):
        self.target_sprite = self.scene.selected_unit
        self.target_x, self.target_y = self.target_sprite.rect.center

        self.rect.center = (
            self.target_x + self.x_offset,
            self.target_y + self.y_offset,
        )

        if self.selected:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(0)


class HitImage(pygame.sprite.Sprite):
    def __init__(self, attack_name, target: object, speed=50, width=256, height=256):
        super().__init__()
        self.target = target
        self.attack_name = attack_name

        self.width = width
        self.height = height

        self.current_frame = 0
        self.last_updated = 0
        self.current_time = 0

        self.animations = []

        self.load_attack_sprites()

        self.anim_speed = speed  # ticks

    def update(self):
        self.current_time = pygame.time.get_ticks()

        if self.current_time - self.last_updated > self.anim_speed:
            self.last_updated = self.current_time
            self.current_frame += 1

            # print(self.target.name, self.current_frame)

        if self.current_frame < len(self.animations):
            self.image = self.animations[self.current_frame]
            self.rect = self.image.get_rect()
            self.rect.center = self.target.rect.center

        else:
            # print(self.current_frame, self.animations)
            self.kill()

    def load_attack_sprites(self):
        """Load attack sprite images"""

        path = Path(f"resources/images/effect/{self.attack_name}")
        image_list = list(path.glob("*.*"))

        # Load images as pygame surfaces

        for frame in image_list:
            image = pygame.image.load(frame).convert_alpha()

            # Size of image
            image = pygame.transform.scale(
                image,
                (
                    self.width,
                    self.height,
                ),
            )

            self.animations.append(image)


class DamageText(pygame.sprite.Sprite):
    def __init__(self, target: object, damage: int, crit=False, color=False):
        super().__init__()
        self.damage_amount = str(damage)
        self.target = target
        self.crit = crit
        self.text_font = "impact"
        self.size = 50

        # If no color is set, use our own default colors
        if not color:
            if self.crit:
                self.color = "yellow"
            else:
                self.color = "white"

            # If damage is 0
            if not damage:
                self.color = "deepskyblue"

        else:
            self.color = color

        try:
            self.font = pygame.font.Font(self.text_font, self.size)
        except:
            self.font = pygame.font.SysFont(self.text_font, self.size)

        self.image = self.font.render(
            self.damage_amount, True, self.color
        ).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.center = self.target.rect.center

        # How many frames before the sprite dies :(
        self.max_lifetime = 180
        self.lifetime = self.max_lifetime

        self.dx = 0
        self.dy = -2

    def update(self):
        self.fade_start = 10

        # move damage text up
        self.rect.move_ip(self.dx, self.dy)

        # Oh no it's growing old
        self.lifetime -= 1

        # Alpha ranges from 0 to 255, so we need to normalise it
        if self.lifetime > self.fade_start:
            normaliser = (self.lifetime - self.fade_start) / (
                self.max_lifetime - self.fade_start
            )
            self.image.set_alpha(int(f"{int((255 * normaliser))}"))

        if self.lifetime <= 0:
            self.kill()


class EnemyRect(pygame.sprite.Sprite):
    def __init__(
        self,
        x=57,
        y=100,
        width=700,
        height=143,
        color="white",
        name=0,
        border_color="grey",
        game=None,
    ):
        super().__init__()
        self.sprites = pygame.sprite.Group()
        self.game = game

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.selected = False

        self.name = name
        self.color = color
        self.border_color = border_color
        self.default_border_color = self.border_color
        self.default_color = self.color
        self.selected_button = 0

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.image.set_alpha(255)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.enemy_name = TextSprite(
            "",
            30,
            None,
            "white",
            self.rect.center[0] - 80,
            self.rect.center[1] - 105,
            f"T{self.name}",
        )

        self.enemy_class = TextSprite(
            "",
            30,
            None,
            "white",
            self.rect.center[0] - 15,
            self.rect.center[1] - 105,
            f"T{self.name}",
        )

        self.sprites.add(self.enemy_name)
        self.sprites.add(self.enemy_class)

    def update(self):
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.sprites.update()

    def draw(self, screen):
        pygame.draw.rect(screen, self.border_color, self.rect, 5)
        self.sprites.draw(screen)


class RectGUI(pygame.sprite.Sprite):
    def __init__(
        self,
        x=57,
        y=100,
        width=700,
        height=143,
        color="white",
        name=0,
        border_color="grey",
        game=None,
    ):
        super().__init__()
        self.sprites = pygame.sprite.Group()
        self.game = game

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.selected = False

        self.name = name
        self.color = color
        self.border_color = border_color
        self.default_border_color = self.border_color
        self.default_color = self.color
        self.selected_button = 0
        # #(57, 100, 853, 143, 213)
        # self.rect = pygame.Rect(x , y, width, height)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.image.set_alpha(255)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.selected_name = TextSprite(
            "Type here",
            30,
            None,
            "white",
            self.rect.center[0] - 80,
            self.rect.center[1] - 105,
            f"T{self.name}",
        )

        self.selected_class = TextSprite(
            "",
            30,
            None,
            "white",
            self.rect.center[0] - 15,
            self.rect.center[1] - 105,
            f"T{self.name}",
        )

        # self.class_text = TextSprite(
        #     "Class: ",
        #     25,
        #     None,
        #     "white",
        #     self.rect.center[0] - 190,
        #     self.rect.center[1] + 5,
        # )

        self.class_button = "another button here"

        # Don't forget to put the buttons into the sprites below
        self.sprites.add([self.selected_name])
        self.sprites.add([self.selected_class])

    def update(self):
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        if self.selected:
            self.border_color = "white"
            self.color = "white"
            # self.selected_name.text = self.game.text_buffer

        else:
            self.border_color = self.default_border_color
            self.color = self.default_color

        # store_text(f"T{self.name}", self.sprites, self.game)
        self.sprites.update()

    def draw(self, screen):
        pygame.draw.rect(screen, self.border_color, self.rect, 5)
        self.sprites.draw(screen)


class Statbar(pygame.sprite.Sprite):
    def __init__(
        self,
        unit: object,
        color="green",
        stat="health",
        y_offset=0,
        static=False,
    ):
        super().__init__()
        self.sprites = pygame.sprite.Group()
        self.unit = unit
        self.width = 100
        self.max_width = self.width
        self.static = static

        # min and max attribute range of unit
        self.stat = stat

        self.y_offset = y_offset
        self.unit.stat_bar_center_offset_x = -(self.width // 2)

        self.height = 15

        self.color = color

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)
        self.image.set_alpha(255)
        self.rect = self.image.get_rect()

        self.rect.midleft = (
            self.unit.rect.center[0] + self.unit.stat_bar_center_offset_x,
            self.unit.rect.center[1]
            + self.unit.stat_bar_center_offset_y
            + self.y_offset,
        )

    # This one should update outside the play.py
    def update(self):
        if not self.static:
            self.ratio = self.unit.check_ratio(self.stat)
            self.width = max(
                0, int(self.max_width * self.ratio)
            )  # omg use max must be ai write one omgggg jk
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.midleft = (
            self.unit.rect.center[0] + self.unit.stat_bar_center_offset_x,
            self.unit.rect.center[1]
            + self.unit.stat_bar_center_offset_y
            + self.y_offset,
        )

        # print(f"Unit: {self.unit.name} HP: {self.unit.health / self.unit.max_health = } Width: {self.width} Rect: {self.rect} Image: {self.image} Ratio: {self.ratio}")

    # currently unused
    def draw(self, screen):
        pygame.draw.rect(screen, self.border_color, self.rect, 5)
        self.sprites.draw(screen)


class InfoGUI:
    """This is basically a function that creates character information GUIs"""

    def __init__(self, unit: object, trackers: dict, sprite_group: pygame.sprite.Group):
        self.unit = unit
        self.bar_offset = 20
        self.sprites = sprite_group
        self.trackers = trackers

        # Trackers dict example: {"green": [unit.health, unit.max_health]}

        self.bars = pygame.sprite.Group()
        self.text_sprites = pygame.sprite.Group()

        # Enumerating that dictionary that already contains a list would be too complicated
        for i, item in enumerate(self.trackers.items()):
            self.bars.add(
                Statbar(
                    self.unit,
                    "grey27",
                    item[1],
                    i * self.bar_offset,
                    True,
                )
            )
            self.bars.add(Statbar(self.unit, item[0], item[1], i * self.bar_offset))

        # 3 DAYS BEFORE DEADLINE HARDCODE TIME
        # Health text
        self.text_sprites.add(
            TrackingText(
                "",
                self.unit,
                "health",
                (
                    self.unit.stat_bar_center_offset_x,
                    self.unit.stat_bar_center_offset_y,
                ),
                16,
            )
        )

        self.text_sprites.add(
            TrackingText(
                "",
                self.unit,
                "mana",
                (
                    self.unit.stat_bar_center_offset_x,
                    self.unit.stat_bar_center_offset_y + self.bar_offset,
                ),
                16,
            )
        )

        # EXP text
        self.text_sprites.add(
            TrackingText(
                "",
                self.unit,
                "exp",
                (
                    self.unit.stat_bar_center_offset_x,
                    self.unit.stat_bar_center_offset_y + (self.bar_offset * 2),
                ),
                16,
                "gold1",
                "newsgoth bt",
            )
        )

        # Unit name
        self.text_sprites.add(
            TrackingText(
                self.unit.name, self.unit, "", (-40, -120), 30, "white", '"newsgoth bt"'
            )
        )

        self.sprites.add([self.bars, self.text_sprites])

    def update(self):
        pass

    def draw(self, screen):
        pass


def create_info_guis(game):
    for sprite in game.all_units:
        trackers = {"green": "health", "deepskyblue1": "mana", "gold1": "exp"}
        InfoGUI(
            sprite,
            trackers,
            game.stat_guis,
        )


class TrackingText(pygame.sprite.Sprite):
    def __init__(
        self,
        text: str,
        unit: object,
        flag="",
        offset=(0, 0),
        size=20,
        color="white",
        font=fonts.pixeloid_sans,
    ):
        super().__init__()
        self.text = text
        self.flag = flag
        self.unit = unit
        self.offset_x = offset[0]
        self.offset_y = offset[1]
        self.size = size
        self.color = color

        try:
            self.font = pygame.font.Font(font, size)
        except:
            self.font = pygame.font.SysFont(font, size)

        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()

        self.rect.center = (
            self.unit.rect.center[0] + self.offset_x,
            self.unit.rect.center[1] + self.offset_y,
        )

    def update(self):

        # No time left let's hardcode this 3 days before deadline woooo
        if self.flag == "exp":
            self.text = f"Lvl: {self.unit.level} EXP: {int(self.unit.exp)}/{self.unit.level_exp_dict[self.unit.level]}"
            self.image = self.font.render(self.text, True, self.color)

        if self.flag == "health":
            self.text = f"{int(self.unit.health)}/{int(self.unit.max_health)}"
            self.image = self.font.render(self.text, True, self.color)

        if self.flag == "mana":
            self.text = f"{int(self.unit.mana)}/{int(self.unit.max_mana)})"
            self.image = self.font.render(self.text, True, self.color)

        self.rect = self.image.get_rect()

        self.rect.midleft = (
            self.unit.rect.center[0] + self.offset_x,
            self.unit.rect.center[1] + self.offset_y,
        )
