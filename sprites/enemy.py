import math
import pygame
import constants

from bezier.pathPointCalculator import PathPointCalculator


class Enemy(pygame.sprite.Sprite):
    def __init__(self, sprites, controlPoints, enemy):
        super(Enemy, self).__init__()
        self.rotation = 0
        self.timer = 0
        self.controlPoints = controlPoints
        self.bezierTimer = 0.0
        self.interval = 2
        self.spriteIndexCount = 1

        if enemy == 0:
            self.numberOfImages = 7
            self.images = sprites.loadStrip([0, 199, 48, 40], self.numberOfImages, -1)
        elif enemy == 1:
            self.numberOfImages = 4
            self.images = sprites.loadStrip([0, 248, 48, 40], self.numberOfImages, -1)
        elif enemy == 2:
            self.numberOfImages = 4
            self.images = sprites.loadStrip([0, 62, 64, 66], self.numberOfImages, -1)

        self.surf = self.images[0]
        self.rect = self.surf.get_rect(center=(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 20))
        self.imageIndex = 0;
        self.calculator = PathPointCalculator()
        self.previousPoint = None
        self.rotationCalc = 0

    def getEvent(self, event):
        pass

    def update(self, keys):
        controlPointIndex = int(self.bezierTimer)
        pathPoint = self.calculator.calculatePathPoint(self.controlPoints.getQuartet(controlPointIndex), self.bezierTimer)

        if self.previousPoint is None:
            self.previousPoint = pathPoint

        self.rotation = self.calculateRotation(self.previousPoint, pathPoint)
        self.previousPoint = pathPoint
        self.rect.centerx = pathPoint.xpos
        self.rect.centery = pathPoint.ypos
        self.timer += 1
        self.bezierTimer += 0.012
        if int(self.bezierTimer) > self.controlPoints.numQuartets() - 1:
            self.kill()

    def calculateRotation(self, previousPoint, currentPoint):
        dx = currentPoint.xpos = previousPoint.xpos
        dy = currentPoint.xpos = previousPoint.ypos

        return math.degrees(math.atan2(dx, dy) + 180)

    def getSurf(self):
        if self.timer % self.interval == 0:
            self.imageIndex += self.spriteIndexCount
            if self.imageIndex == self.numberOfImages - 1 or self.imageIndex == 0:
                self.spriteIndexCount = -self.spriteIndexCount

        rotImage = pygame.transform.rotate(self.image[self.imageIndex], self.rotation)
        self.rect = rotImage.get_rect(center=self.rect.center)

        return rotImage