import pygame, time

import gui2.screen as scr
import resources2.sounds as sounds
import resources2.images as images

from scenes.menu import MainMenu

clock = pygame.time.Clock()
clock.tick(60)

# We'll use a state stack system instead of each scene having its own individual loop
class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, True
        self.actions = {"up": False,
                "left": False,
                "down": False,
                "right": False,
                "space": False,
                "backspace": False,
                "enter": False,
                "escape": False
                }
        self.dt, self.prev_time = 0, 0
        
        self.screen_width = scr.SCREEN_WIDTH
        self.screen_height = scr.SCREEN_HEIGHT
        
        self.canvas = pygame.Surface((self.screen_width, self.screen_height))
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        self.stack = []
        self.sprites = pygame.sprite.Group()
        self.all_units = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
         
        self.start()
        
        self.music = True
        self.sound = True
        self.volume = 1
        
        pygame.mixer.music.load(sounds.copyright_pls)
        if self.music:
            pygame.mixer.music.play(-1)
        

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.event_handler()
            self.update()
            self.render()

            
    def get_dt(self):
        current_time = time.time()
        self.dt = current_time - self.prev_time
        self.prev_time = current_time
        
    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                        
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.actions["up"] = True
                    
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.actions["left"] = True
                    
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.actions["down"] = True
                
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.actions["right"] = True
                    
                if event.key == pygame.K_SPACE:
                    self.actions["space"] = True
                
                if event.key == pygame.K_BACKSPACE:
                    self.actions["backspace"] = True
                
                if event.key == pygame.K_RETURN:
                    self.actions["enter"] = True
                
                if event.key == pygame.K_ESCAPE:
                    self.actions["escape"] = True
                
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.actions["up"] = False
                    
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.actions["left"] = False
                    
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.actions["down"] = False
                
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.actions["right"] = False
                                
                if event.key == pygame.K_SPACE:
                    self.actions["space"] = False
                
                if event.key == pygame.K_BACKSPACE:
                    self.actions["backspace"] = False
                
                if event.key == pygame.K_RETURN:
                    self.actions["enter"] = False
                
                if event.key == pygame.K_ESCAPE:
                    self.actions["escape"] = False
                    
    def update(self):
        self.stack[-1].update(self.dt, self.actions)

    def render(self):
        self.stack[-1].render(self.canvas)
        
        self.screen.blit(pygame.transform.scale(self.canvas, (self.screen_width, self.screen_height)), (0, 0))
        
        pygame.display.update()
        
    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False
            
    def start(self):
        # Initialise the first item in the stack, which is the Main Menu
        self.start = MainMenu(self)
        self.stack.append(self.start)
        
# Make sure the function below only runs if this is the main file
if __name__ == "__main__":
    # Initialise the game class
    game = Game()
    
    # Set game.running to False to stop the game
    while game.running:
        
        # game_loop loops through the state checking methods as long as game.playing is True
        game.game_loop()