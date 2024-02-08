import gui.screen as sc
import resources.font as font

import pygame

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
    ('Desmond Foo Fong Yoong (GL)', *font.credit_name, True, sc.SCREEN_HEIGHT + 250),
    ('Assistant Designer', *font.credit_title, True, sc.SCREEN_HEIGHT + 350),
    ('Haarith Bin Naguri Ibrahim', *font.credit_name, True, sc.SCREEN_HEIGHT + 400),
    ('0 Github commits >:(', *font.credit_title, True, sc.SCREEN_HEIGHT + 500),
    ('Haohong Luo', *font.credit_name, True, sc.SCREEN_HEIGHT + 550),
    ('Qiao Er Kang', *font.credit_name, True, sc.SCREEN_HEIGHT + 600),
    ('Xu Xiang (Ye Xuxiang) Yap', *font.credit_name, True, sc.SCREEN_HEIGHT + 650),
    ('Yi Soon Pong', *font.credit_name, True, sc.SCREEN_HEIGHT + 700)
    ]

credits_footer = [
    ('[ Code Refactorer ]', 40, "freesansbold", "yellow", True, 550),
    ('Rui Zheng', 30, "freesansbold", "white", True, 500),
    ('"Desmond wrote 99.9% of this game by himself btw"', 20, "High Tower Text", "grey75", True, 450),
    ('"Not his groupmates"', 16, "High Tower Text", "grey75", True, 400)
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
credits_list = [credits_header, credits_body]

for section in credits_list:
    for credit in section:
        text_sprite = font.TextSprite(*credit, *falling_speed)
        text_sprites.add(text_sprite)

def draw_menu_credit():
    """Draws all the credits onto the screen"""
    sc.screen.fill((0, 0, 0))