import pygame
import math
import constants

class Rocket(pygame.sprite.Sprite):
    def __init__(self, sprites, xSpeed, ySpeed):
        super(Rocket, self).__init__()
        self.timer = 0
        self.interval = 2
        self.numberOfImages = 3
        self.ySpeed = ySpeed
        self.xSpeed = xSpeed
        self.images = sprites.loadStrip([0, 177, 12, 14], self.numberOfImages, -1)

        self.surf = self.images[1]
        self.rect = self.surf.get_rect(center=(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 20))
        self.imageIndex = 0
        self.rotation = 0
        if self.ySpeed > 0:
            self.rotation = math.degrees(math.atan2(xSpeed, ySpeed)) + 180

    def update(self, keys):
        self.timer += 1
        self.rect.move_ip(self.xSpeed, self.ySpeed)

        if self.rect.bottom < 0 or self.rect.top > constants.SCREEN_WIDTH:
            self.kill()

    def getEvent(self, event):
        pass

    def getSurf(self):
        if self.timer % self.interval == 0:
            self.imageIndex += 1
        if self.imageIndex >= self.numberOfImages:
            self.imageIndex = 0

        rotImage = pygame.transform.rotate(self.images[self.imageIndex], self.rotation)
        self.rect = rotImage.get_rect(center=self.rect.center)

        return rotImage