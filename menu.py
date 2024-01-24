import pygame
import button


pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = 'main'

#define font
font = pygame.font.SysFont("arialblack" , 40) 

#define colours
TEXT_COL = (255,255,255)

#load buttom images
resume_img = pygame.image.load('picture/button/resumebut.png')
resume_img = pygame.transform.scale(resume_img, (resume_img.get_width()*3 ,resume_img.get_height()*3))
option_img = pygame.image.load('picture/button/optionbut.png')
option_img = pygame.transform.scale(option_img, (option_img.get_width()*3 ,option_img.get_height()*3))
quit_img = pygame.image.load('picture/button/quitbut.png')
quit_img = pygame.transform.scale(quit_img, (quit_img.get_width()*3 ,quit_img.get_height()*3))
video_img = pygame.image.load('picture/button/videobut.png')
video_img = pygame.transform.scale(video_img, (video_img.get_width()*3 ,video_img.get_height()*3))
audio_img = pygame.image.load('picture/button/audiobut.png')
audio_img = pygame.transform.scale(audio_img, (audio_img.get_width()*3 ,audio_img.get_height()*3))
back_img = pygame.image.load('picture/button/backbut.png')
back_img = pygame.transform.scale(back_img, (back_img.get_width()*3 ,back_img.get_height()*3))

#create button instances
resume_button = button.Button(5, 180, resume_img, 1)
option_button = button.Button(270, 180, option_img, 1)
quit_button = button.Button(530, 180, quit_img, 1)
video_button = button.Button(150, 40, video_img, 1)
audio_button = button.Button(350, 40, audio_img, 1)
back_button = button.Button(250, 350, back_img, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#game loop 
run = True
while run:

    screen.fill((52, 78, 91))

    #check if game is paused
    if game_paused == True:
        #check menu state
        if menu_state == 'main':
            #draw pause screen button
            if resume_button.draw(screen):
                game_paused = False
            if option_button.draw(screen):
                menu_state = 'option'
            if quit_button.draw(screen):
                run = False
        # check if the option menu is open
        if menu_state == 'option':
            if video_button.draw(screen):
                print('i didnt make a code for Video Settings :3')
            if audio_button.draw(screen):
                print('i didnt make a code for Audio Settings :3')
            if back_button.draw(screen):
                menu_state = 'main'
            #draw the different option button
    else:
        draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_paused =  True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu_state == 'game'
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()