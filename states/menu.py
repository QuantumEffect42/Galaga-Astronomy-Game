import pygame
from .state import State  # inherits the base state class which we will override


class Menu(State):
    def __init__(self) -> None:
        super(Menu, self).__init__()
        self.activeIndex = 0
        self.options = ["Start", "Exit"]
        self.nextState = "GAMEPLAY"

    def textRender(self, index):
        if index == self.activeIndex:
            color = pygame.Color("red")
        else:
            color = pygame.Color("white")

        return self.font.render(self.options[index], True, color)

    def getTextPosition(self, text, index):
        newCenter = (self.screenRect.center[0], self.screenRect.center[1] + (index * 50))

        return text.get_rect(center=newCenter)

    # changes the necessary boolean based on the option chosen
    def actionHandle(self):
        if self.activeIndex == 0:
            self.done = True
        elif self.activeIndex == 1:
            self.quit = True

    # handles the key presses to scroll through the menu
    def getEvent(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if self.activeIndex <= 0:
                    self.activeIndex = 1
                else:
                    self.activeIndex = 0
            elif event.key == pygame.K_DOWN:
                if self.activeIndex >= 1:
                    self.activeIndex = 0
                else:
                    self.activeIndex = 1
            elif event.key == pygame.K_RETURN:
                self.actionHandle()

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        for index, option in enumerate(self.options):
            textRender = self.textRender(index)
            surface.blit(textRender, self.getTextPosition(textRender, index))
