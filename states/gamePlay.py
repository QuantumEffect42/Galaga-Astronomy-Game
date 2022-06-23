import pygame
import random
import spritesheet
import constants

from .state import State
from sprites.player import Player
from sprites.rocket import Rocket
from sprites.enemy import Enemy
from sprites.controlPoint import ControlPoint
from sprites.explosion import Explosion

# import bezier calculator stuff here
ADDENEMY = pygame.USEREVENT + 1
ENEMYSHOOTS = pygame.USEREVENT + 2
FREEZE = pygame.USEREVENT + 3


class Gameplay(State):
    def __init__(self) -> None:
        super(Gameplay, self).__init__()