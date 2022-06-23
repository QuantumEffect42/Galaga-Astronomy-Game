import pygame
import math
import constants

class Rocket(pygame.sprite.Sprite):
    def __init__(self, sprites, xSpeed, ySpeed):
        super(Rocket, self).__init__()
        self.timer = 0
        self.interval = 2
