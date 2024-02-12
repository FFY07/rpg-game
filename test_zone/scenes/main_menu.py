import pygame, sys

import gui2.screen as scr
import scenes.char_create as char_create
import gui2.ui_functions as ui_functions
import resources2.images

pygame.init()
buttons = pygame.sprite.Group()
button_dict = {}

play_button = ui_functions.Button(100, 50, "green")
other_button = ui_functions.Button(100, 50, "yellow", True, 450)

buttons.add(play_button)
buttons.add(other_button)

button_dict[0] = play_button
button_dict[1] = other_button

def main():
    
    # Resets all buttons
    for key, button in button_dict.items():
        button.selected = False
        
    # Sets the first button
    current_selection = 0
    button_dict[current_selection].selected = True
    
    pygame.display.set_caption("Main Menu")
    
    while True:
        scr.screen.blit(resources2.images.menubackground_img, (0, 0))

            
        action = ui_functions.key_handler()
        if action["left"]:
            print("Going to Character Creation")
            char_create.create()
        
        if action["down"]:
            button_dict[current_selection].selected = False
            try:
                current_selection += 1
                button_dict[current_selection].selected = True
            except KeyError:
                current_selection = 0
                button_dict[current_selection].selected = True
        
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