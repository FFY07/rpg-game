import gui.screen as sc
import resources.font as font

import pygame

credits_header = [
    ('[ Credits ]', font.menu_font, font.YELLOW, -220),
    ('PSB INTRODUCTION TO PROGRAMMING ASSIGNMENT', font.menucontent_font, font.GREEN, - 180),
    ('GAME CREATED BY (GROUP A1) ', font.menucontent_font, font.GREEN, - 150)
    ]

credits_body = [
    ('[ Members ]', font.menu_font, font.YELLOW,- 110),
    ('Desmond Foo Fong Yoong (GL)', font.menucontent_font, font.WHITE,- 70),
    ('Haarith Bin Naguri Ibrahim', font.menucontent_font, font.WHITE,- 40),
    ('Haohong Luo', font.menucontent_font, font.WHITE,- 10),
    ('Qiao Er Kang', font.menucontent_font, font.WHITE, 20),
    ('Xu Xiang (Ye Xuxiang) Yap', font.menucontent_font, font.WHITE, 50),
    ('Yi Soon Pong', font.menucontent_font, font.WHITE, 80),
    ]

credits_footer = [
    ('[ Code Refactorer ]', font.font_make(40), font.YELLOW, sc.SCREEN_HEIGHT // 4.5),
    ('Rui Zheng', font.menucontent_font, font.WHITE, sc.SCREEN_HEIGHT // 3.5),
    ('"Desmond wrote 99.9% of this game by himself btw"', font.font_make(20, "High Tower Text"), "grey75", sc.SCREEN_HEIGHT // 3),
    ('"Not his groupmates"', font.font_make(16, "High Tower Text"), "grey75", sc.SCREEN_HEIGHT // 2.65),
]

# Easier to organise, but no functional difference
credits_list = [credits_header, credits_body, credits_footer]


text_sprites = pygame.sprite.Group()

example_test = font.TextSprite("HALLO", 80, "freesansbold", "crimson", True, 0, True)
text_sprites.add(example_test)

def draw_menu_credit():
    """Draws all the credits onto the screen"""
    sc.screen.fill((0, 0, 0))
    
    for section in credits_list:
        for credit in section:
            sc.draw_centertext(*credit)