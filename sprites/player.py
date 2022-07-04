import pygame
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
)

import constants


class Player(pygame.sprite.Sprite):
    def __init__(self, sprites):
        super(Player, self).__init__()
        self.timer = 0
        self.interval = 2
        self.numberOfImages = 6
        self.images = sprites.loadStrip([0, 130, 48, 45], self.numberOfImages, 1)
        self.surf = self.images[0]
        self.rect = self.surf.get_rect(center=(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 40))
        self.imageIndex = 0

    def getEvent(self, event):
        pass

    def update(self, pressedKeys):
        self.timer += 1

        if pressedKeys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressedKeys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > constants.SCREEN_WIDTH:
            self.rect.right = constants.SCREEN_WIDTH

    def getSurf(self):
        if self.timer % self.interval == 0:
            self.imageIndex += 1
            if self.imageIndex >= self.numberOfImages:
                self.imageIndex = 0

        return self.images[self.imageIndex]