import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, sprites, x, y):
        super(Explosion, self).__init__()
        self.timer = 0
        self.interval = 2
