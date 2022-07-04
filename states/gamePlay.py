import pygame
import random
import spritesheet
import constants
from starfield import StarField

from .state import State
from sprites.player import Player
from sprites.rocket import Rocket
from sprites.enemy import Enemy
from sprites.controlPoint import ControlPoint
from sprites.explosion import Explosion

from bezier.controlPointCollectionFactory import ControlPointCollectionFactory
from bezier.pathPointCalculator import PathPointCalculator
from bezier.controlHandlerMover import ControlHandlerMover
from bezier.pathPointSelector import PathPointSelector

ADDENEMY = pygame.USEREVENT + 1
ENEMYSHOOTS = pygame.USEREVENT + 2
FREEZE = pygame.USEREVENT + 3


class Gameplay(State):
    def __init__(self):
        super(Gameplay, self).__init__()
        pygame.time.set_timer(ADDENEMY, 450)
        pygame.time.set_timer(ENEMYSHOOTS, 1000)
        pygame.time.set_timer(FREEZE, 2000)

        self.rect = pygame.Rect((0, 0), (80, 80))
        self.nextState = "GAME_OVER"  # This might be where we need to change things here to go to the question screen instead of game over
        self.sprites = spritesheet.SpriteSheet(constants.SPRITE_SHEET)
        self.explosion_sprites = spritesheet.SpriteSheet(constants.SPRITE_SHEET_EXPLOSION)
        self.starfield = StarField()
        self.controlPoints1 = ControlPointCollectionFactory.createCollection1()
        self.controlPoints2 = ControlPointCollectionFactory.createCollection2()
        self.controlPoints3 = ControlPointCollectionFactory.createCollection3()
        self.controlPoints4 = ControlPointCollectionFactory.createCollection4()
        self.pathPointSelector = PathPointSelector(self.controlPoints1)
        self.pathPointSelector.createPathPointMapping()
        self.mover = ControlHandlerMover(self.controlPoints1, self.pathPointSelector)
        self.controlSprites = pygame.sprite.Group()
        self.addControlPoints()
        self.player = Player(self.sprites)
        self.allSprites = pygame.sprite.Group()
        self.allSprites.add(self.player)
        self.waveCount = 0
        self.enemies = 0
        self.numEnemies = 13
        self.score = 0
        self.highScore = 0
        self.freeze = False

        self.allEnemies = pygame.sprite.Group()
        self.allRockets = pygame.sprite.Group()
        self.enemyRockets = pygame.sprite.Group()
        self.shootSound = pygame.mixer.Sound("./assets/sounds/13 Fighter Shot1.mp3")
        self.killSound = pygame.mixer.Sound("./assets/sounds/kill.mp3")
        self.showControl = False
        self.mover.allignAll()

    def startup(self):
        pygame.mixer.music.load("./assets/sounds/02 Start Music.mp3")
        pygame.mixer.music.play()
        self.player = Player(self.sprites)
        self.allSprites = pygame.sprite.Group()
        self.allSprites.add(self.player)
        self.waveCount = 0
        self.enemies = 0
        self.numEnemies = 10
        self.score = 0
        self.freeze = False

        self.allEnemies = pygame.sprite.Group()
        self.allRockets = pygame.sprite.Group()
        self.enemyRockets = pygame.sprite.Group()
        self.shootSound = pygame.mixer.Sound("./assets/sounds/13 Fighter Shot1.mp3")
        self.killSound = pygame.mixer.Sound("./assets/sounds/kill.mp3")
        self.showControl = False
        self.mover.allignAll()

    def addControlPoints(self):
        for quartetIndex in range(self.controlPoints1.numQuartets()):
            for pointIndex in range(4):
                quartet = self.controlPoints1.getQuartet(quartetIndex)
                point = quartet.getPoint(pointIndex)
                self.controlSprites.add(
                    ControlPoint(point.x, point.y, (255, 120, 120), quartetIndex, pointIndex, self.controlPoints1,
                                 self.mover))

    def getEvent(self, event):
        for entity in self.allSprites:
            entity.getEvent(event)

        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == ADDENEMY:
            if self.enemies < self.numEnemies:
                self.addEnemy()
            elif len(self.allEnemies) == 0:
                self.enemies = 0
                self.waveCount += 1
                if self.waveCount > 2:
                    self.waveCount = 0
        if event.type == ENEMYSHOOTS:
            self.enemyShoots()
        if event.type == FREEZE:
            if self.freeze:
                self.done = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.controlPoints1.saveControlPoints()
                self.done = True
            if event.key == pygame.K_s:
                self.showControl = not self.showControl
            if event.key == pygame.K_SPACE:
                if len(self.allRockets) < 2:
                    self.shootRocket()

    def addEnemy(self):
        self.enemies += 1
        if self.waveCount == 0:
            enemy1 = Enemy(self.sprites, self.controlPoints1, self.waveCount)
            enemy2 = Enemy(self.sprites, self.controlPoints2, self.waveCount)
        else:
            enemy1 = Enemy(self.sprites, self.controlPoints3, self.waveCount)
            enemy2 = Enemy(self.sprites, self.controlPoints4, self.waveCount)

        self.allEnemies.add(enemy1)
        self.allSprites.add(enemy1)
        self.allEnemies.add(enemy2)
        self.allSprites.add(enemy2)

    def shootRocket(self):
        rocket = Rocket(self.sprites, 0, 15)
        rocket.rect.centerx = self.player.rect.centerx
        self.allRockets.add(rocket)
        self.allSprites.add(rocket)
        self.shootSound.play()

    def enemyShoots(self):
        numEnemies = len(self.allEnemies)

        if numEnemies > 0:
            enemyIndex = random.randint(0, numEnemies - 1)
            startRocket = None

            for index, enemy in enumerate(self.allEnemies):
                if index == enemyIndex:
                    startRocket = enemy.rect.center

            if startRocket[1] < 400:
                ySpeed = 7
                dx = self.player.rect.centerx - startRocket[0]
                dy = self.player.rect.centery - startRocket[1]

                numSteps = dy / ySpeed
                xSpeed = dx / numSteps

                rocket = Rocket(self.sprites, xSpeed, ySpeed)
                rocket.rect.centerx = startRocket[0]
                rocket.rect.centery = startRocket[1]

                self.enemyRockets.add(rocket)
                self.allSprites.add(rocket)

    def draw(self, screen):
        self.starfield.render(screen)
        pressedKeys = pygame.key.get_pressed()

        for entity in self.controlSprites:
            entity.update(pressedKeys)

        for entity in self.allSprites:
            entity.update(pressedKeys)

        if self.showControl:
            for entity in self.controlSprites:
                screen.blit(entity.getSurf(), entity.rect)

            self.drawPath(screen)
            self.drawControlLines(screen)

        self.drawScore(screen)

        result = pygame.sprite.groupcollide(self.allRockets, self.allEnemies, True, True)
        if result:
            for key in result:
                self.score += 120
                if self.score > self.highScore:
                    self.highScore = self.score
                self.allSprites.add(Explosion(self.explosion_sprites, key.rect[0], key.rect[1]))
                self.killSound.play()

        result = pygame.sprite.spritecollideany(self.player, self.enemyRockets)
        if result:
            self.allSprites.add(Explosion(self.explosion_sprites, result.rect[0], result.rect[1]))
            self.allSprites.add(Explosion(self.explosion_sprites, result.rect[0] - 30, result.rect[1] - 30))
            self.allSprites.add(Explosion(self.explosion_sprites, result.rect[0] + 30, result.rect[1] + 30))
            self.allSprites.add(Explosion(self.explosion_sprites, result.rect[0], result.rect[1] - 30))
            self.killSound.play()
            self.freeze = True
            self.player.kill()

    def drawPath(self, screen):
        calculator = PathPointCalculator
        bezierTimer = 0
        previousPathPoint = None

        while bezierTimer < self.controlPoints1.numQuartets():
            controlPointIndex = int(bezierTimer)
            pathPoint = calculator.calculatePathPoint(self.controlPoints1.getQuartet(controlPointIndex), bezierTimer)

            if previousPathPoint is None:
                previousPathPoint = pathPoint

            pygame.draw.line(screen, (255, 255, 255), (previousPathPoint.xpos, previousPathPoint.ypos),
                             (pathPoint.xpos, pathPoint.ypos))
            previousPathPoint = pathPoint
            bezierTimer += 0.05

    def drawControlLines(self, screen):
        for pair in self.pathPointSelector.getControlPointPairs():
            pygame.draw.line(screen, (255, 255, 255), pair[0], pair[1])

    def drawScore(self, screen):
        score = self.font.render("SCORE", True, (255, 20, 20))
        screen.blit(score, (constants.SCREEN_WIDTH / 2 - 300 - score.get_rect().width / 2, 10))
        score = self.font.render(str(self.score), True, (255, 255, 255))
        screen.blit(score, (constants.SCREEN_WIDTH / 2 - 300 - score.get_rect().width / 2, 40))

        score = self.font.render("HIGH SCORE", True, (255, 20, 20))
        screen.blit(score, (constants.SCREEN_WIDTH / 2 - score.get_rect().width / 2, 10))
        score = self.font.render(str(self.highScore), True, (255, 255, 255))
        screen.blit(score, (constants.SCREEN_WIDTH / 2 - score.get_rect().width / 2, 40))
