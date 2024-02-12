import pygame, sys
import gui2.screen as scr



def key_handler():
    actions = {"up": False,
               "left": False,
               "down": False,
               "right": False,
               "space": False,
               "backspace": False,
               "enter": False,
               "escape": False
               }
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w or event.key == pygame.K_UP:
                actions["up"] = True
                
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                actions["left"] = True
                
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                actions["down"] = True
            
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                actions["right"] = True
                
            if event.key == pygame.K_SPACE:
                actions["space"] = True
            
            if event.key == pygame.K_BACKSPACE:
                actions["backspace"] = True
            
            if event.key == pygame.K_RETURN:
                actions["enter"] = True
            
            if event.key == pygame.K_ESCAPE:
                actions["escape"] = True
            
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_w or event.key == pygame.K_UP:
                actions["up"] = False
                
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                actions["left"] = False
                
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                actions["down"] = False
            
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                actions["right"] = False
                            
            if event.key == pygame.K_SPACE:
                actions["space"] = False
            
            if event.key == pygame.K_BACKSPACE:
                actions["backspace"] = False
            
            if event.key == pygame.K_RETURN:
                actions["enter"] = False
            
            if event.key == pygame.K_ESCAPE:
                actions["escape"] = False
                
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    return actions

class TextSprite(pygame.sprite.Sprite):
    # Creates a text sprite; replace me with a docstring once all the parameters are done
    def __init__(self, text: str, 
                size: int, 
                text_font = "freesansbold", 
                color = "white", 
                x_centered = True, 
                y_centered = True, 
                dx = 0, 
                dy = 0):
        """Generates a text sprite
        
        Args:
            text (str): The text to display
            size (int): The size of the text
            text_font (str, optional): The font name. Defaults to "freesansbold".
            color (str, optional): The font color. Defaults to "white".
            x (bool, optional): The x coordinate. True = Centered.
            y (bool, optional): The y coordinate. True = Centered.
            dx (bool, optional): Movement along x coordinate. Defaults to 0
            flying (bool, optional): Movement along y coordinate. Default to 0
        """
        super().__init__()
        
        if x_centered is True:
            self.x = scr.SCREEN_WIDTH // 2
        else:
            self.x = x_centered
            
        if y_centered is True:
            self.y = scr.SCREEN_HEIGHT // 2
        else:
            self.y = y_centered
            
        self.dx = dx
        self.dy = dy
        
        self.font = pygame.font.SysFont(text_font, size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    
    def update(self):
        self.rect.move_ip(self.dx, self.dy)
        
        # Check if we're going upwards
        if self.dy < 0:
            if self.rect.bottom < 0:
                self.kill()
        else:
            if self.rect.top > scr.SCREEN_HEIGHT:
                self.kill()
        
        # EVERYTHING HERE IS NOT TESTED BECAUSE IDK WHICH SIDE IS WHICH
        if self.dx < 0:
            if self.rect.left < 0:
                self.kill()
        else:
            if self.rect.right > scr.SCREEN_WIDTH:
                self.kill()
                

class Button(pygame.sprite.Sprite):
    def __init__(self, width, height, color, x = True, y = True, selected = False):
        super().__init__()
        self.width = width
        self.height = height
        
        if x is True:
            self.x = scr.SCREEN_WIDTH // 2
        else:
            self.x = x
        
        if y is True:
            self.y = scr.SCREEN_HEIGHT // 2
        else:
            self.y = y
        
        self.color = color
        
        self.selected = selected
        
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    
    def update(self):
        if self.selected:
            self.image.fill("red")
        else:
            self.image.fill(self.color)
        
class ButtonBG(pygame.sprite.Sprite):
    pass