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