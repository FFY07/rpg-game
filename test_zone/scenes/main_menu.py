import pygame, sys

import gui2.screen as scr
import scenes.char_create as char_create
import gui2.ui_functions as ui_functions
import resources2.images

pygame.init()
buttons = pygame.sprite.Group()

button_list = []
text_list = []

# Color doesn't matter
play_button = ui_functions.Button(140, 50, "green", True, 400)
play_text = ui_functions.TextSprite("Play", 30, "freesansbold", "white", True, 400)

options_button = ui_functions.Button(140, 50, "cyan", True, 450)
options_text = ui_functions.TextSprite("Options", 30, "freesansbold", "white", True, 450)

credits_button = ui_functions.Button(140, 50, "yellow", True, 500)
credits_text = ui_functions.TextSprite("Credits", 30, "freesansbold", "white", True, 500)

escape_button = ui_functions.Button(140, 50, "grey", True, 550)
escape_text = ui_functions.TextSprite("Quit", 30, "freesansbold", "white", True, 550)

# Add to pygame sprite group
buttons.add(play_button)
buttons.add(play_text)

buttons.add(options_button)
buttons.add(options_text)

buttons.add(credits_button)
buttons.add(credits_text)

buttons.add(escape_button)
buttons.add(escape_text)

# Add to our manual lists
button_list.append(play_button)
button_list.append(options_button)
button_list.append(credits_button)
button_list.append(escape_button)


text_list.append(play_text)
text_list.append(options_text)
text_list.append(credits_text)
text_list.append(escape_text)

# Static stuff
background = resources2.images.menubackground_img

menu_text = ui_functions.TextSprite("[ CASTLE ADVENTURE ]", 70, "High Tower Text", "crimson", True, 200)
menu_text.selected = True
buttons.add(menu_text)

menu_subtext = ui_functions.TextSprite("A Turn-Based RPG built in Python", 40, "High Tower Text", "grey75", True, 80)
menu_subtext.selected = True
buttons.add(menu_subtext)

def main():
    
    # Resets all buttons and text
    for button in button_list:
        button.selected = False
    for text in text_list:
        text.selected = False
        
    # Sets the first button
    current_selection = 0
    button_list[current_selection].selected = True
    text_list[current_selection].selected = True
    
    pygame.display.set_caption("Main Menu")

    while True:
        scr.screen.blit(background, (0, 0))

        action = ui_functions.key_handler()
        
        if action["down"]:
            button_list[current_selection].selected = False
            text_list[current_selection].selected = False
            try:
                current_selection += 1
                button_list[current_selection].selected = True
                text_list[current_selection].selected = True
                
            except IndexError:
                current_selection = 0
                button_list[current_selection].selected = True
                text_list[current_selection].selected = True
                
        if action["up"]:
            button_list[current_selection].selected = False
            text_list[current_selection].selected = False
            if current_selection >= 0:
                current_selection -= 1
                button_list[current_selection].selected = True
                text_list[current_selection].selected = True
                
            else:
                current_selection = 0
                button_list[current_selection].selected = True
                text_list[current_selection].selected = True

        if action["enter"]:
            print("Enter key pressed")
            if current_selection == 0:
                print("Entering character creation")
                char_create.create()
            
            elif current_selection == 1:
                print("options screen")
                
            elif current_selection == 2:
                print("credits screen")
                
            elif current_selection == 3:
                pygame.quit()
                sys.exit()
                
        buttons.update()
        buttons.draw(scr.screen)

        pygame.display.update()