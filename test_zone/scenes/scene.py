# Parent class for the different scenes

class Scene():
    def __init__(self, game: object):
        self.game = game
        self.prev = None
    
    def update(self, actions):
        pass
    
    def render(self, screen):
        pass
        
    def start_scene(self):
        # If this is not the only (bottom) item in the stack
        if len(self.game.stack) > 1:
            self.prev = self.game.stack[-1]
        
        # Add ourselves to the end of the state stack
        self.game.state_stack.append(self)
        
    def exit_scene(self):
        # Removes ourselves from the list as we go back down the stack
        self.game.state_stack.pop()