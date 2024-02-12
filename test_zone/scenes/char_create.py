import pygame
import sys

import gui2.screen as scr
import gui2.ui_functions as ui_functions
import scenes.main_menu as main_menu

def create():
    pygame.display.set_caption("Character Creation")
 
    while True:
        scr.screen.fill((25, 25, 25))
    
        actions = ui_functions.key_handler()
        
        if actions["left"]:
            print("going left")
            
        if actions["right"]:
            print("Going back to main menu")
            main_menu.main()
            
        
        # Key handler already calls this for us so it's optional
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()