import pygame
import random
import constants

LIGHTGREY = (120, 120, 120)
DARKGREY = (100, 100, 100)
YELLOW = (120, 120, 0)

class StarField():
    def __init__(self):
        self.starFieldSlow = self.createStars(50)
        self.starFieldMed = self.createStars(40)
        self.starFieldFast = self.createStars(30)

    def createStars(self, numStars):
        stars = []
        for _ in range(numStars):
            starLocX = random.randrange(0, constants.SCREEN_WIDTH)
            starLocY = random.randrange(0, constants.SCREEN_HEIGHT)
            stars.append([starLocX, starLocY])
        return stars

    def renderStars(self, screen, starCollection, speed, size, color):
        for star in starCollection:
            star[1] += speed
            if star[1] > constants.SCREEN_HEIGHT:
                star[0] = random.randrange(0, constants.SCREEN_WIDTH)
                star[1] = random.randrange(-20, 5)
            pygame.draw.circle(screen, color, star, size)

    def render(self, screen):
        self.renderStars(screen, self.starFieldSlow, 1, 3, DARKGREY)
        self.renderStars(screen, self.starFieldMed, 4, 2, LIGHTGREY)
        self.renderStars(screen, self.starFieldFast, 8, 1, YELLOW)
