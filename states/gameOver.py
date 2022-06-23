import pygame
from .state import State


class GameOver(State):
    def __init__(self) -> None:
        super(GameOver, self).__init__()
        self.title = self.font.render("Game Over", True, pygame.Color("white"))
        self.titleRect = self.title.get_rect(center = self.screenRect.center)
        self.instructions = self.font.render("Press R to restart, or enter to go to main menu", True, pygame.Color("white"))
        instructionsCenter = (self.screenRect.center[0], self.screenRect.center[1] + 50)
        self.instructionsRect = self.instructions.get_rect(center=instructionsCenter)

    def getEvent(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                self.next_state = "MENU"
                self.done = True
            elif event.key == pygame.K_r:
                self.next_state = "GAMEPLAY"
                self.done = True
            elif event.key == pygame.K_ESCAPE:
                self.quit = True
    
    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        surface.blit(self.title, self.titleRect)
        surface.blit(self.instructions, self.instructionsRect)
