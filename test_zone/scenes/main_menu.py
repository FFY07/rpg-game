import pygame, sys

import gui2.screen as scr
import scenes.char_create as char_create
import gui2.ui_functions as ui_functions
import resources2.images



pygame.init()
buttons = pygame.sprite.Group()

button_list = []

play_button = ui_functions.Button(100, 50, "green")
escape_button = ui_functions.Button(100, 50, "red", True, 450)

play_text = ui_functions.TextSprite("Play", 25)
escape_text = ui_functions.TextSprite("Quit", 25, "freesansbold", "white", True, 450)

buttons.add(play_button)
buttons.add(play_text)

buttons.add(escape_button)
buttons.add(escape_text)

button_list.append(play_button)
button_list.append(escape_button)


def main():
    
    # Resets all buttons
    for button in button_list:
        button.selected = False
        
    # Sets the first button
    current_selection = 0
    button_list[current_selection].selected = True
    
    pygame.display.set_caption("Main Menu")
    
    while True:
        scr.screen.blit(resources2.images.menubackground_img, (0, 0))

            
        action = ui_functions.key_handler()
        if action["left"]:
            print("Going to Character Creation")
            char_create.create()
        
        if action["down"]:
            button_list[current_selection].selected = False
            try:
                current_selection += 1
                button_list[current_selection].selected = True
            except IndexError:
                current_selection = 0
                button_list[current_selection].selected = True
        
        if action["enter"]:
            print("Enter key pressed")
            if current_selection == 0:
                char_create.create()
            
            elif current_selection == 1:
                pygame.quit()
                sys.exit()
                
        buttons.update()
        buttons.draw(scr.screen)

        pygame.display.update()