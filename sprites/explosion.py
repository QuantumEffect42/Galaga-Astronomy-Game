import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, sprites, x, y):
        super(Explosion, self).__init__()
        self.timer = 0
        self.interval = 2
        self.numberOfImages = 10
        self.images = sprites.loadStrip([64, 0, 64, 64], 3, -1)
        self.images.extend(sprites.loadStrip([0, 64, 64, 64], 4, -1))
        self.images.extend(sprites.loadStrip([0, 128, 64, 64], 3, -1))

        for index, image in enumerate(self.images):
            self.images[index] = pygame.transform.scale(image, (128, 128))

        self.surf = self.images[0]
        self.rect = self.surf.get_rect(center=(x, y))
        self.imageIndex = 0

    def getEvent(self, event):
        pass

    def update(self, pressedKeys):
        self.timer += 1
        if self.timer % self.interval == 0:
            self.imageIndex += 1

        if self.imageIndex >= self.numberOfImages:
            self.kill()

    def getSurf(self):
        return self.images[self.imageIndex]