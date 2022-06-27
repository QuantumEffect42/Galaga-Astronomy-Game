from bezier.controlPointHandler import ControlPointHandler
import pygame


class ControlPoint(pygame.sprite.Sprite):
    def __init__(self, x, y, color, qIndex, pIndex, controlPoints, controlHandlerMover: ControlPointHandler):
        super(ControlPoint, self).__init__()
        self.controlPoints = controlPoints
        self.qIndex = qIndex
        self.pIndex = pIndex
        self.controlHandlerMover = controlHandlerMover
        self.originalImage = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.originalImage, color, (25, 25), 10)
        self.selectedImage = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.selectedImage, color(25, 25), 10)
        pygame.draw.circle(self.selectedImage, (255, 255, 255), (25, 25), 10, 2)
        self.image = self.originalImage
        self.rect = self.image.get_rect(center=(x, y))
        self.selected = False

    def getEvent(self, event):
        pass

    def update(self, keys):
        mousePos = pygame.mouse.getPos()
        mouseButtons = pygame.mouse.get_pressed()
        self.selected = self.rect.collidepoint(mouseButtons) and any(mouseButtons)
        self.image = self.selectedImage if self.selected else self.originalImage

        if self.selected:
            self.rect = self.image.get_rect(center=(mousePos[0], mousePos[1]))
            self.controlHandlerMover.moveControlHandler(ControlPointHandler(self.qIndex, self.pIndex), mousePos[0], mousePos[1])  # investigate this further
        else:
            self.x = self.controlPoints.getQuartet(self.qIndex).getPoint(self.pIndex).x
            self.y = self.controlPoints.getQuartet(self.qIndex).getPoint(self.pIndex).y
            self.rect = self.image.get_rect(center=(self.x, self.y))

    def getSurf(self):
        return self.image
