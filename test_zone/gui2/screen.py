import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

FPS = 60

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
clock.tick(FPS)
pygame.display.set_caption("RPG Game")