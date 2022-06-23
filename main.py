import sys
import pygame

from states.splash import Splash
from states.menu import Menu
from states.gamePlay import Gameplay
from states.gameOver import GameOver
from game import Game
import constants

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

states = {
    "MENU": Menu(),
    "SPLASH": Splash(),
    "GAMEPLAY": Gameplay(),
    "GAMEOVER": GameOver()
}

game = Game(screen, states, "SPLASH")
game.run()
pygame.quit()
sys.exit()