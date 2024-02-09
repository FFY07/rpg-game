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
    
    ('> 3000 Lines Committed to Github', *font.credit_title, True, sc.SCREEN_HEIGHT + 350),
    ('Desmond Foo Fong Yoong 👑', *font.credit_name, True, sc.SCREEN_HEIGHT + 400),
    
    ('> 50 Lines Committed to Github', *font.credit_title, True, sc.SCREEN_HEIGHT + 500),
    ('Haarith Bin Naguri Ibrahim 🎉', *font.credit_name, True, sc.SCREEN_HEIGHT + 550),
    
    ('0 Lines Committed to Github', *font.credit_title, True, sc.SCREEN_HEIGHT + 650),
    ('Haohong Luo 💀', *font.credit_name, True, sc.SCREEN_HEIGHT + 700),
    ('Qiao Er Kang 💀', *font.credit_name, True, sc.SCREEN_HEIGHT + 750),
    ('Xu Xiang (Ye Xuxiang) Yap 💀', *font.credit_name, True, sc.SCREEN_HEIGHT + 800),
    ('Yi Soon Pong 💀', *font.credit_name, True, sc.SCREEN_HEIGHT + 850)
    ]

credits_footer = [
    ('THANKS FOR PLAYING', *font.credit_section, True, sc.SCREEN_HEIGHT + 1000),
    ('THERE\'S NOTHING ELSE HERE', *font.credit_title, True, sc.SCREEN_HEIGHT + 1500),
    ('PRESS ESCAPE TO QUIT BTW', *font.credit_title, True, sc.SCREEN_HEIGHT + 2000),
    ('...why are you still here?', *font.credit_title, True, sc.SCREEN_HEIGHT + 3000),
    ('please leave', *font.credit_title, True, sc.SCREEN_HEIGHT + 3500),
    ('Desmond are you still talking or something why am I still running', *font.credit_title, True, sc.SCREEN_HEIGHT + 4000),
    ('...', *font.credit_title, True, sc.SCREEN_HEIGHT + 5000),
    ('Why did the chicken cross the road?', *font.credit_title, True, sc.SCREEN_HEIGHT + 5500),
    ('TO GET AWAY FROM YOU!!! NOW PRESS ESCAPE TO QUIT', *font.credit_title, True, sc.SCREEN_HEIGHT + 6000),
    ('if you still don\'t leave i\'m calling the cops', *font.credit_title, True, sc.SCREEN_HEIGHT + 6500),
    ('i\'m calling the cops', *font.credit_title, True, sc.SCREEN_HEIGHT + 7000),
    ('they\'re coming anytime now~', *font.credit_title, True, sc.SCREEN_HEIGHT + 7500),
    ('...', *font.credit_title, True, sc.SCREEN_HEIGHT + 8000),
    ('... ok fine you win please just leave', *font.credit_title, True, sc.SCREEN_HEIGHT + 9000),
    ('...', *font.credit_title, True, sc.SCREEN_HEIGHT + 10000),
    ('...', *font.credit_title, True, sc.SCREEN_HEIGHT + 11000),
    ('...', *font.credit_title, True, sc.SCREEN_HEIGHT + 12000),
    ('you know there\'s nothing else after this right?', *font.credit_title, True, sc.SCREEN_HEIGHT + 13000),
    ('...', *font.credit_title, True, sc.SCREEN_HEIGHT + 14000),
    ('..', *font.credit_title, True, sc.SCREEN_HEIGHT + 15000),
    ('.', *font.credit_title, True, sc.SCREEN_HEIGHT + 16000),
    ('you\'re a donkey.', *font.credit_title, True, sc.SCREEN_HEIGHT + 18000)
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