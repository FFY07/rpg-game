import pygame

import gui2.screen as scr
import resources2 as rsc

import scenes.main_menu as main_menu

pygame.init()

SCREEN = pygame.display.set_mode ((1280, 720))
pygame.display.set_caption("Main")

# Make sure the function below only runs if this is the main file
if __name__ == "__main__":
    main_menu.main()