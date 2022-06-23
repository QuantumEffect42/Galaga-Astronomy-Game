import pygame


class SpriteSheet:
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
            self.sheet.set_colorkey(-1, pygame.RLEACCEL)
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

    def imageAt(self, rectangle, colorKey=None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorKey is not None:
            if colorKey == -1:
                colorKey = image.get_at((0, 0))
            image.set_colorkey(colorKey, pygame.RLEACCEL)
        return image

    def imagesAt(self, rects, colorKey=None):
        return [self.imageAt(rect, colorKey) for rect in rects]

    def loadStrip(self, rect, imageCount, colorKey=None):
        for x in range(imageCount):
            tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])]
        return self.imagesAt(tups, colorKey)