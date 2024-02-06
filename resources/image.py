import pygame
from pathlib import Path

#menu background
menubackground_img = pygame.image.load(f"{Path('resources/picture/menubackground.png')}")
#background image
background_img = pygame.image.load(f"{Path('resources/picture/background3.png')}")

#panel image
panel_img = pygame.image.load(f"{Path('resources/picture/UI board Large parchment.png')}")

#load buttom images
resume_img = pygame.image.load(f"{Path('resources/picture/button/resumebut.png')}")
resume_img = pygame.transform.scale(resume_img, (resume_img.get_width()*3 ,resume_img.get_height()*3))

option_img = pygame.image.load(f"{Path('resources/picture/button/optionbut.png')}")
option_img = pygame.transform.scale(option_img, (option_img.get_width()*3 ,option_img.get_height()*3))

quit_img = pygame.image.load(f"{Path('resources/picture/button/quitbut.png')}")
quit_img = pygame.transform.scale(quit_img, (quit_img.get_width()*3 ,quit_img.get_height()*3))

video_img = pygame.image.load(f"{Path('resources/picture/button/videobut.png')}")
video_img = pygame.transform.scale(video_img, (video_img.get_width()*3 ,video_img.get_height()*3))

audio_img = pygame.image.load(f"{Path('resources/picture/button/audiobut.png')}")
audio_img = pygame.transform.scale(audio_img, (audio_img.get_width()*3 ,audio_img.get_height()*3))

back_img = pygame.image.load(f"{Path('resources/picture/button/backbut.png')}")
back_img = pygame.transform.scale(back_img, (back_img.get_width()*3 ,back_img.get_height()*3))

#load image
#load victory and defeat images
victory_img = pygame.image.load(f"{Path('resources/picture/victory.png')}")
victory_img = pygame.transform.scale(victory_img, (600,500))

defeat_img = pygame.image.load(f"{Path('resources/picture/defeat.png')}")
defeat_img = pygame.transform.scale(defeat_img, (600,500))

#sword pointer image
sword_img = pygame.image.load(f"{Path('resources/picture/icon(trans)/PineTools.com_files/row-6-column-5.png')}")