import pygame

import gui2.screen as scr
import scenes.char_create as char_create
import gui2.ui_functions as ui_functions
import resources2.images

pygame.init()
buttons = pygame.sprite.Group()
button_list = []

play_button = ui_functions.Button(100, 50, "green")
other_button = ui_functions.Button(100, 50, "yellow", True, 250)

buttons.add(play_button)
buttons.add(other_button)

button_list.append(play_button)
button_list.append(other_button)

def main():
    current_selection = 0
    pygame.display.set_caption("Main Menu")
    
    while True:
        scr.screen.blit(resources2.images.menubackground_img, (0, 0))
        
        buttons.update()
        buttons.draw(scr.screen)
            
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

            
        pygame.display.update()