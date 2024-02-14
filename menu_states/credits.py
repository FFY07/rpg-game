import gui.screen as sc
import resources.font as font

import pygame

# Credits should play after game over screen

# Initialise text sprite group
text_sprites = pygame.sprite.Group()

falling_speed = (0, -1)

credits_header = [
    ('[ Credits ]', *font.credit_section, True, sc.SCREEN_HEIGHT - 50),
    ('PSB INTRODUCTION TO PROGRAMMING ASSIGNMENT', *font.credit_desc, True, sc.SCREEN_HEIGHT),
    ('GAME CREATED BY (GROUP A1) ', *font.credit_desc, True, sc.SCREEN_HEIGHT + 50)
    ]

credits_body = [
    ('[ Members ]', *font.credit_section, True, sc.SCREEN_HEIGHT + 150),
    
    ('Group Leader', *font.credit_title, True, sc.SCREEN_HEIGHT + 200),
    ('Desmond Foo Fong Yoong', *font.credit_name, True, sc.SCREEN_HEIGHT + 250),
    ('Group Members', *font.credit_title, True, sc.SCREEN_HEIGHT + 300),
    ('Haarith Bin Naguri Ibrahim', *font.credit_name, True, sc.SCREEN_HEIGHT + 350),
    ('Haohong Luo ', *font.credit_name, True, sc.SCREEN_HEIGHT + 400),
    ('Qiao Er Kang ', *font.credit_name, True, sc.SCREEN_HEIGHT + 450),
    ('Xu Xiang (Ye Xuxiang) Yap ', *font.credit_name, True, sc.SCREEN_HEIGHT + 500),
    ('Yi Soon Pong ', *font.credit_name, True, sc.SCREEN_HEIGHT + 550)
    ]
credits_footer = [
    ('THANKS FOR PLAYING', *font.credit_section, True, sc.SCREEN_HEIGHT + 550)
    ]

joke_credits = [
    ("[ Game made by ]", *font.credit_section, True, 500),
    ("Desmond", *font.credit_name, True, 550),
    ("Director", *font.credit_title, True, 700),
    ("Desmond", *font.credit_name, True, 750),
    ("Writer", *font.credit_title, True, 900),
    ("Desmond", *font.credit_name, True, 950),
    ("Visual Effects", *font.credit_title, True, 1100),
    ("Desmond", *font.credit_name, True, 1150),
    ("Stunts", *font.credit_title, True, 1300),
    ("Desmond", *font.credit_name, True, 1350)    
]

# Add the sections you want to load into this list
credits_list = [credits_header, credits_body, credits_footer]

for section in credits_list:
    for credit in section:
        text_sprite = font.TextSprite(*credit, *falling_speed)
        text_sprites.add(text_sprite)

def draw_menu_credit():
    """Draws all the credits onto the screen"""
    sc.screen.fill((0, 0, 0))