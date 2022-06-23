import pygame
from .state import State


class Splash(State):
    def __init__(self):
        super(Splash, self).__init__()
        self.title = self.font.render("Galaga", True, pygame.Color("blue"))
        self.titleRect = self.title.get_rect(center=self.screenRect.center)
        self.nextState = "MENU"
        self.timeActive = 0

    def update(self, dt):
        self.timeActive += dt
        if self.timeActive >= 3000:
            self.done = True

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        surface.blit(self.title, self.titleRect)
