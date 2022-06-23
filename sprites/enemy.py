import math
import pygame
import constants

#import and create the bezier point calculator

class Enemy(pygame.sprite.Sprite):
    def __init__(self, sprites, controlPoints, enemey):
        super(Enemy, self).__init__()
        self.rotation = 0
        self.timer = 0
        self.controlPoints = controlPoints
        self.bezierTimer = 0.0
        self.interval = 2
        self.spriteIndexCount = 1