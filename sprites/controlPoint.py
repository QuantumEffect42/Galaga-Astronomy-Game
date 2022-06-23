# import the bezier control point handler

import pygame


class ControlPoint(pygame.sprite.Sprite):
    def __init__(self, x, y, color, qIndex, pIndex, controlPoints):
        super(ControlPoint, self).__init__()
        self.controlPoints = controlPoints
        self.qIndex = qIndex
        self.pIndex = pIndex
