import pygame

###base state class that will be inherited by all of the other state classes to be used

class State(object):
    def __init__(self) -> None:
        self.done = False #boolean for determining if the state has completed its function
        self.quit = False
        self.nextState = None #holds the next state object to tell where to transition to
        self.screenRect = pygame.display.get_surface().get_rect()
        self.font = pygame.font.Font(None, 32)

    def startup(self):
        pass

    def getEvent(self, event):
        pass
    
    def update(self, dt):
        pass

    def draw(self, surface):
        pass